#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import secrets
import sqlite3
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"

FIELD_CANDIDATES: dict[str, tuple[str, ...]] = {
    "event_id": ("event_id", "id"),
    "project_id": ("project_id",),
    "category": ("category",),
    "event_type": ("event_type", "type"),
    "status": ("status",),
    "summary": ("summary", "description", "detail"),
    "event_time_utc": ("event_time_utc", "created_at_utc", "timestamp_utc", "created_at"),
    "metadata": ("metadata_json", "metadata", "details_json", "details", "notes"),
}
REQUIRED_FIELDS = ("project_id", "category", "event_type", "status", "summary", "event_time_utc")


def connect(path: Path | str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(path or DB)
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row
    return conn


def _columns(conn: sqlite3.Connection, table: str) -> dict[str, sqlite3.Row]:
    return {str(row[1]): row for row in conn.execute(f"PRAGMA table_info({table})")}


def event_schema(conn: sqlite3.Connection) -> dict[str, str]:
    columns = _columns(conn, "events")
    if not columns:
        raise ValueError("events_table_missing")
    resolved: dict[str, str] = {}
    for logical, candidates in FIELD_CANDIDATES.items():
        for candidate in candidates:
            if candidate in columns:
                resolved[logical] = candidate
                break
    missing = [field for field in REQUIRED_FIELDS if field not in resolved]
    if missing:
        raise ValueError("events_schema_missing:" + ",".join(missing))
    return resolved


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _text(value: str, field: str) -> str:
    clean = " ".join(value.strip().split())
    if not clean:
        raise ValueError(f"{field}_empty")
    return clean


def parse_metadata(raw: str | None) -> str | None:
    if raw is None:
        return None
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("metadata_invalid_json") from exc
    if not isinstance(value, dict):
        raise ValueError("metadata_must_be_object")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _project_exists(conn: sqlite3.Connection, project_id: int) -> bool:
    return conn.execute("select 1 from projects where project_id=?", (project_id,)).fetchone() is not None


def _generated_text_id() -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"EVT-{stamp}-{secrets.token_hex(4)}"


def create_event(
    conn: sqlite3.Connection,
    *,
    project_id: int,
    category: str,
    event_type: str,
    status: str,
    summary: str,
    metadata_json: str | None = None,
) -> Any:
    schema = event_schema(conn)
    if project_id <= 0:
        raise ValueError("project_id_invalid")
    if not _project_exists(conn, project_id):
        raise ValueError("project_not_found")
    values: dict[str, Any] = {
        schema["project_id"]: project_id,
        schema["category"]: _text(category, "category"),
        schema["event_type"]: _text(event_type, "type"),
        schema["status"]: _text(status, "status"),
        schema["summary"]: _text(summary, "summary"),
        schema["event_time_utc"]: _utc_now(),
    }
    if metadata_json is not None and "metadata" in schema:
        values[schema["metadata"]] = metadata_json

    id_column = schema.get("event_id")
    id_is_integer_pk = False
    if id_column:
        info = _columns(conn, "events")[id_column]
        id_is_integer_pk = bool(int(info[5]) == 1 and "INT" in str(info[2]).upper())
        if not id_is_integer_pk:
            values[id_column] = _generated_text_id()

    columns = list(values)
    placeholders = ",".join("?" for _ in columns)
    sql = f"insert into events({','.join(columns)}) values({placeholders})"
    cursor = conn.execute(sql, [values[column] for column in columns])
    if id_column:
        return int(cursor.lastrowid) if id_is_integer_pk else values[id_column]
    return int(cursor.lastrowid)


def _event_rows(conn: sqlite3.Connection, *, event_id: str | None, project_id: int | None) -> tuple[dict[str, str], list[sqlite3.Row]]:
    schema = event_schema(conn)
    if event_id is not None:
        id_column = schema.get("event_id")
        if not id_column:
            raise ValueError("events_schema_missing:event_id")
        rows = conn.execute(f"select * from events where {id_column}=?", (event_id,)).fetchall()
    else:
        assert project_id is not None
        rows = conn.execute(f"select * from events where {schema['project_id']}=?", (project_id,)).fetchall()
    return schema, rows


def validate_event_scope(conn: sqlite3.Connection, *, event_id: str | None = None, project_id: int | None = None) -> dict[str, Any]:
    if (event_id is None) == (project_id is None):
        raise ValueError("choose_exactly_one_scope")
    if project_id is not None:
        if project_id <= 0:
            raise ValueError("project_id_invalid")
        if not _project_exists(conn, project_id):
            raise ValueError("project_not_found")
    schema, rows = _event_rows(conn, event_id=event_id, project_id=project_id)
    if event_id is not None and not rows:
        raise ValueError("event_not_found")
    errors: list[str] = []
    for row in rows:
        row_project = row[schema["project_id"]]
        if row_project is None or not _project_exists(conn, int(row_project)):
            errors.append(f"missing_project:{row_project}")
        for logical in ("category", "event_type", "status", "summary", "event_time_utc"):
            value = row[schema[logical]]
            if value is None or not str(value).strip():
                errors.append(f"empty_{logical}")
    return {"valid": not errors, "rows": len(rows), "errors": sorted(set(errors))}


def event_create_command(args: argparse.Namespace) -> int:
    try:
        metadata = parse_metadata(args.metadata)
        conn = connect()
        try:
            with conn:
                event_id = create_event(
                    conn,
                    project_id=args.project_id,
                    category=args.category,
                    event_type=args.type,
                    status=args.status,
                    summary=args.summary,
                    metadata_json=metadata,
                )
        finally:
            conn.close()
    except (ValueError, sqlite3.Error) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps({"status": "created", "event_id": event_id, "project_id": args.project_id}, sort_keys=True))
    return 0


def event_validate_command(args: argparse.Namespace) -> int:
    try:
        conn = connect()
        try:
            result = validate_event_scope(conn, event_id=args.event_id, project_id=args.project_id)
        finally:
            conn.close()
    except (ValueError, sqlite3.Error) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    result["status"] = "pass" if result["valid"] else "fail"
    print(json.dumps(result, sort_keys=True))
    return 0 if result["valid"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    sub = parser.add_subparsers(dest="cmd")
    create = sub.add_parser("event-create")
    create.add_argument("--project-id", type=int, required=True)
    create.add_argument("--category", required=True)
    create.add_argument("--type", required=True)
    create.add_argument("--status", required=True)
    create.add_argument("--summary", required=True)
    create.add_argument("--metadata")
    validate = sub.add_parser("event-validate")
    scope = validate.add_mutually_exclusive_group(required=True)
    scope.add_argument("--event-id")
    scope.add_argument("--project-id", type=int)
    return parser


def dispatch(argv: list[str]) -> int | None:
    if not argv or argv[0] not in {"event-create", "event-validate"}:
        return None
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.cmd == "event-create":
        return event_create_command(args)
    if args.cmd == "event-validate":
        return event_validate_command(args)
    return 2
