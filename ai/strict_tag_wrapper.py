#!/usr/bin/env python3
from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

from ai import megavault_core as _core

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
INCIDENT_POLICY = (
    "identity=one_observed_occurrence",
    "id=SQLite_AUTOINCREMENT;immediate;unique;never_reused",
    "same_symptom_same_cause_new_time=new_incident",
    "cause=nullable;UNKNOWN_allowed;does_not_affect_id",
    "merge=forbidden",
    "linking=canonical_tags_only",
    "source=megavault.sqlite:tags+tag_aliases",
    "reuse_existing=mandatory",
    "free_text=forbidden",
    "new_tag=only_if_no_canonical_or_alias_match",
    "format=lowercase_atomic",
    "aliases=search_only;canonical_link_only",
    "incident_search=tag_intersection+text",
)

_core.ROOT = ROOT
_core.DB = DB
_core.PROTOCOL = PROTOCOL
_core.REQUIRED_PROTOCOL_FAMILIES["incident_policy"] = INCIDENT_POLICY


class TagNotFoundError(ValueError):
    """Raised when an incident references an unregistered tag or alias."""


def connect(path: Path | str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(path or DB)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def link_incident_tag(
    conn: sqlite3.Connection, incident_id: int, name_or_alias: str
) -> tuple[int, str]:
    resolved = _core.resolve_tag(conn, name_or_alias)
    if not resolved:
        raise TagNotFoundError(
            f"tag or alias not found: {name_or_alias!r}; create it explicitly with 'megavault.py tag'"
        )
    tag_id, canonical_name = resolved
    conn.execute(
        "insert or ignore into incident_tags(incident_id, tag_id) values (?, ?)",
        (incident_id, tag_id),
    )
    return tag_id, canonical_name


def incident_tag_command(args):
    conn = connect()
    try:
        with conn:
            tag_id, canonical_name = link_incident_tag(conn, args.incident_id, args.tag)
    except TagNotFoundError as exc:
        print(f"INCIDENT_TAG=NOT_FOUND {exc}", file=sys.stderr)
        return 1
    print(f"incident_id={args.incident_id}")
    print(f"tag_id={tag_id}")
    print(f"name={canonical_name}")
    return 0


def incident_create_command(args):
    conn = connect()
    try:
        with conn:
            incident_id = _core.create_incident(
                conn,
                title=args.title,
                status=args.status,
                project_id=args.project_id,
                first_seen_utc=args.first_seen_utc,
                last_seen_utc=args.last_seen_utc,
                severity=args.severity,
                root_cause=args.root_cause,
                resolution_summary=args.resolution_summary,
                systems=args.systems,
                alerts=args.alerts,
                prompt_refs=args.prompt_refs,
                commit_refs=args.commit_refs,
                notes=args.notes,
                source_ref=args.source_ref,
                tags=args.tag,
            )
    except TagNotFoundError as exc:
        print(f"INCIDENT_CREATE=TAG_NOT_FOUND {exc}", file=sys.stderr)
        return 1
    print(f"incident_id={incident_id}")
    return 0


_core.connect = connect
_core.link_incident_tag = link_incident_tag
_core.incident_tag_command = incident_tag_command
_core.incident_create_command = incident_create_command
_core.TagNotFoundError = TagNotFoundError

for _name in dir(_core):
    if not _name.startswith("_"):
        globals()[_name] = getattr(_core, _name)

globals().update(
    {
        "ROOT": ROOT,
        "DB": DB,
        "PROTOCOL": PROTOCOL,
        "INCIDENT_POLICY": INCIDENT_POLICY,
        "connect": connect,
        "link_incident_tag": link_incident_tag,
        "incident_tag_command": incident_tag_command,
        "incident_create_command": incident_create_command,
        "TagNotFoundError": TagNotFoundError,
    }
)


def main(argv=None):
    return _core.main(argv)
