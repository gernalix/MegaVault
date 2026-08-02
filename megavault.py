#!/usr/bin/env python3
"""Minimal MegaVault validator, lookup, and incident tagging tool."""

from __future__ import annotations

import argparse
import re
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB = ROOT / "megavault.sqlite"
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
SCHEMA_VERSION = 3
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
REQUIRED_PROTOCOL_FAMILIES = {
    "capsulization": (
        "CAPSULIZATION=mandatory_all_projects",
        "CAPSULE_TARGET=100_percent",
        "NEW_CODE=capsule_only",
        "SHARED_LOGIC=capsule_only",
        "UI_DIRECT_DEPENDENCY=forbidden",
        "CROSS_MODULE_ACCESS=through_capsules_only",
        "LEGACY_REFACTOR=progressively_until_100_percent",
        "FINAL_GATE=verify_capsulization_before_final",
    ),
    "python_environment": (
        "PYTHON:",
        "env=global",
        "isolation=forbidden",
        "tools=venv|virtualenv|pipenv|poetry|uv",
        "override=user_explicit_request",
        "packages=reuse_global>install_global",
        "venv_without_override=protocol_violation",
    ),
    "single_trunk_git": (
        "model=trunk_based_single_developer;operative_branches=1",
        "direct_canonical_work=default",
        "per_task_branch=forbidden",
        "branch_chaining=forbidden",
        "commit_push_before_final=required_unless_user_explicitly_forbids",
        "final_branch_fields=repository,canonical_branch,current_branch,temp_branch_reason,integration_status,cleanup_status",
    ),
    "secret_policy": (
        "secret_values=never_store;reference_paths_only",
        "secrets=no_prompt_echo,no_command_echo,no_secret_values_in_logs_reports_repo_history",
        "secret_handling=read_only_when_task_requires;canonical_paths_from_database;reprompt_for_known_path_forbidden;rotation_manual_explicit_only",
    ),
    "project_id_authority": (
        "project_id_source=megavault.sqlite:projects+project_aliases_only;INTEGER_PRIMARY_KEY",
        "project_lifecycle=never_delete_project;archive_only;never_reuse_project_id;ids_unique_permanent_not_dense",
    ),
    "no_duplicate_truth": (
        "duplicate_truth=forbidden",
        "forbidden=reports_done,human_mirror,project_docs_in_MegaVault,generated_timeline_markdown,duplicate_registries",
        "project_docs=owner_repo_docs_code_tests;MegaVault_only_global_transversal_knowledge",
    ),
    "incident_policy": (
        "incidents=store_in_megavault.sqlite:incidents+incident_events+tags+tag_aliases+incident_tags;id=sqlite_autoincrement_occurrence;semantic_links=canonical_tags_only;forbid=problem_family|recurring_incidents|automatic_merge|tag_hierarchy;status=OPEN|MITIGATED|RESOLVED|ACCEPTED",
    ),
    "final_reporting": (
        "final_fields=files_changed,tests,test_result,docs_or_MegaVault_updates,repo_status,commit,push,sync_state,branch_fields,execution_insights,blockers,optimization_opportunities,remaining_unresolved",
        "blockers=root_cause,impact,workaround,resolution,status;silent_workaround_retry_skip=forbidden",
        "optimization=root_cause,impact,estimated_future_savings,one_time_fix,priority,confidence,status;section=mandatory",
        "success_forbid=silent_failure,false_success,unverified_PASS",
    ),
    "android_policy": (
        "required_for=android_projects,android_builds,android_releases,android_tooling",
        "version=version.txt_integer_monotonic;derive_versionCode_versionName_apk_name;home_v_visible;skip_reuse_forbidden",
        "saf_sqlite=autoexport_all_app_data_on_db_change;atomic;validate_after_write;failure_visible;preserve_last_good;test_required",
        "i18n=en+it;no_hardcoded_user_visible_text;missing_translation_blocker",
    ),
}
SECRET_PATTERNS = (
    ("private_key", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----")),
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{36,}")),
    ("openai_key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}")),
    ("telegram_token", re.compile(r"\b[0-9]{8,10}:[A-Za-z0-9_-]{35,}\b")),
)


class TagConflictError(ValueError):
    """Raised when a tag alias and canonical tag name would be ambiguous."""


def connect(path: Path | str = DB) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def table_columns(conn: sqlite3.Connection, table: str) -> dict[str, sqlite3.Row | tuple]:
    return {row[1]: row for row in conn.execute(f"PRAGMA table_info({table})")}


