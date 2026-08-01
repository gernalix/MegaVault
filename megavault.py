#!/usr/bin/env python3
"""Minimal MegaVault validator and lookup tool."""

from __future__ import annotations

import argparse
import os
import re
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB = ROOT / "megavault.sqlite"
ROOT_ALLOWLIST = {
    ".git",
    ".gitignore",
    "ai",
    "legacy",
    "megavault.py",
    "megavault.sqlite",
    "tests",
}
TRACKED_FORBIDDEN_PREFIXES = (
    "human/",
    "docs/",
    "dev/",
    "backups/",
    "secrets/",
    "private/",
    "projects/",
    "ai/archive/",
    "ai/global/",
    "ai/projects/",
    "ai/reports/",
)
TRACKED_FORBIDDEN_FILES = {
    "codex_global_timeline.md",
    "codex_global_timeline_ai.md",
    "codex_global_timeline.sqlite",
    "build_codex_global_timeline.py",
    "protocol_lint.py",
}


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def git_tracked() -> list[str]:
    git_dir = ROOT / ".git"
    if not git_dir.exists():
        return []
    import subprocess

    proc = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return [line for line in proc.stdout.splitlines() if line]


def validate() -> int:
    errors: list[str] = []
    if not DB.exists():
        errors.append("missing megavault.sqlite")
        print_errors(errors)
        return 1

    conn = connect()
    integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        errors.append(f"sqlite integrity_check failed: {integrity}")
    fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        errors.append(f"foreign_key_check failed: {fk_errors!r}")

    ids = [row[0] for row in conn.execute("select project_id from projects order by project_id")]
    if not ids or any(not re.fullmatch(r"P[0-9]{4}", value) for value in ids):
        errors.append("project_id format violation")
    if len(ids) != len(set(ids)):
        errors.append("duplicate project_id")
    expected = [f"P{i:04d}" for i in range(1, len(ids) + 1)]
    if ids != expected:
        errors.append("project_id range is not dense from P0001")

    alias_dupes = conn.execute(
        "select alias, count(*) from project_aliases group by alias having count(*) > 1"
    ).fetchall()
    if alias_dupes:
        errors.append(f"duplicate aliases: {alias_dupes!r}")

    missing_permanent = conn.execute(
        """
        select p.project_id
        from projects p
        left join permanent_ids i
          on i.entity_type='project' and i.entity_id=p.project_id
        where i.entity_id is null
        """
    ).fetchall()
    if missing_permanent:
        errors.append(f"projects missing permanent_ids: {missing_permanent!r}")

    root_entries = {p.name for p in ROOT.iterdir()}
    unexpected = sorted(root_entries - ROOT_ALLOWLIST)
    if unexpected:
        errors.append(f"unexpected root entries: {unexpected}")

    tracked = git_tracked()
    for path in tracked:
        if path in TRACKED_FORBIDDEN_FILES or path.startswith(TRACKED_FORBIDDEN_PREFIXES):
            errors.append(f"competing tracked registry/artifact: {path}")
        if re.search(r"(^|/)(access\\.env|oracle-vm-rsa|.*secret.*|.*token.*)$", path, re.I):
            errors.append(f"tracked secret-like path: {path}")

    allowed_md = {"ai/MEGAVAULT_PROTOCOL.md", "ai/GLOBAL_INDEX.md", "legacy/README.md"}
    tracked_md = {path for path in tracked if path.endswith(".md")}
    extra_md = sorted(tracked_md - allowed_md)
    if extra_md:
        errors.append(f"extra tracked markdown: {extra_md}")

    print_errors(errors)
    if errors:
        return 1

    counts = {
        table: conn.execute(f"select count(*) from {table}").fetchone()[0]
        for table in (
            "projects",
            "project_aliases",
            "repositories",
            "hosts",
            "integrations",
            "services",
            "secret_refs",
            "data_assets",
            "incidents",
            "events",
        )
    }
    print("VALIDATE=PASS " + " ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


def print_errors(errors: list[str]) -> None:
    for error in errors:
        print(f"VALIDATE=FAIL {error}", file=sys.stderr)


def project(alias: str) -> int:
    conn = connect()
    row = conn.execute(
        """
        select p.project_id, p.slug, p.name, p.status, p.archived
        from project_aliases a
        join projects p on p.project_id=a.project_id
        where a.alias=?
        """,
        (alias,),
    ).fetchone()
    if not row:
        print(f"PROJECT=NOT_FOUND alias={alias}", file=sys.stderr)
        return 1
    repo_rows = conn.execute(
        "select location, kind, branch, head, status from repositories where project_id=? order by canonical desc, repository_id",
        (row[0],),
    ).fetchall()
    print(f"project_id={row[0]}")
    print(f"slug={row[1]}")
    print(f"name={row[2]}")
    print(f"status={row[3]}")
    print(f"archived={row[4]}")
    for location, kind, branch, head, status in repo_rows:
        print(f"repo={location};kind={kind};branch={branch or ''};head={head or ''};status={status or ''}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    project_parser = sub.add_parser("project")
    project_parser.add_argument("alias")
    args = parser.parse_args(argv)
    if args.cmd == "validate":
        return validate()
    if args.cmd == "project":
        return project(args.alias)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
