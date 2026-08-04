#!/usr/bin/env python3
"""Minimal MegaVault validator, lookup, and incident tagging tool."""

from __future__ import annotations

import argparse
import re
import sqlite3
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DB = ROOT / "megavault.sqlite"
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
SCHEMA_VERSION = 6
CANONICAL_TAG_RE = re.compile(r"^[a-z][a-z0-9_]*$")
DEFAULT_CANONICAL_TAGS = {
    "alerts": "observable alerting, monitor red states, or notification signals",
    "android": "Android platform or Android application runtime",
    "android_studio": "Android Studio IDE/runtime",
    "autokey": "AutoKey automation/input tool",
    "backup": "backup or restore workflow",
    "boot": "bootloader, initramfs, or startup path",
    "btrfs": "Btrfs filesystem",
    "codec": "media codec or decoder behavior",
    "codex": "Codex CLI, plugins, logs, or quota tooling",
    "data_analytics": "Data Analytics plugin or related workflow",
    "disk": "disk usage or disk I/O condition",
    "espanso": "Espanso text expansion tool",
    "fedora": "Fedora host, desktop, or system service",
    "fedora_system_monitor": "Fedora System Monitor project/runtime",
    "flatpak": "Flatpak packaging/runtime",
    "git": "Git repository or branch state",
    "gnome": "GNOME desktop/session behavior",
    "input": "keyboard, mouse, compositor input, or automation input path",
    "luks": "LUKS encrypted block device",
    "megavault": "MegaVault repository, protocol, schema, or canonical data",
    "metered": "metered network/background data policy",
    "monitor": "monitoring service or quota monitor",
    "multitimer": "MultiTimeTracker app/project",
    "network": "network connectivity or network service state",
    "notifications": "notification delivery, channel, listener, or user alert path",
    "ntfs": "NTFS filesystem or ntfs-3g path",
    "oracle": "Oracle VM or Oracle infrastructure",
    "performance": "CPU, thermal, fan, or resource runaway",
    "persistence": "state persistence, export, or durable mutation behavior",
    "pixel": "Google Pixel device family",
    "plugin": "Codex/OpenAI plugin runtime",
    "protocol": "MegaVault protocol/bootstrap contract",
    "quota": "usage/quota accounting",
    "secure_boot": "Secure Boot or signed boot chain",
    "silent": "silent, muted, or no-sound alert behavior",
    "sleep": "suspend, idle, screen-off, or dozing behavior",
    "smart": "SMART health checks or disk-health telemetry",
    "sqlite": "SQLite database, WAL, schema, or query behavior",
    "storage": "storage device, mount, filesystem capacity, or external volume",
    "swap": "swap or zram memory pressure accounting",
    "systemd": "systemd service/timer/user unit behavior",
    "t7": "Samsung T7 external SSD",
    "telegram": "Telegram notification integration",
    "vlc": "VLC media player",
    "wayland": "Wayland compositor/session behavior",
    "whatsapp": "WhatsApp app/service behavior",
    "wifi": "WiFi interface or wireless connectivity",
    "zram": "zram compressed swap device",
}
DEFAULT_TAG_ALIASES = {
    "com.whatsapp": "whatsapp",
    "com.whatsapp 2.26.29.73": "whatsapp",
    "notification": "notifications",
    "notifiche": "notifications",
    "notifica": "notifications",
    "notificationmanager": "notifications",
    "notisave": "notifications",
    "xiaomi wearable": "notifications",
    "tasker": "notifications",
    "no_sound": "silent",
    "muted": "silent",
    "silent_notification": "silent",
    "audioservice": "notifications",
    "pixel_8a": "pixel",
    "pixel 8a": "pixel",
    "google pixel 8a": "pixel",
    "android 17": "android",
    "metered_background": "metered",
    "networkpolicymanager": "metered",
    "fedora 44": "fedora",
    "fedora 44 host": "fedora",
    "fedora host": "fedora",
    "gnome wayland": "wayland",
    "gnome_wayland": "wayland",
    "sqlite wal": "sqlite",
    "samsung t7": "t7",
    "samsung t7 shield usb nvme": "t7",
    "zram-generator": "zram",
}
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


