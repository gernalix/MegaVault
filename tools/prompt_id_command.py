#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import megavault

REQUEST_ID_RE = re.compile(r"[A-Za-z0-9._-]{1,180}\Z")
ALLOWED_CONTENT_PREFIX = "https://raw.githubusercontent.com/gernalix/codex-roadmap/"
EXPECTED_STATUS = {"allocate": "allocated", "materialize": "materialized"}


class PromptIdCommandError(RuntimeError):
    pass


def canonical_payload_sha256(request: dict[str, Any]) -> str:
    payload = json.dumps(
        request,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def receipt_path(receipt_dir: Path, request_id: str) -> Path:
    if not REQUEST_ID_RE.fullmatch(request_id):
        raise PromptIdCommandError(f"invalid_request_id:{request_id}")
    return receipt_dir / f"{request_id}.json"


def read_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PromptIdCommandError(f"invalid_json:{path}") from exc
    if not isinstance(value, dict):
        raise PromptIdCommandError(f"invalid_json_object:{path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, indent=2, sort_keys=True) + "\n"
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        delete=False,
    ) as handle:
        handle.write(data)
        tmp = Path(handle.name)
    tmp.replace(path)


def validate_registry_row(
    db_path: Path,
    *,
    prompt_id: int,
    expected_status: str,
) -> None:
    conn = sqlite3.connect(db_path)
    try:
        if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise PromptIdCommandError("registry_integrity_check_failed")
        fk = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk:
            raise PromptIdCommandError(f"registry_foreign_key_errors:{len(fk)}")
        row = conn.execute(
            "SELECT status FROM prompt_id_registry WHERE prompt_id=?",
            (prompt_id,),
        ).fetchone()
        if not row or str(row[0]) != expected_status:
            raise PromptIdCommandError(
                f"registry_state_mismatch:{prompt_id}:{row[0] if row else 'missing'}:{expected_status}"
            )
    finally:
        conn.close()


def validate_receipt(
    receipt: dict[str, Any],
    *,
    request_id: str,
    command: str,
    payload_sha256: str,
    db_path: Path,
) -> dict[str, Any]:
    if str(receipt.get("request_id") or "") != request_id:
        raise PromptIdCommandError(f"receipt_request_id_mismatch:{request_id}")
    if str(receipt.get("command") or "") != command:
        raise PromptIdCommandError(f"request_id_conflict:{request_id}:command")
    recorded_hash = str(receipt.get("payload_sha256") or "")
    if recorded_hash and recorded_hash != payload_sha256:
        raise PromptIdCommandError(f"request_id_conflict:{request_id}:payload")
    try:
        prompt_id = int(receipt["prompt_id"])
    except (KeyError, TypeError, ValueError) as exc:
        raise PromptIdCommandError(f"invalid_receipt_prompt_id:{request_id}") from exc
    expected_status = EXPECTED_STATUS[command]
    if str(receipt.get("status") or "") != expected_status:
        raise PromptIdCommandError(f"invalid_receipt_status:{request_id}")
    validate_registry_row(
        db_path,
        prompt_id=prompt_id,
        expected_status=expected_status,
    )
    return {
        "request_id": request_id,
        "command": command,
        "prompt_id": prompt_id,
        "status": expected_status,
        "payload_sha256": payload_sha256,
    }


def legacy_response_replay(
    response_path: Path,
    request: dict[str, Any],
    *,
    payload_sha256: str,
    db_path: Path,
) -> dict[str, Any] | None:
    response = read_json(response_path)
    if not response:
        return None
    request_id = str(request["request_id"])
    command = str(request["command"])
    if str(response.get("request_id") or "") != request_id:
        return None
    if str(response.get("command") or "") != command:
        raise PromptIdCommandError(f"request_id_conflict:{request_id}:legacy_command")
    try:
        prompt_id = int(response["prompt_id"])
    except (KeyError, TypeError, ValueError) as exc:
        raise PromptIdCommandError(f"invalid_legacy_response:{request_id}") from exc
    if command == "materialize" and prompt_id != int(request["prompt_id"]):
        raise PromptIdCommandError(f"request_id_conflict:{request_id}:prompt_id")
    expected_status = EXPECTED_STATUS[command]
    if str(response.get("status") or "") != expected_status:
        raise PromptIdCommandError(f"invalid_legacy_response_status:{request_id}")
    validate_registry_row(
        db_path,
        prompt_id=prompt_id,
        expected_status=expected_status,
    )
    return {
        "request_id": request_id,
        "command": command,
        "prompt_id": prompt_id,
        "status": expected_status,
        "payload_sha256": payload_sha256,
    }


def download_prompt(url: str) -> bytes:
    if not url.startswith(ALLOWED_CONTENT_PREFIX):
        raise PromptIdCommandError("content_url_not_allowed")
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return response.read()
    except Exception as exc:
        raise PromptIdCommandError(f"content_download_failed:{exc}") from exc


def execute_request(
    request: dict[str, Any],
    *,
    db_path: Path,
    response_path: Path,
    receipt_dir: Path,
) -> dict[str, Any]:
    command = str(request.get("command") or "").strip()
    if command not in EXPECTED_STATUS:
        raise PromptIdCommandError("command_must_be_allocate_or_materialize")
    request_id = str(request.get("request_id") or "").strip()
    if not REQUEST_ID_RE.fullmatch(request_id):
        raise PromptIdCommandError(f"invalid_request_id:{request_id}")
    payload_sha256 = canonical_payload_sha256(request)
    receipt_file = receipt_path(receipt_dir, request_id)

    receipt = read_json(receipt_file)
    if receipt:
        result = validate_receipt(
            receipt,
            request_id=request_id,
            command=command,
            payload_sha256=payload_sha256,
            db_path=db_path,
        )
        write_json(response_path, result)
        return {**result, "replayed": True}

    legacy = legacy_response_replay(
        response_path,
        request,
        payload_sha256=payload_sha256,
        db_path=db_path,
    )
    if legacy:
        write_json(receipt_file, legacy)
        write_json(response_path, legacy)
        return {**legacy, "replayed": True, "legacy_replay": True}

    if command == "allocate":
        source = str(request.get("source") or "").strip()
        if not source:
            raise PromptIdCommandError("source_required_for_allocate")
        project_id = request.get("project_id")
        parent_prompt_id = request.get("parent_prompt_id")
        prompt_id = megavault.allocate_prompt_id(
            db_path,
            source=source,
            project_id=None if project_id is None else int(project_id),
            parent_prompt_id=None if parent_prompt_id is None else int(parent_prompt_id),
        )
    else:
        try:
            prompt_id = int(request["prompt_id"])
        except (KeyError, TypeError, ValueError) as exc:
            raise PromptIdCommandError("prompt_id_required_for_materialize") from exc
        content_url = str(request.get("content_url") or "").strip()
        payload = download_prompt(content_url)
        try:
            text = payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise PromptIdCommandError("prompt_content_not_utf8") from exc
        if not re.search(
            rf"(?m)^PROMPT_ID={prompt_id}(?:\s|$)",
            text,
        ):
            raise PromptIdCommandError(f"prompt_id_marker_missing:{prompt_id}")
        megavault.materialize_prompt_id(
            prompt_id,
            content_sha256=hashlib.sha256(payload).hexdigest(),
            db_path=db_path,
        )

    status = EXPECTED_STATUS[command]
    result = {
        "request_id": request_id,
        "command": command,
        "prompt_id": prompt_id,
        "status": status,
        "payload_sha256": payload_sha256,
    }
    validate_registry_row(
        db_path,
        prompt_id=prompt_id,
        expected_status=status,
    )
    write_json(receipt_file, result)
    write_json(response_path, result)
    return {**result, "replayed": False}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Apply one immutable PROMPT_ID command idempotently."
    )
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--db", type=Path, default=ROOT / "megavault.sqlite")
    parser.add_argument(
        "--response",
        type=Path,
        default=ROOT / ".github" / "prompt-id-response.json",
    )
    parser.add_argument(
        "--receipt-dir",
        type=Path,
        default=ROOT / ".github" / "prompt-id-receipts",
    )
    args = parser.parse_args(argv)

    try:
        request = read_json(args.request)
        if request is None:
            raise PromptIdCommandError("request_missing")
        result = execute_request(
            request,
            db_path=args.db,
            response_path=args.response,
            receipt_dir=args.receipt_dir,
        )
    except (OSError, ValueError, sqlite3.Error, PromptIdCommandError) as exc:
        print(json.dumps({"status": "blocked", "error": str(exc)}, sort_keys=True))
        return 2

    print(json.dumps({"status": "ok", **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
