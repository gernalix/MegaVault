#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

DEFAULT_REMOTE = "gernalix/MegaVault"
DEFAULT_BRANCH = "master"
DEFAULT_CACHE = Path.home() / ".local" / "share" / "megavault-prompt-id-worker" / "repo"
DEFAULT_LOCK = Path.home() / ".local" / "state" / "megavault-prompt-id-worker.lock"
ISSUE_PREFIX = "[prompt-id-command] "


class WorkerError(RuntimeError):
    pass


def run(
    args: list[str],
    *,
    cwd: Path | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    try:
        proc = subprocess.run(
            args,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={**os.environ, "GH_HOST": "github.com"},
        )
    except FileNotFoundError as exc:
        raise WorkerError(f"command_missing:{args[0]}") from exc
    if check and proc.returncode:
        raise WorkerError(
            f"command_failed:{args[0]}:{proc.stderr.strip() or proc.stdout.strip()}"
        )
    return proc


def ensure_cache(cache: Path, remote: str, branch: str) -> None:
    cache.parent.mkdir(parents=True, exist_ok=True)
    if not (cache / ".git").is_dir():
        if cache.exists():
            shutil.rmtree(cache)
        run(
            [
                "gh",
                "repo",
                "clone",
                remote,
                str(cache),
                "--",
                "--branch",
                branch,
                "--single-branch",
            ]
        )
    run(["git", "fetch", "--quiet", "origin", branch], cwd=cache)
    run(["git", "reset", "--hard", f"origin/{branch}"], cwd=cache)
    run(["git", "clean", "-fd"], cwd=cache)


def list_open_commands(remote: str) -> list[dict[str, Any]]:
    proc = run(
        [
            "gh",
            "issue",
            "list",
            "--repo",
            remote,
            "--state",
            "open",
            "--limit",
            "100",
            "--json",
            "number,title,body",
        ]
    )
    try:
        rows = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise WorkerError("invalid_issue_list") from exc
    if not isinstance(rows, list):
        raise WorkerError("invalid_issue_list")
    result = [
        row
        for row in rows
        if isinstance(row, dict)
        and str(row.get("title") or "").startswith(ISSUE_PREFIX)
    ]
    return sorted(result, key=lambda row: int(row["number"]))


def apply_request(cache: Path, body: str) -> dict[str, Any]:
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        suffix=".json",
        delete=False,
    ) as handle:
        handle.write(body)
        request_path = Path(handle.name)
    try:
        proc = run(
            [
                sys.executable,
                "tools/prompt_id_command.py",
                "--request",
                str(request_path),
            ],
            cwd=cache,
        )
        try:
            result = json.loads(proc.stdout.strip().splitlines()[-1])
        except (IndexError, json.JSONDecodeError) as exc:
            raise WorkerError("invalid_command_output") from exc
        if result.get("status") not in {"allocated", "materialized"}:
            raise WorkerError(f"command_not_ok:{result}")
        return result
    finally:
        request_path.unlink(missing_ok=True)


def commit_and_push(cache: Path, branch: str, request_id: str) -> bool:
    run(
        [
            "git",
            "add",
            "megavault.sqlite",
            ".github/prompt-id-response.json",
            ".github/prompt-id-receipts",
        ],
        cwd=cache,
    )
    status = run(["git", "diff", "--cached", "--quiet"], cwd=cache, check=False)
    if status.returncode == 0:
        return True
    run(
        ["git", "commit", "-m", f"PROMPT_ID registry command {request_id}"],
        cwd=cache,
    )
    pushed = run(
        ["git", "push", "origin", f"HEAD:{branch}"],
        cwd=cache,
        check=False,
    )
    return pushed.returncode == 0


def close_issue(remote: str, issue_number: int, result: dict[str, Any]) -> None:
    body = (
        f"PROMPT_ID={result['prompt_id']}\n"
        f"status={result['status']}\n"
        f"request_id={result['request_id']}\n"
        f"replayed={str(bool(result.get('replayed'))).lower()}\n"
        "processor=local-fallback"
    )
    run(
        [
            "gh",
            "issue",
            "comment",
            str(issue_number),
            "--repo",
            remote,
            "--body",
            body,
        ],
        check=False,
    )
    run(
        [
            "gh",
            "issue",
            "close",
            str(issue_number),
            "--repo",
            remote,
            "--reason",
            "completed",
        ],
        check=False,
    )


def process_issue(
    cache: Path,
    remote: str,
    branch: str,
    issue: dict[str, Any],
) -> dict[str, Any]:
    issue_number = int(issue["number"])
    body = str(issue.get("body") or "")
    if not body.strip():
        raise WorkerError(f"empty_issue_body:{issue_number}")

    for attempt in range(1, 4):
        ensure_cache(cache, remote, branch)
        result = apply_request(cache, body)
        if commit_and_push(cache, branch, str(result["request_id"])):
            close_issue(remote, issue_number, result)
            return {
                "issue_number": issue_number,
                "prompt_id": result["prompt_id"],
                "status": result["status"],
                "request_id": result["request_id"],
                "attempt": attempt,
            }
    raise WorkerError(f"push_race_exhausted:{issue_number}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Process MegaVault PROMPT_ID command Issues locally when GitHub Actions is unavailable."
    )
    parser.add_argument("--remote", default=DEFAULT_REMOTE)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--max-issues", type=int, default=20)
    args = parser.parse_args(argv)

    args.lock.parent.mkdir(parents=True, exist_ok=True)
    with args.lock.open("a+") as lock_handle:
        try:
            fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print(json.dumps({"status": "ok", "skipped": "already_running"}, sort_keys=True))
            return 0

        try:
            ensure_cache(args.cache, args.remote, args.branch)
            issues = list_open_commands(args.remote)[: max(0, args.max_issues)]
            processed: list[dict[str, Any]] = []
            failures: list[dict[str, Any]] = []
            for issue in issues:
                try:
                    processed.append(
                        process_issue(
                            args.cache,
                            args.remote,
                            args.branch,
                            issue,
                        )
                    )
                except WorkerError as exc:
                    failures.append(
                        {
                            "issue_number": int(issue["number"]),
                            "error": str(exc),
                        }
                    )
            payload = {
                "status": "ok" if not failures else "partial",
                "open_commands": len(issues),
                "processed": processed,
                "failures": failures,
            }
            print(json.dumps(payload, sort_keys=True))
            return 0 if not failures else 2
        except WorkerError as exc:
            print(json.dumps({"status": "blocked", "error": str(exc)}, sort_keys=True))
            return 2


if __name__ == "__main__":
    raise SystemExit(main())