def table_exists(conn: sqlite3.Connection, table: str) -> bool:
    return (
        conn.execute(
            "select 1 from sqlite_master where type in ('table','view') and name=?",
            (table,),
        ).fetchone()
        is not None
    )


def incident_id_is_integer(conn: sqlite3.Connection) -> bool:
    columns = table_columns(conn, "incidents")
    column = columns.get("incident_id")
    return bool(column and column[5] == 1 and "INTEGER" in str(column[2]).upper())


def normalize_tag_name(name: str) -> str:
    normalized = " ".join(name.strip().split())
    if not normalized:
        raise ValueError("tag name must not be empty")
    return normalized


def resolve_tag(conn: sqlite3.Connection, name_or_alias: str) -> tuple[int, str] | None:
    name = normalize_tag_name(name_or_alias)
    row = conn.execute(
        "select tag_id, name from tags where name=? collate nocase",
        (name,),
    ).fetchone()
    if row:
        return int(row[0]), str(row[1])
    row = conn.execute(
        """
        select t.tag_id, t.name
        from tag_aliases a
        join tags t on t.tag_id=a.tag_id
        where a.alias=? collate nocase
        """,
        (name,),
    ).fetchone()
    if row:
        return int(row[0]), str(row[1])
    return None


def create_tag(
    conn: sqlite3.Connection, name: str, description: str | None = None
) -> tuple[int, str]:
    canonical = normalize_tag_name(name)
    row = conn.execute(
        "select tag_id, name from tags where name=? collate nocase",
        (canonical,),
    ).fetchone()
    if row:
        return int(row[0]), str(row[1])
    alias_row = conn.execute(
        """
        select a.alias, t.tag_id, t.name
        from tag_aliases a
        join tags t on t.tag_id=a.tag_id
        where a.alias=? collate nocase
        """,
        (canonical,),
    ).fetchone()
    if alias_row:
        raise TagConflictError(
            f"canonical tag {canonical!r} conflicts with alias for {alias_row[2]!r}"
        )
    cursor = conn.execute(
        "insert into tags(name, description) values (?, ?)",
        (canonical, description),
    )
    return int(cursor.lastrowid), canonical


def resolve_or_create_tag(
    conn: sqlite3.Connection, name_or_alias: str, description: str | None = None
) -> tuple[int, str]:
    resolved = resolve_tag(conn, name_or_alias)
    if resolved:
        return resolved
    return create_tag(conn, name_or_alias, description)


def add_tag_alias(conn: sqlite3.Connection, alias: str, tag_name_or_id: str | int) -> tuple[str, int]:
    normalized_alias = normalize_tag_name(alias)
    if isinstance(tag_name_or_id, int) or str(tag_name_or_id).isdigit():
        row = conn.execute(
            "select tag_id, name from tags where tag_id=?",
            (int(tag_name_or_id),),
        ).fetchone()
    else:
        row = resolve_tag(conn, str(tag_name_or_id))
    if not row:
        raise ValueError(f"tag not found: {tag_name_or_id!r}")
    tag_id, canonical_name = int(row[0]), str(row[1])
    canonical_conflict = conn.execute(
        "select tag_id, name from tags where name=? collate nocase",
        (normalized_alias,),
    ).fetchone()
    if canonical_conflict:
        raise TagConflictError(
            f"alias {normalized_alias!r} conflicts with canonical tag {canonical_conflict[1]!r}"
        )
    existing = conn.execute(
        """
        select a.tag_id, t.name
        from tag_aliases a
        join tags t on t.tag_id=a.tag_id
        where a.alias=? collate nocase
        """,
        (normalized_alias,),
    ).fetchone()
    if existing:
        if int(existing[0]) != tag_id:
            raise TagConflictError(
                f"alias {normalized_alias!r} already points to {existing[1]!r}"
            )
        return normalized_alias, tag_id
    conn.execute(
        "insert into tag_aliases(alias, tag_id) values (?, ?)",
        (normalized_alias, tag_id),
    )
    return normalized_alias, tag_id


def link_incident_tag(
    conn: sqlite3.Connection, incident_id: int, name_or_alias: str
) -> tuple[int, str]:
    tag_id, canonical_name = resolve_or_create_tag(conn, name_or_alias)
    conn.execute(
        "insert or ignore into incident_tags(incident_id, tag_id) values (?, ?)",
        (incident_id, tag_id),
    )
    return tag_id, canonical_name