def ensure_column(
    conn: sqlite3.Connection, table: str, column: str, definition: str
) -> bool:
    if column in table_columns(conn, table):
        return False
    conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")
    return True


def incident_id_is_integer(conn: sqlite3.Connection) -> bool:
    columns = table_columns(conn, "incidents")
    column = columns.get("incident_id")
    return bool(column and column[5] == 1 and "INTEGER" in str(column[2]).upper())


def normalize_tag_name(name: str) -> str:
    normalized = " ".join(name.strip().lower().split())
    if not normalized:
        raise ValueError("tag name must not be empty")
    return normalized


def normalize_canonical_tag_name(name: str) -> str:
    canonical = normalize_tag_name(name)
    if not CANONICAL_TAG_RE.fullmatch(canonical):
        raise ValueError(
            "canonical tag must be lowercase atomic: /^[a-z][a-z0-9_]*$/"
        )
    return canonical


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
    canonical = normalize_canonical_tag_name(name)
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


def ensure_default_incident_taxonomy(conn: sqlite3.Connection) -> None:
    for name, description in DEFAULT_CANONICAL_TAGS.items():
        create_tag(conn, name, description)
    for alias, tag_name in DEFAULT_TAG_ALIASES.items():
        add_tag_alias(conn, alias, tag_name)


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
    resolved = resolve_tag(conn, name_or_alias)
    if not resolved:
        raise ValueError(f"tag or alias not found: {name_or_alias!r}")
    tag_id, canonical_name = resolved
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
    ensure_default_incident_taxonomy(conn)
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
            resolved = resolve_tag(conn, token)
            if resolved:
                tag_id = resolved[0]
            else:
                try:
                    tag_id, _ = create_tag(
                        conn, token, "deterministic import from legacy incident fields"
                    )
                except ValueError:
                    continue
            before = conn.total_changes
            conn.execute(
                "insert or ignore into incident_tags(incident_id, tag_id) values (?, ?)",
                (incident_id, tag_id),
            )
            changed = changed or conn.total_changes > before
    return changed