def search_incidents_by_tags(
    conn: sqlite3.Connection, names_or_aliases: list[str]
) -> list[sqlite3.Row | tuple]:
    tag_ids: list[int] = []
    seen: set[int] = set()
    for value in names_or_aliases:
        resolved = resolve_tag(conn, value)
        if not resolved:
            return []
        tag_id = resolved[0]
        if tag_id not in seen:
            tag_ids.append(tag_id)
            seen.add(tag_id)
    if not tag_ids:
        return list(
            conn.execute(
                """
                select incident_id, title, status, first_seen_utc, last_seen_utc
                from incidents
                order by coalesce(last_seen_utc, first_seen_utc, '') desc, incident_id desc
                """
            )
        )
    placeholders = ",".join("?" for _ in tag_ids)
    return list(
        conn.execute(
            f"""
            select i.incident_id, i.title, i.status, i.first_seen_utc, i.last_seen_utc
            from incidents i
            join incident_tags it on it.incident_id=i.incident_id
            where it.tag_id in ({placeholders})
            group by i.incident_id
            having count(distinct it.tag_id)=?
            order by coalesce(i.last_seen_utc, i.first_seen_utc, '') desc, i.incident_id desc
            """,
            (*tag_ids, len(tag_ids)),
        )
    )


def split_legacy_tag_tokens(raw: str | None) -> list[str]:
    if not raw:
        return []
    return [token.strip() for token in raw.split(";") if token.strip()]


def create_incident(
    conn: sqlite3.Connection,
    *,
    title: str,
    status: str,
    project_id: int | None = None,
    first_seen_utc: str | None = None,
    last_seen_utc: str | None = None,
    severity: str | None = None,
    root_cause: str | None = None,
    resolution_summary: str | None = None,
    systems: str | None = None,
    alerts: str | None = None,
    prompt_refs: str | None = None,
    commit_refs: str | None = None,
    notes: str | None = None,
    source_ref: str | None = None,
    tags: list[str] | None = None,
) -> int:
    cursor = conn.execute(
        """
        insert into incidents(
            project_id, title, first_seen_utc, last_seen_utc, severity, status,
            root_cause, resolution_summary, systems, alerts, prompt_refs,
            commit_refs, notes, source_ref
        )
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            project_id,
            title,
            first_seen_utc,
            last_seen_utc,
            severity,
            status,
            root_cause,
            resolution_summary,
            systems,
            alerts,
            prompt_refs,
            commit_refs,
            notes,
            source_ref,
        ),
    )
    incident_id = int(cursor.lastrowid)
    for tag_name in tags or []:
        link_incident_tag(conn, incident_id, tag_name)
    return incident_id


def execute_statements(conn: sqlite3.Connection, script: str) -> None:
    for statement in script.split(";"):
        statement = statement.strip()
        if statement:
            conn.execute(statement)


def create_incident_tables(conn: sqlite3.Connection) -> None:
    execute_statements(
        conn,
        """
        CREATE TABLE IF NOT EXISTS incidents (
          incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
          legacy_incident_key TEXT UNIQUE,
          project_id INTEGER REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE SET NULL,
          title TEXT NOT NULL,
          first_seen_utc TEXT,
          last_seen_utc TEXT,
          legacy_occurrence_note TEXT,
          severity TEXT,
          status TEXT NOT NULL,
          root_cause TEXT,
          resolution_summary TEXT,
          systems TEXT,
          alerts TEXT,
          prompt_refs TEXT,
          commit_refs TEXT,
          notes TEXT,
          source_ref TEXT
        );
        CREATE TABLE IF NOT EXISTS incident_events (
          incident_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
          incident_id INTEGER NOT NULL REFERENCES incidents(incident_id) ON UPDATE CASCADE ON DELETE CASCADE,
          event_time_utc TEXT NOT NULL,
          severity TEXT,
          status TEXT,
          source TEXT,
          detail TEXT
        );
        CREATE TABLE IF NOT EXISTS tags (
          tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL COLLATE NOCASE UNIQUE,
          description TEXT,
          created_at_utc TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS tag_aliases (
          alias TEXT PRIMARY KEY COLLATE NOCASE,
          tag_id INTEGER NOT NULL REFERENCES tags(tag_id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS incident_tags (
          incident_id INTEGER NOT NULL REFERENCES incidents(incident_id) ON UPDATE CASCADE ON DELETE CASCADE,
          tag_id INTEGER NOT NULL REFERENCES tags(tag_id) ON UPDATE CASCADE ON DELETE RESTRICT,
          PRIMARY KEY (incident_id, tag_id)
        );
        CREATE INDEX IF NOT EXISTS idx_incidents_project ON incidents(project_id);
        CREATE INDEX IF NOT EXISTS idx_incidents_status ON incidents(status);
        CREATE INDEX IF NOT EXISTS idx_incidents_seen ON incidents(last_seen_utc, first_seen_utc);
        CREATE INDEX IF NOT EXISTS idx_incident_events_incident ON incident_events(incident_id);
        CREATE INDEX IF NOT EXISTS idx_tag_aliases_tag ON tag_aliases(tag_id);
        CREATE INDEX IF NOT EXISTS idx_incident_tags_tag_incident ON incident_tags(tag_id, incident_id);
        """
    )


def migrate_incident_schema(conn: sqlite3.Connection) -> bool:
    migrated = False
    create_incident_tables(conn)
    if not incident_id_is_integer(conn):
        execute_statements(
            conn,
            """
            DROP TABLE IF EXISTS incident_tags;
            DROP TABLE IF EXISTS tag_aliases;
            DROP TABLE IF EXISTS tags;
            CREATE TABLE incidents_new (
              incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
              legacy_incident_key TEXT UNIQUE,
              project_id INTEGER REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE SET NULL,
              title TEXT NOT NULL,
              first_seen_utc TEXT,
              last_seen_utc TEXT,
              legacy_occurrence_note TEXT,
              severity TEXT,
              status TEXT NOT NULL,
              root_cause TEXT,
              resolution_summary TEXT,
              systems TEXT,
              alerts TEXT,
              prompt_refs TEXT,
              commit_refs TEXT,
              notes TEXT,
              source_ref TEXT
            );
            """
        )
        conn.execute(
            """
            insert into incidents_new(
                legacy_incident_key, project_id, title, first_seen_utc, last_seen_utc,
                legacy_occurrence_note, severity, status, root_cause,
                resolution_summary, systems, alerts, prompt_refs, commit_refs,
                notes, source_ref
            )
            select incident_id, project_id, title, first_seen_utc, last_seen_utc,
                   occurrence_count, severity, status, root_cause,
                   resolution_summary, systems, alerts, prompt_refs, commit_refs,
                   notes, source_ref
            from incidents
            order by incident_id
            """
        )
        execute_statements(
            conn,
            """
            ALTER TABLE incidents RENAME TO incidents_legacy;
            ALTER TABLE incidents_new RENAME TO incidents;
            CREATE TABLE incident_events_new (
              incident_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
              incident_id INTEGER NOT NULL REFERENCES incidents(incident_id) ON UPDATE CASCADE ON DELETE CASCADE,
              event_time_utc TEXT NOT NULL,
              severity TEXT,
              status TEXT,
              source TEXT,
              detail TEXT
            );
            """
        )
        old_event_count = conn.execute("select count(*) from incident_events").fetchone()[0]
        conn.execute(
            """
            insert into incident_events_new(
                incident_event_id, incident_id, event_time_utc, severity, status, source, detail
            )
            select e.incident_event_id, n.incident_id, e.event_time_utc,
                   e.severity, e.status, e.source, e.detail
            from incident_events e
            join incidents n on n.legacy_incident_key=e.incident_id
            order by e.incident_event_id
            """
        )
        new_event_count = conn.execute("select count(*) from incident_events_new").fetchone()[0]
        if new_event_count != old_event_count:
            raise RuntimeError(
                f"incident event migration mismatch: old={old_event_count} new={new_event_count}"
            )
        execute_statements(
            conn,
            """
            DROP TABLE incident_events;
            DROP TABLE incidents_legacy;
            ALTER TABLE incident_events_new RENAME TO incident_events;
            """
        )
        migrated = True
    create_incident_tables(conn)
    backfilled = backfill_legacy_incident_tags(conn)
    conn.execute(
        "insert or replace into schema_meta(key, value) values ('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    return migrated or backfilled


def backfill_legacy_incident_tags(conn: sqlite3.Connection) -> bool:
    changed = False
    for incident_id, systems, alerts in conn.execute(
        """
        select incident_id, systems, alerts
        from incidents
        where legacy_incident_key is not null
        order by incident_id
        """
    ).fetchall():
        for token in split_legacy_tag_tokens(systems) + split_legacy_tag_tokens(alerts):
            tag_id, _ = resolve_or_create_tag(
                conn, token, "deterministic import from legacy incident fields"
            )
            before = conn.total_changes
            conn.execute(
                "insert or ignore into incident_tags(incident_id, tag_id) values (?, ?)",
                (incident_id, tag_id),
            )
            changed = changed or conn.total_changes > before
    return changed


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


def protocol_semantic_errors(raw: str | None = None) -> list[str]:
    errors: list[str] = []
    if raw is None:
        if not PROTOCOL.exists():
            return ["protocol_semantic_missing:file"]
        raw = PROTOCOL.read_text(encoding="utf-8")

    version_match = re.search(r"(?m)^VERSION=(\d+)$", raw)
    if not version_match or int(version_match.group(1)) < 19:
        errors.append("protocol_semantic_missing:version_at_least_19")

    for family, snippets in REQUIRED_PROTOCOL_FAMILIES.items():
        for snippet in snippets:
            if snippet not in raw:
                errors.append(f"protocol_semantic_missing:{family}:{snippet}")
    return errors


def secret_scan_errors(paths: list[str]) -> list[str]:
    errors: list[str] = []
    skip_suffixes = {".sqlite", ".pyc"}
    for path_text in paths:
        path = ROOT / path_text
        if path.suffix in skip_suffixes or not path.is_file():
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in SECRET_PATTERNS:
            if pattern.search(raw):
                errors.append(f"secret_scan:{name}:{path_text}")
    return errors


def schema_errors(conn: sqlite3.Connection) -> list[str]:
    errors: list[str] = []
    required_tables = {
        "projects",
        "permanent_ids",
        "project_aliases",
        "repositories",
        "hosts",
        "integrations",
        "services",
        "secret_refs",
        "data_assets",
        "incidents",
        "incident_events",
        "tags",
        "tag_aliases",
        "incident_tags",
        "events",
        "knowledge_notes",
    }
    missing = sorted(table for table in required_tables if not table_exists(conn, table))
    if missing:
        errors.append(f"missing required tables: {missing}")
        return errors
    if not incident_id_is_integer(conn):
        errors.append("incidents.incident_id must be INTEGER PRIMARY KEY")
    incident_columns = table_columns(conn, "incidents")
    if "occurrence_count" in incident_columns:
        errors.append("incidents.occurrence_count legacy coalescing column must not exist")
    for forbidden in (
        "problem_family",
        "incident_families",
        "recurring_incidents",
        "incident_merges",
        "tag_parents",
        "tag_hierarchy",
    ):
        if table_exists(conn, forbidden):
            errors.append(f"forbidden incident abstraction table exists: {forbidden}")
    tag_dupes = conn.execute(
        "select lower(name), count(*) from tags group by lower(name) having count(*) > 1"
    ).fetchall()
    if tag_dupes:
        errors.append(f"duplicate case-insensitive tags: {tag_dupes!r}")
    alias_dupes = conn.execute(
        "select lower(alias), count(*) from tag_aliases group by lower(alias) having count(*) > 1"
    ).fetchall()
    if alias_dupes:
        errors.append(f"duplicate case-insensitive tag aliases: {alias_dupes!r}")
    alias_name_conflicts = conn.execute(
        """
        select a.alias, t.name
        from tag_aliases a
        join tags t on t.name=a.alias collate nocase
        """
    ).fetchall()
    if alias_name_conflicts:
        errors.append(f"tag alias conflicts with canonical name: {alias_name_conflicts!r}")
    schema_version = conn.execute(
        "select value from schema_meta where key='schema_version'"
    ).fetchone()
    if not schema_version or int(schema_version[0]) < SCHEMA_VERSION:
        errors.append(f"schema_version must be at least {SCHEMA_VERSION}")
    return errors


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
    errors.extend(schema_errors(conn))

    ids = [row[0] for row in conn.execute("select project_id from projects")]
    if not ids or any(not isinstance(value, int) or value <= 0 for value in ids):
        errors.append("project_id must be positive integers")
    if len(ids) != len(set(ids)):
        errors.append("duplicate project_id")

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

    errors.extend(protocol_semantic_errors())
    errors.extend(secret_scan_errors(tracked))

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
            "tags",
            "tag_aliases",
            "incident_tags",
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


def migrate_database() -> int:
    conn = sqlite3.connect(DB)
    conn.isolation_level = None
    try:
        conn.execute("PRAGMA legacy_alter_table=ON")
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.execute("BEGIN")
        changed = migrate_incident_schema(conn)
        conn.execute("COMMIT")
    except Exception:
        if conn.in_transaction:
            conn.execute("ROLLBACK")
        raise
    finally:
        conn.execute("PRAGMA legacy_alter_table=OFF")
        conn.execute("PRAGMA foreign_keys=ON")
    fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        print(f"MIGRATE=FAIL foreign_key_check={fk_errors!r}", file=sys.stderr)
        return 1
    status = "changed" if changed else "unchanged"
    version = conn.execute(
        "select value from schema_meta where key='schema_version'"
    ).fetchone()[0]
    print(f"MIGRATE=PASS status={status} schema_version={version}")
    return 0


def print_incident_rows(rows: list[sqlite3.Row | tuple]) -> None:
    for row in rows:
        print(
            "incident_id={};status={};first_seen_utc={};last_seen_utc={};title={}".format(
                row[0],
                row[2],
                row[3] or "",
                row[4] or "",
                row[1],
            )
        )


def tag_command(args: argparse.Namespace) -> int:
    conn = connect()
    with conn:
        tag_id, canonical_name = resolve_or_create_tag(conn, args.name, args.description)
    print(f"tag_id={tag_id}")
    print(f"name={canonical_name}")
    return 0


def tag_alias_command(args: argparse.Namespace) -> int:
    conn = connect()
    try:
        with conn:
            alias, tag_id = add_tag_alias(conn, args.alias, args.tag)
    except TagConflictError as exc:
        print(f"TAG_ALIAS=CONFLICT {exc}", file=sys.stderr)
        return 1
    print(f"alias={alias}")
    print(f"tag_id={tag_id}")
    return 0


def incident_tag_command(args: argparse.Namespace) -> int:
    conn = connect()
    with conn:
        tag_id, canonical_name = link_incident_tag(conn, args.incident_id, args.tag)
    print(f"incident_id={args.incident_id}")
    print(f"tag_id={tag_id}")
    print(f"name={canonical_name}")
    return 0


def incident_search_command(args: argparse.Namespace) -> int:
    conn = connect()
    rows = search_incidents_by_tags(conn, args.tag)
    print_incident_rows(rows)
    return 0


def incident_create_command(args: argparse.Namespace) -> int:
    conn = connect()
    with conn:
        incident_id = create_incident(
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
    print(f"incident_id={incident_id}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    sub.add_parser("migrate")
    project_parser = sub.add_parser("project")
    project_parser.add_argument("alias")
    tag_parser = sub.add_parser("tag")
    tag_parser.add_argument("name")
    tag_parser.add_argument("--description")
    tag_alias_parser = sub.add_parser("tag-alias")
    tag_alias_parser.add_argument("alias")
    tag_alias_parser.add_argument("tag")
    incident_tag_parser = sub.add_parser("incident-tag")
    incident_tag_parser.add_argument("incident_id", type=int)
    incident_tag_parser.add_argument("tag")
    incident_search_parser = sub.add_parser("incident-search")
    incident_search_parser.add_argument("--tag", action="append", required=True)
    incident_create_parser = sub.add_parser("incident-create")
    incident_create_parser.add_argument("--title", required=True)
    incident_create_parser.add_argument("--status", required=True)
    incident_create_parser.add_argument("--project-id", type=int)
    incident_create_parser.add_argument("--first-seen-utc")
    incident_create_parser.add_argument("--last-seen-utc")
    incident_create_parser.add_argument("--severity")
    incident_create_parser.add_argument("--root-cause")
    incident_create_parser.add_argument("--resolution-summary")
    incident_create_parser.add_argument("--systems")
    incident_create_parser.add_argument("--alerts")
    incident_create_parser.add_argument("--prompt-refs")
    incident_create_parser.add_argument("--commit-refs")
    incident_create_parser.add_argument("--notes")
    incident_create_parser.add_argument("--source-ref")
    incident_create_parser.add_argument("--tag", action="append", default=[])
    args = parser.parse_args(argv)
    if args.cmd == "validate":
        return validate()
    if args.cmd == "migrate":
        return migrate_database()
    if args.cmd == "project":
        return project(args.alias)
    if args.cmd == "tag":
        return tag_command(args)
    if args.cmd == "tag-alias":
        return tag_alias_command(args)
    if args.cmd == "incident-tag":
        return incident_tag_command(args)
    if args.cmd == "incident-search":
        return incident_search_command(args)
    if args.cmd == "incident-create":
        return incident_create_command(args)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