def normalize_remote_url(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    if value.startswith("remote:"):
        value = value.removeprefix("remote:")
    if value.endswith(".git"):
        value = value[:-4]
    return value or None


def git_value(path: str, *args: str) -> str | None:
    proc = subprocess.run(
        ["git", "-C", path, *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    value = proc.stdout.strip()
    if proc.returncode != 0:
        return None
    return value or None


def repository_runtime_parts(location: str) -> tuple[str | None, str | None]:
    raw = location.removeprefix("remote:")
    if raw.startswith("ubuntu@"):
        _, _, path = raw.partition(":")
        return "H0002", path or None
    if location.startswith("Windows:"):
        return "H0003", location.removeprefix("Windows:") or None
    return None, None


def infer_repository_kind(kind: str, location: str) -> str:
    if kind == "local":
        return "local_worktree"
    if kind == "legacy" or location.startswith("legacy:"):
        return "legacy"
    if location.startswith("remote:http"):
        return "remote_repository"
    if location.startswith("Windows:"):
        return "remote_host"
    if kind == "remote" or location.startswith("remote:"):
        return "runtime"
    return kind


def refresh_repository_index_rows(conn: sqlite3.Connection) -> bool:
    changed = False
    rows = conn.execute(
        """
        select repository_id, location, kind, branch, head, status, canonical,
               repository_kind, host_id, worktree_path, remote_url, runtime_path
        from repositories
        order by repository_id
        """
    ).fetchall()
    for row in rows:
        (
            repository_id,
            location,
            kind,
            branch,
            head,
            status,
            canonical,
            current_repository_kind,
            current_host_id,
            current_worktree_path,
            current_remote_url,
            current_runtime_path,
        ) = row
        repository_kind = infer_repository_kind(kind, location)
        host_id = current_host_id
        worktree_path = current_worktree_path
        remote_url = current_remote_url
        runtime_path = current_runtime_path
        next_branch = branch
        next_head = head

        if repository_kind == "local_worktree":
            host_id = "H0001"
            worktree_path = location
            path = Path(location)
            if (path / ".git").exists():
                next_branch = git_value(location, "branch", "--show-current") or branch
                if path.resolve() == ROOT.resolve():
                    next_head = None
                else:
                    next_head = git_value(location, "rev-parse", "HEAD") or head
                remote_url = normalize_remote_url(
                    git_value(location, "remote", "get-url", "origin")
                )
            if path.exists() and not status:
                status = "present"
        elif repository_kind == "remote_repository":
            remote_url = normalize_remote_url(location)
        elif repository_kind in {"runtime", "remote_host"}:
            parsed_host_id, parsed_runtime_path = repository_runtime_parts(location)
            host_id = parsed_host_id or host_id
            runtime_path = parsed_runtime_path or runtime_path
        elif repository_kind == "legacy":
            worktree_path = None
            legacy_path = Path(location.removeprefix("legacy:"))
            if not legacy_path.exists():
                canonical = 0

        values = (
            repository_kind,
            host_id,
            worktree_path,
            remote_url,
            runtime_path,
            next_branch,
            next_head,
            canonical,
            repository_id,
        )
        before = conn.total_changes
        conn.execute(
            """
            update repositories
            set repository_kind=?,
                host_id=?,
                worktree_path=?,
                remote_url=?,
                runtime_path=?,
                branch=?,
                head=?,
                canonical=?
            where repository_id=?
              and (
                repository_kind is not ? or host_id is not ? or
                worktree_path is not ? or remote_url is not ? or
                runtime_path is not ? or branch is not ? or head is not ? or
                canonical is not ?
              )
            """,
            (*values[:-1], repository_id, *values[:-1]),
        )
        changed = changed or conn.total_changes > before
    return changed


def normalized_sql(value: str | None) -> str:
    return " ".join((value or "").split())


def ensure_codex_project_index_view(conn: sqlite3.Connection) -> None:
    view_sql = """
        CREATE VIEW codex_project_index AS
        WITH
        worktree AS (
          SELECT *
          FROM (
            SELECT
              r.project_id,
              r.repository_kind,
              h.name AS host_name,
              r.worktree_path,
              r.remote_url,
              r.branch,
              r.head,
              r.status,
              row_number() OVER (
                PARTITION BY r.project_id
                ORDER BY r.canonical DESC, r.repository_id
              ) AS rn
            FROM repositories r
            LEFT JOIN hosts h ON h.host_id=r.host_id
            WHERE r.repository_kind='local_worktree'
              AND r.worktree_path IS NOT NULL
          )
          WHERE rn=1
        ),
        remote_repo AS (
          SELECT *
          FROM (
            SELECT
              r.project_id,
              r.repository_kind,
              r.remote_url,
              r.branch,
              r.head,
              r.status,
              row_number() OVER (
                PARTITION BY r.project_id
                ORDER BY r.canonical DESC, r.repository_id
              ) AS rn
            FROM repositories r
            WHERE r.remote_url IS NOT NULL
          )
          WHERE rn=1
        ),
        runtime_repo AS (
          SELECT *
          FROM (
            SELECT
              r.project_id,
              r.repository_kind,
              h.name AS host_name,
              r.runtime_path,
              r.branch,
              r.status,
              row_number() OVER (
                PARTITION BY r.project_id
                ORDER BY r.canonical DESC, r.repository_id
              ) AS rn
            FROM repositories r
            LEFT JOIN hosts h ON h.host_id=r.host_id
            WHERE r.repository_kind IN ('runtime', 'remote_host')
          )
          WHERE rn=1
        ),
        runtime_service AS (
          SELECT *
          FROM (
            SELECT
              s.project_id,
              h.name AS host_name,
              s.runtime_path,
              row_number() OVER (
                PARTITION BY s.project_id
                ORDER BY
                  CASE WHEN s.state LIKE '%removed%' OR s.state LIKE '%not-found%' THEN 1 ELSE 0 END,
                  CASE WHEN h.kind='remote_server' THEN 0 ELSE 1 END,
                  s.service_id
              ) AS rn
            FROM services s
            LEFT JOIN hosts h ON h.host_id=s.host_id
            WHERE s.project_id IS NOT NULL
              AND s.runtime_path IS NOT NULL
          )
          WHERE rn=1
        ),
        legacy_project AS (
          SELECT DISTINCT project_id
          FROM repositories
          WHERE repository_kind='legacy'
        )
        SELECT
          p.project_id,
          p.slug,
          CASE
            WHEN p.archived=1 THEN 'ARCHIVED'
            WHEN worktree.worktree_path IS NOT NULL THEN 'LOCAL'
            WHEN runtime_service.runtime_path IS NOT NULL
              OR runtime_repo.host_name IS NOT NULL
              OR runtime_repo.runtime_path IS NOT NULL
              OR remote_repo.remote_url IS NOT NULL
              THEN 'REMOTE_ONLY'
            WHEN legacy_project.project_id IS NOT NULL THEN 'MISSING'
            ELSE 'MISSING'
          END AS project_status,
          p.archived,
          COALESCE(worktree.host_name, runtime_service.host_name, runtime_repo.host_name) AS canonical_host,
          worktree.worktree_path AS canonical_worktree,
          COALESCE(worktree.repository_kind, remote_repo.repository_kind, runtime_repo.repository_kind, 'legacy') AS repository_kind,
          COALESCE(worktree.branch, remote_repo.branch, runtime_repo.branch) AS canonical_branch,
          COALESCE(remote_repo.remote_url, worktree.remote_url) AS remote_url,
          COALESCE(worktree.head, remote_repo.head) AS head,
          COALESCE(worktree.status, remote_repo.status, runtime_repo.status) AS repository_status,
          COALESCE(runtime_service.host_name, runtime_repo.host_name) AS runtime_host,
          COALESCE(runtime_service.runtime_path, runtime_repo.runtime_path) AS runtime_path
        FROM projects p
        LEFT JOIN worktree ON worktree.project_id=p.project_id
        LEFT JOIN remote_repo ON remote_repo.project_id=p.project_id
        LEFT JOIN runtime_repo ON runtime_repo.project_id=p.project_id
        LEFT JOIN runtime_service ON runtime_service.project_id=p.project_id
        LEFT JOIN legacy_project ON legacy_project.project_id=p.project_id
        """
    current = conn.execute(
        """
        select sql
        from sqlite_master
        where type='view' and name='codex_project_index'
        """
    ).fetchone()
    if current and normalized_sql(current[0]) == normalized_sql(view_sql):
        return
    conn.execute("DROP VIEW IF EXISTS codex_project_index")
    conn.execute(view_sql)


def migrate_project_index_schema(conn: sqlite3.Connection) -> bool:
    changed = False
    if not table_exists(conn, "repositories"):
        return False
    changed = ensure_column(conn, "repositories", "repository_kind", "TEXT") or changed
    changed = ensure_column(
        conn,
        "repositories",
        "host_id",
        "TEXT REFERENCES hosts(host_id) ON UPDATE CASCADE ON DELETE SET NULL",
    ) or changed
    changed = ensure_column(conn, "repositories", "worktree_path", "TEXT") or changed
    changed = ensure_column(conn, "repositories", "remote_url", "TEXT") or changed
    changed = ensure_column(conn, "repositories", "runtime_path", "TEXT") or changed
    changed = refresh_repository_index_rows(conn) or changed
    execute_statements(
        conn,
        """
        CREATE INDEX IF NOT EXISTS idx_repositories_project_kind
          ON repositories(project_id, repository_kind, canonical, repository_id);
        CREATE UNIQUE INDEX IF NOT EXISTS idx_repositories_one_canonical_worktree
          ON repositories(project_id)
          WHERE repository_kind='local_worktree' AND canonical=1;
        """
    )
    ensure_codex_project_index_view(conn)
    stable_remote_facts = (
        ("R0031", "H0002", "/opt/uptime-kuma", None),
        ("R0033", "H0002", "/home/ubuntu/bots/owntracks_http_server", "main"),
    )
    for repository_id, host_id, runtime_path, branch in stable_remote_facts:
        before = conn.total_changes
        conn.execute(
            """
            update repositories
            set host_id=?,
                runtime_path=coalesce(runtime_path, ?),
                branch=coalesce(branch, ?)
            where repository_id=?
              and (
                host_id is not ?
                or runtime_path is null
                or (branch is null and ? is not null)
              )
            """,
            (host_id, runtime_path, branch, repository_id, host_id, branch),
        )
        changed = changed or conn.total_changes > before
    for project_id, classification in conn.execute(
        """
        WITH project_classification AS (
          SELECT
            p.project_id,
            CASE
              WHEN EXISTS (
                SELECT 1
                FROM repositories local_repo
                WHERE local_repo.project_id=p.project_id
                  AND local_repo.repository_kind='local_worktree'
                  AND local_repo.canonical=1
                  AND local_repo.worktree_path IS NOT NULL
              ) THEN 'LOCAL'
              WHEN EXISTS (
                SELECT 1
                FROM repositories remote_repo
                WHERE remote_repo.project_id=p.project_id
                  AND remote_repo.repository_kind IN ('runtime', 'remote_host', 'remote_repository')
                  AND (
                    remote_repo.host_id IS NOT NULL
                    OR remote_repo.runtime_path IS NOT NULL
                    OR remote_repo.remote_url IS NOT NULL
                  )
              )
              OR EXISTS (
                SELECT 1
                FROM services service
                WHERE service.project_id=p.project_id
                  AND service.runtime_path IS NOT NULL
              ) THEN 'REMOTE_ONLY'
              ELSE 'MISSING'
            END AS classification
          FROM projects p
          WHERE p.archived=0
        )
        SELECT project_id, classification
        FROM project_classification
        WHERE classification<>'LOCAL'
        ORDER BY project_id
        """
    ).fetchall():
        before = conn.total_changes
        conn.execute(
            "update projects set status=? where project_id=? and status is not ?",
            (classification, project_id, classification),
        )
        changed = changed or conn.total_changes > before
        before = conn.total_changes
        conn.execute(
            """
            update repositories
            set status=?
            where project_id=?
              and repository_kind<>'local_worktree'
              and status is not ?
            """,
            (classification, project_id, classification),
        )
        changed = changed or conn.total_changes > before
    before = conn.total_changes
    conn.execute(
        "update projects set status='active' where project_id=23 and status<>'active'"
    )
    changed = changed or conn.total_changes > before
    before = conn.total_changes
    conn.execute(
        "update repositories set status='active' where project_id=23 and status<>'active'"
    )
    changed = changed or conn.total_changes > before
    before = conn.total_changes
    conn.execute(
        """
        insert or ignore into data_assets(
            data_asset_id, project_id, host_id, name, asset_type, path, status, notes
        )
        values (
            'DATA0011', 23, 'H0001', 'megavault.sqlite', 'sqlite',
            '/home/daniele/MegaVault/megavault.sqlite', 'canonical', 'PROMPT_ID=731604'
        )
        """
    )
    changed = changed or conn.total_changes > before
    current_version = conn.execute(
        "select value from schema_meta where key='schema_version'"
    ).fetchone()
    if not current_version or current_version[0] != str(SCHEMA_VERSION):
        conn.execute(
            "insert or replace into schema_meta(key, value) values ('schema_version', ?)",
            (str(SCHEMA_VERSION),),
        )
        changed = True
    return changed


def git_tracked() -> list[str]:
    git_dir = ROOT / ".git"
    if not git_dir.exists():
        return []

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
    repository_columns = table_columns(conn, "repositories")
    for column in (
        "repository_kind",
        "host_id",
        "worktree_path",
        "remote_url",
        "runtime_path",
    ):
        if column not in repository_columns:
            errors.append(f"repositories missing operational column: {column}")
    if not table_exists(conn, "codex_project_index"):
        errors.append("missing codex_project_index view")
    else:
        project_count = conn.execute("select count(*) from projects").fetchone()[0]
        view_count = conn.execute("select count(*) from codex_project_index").fetchone()[0]
        if view_count != project_count:
            errors.append(
                f"codex_project_index row count mismatch: projects={project_count} view={view_count}"
            )
        duplicate_view_rows = conn.execute(
            """
            select project_id, count(*)
            from codex_project_index
            group by project_id
            having count(*)<>1
            """
        ).fetchall()
        if duplicate_view_rows:
            errors.append(f"codex_project_index duplicate rows: {duplicate_view_rows!r}")
        invalid_project_statuses = conn.execute(
            """
            select project_id, project_status
            from codex_project_index
            where project_status not in ('LOCAL', 'REMOTE_ONLY', 'MISSING', 'ARCHIVED')
            order by project_id
            """
        ).fetchall()
        if invalid_project_statuses:
            errors.append(f"codex_project_index invalid statuses: {invalid_project_statuses!r}")
    if "repository_kind" in repository_columns:
        ambiguous_worktrees = conn.execute(
            """
            select project_id, count(*)
            from repositories
            where repository_kind='local_worktree' and canonical=1
            group by project_id
            having count(*) > 1
            """
        ).fetchall()
        if ambiguous_worktrees:
            errors.append(f"ambiguous canonical worktrees: {ambiguous_worktrees!r}")
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
    invalid_tags = conn.execute(
        "select tag_id, name from tags where name not glob '[a-z]*'"
    ).fetchall()
    invalid_tags.extend(
        [
            row
            for row in conn.execute("select tag_id, name from tags").fetchall()
            if not CANONICAL_TAG_RE.fullmatch(str(row[1]))
        ]
    )
    if invalid_tags:
        unique_invalid = sorted(set((int(row[0]), str(row[1])) for row in invalid_tags))
        errors.append(f"non-canonical tag names: {unique_invalid!r}")
    untagged_incidents = conn.execute(
        """
        select i.incident_id
        from incidents i
        left join incident_tags it on it.incident_id=i.incident_id
        where it.incident_id is null
        order by i.incident_id
        """
    ).fetchall()
    if untagged_incidents:
        errors.append(f"incidents missing canonical tags: {untagged_incidents!r}")
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


CODEX_PROJECT_FIELDS = (
    "project_id",
    "slug",
    "project_status",
    "archived",
    "canonical_host",
    "canonical_worktree",
    "repository_kind",
    "canonical_branch",
    "remote_url",
    "head",
    "repository_status",
    "runtime_host",
    "runtime_path",
)


def project_index_row(conn: sqlite3.Connection, project_id: int) -> sqlite3.Row | tuple | None:
    return conn.execute(
        """
        select project_id, slug, project_status, archived, canonical_host,
               canonical_worktree, repository_kind, canonical_branch, remote_url,
               head, repository_status, runtime_host, runtime_path
        from codex_project_index
        where project_id=?
        """,
        (project_id,),
    ).fetchone()


def project_list_command() -> int:
    conn = connect()
    for row in conn.execute(
        """
        select project_id, slug, project_status, canonical_host, canonical_worktree,
               runtime_host, runtime_path
        from codex_project_index
        order by project_id
        """
    ):
        print(
            "project_id={};slug={};project_status={};canonical_host={};"
            "canonical_worktree={};runtime_host={};runtime_path={}".format(
                row[0],
                row[1],
                row[2],
                row[3] or "",
                row[4] or "",
                row[5] or "",
                row[6] or "",
            )
        )
    return 0


def project_show_command(project_id: int) -> int:
    conn = connect()
    row = project_index_row(conn, project_id)
    if not row:
        print(f"PROJECT=NOT_FOUND project_id={project_id}", file=sys.stderr)
        return 1
    for label, value in zip(CODEX_PROJECT_FIELDS, row):
        print(f"{label}={value if value is not None else ''}")
    services = conn.execute(
        """
        select coalesce(h.name, ''), s.name, coalesce(s.scope, ''),
               coalesce(s.unit, ''), coalesce(s.runtime_path, ''),
               coalesce(s.state, '')
        from services s
        left join hosts h on h.host_id=s.host_id
        where s.project_id=?
        order by s.service_id
        """,
        (project_id,),
    ).fetchall()
    for host, name, scope, unit, runtime_path, state in services:
        print(
            f"service={name};host={host};scope={scope};unit={unit};"
            f"runtime_path={runtime_path};state={state}"
        )
    return 0


def project_path_command(project_id: int, status_only: bool = False) -> int:
    conn = connect()
    row = project_index_row(conn, project_id)
    if not row:
        if status_only:
            print("ABSENT")
            return 1
        print(f"PROJECT_PATH=NOT_FOUND project_id={project_id}", file=sys.stderr)
        return 1
    if status_only:
        print(row[2])
        return 0
    ambiguous = conn.execute(
        """
        select count(*)
        from repositories
        where project_id=?
          and repository_kind='local_worktree'
          and canonical=1
          and worktree_path is not null
        """,
        (project_id,),
    ).fetchone()[0]
    if ambiguous > 1:
        print(f"PROJECT_PATH=AMBIGUOUS project_id={project_id}", file=sys.stderr)
        return 1
    path = row[5]
    if row[2] != "LOCAL" or not path:
        print(f"PROJECT_PATH=ABSENT project_id={project_id}", file=sys.stderr)
        return 1
    print(path)
    return 0


def migrate_database() -> int:
    conn = sqlite3.connect(DB)
    conn.isolation_level = None
    try:
        conn.execute("PRAGMA legacy_alter_table=ON")
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.execute("BEGIN")
        schema_version = conn.execute(
            "select value from schema_meta where key='schema_version'"
        ).fetchone()
        incident_schema_current = schema_version and int(schema_version[0]) >= 4
        changed = False
        if not incident_schema_current or not incident_id_is_integer(conn):
            changed = migrate_incident_schema(conn)
        changed = migrate_project_index_schema(conn) or changed
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


def tag_list_command() -> int:
    conn = connect()
    for tag_id, name, description in conn.execute(
        "select tag_id, name, coalesce(description, '') from tags order by name"
    ):
        print(f"tag_id={tag_id};name={name};description={description}")
    return 0


def tag_resolve_command(term: str) -> int:
    conn = connect()
    resolved = resolve_tag(conn, term)
    if not resolved:
        print(f"TAG=NOT_FOUND term={term}", file=sys.stderr)
        return 1
    tag_id, canonical_name = resolved
    print(f"tag_id={tag_id}")
    print(f"name={canonical_name}")
    return 0


def tag_create_command(name: str, description: str | None = None) -> int:
    conn = connect()
    resolved = resolve_tag(conn, name)
    if resolved:
        tag_id, canonical_name = resolved
    else:
        with conn:
            tag_id, canonical_name = create_tag(conn, name, description)
    print(f"tag_id={tag_id}")
    print(f"name={canonical_name}")
    return 0


def tag_command(args: argparse.Namespace) -> int:
    if not args.tag_args:
        print("TAG=FAIL missing subcommand or tag name", file=sys.stderr)
        return 2
    if args.tag_args[0] == "list":
        if len(args.tag_args) != 1:
            print("TAG=FAIL usage: megavault.py tag list", file=sys.stderr)
            return 2
        return tag_list_command()
    if args.tag_args[0] == "resolve":
        if len(args.tag_args) != 2:
            print("TAG=FAIL usage: megavault.py tag resolve <term>", file=sys.stderr)
            return 2
        return tag_resolve_command(args.tag_args[1])
    if len(args.tag_args) != 1:
        print("TAG=FAIL usage: megavault.py tag <name>", file=sys.stderr)
        return 2
    try:
        return tag_create_command(args.tag_args[0], args.description)
    except (TagConflictError, ValueError) as exc:
        print(f"TAG=FAIL {exc}", file=sys.stderr)
        return 1


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
    tags = args.tags or args.tag or []
    rows = search_incidents_by_tags(conn, tags)
    print_incident_rows(rows)
    return 0


def incident_command(args: argparse.Namespace) -> int:
    conn = connect()
    row = conn.execute(
        """
        select incident_id, title, status, first_seen_utc, last_seen_utc,
               severity, root_cause, resolution_summary, systems, alerts,
               prompt_refs, source_ref
        from incidents
        where incident_id=?
        """,
        (args.incident_id,),
    ).fetchone()
    if not row:
        print(f"INCIDENT=NOT_FOUND incident_id={args.incident_id}", file=sys.stderr)
        return 1
    labels = (
        "incident_id",
        "title",
        "status",
        "first_seen_utc",
        "last_seen_utc",
        "severity",
        "root_cause",
        "resolution_summary",
        "systems",
        "alerts",
        "prompt_refs",
        "source_ref",
    )
    for label, value in zip(labels, row):
        print(f"{label}={value or ''}")
    tags = conn.execute(
        """
        select t.name
        from incident_tags it
        join tags t on t.tag_id=it.tag_id
        where it.incident_id=?
        order by t.name
        """,
        (args.incident_id,),
    ).fetchall()
    print("tags=" + ",".join(str(tag[0]) for tag in tags))
    related = conn.execute(
        """
        select other.incident_id, other.title, count(*) as shared_tags
        from incident_tags current
        join incident_tags other_tags on other_tags.tag_id=current.tag_id
        join incidents other on other.incident_id=other_tags.incident_id
        where current.incident_id=? and other.incident_id<>?
        group by other.incident_id
        order by shared_tags desc, other.incident_id desc
        limit 10
        """,
        (args.incident_id, args.incident_id),
    ).fetchall()
    for incident_id, title, shared_tags in related:
        print(f"related_incident_id={incident_id};shared_tags={shared_tags};title={title}")
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
    sub.add_parser("project-list")
    project_show_parser = sub.add_parser("project-show")
    project_show_parser.add_argument("project_id", type=int)
    project_path_parser = sub.add_parser("project-path")
    project_path_parser.add_argument("--status", action="store_true")
    project_path_parser.add_argument("project_id", type=int)
    tag_parser = sub.add_parser("tag")
    tag_parser.add_argument("tag_args", nargs="+")
    tag_parser.add_argument("--description")
    tag_alias_parser = sub.add_parser("tag-alias")
    tag_alias_parser.add_argument("alias")
    tag_alias_parser.add_argument("tag")
    incident_tag_parser = sub.add_parser("incident-tag")
    incident_tag_parser.add_argument("incident_id", type=int)
    incident_tag_parser.add_argument("tag")
    incident_parser = sub.add_parser("incident")
    incident_parser.add_argument("incident_id", type=int)
    incident_search_parser = sub.add_parser("incident-search")
    incident_search_parser.add_argument("tags", nargs="*")
    incident_search_parser.add_argument("--tag", action="append")
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
    if args.cmd == "project-list":
        return project_list_command()
    if args.cmd == "project-show":
        return project_show_command(args.project_id)
    if args.cmd == "project-path":
        return project_path_command(args.project_id, args.status)
    if args.cmd == "tag":
        return tag_command(args)
    if args.cmd == "tag-alias":
        return tag_alias_command(args)
    if args.cmd == "incident-tag":
        return incident_tag_command(args)
    if args.cmd == "incident":
        return incident_command(args)
    if args.cmd == "incident-search":
        return incident_search_command(args)
    if args.cmd == "incident-create":
        return incident_create_command(args)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
