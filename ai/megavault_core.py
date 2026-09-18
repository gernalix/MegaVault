#!/usr/bin/env python3
"""Minimal MegaVault validator, lookup, and incident tagging tool."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import secrets
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
SCHEMA_VERSION = 9
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
    ".github",
    ".gitignore",
    "ai",
    "legacy",
    "megavault.py",
    "megavault.sqlite",
    "tests",
}
ALLOWED_TRACKED_MARKDOWN = {
    "ai/MEGAVAULT_PROTOCOL.md",
    "ai/GLOBAL_INDEX.md",
    "ai/personalhubdoc.md",
    "ai/repository-public-private-matrix.md",
    "ai/repository-retention-checklist.md",
    "legacy/README.md",
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
        "CAPSULE_TARGET=progressive",
        "NEW_CODE=capsule_only",
        "SHARED_LOGIC=capsule_only",
        "UI_DIRECT_DEPENDENCY=forbidden",
        "CROSS_MODULE_ACCESS=through_capsules_only",
        "LEGACY_REFACTOR=reduce_when_benefit_exceeds_cost_risk",
        "LEGACY_RESIDUALS=document_and_verify",
        "FINAL_GATE=verify_capsule_first_boundaries_and_documented_residuals_before_final",
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
        "SECRETS:",
        "values=never_store_in_MegaVault_or_Git",
        "secrets=follow_SECRETS_section",
        "secret_handling=read_only_when_task_requires;canonical_root_first;canonical_paths_from_database;reprompt_for_known_path_forbidden;rotation_manual_explicit_only",
    ),
    "project_id_authority": (
        "project_id_source=megavault.sqlite:projects+project_aliases_only;INTEGER_PRIMARY_KEY",
        "project_lifecycle=never_delete_project;archive_only;never_reuse_project_id;ids_unique_permanent_not_dense",
    ),
    "prompt_id_policy": (
        "prompt_id_identity=one_materialized_prompt_one_new_id_absolute",
        "prompt_id_revision=any_textual_or_semantic_change_requires_new_id",
        "prompt_id_reuse=forbidden_forever",
        "prompt_id_parentage=parent_prompt_id_only;id_inheritance=forbidden",
        "prompt_id_allocator=centralized_registry+CSPRNG+SQLite_PRIMARY_KEY+transaction",
        "prompt_id_content_hash=audit_only;deduplication=forbidden",
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


class TagNotFoundError(ValueError):
    """Raised when incident tagging references an unknown canonical tag or alias."""


class MegaVaultConnection(sqlite3.Connection):
    """SQLite connection with a defensive finalizer for short-lived CLI reads."""

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


def connect(path: Path | str | None = None) -> sqlite3.Connection:
    conn = sqlite3.connect(path or DB, factory=MegaVaultConnection)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


PROMPT_ID_MIN = 100_000
PROMPT_ID_SPACE = 900_000
PROMPT_ID_STATUSES = ("allocated", "materialized", "used", "cancelled")


def ensure_prompt_id_schema(conn: sqlite3.Connection) -> bool:
    required_objects = {
        "table": {"prompt_id_registry", "prompt_id_events"},
        "index": {
            "idx_prompt_id_parent",
            "idx_prompt_id_project_created",
            "idx_prompt_id_status",
            "idx_prompt_id_events_prompt",
        },
        "trigger": {
            "prompt_id_registry_no_delete",
            "prompt_id_identity_immutable",
            "prompt_id_hash_immutable_after_set",
            "prompt_id_state_transition_guard",
            "prompt_id_events_no_update",
            "prompt_id_events_no_delete",
            "prompt_id_event_allocated",
            "prompt_id_event_state_change",
        },
    }
    existing = {
        kind: {
            row[0]
            for row in conn.execute(
                "select name from sqlite_master where type=?",
                (kind,),
            )
        }
        for kind in required_objects
    }
    changed = any(
        not names.issubset(existing[kind])
        for kind, names in required_objects.items()
    )

    execute_statements(
        conn,
        """
        CREATE TABLE IF NOT EXISTS prompt_id_registry (
          prompt_id INTEGER PRIMARY KEY
            CHECK (prompt_id BETWEEN 100000 AND 999999),
          parent_prompt_id INTEGER
            REFERENCES prompt_id_registry(prompt_id)
            ON UPDATE CASCADE ON DELETE RESTRICT,
          project_id INTEGER
            REFERENCES projects(project_id)
            ON UPDATE CASCADE ON DELETE SET NULL,
          source TEXT NOT NULL,
          status TEXT NOT NULL DEFAULT 'allocated'
            CHECK (status IN ('allocated', 'materialized', 'used', 'cancelled')),
          content_sha256 TEXT
            CHECK (
              content_sha256 IS NULL OR (
                length(content_sha256)=64
                AND content_sha256 NOT GLOB '*[^0-9a-f]*'
              )
            ),
          created_at_utc TEXT NOT NULL
            DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
          materialized_at_utc TEXT,
          used_at_utc TEXT,
          cancelled_at_utc TEXT,
          CHECK (parent_prompt_id IS NULL OR parent_prompt_id <> prompt_id),
          CHECK (
            (
              status='allocated'
              AND content_sha256 IS NULL
              AND materialized_at_utc IS NULL
              AND used_at_utc IS NULL
              AND cancelled_at_utc IS NULL
            )
            OR
            (
              status='materialized'
              AND content_sha256 IS NOT NULL
              AND materialized_at_utc IS NOT NULL
              AND used_at_utc IS NULL
              AND cancelled_at_utc IS NULL
            )
            OR
            (
              status='used'
              AND content_sha256 IS NOT NULL
              AND materialized_at_utc IS NOT NULL
              AND used_at_utc IS NOT NULL
              AND cancelled_at_utc IS NULL
            )
            OR
            (
              status='cancelled'
              AND used_at_utc IS NULL
              AND cancelled_at_utc IS NOT NULL
              AND (
                (
                  content_sha256 IS NULL
                  AND materialized_at_utc IS NULL
                )
                OR
                (
                  content_sha256 IS NOT NULL
                  AND materialized_at_utc IS NOT NULL
                )
              )
            )
          )
        );
        CREATE INDEX IF NOT EXISTS idx_prompt_id_parent
          ON prompt_id_registry(parent_prompt_id);
        CREATE INDEX IF NOT EXISTS idx_prompt_id_project_created
          ON prompt_id_registry(project_id, created_at_utc);
        CREATE INDEX IF NOT EXISTS idx_prompt_id_status
          ON prompt_id_registry(status, created_at_utc);
        CREATE TABLE IF NOT EXISTS prompt_id_events (
          event_id INTEGER PRIMARY KEY AUTOINCREMENT,
          prompt_id INTEGER NOT NULL
            REFERENCES prompt_id_registry(prompt_id)
            ON UPDATE CASCADE ON DELETE RESTRICT,
          event_type TEXT NOT NULL
            CHECK (event_type IN ('allocated', 'materialized', 'used', 'cancelled')),
          event_at_utc TEXT NOT NULL
            DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now')),
          detail TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_prompt_id_events_prompt
          ON prompt_id_events(prompt_id, event_id);
        """,
    )

    triggers = (
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_registry_no_delete
        BEFORE DELETE ON prompt_id_registry
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_REUSE_FORBIDDEN');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_identity_immutable
        BEFORE UPDATE OF
          prompt_id, parent_prompt_id, project_id, source, created_at_utc
        ON prompt_id_registry
        WHEN
          NEW.prompt_id IS NOT OLD.prompt_id
          OR NEW.parent_prompt_id IS NOT OLD.parent_prompt_id
          OR NEW.project_id IS NOT OLD.project_id
          OR NEW.source IS NOT OLD.source
          OR NEW.created_at_utc IS NOT OLD.created_at_utc
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_IDENTITY_IMMUTABLE');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_hash_immutable_after_set
        BEFORE UPDATE OF content_sha256 ON prompt_id_registry
        WHEN
          OLD.content_sha256 IS NOT NULL
          AND NEW.content_sha256 IS NOT OLD.content_sha256
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_CONTENT_IMMUTABLE');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_state_transition_guard
        BEFORE UPDATE OF status ON prompt_id_registry
        WHEN
          NEW.status IS NOT OLD.status
          AND NOT (
            (OLD.status='allocated' AND NEW.status IN ('materialized', 'cancelled'))
            OR
            (OLD.status='materialized' AND NEW.status IN ('used', 'cancelled'))
          )
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_INVALID_STATE_TRANSITION');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_events_no_update
        BEFORE UPDATE ON prompt_id_events
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_EVENT_IMMUTABLE');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_events_no_delete
        BEFORE DELETE ON prompt_id_events
        BEGIN
          SELECT RAISE(ABORT, 'PROMPT_ID_EVENT_IMMUTABLE');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_event_allocated
        AFTER INSERT ON prompt_id_registry
        BEGIN
          INSERT INTO prompt_id_events(prompt_id, event_type)
          VALUES (NEW.prompt_id, 'allocated');
        END
        """,
        """
        CREATE TRIGGER IF NOT EXISTS prompt_id_event_state_change
        AFTER UPDATE OF status ON prompt_id_registry
        WHEN NEW.status IS NOT OLD.status
        BEGIN
          INSERT INTO prompt_id_events(prompt_id, event_type)
          VALUES (NEW.prompt_id, NEW.status);
        END
        """,
    )
    for trigger_sql in triggers:
        conn.execute(trigger_sql)
    return changed


def allocate_prompt_id(
    db_path: Path | str | None = None,
    *,
    source: str,
    project_id: int | None = None,
    parent_prompt_id: int | None = None,
    busy_timeout_ms: int = 30_000,
) -> int:
    source = source.strip()
    if not source:
        raise ValueError("source must not be empty")
    conn = sqlite3.connect(db_path or DB, timeout=busy_timeout_ms / 1000, isolation_level=None)
    try:
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute(f"PRAGMA busy_timeout={int(busy_timeout_ms)}")
        conn.execute("BEGIN IMMEDIATE")
        if not table_exists(conn, "prompt_id_registry"):
            raise RuntimeError("prompt_id_registry missing; run 'megavault.py migrate' first")
        allocated_count = conn.execute(
            "select count(*) from prompt_id_registry"
        ).fetchone()[0]
        if allocated_count >= PROMPT_ID_SPACE:
            raise RuntimeError("PROMPT_ID space exhausted")
        for _ in range(10_000):
            prompt_id = PROMPT_ID_MIN + secrets.randbelow(PROMPT_ID_SPACE)
            try:
                conn.execute(
                    """
                    INSERT INTO prompt_id_registry(
                      prompt_id, parent_prompt_id, project_id, source
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (prompt_id, parent_prompt_id, project_id, source),
                )
                conn.execute("COMMIT")
                return prompt_id
            except sqlite3.IntegrityError:
                collision = conn.execute(
                    "select 1 from prompt_id_registry where prompt_id=?",
                    (prompt_id,),
                ).fetchone()
                if collision:
                    continue
                raise
        raise RuntimeError("PROMPT_ID allocation failed after 10000 collision retries")
    except Exception:
        if conn.in_transaction:
            conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()


def backfill_prompt_ids(
    prompt_ids: list[int],
    *,
    source: str,
    db_path: Path | str | None = None,
    busy_timeout_ms: int = 30_000,
) -> tuple[int, int]:
    source = source.strip()
    if not source:
        raise ValueError("source must not be empty")
    if not source.startswith("historical-"):
        raise ValueError("historical backfill source must start with 'historical-'")
    normalized = sorted(set(int(value) for value in prompt_ids))
    invalid = [value for value in normalized if value < PROMPT_ID_MIN or value >= PROMPT_ID_MIN + PROMPT_ID_SPACE]
    if invalid:
        raise ValueError(f"invalid historical PROMPT_ID values: {invalid!r}")
    conn = sqlite3.connect(db_path or DB, timeout=busy_timeout_ms / 1000, isolation_level=None)
    inserted = 0
    existing = 0
    try:
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute(f"PRAGMA busy_timeout={int(busy_timeout_ms)}")
        conn.execute("BEGIN IMMEDIATE")
        if not table_exists(conn, "prompt_id_registry"):
            raise RuntimeError("prompt_id_registry missing; run 'megavault.py migrate' first")
        for prompt_id in normalized:
            try:
                conn.execute(
                    """
                    INSERT INTO prompt_id_registry(prompt_id, source)
                    VALUES (?, ?)
                    """,
                    (prompt_id, source),
                )
                inserted += 1
            except sqlite3.IntegrityError:
                row = conn.execute(
                    """
                    select prompt_id, source
                    from prompt_id_registry
                    where prompt_id=?
                    """,
                    (prompt_id,),
                ).fetchone()
                if not row:
                    raise
                if not str(row[1]).startswith("historical-"):
                    raise RuntimeError(
                        f"historical PROMPT_ID collides with non-historical reservation: {prompt_id}"
                    )
                existing += 1
        conn.execute("COMMIT")
        return inserted, existing
    except Exception:
        if conn.in_transaction:
            conn.execute("ROLLBACK")
        raise
    finally:
        conn.close()


def parse_prompt_id_file(path: Path | str) -> list[int]:
    values: list[int] = []
    for line_number, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        text = raw.strip()
        if not text or text.startswith("#"):
            continue
        if not re.fullmatch(r"\d{6}", text):
            raise ValueError(f"invalid PROMPT_ID at line {line_number}: {text!r}")
        values.append(int(text))
    return values



PROMPT_ID_TEXT_PATTERNS = (
    re.compile(r"\bPROMPT_ID\s*=\s*(\d{6})\b", re.I),
    re.compile(r"""["']prompt_id["']\s*:\s*["']?(\d{6})\b""", re.I),
)
PROMPT_ID_SCAN_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".jsonl",
    ".yaml",
    ".yml",
    ".toml",
    ".py",
    ".sh",
    ".kt",
    ".kts",
    ".xml",
    ".csv",
}


def extract_prompt_ids(text: str) -> set[int]:
    values: set[int] = set()
    for pattern in PROMPT_ID_TEXT_PATTERNS:
        values.update(int(match.group(1)) for match in pattern.finditer(text))
    return values


def prompt_ids_from_git_history(repo: Path | str) -> set[int]:
    root = Path(repo).expanduser()
    if not (root / ".git").exists():
        raise ValueError(f"not a git worktree: {root}")
    proc = subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "log",
            "--all",
            "-G",
            "PROMPT_ID",
            "-p",
            "--no-ext-diff",
            "--text",
            "--format=",
        ],
        text=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git history scan failed for {root}: {stderr}")
    values = extract_prompt_ids(proc.stdout.decode("utf-8", errors="ignore"))
    current = subprocess.run(
        ["git", "-C", str(root), "grep", "-I", "-h", "-E", "PROMPT_ID|prompt_id", "HEAD"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if current.returncode not in (0, 1):
        raise RuntimeError(
            f"git tree scan failed for {root}: {current.stderr.strip()}"
        )
    values.update(extract_prompt_ids(current.stdout))
    return values


def prompt_ids_from_prompt_dir(root: Path | str) -> set[int]:
    base = Path(root).expanduser()
    prompts = base / "prompts"
    if not prompts.is_dir():
        raise ValueError(f"prompt directory missing: {prompts}")
    return {
        int(child.name)
        for child in prompts.iterdir()
        if child.is_dir() and re.fullmatch(r"\d{6}", child.name)
    }


def prompt_ids_from_text_tree(root: Path | str, *, max_file_bytes: int = 20_000_000) -> set[int]:
    base = Path(root).expanduser()
    if not base.is_dir():
        raise ValueError(f"text tree missing: {base}")
    values: set[int] = set()
    prompt_dir = base / "prompts"
    if prompt_dir.is_dir():
        values.update(
            int(child.name)
            for child in prompt_dir.iterdir()
            if child.is_dir() and re.fullmatch(r"\d{6}", child.name)
        )
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in PROMPT_ID_SCAN_SUFFIXES:
            continue
        try:
            if path.stat().st_size > max_file_bytes:
                continue
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        values.update(extract_prompt_ids(raw))
    return values


def create_prompt_id_backup(
    db_path: Path | str | None = None,
    *,
    output_dir: Path | str | None = None,
) -> Path:
    source_path = Path(db_path or DB)
    if not source_path.is_file():
        raise ValueError(f"database missing: {source_path}")
    target_dir = Path(output_dir).expanduser() if output_dir else Path(tempfile.gettempdir())
    target_dir.mkdir(parents=True, exist_ok=True)
    fd, raw_path = tempfile.mkstemp(
        prefix="megavault-prompt-id-",
        suffix=".sqlite",
        dir=target_dir,
    )
    os.close(fd)
    target = Path(raw_path)
    os.chmod(target, 0o600)
    source = sqlite3.connect(source_path)
    destination = sqlite3.connect(target)
    try:
        source.backup(destination)
    except Exception:
        destination.close()
        source.close()
        target.unlink(missing_ok=True)
        raise
    else:
        destination.close()
        source.close()
    if target.stat().st_mode & 0o777 != 0o600:
        target.unlink(missing_ok=True)
        raise RuntimeError("backup permissions are not 0600")
    return target


def backfill_prompt_ids_from_sources(
    *,
    source: str,
    git_repos: list[str] | None = None,
    prompt_dir_roots: list[str] | None = None,
    text_trees: list[str] | None = None,
    optional_text_trees: list[str] | None = None,
    required_ids: list[int] | None = None,
    db_path: Path | str | None = None,
) -> tuple[int, int, int, int]:
    values: set[int] = set()
    source_count = 0
    optional_missing = 0
    for repo in git_repos or []:
        values.update(prompt_ids_from_git_history(repo))
        source_count += 1
    for root in prompt_dir_roots or []:
        values.update(prompt_ids_from_prompt_dir(root))
        source_count += 1
    for root in text_trees or []:
        values.update(prompt_ids_from_text_tree(root))
        source_count += 1
    for root in optional_text_trees or []:
        path = Path(root).expanduser()
        if not path.is_dir():
            optional_missing += 1
            continue
        values.update(prompt_ids_from_text_tree(path))
        source_count += 1
    missing_required = sorted(set(required_ids or []) - values)
    if missing_required:
        raise ValueError(f"required PROMPT_ID values missing from sources: {missing_required!r}")
    if not values:
        raise ValueError("historical PROMPT_ID discovery returned zero IDs")
    inserted, existing = backfill_prompt_ids(
        sorted(values),
        source=source,
        db_path=db_path,
    )
    return len(values), inserted, existing, optional_missing


def prompt_id_backup_command(args: argparse.Namespace) -> int:
    try:
        path = create_prompt_id_backup(output_dir=args.output_dir)
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_BACKUP=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"backup_path={path}")
    print("mode=0600")
    return 0


def prompt_id_backfill_sources_command(args: argparse.Namespace) -> int:
    try:
        total, inserted, existing, optional_missing = backfill_prompt_ids_from_sources(
            source=args.source,
            git_repos=args.git_repo,
            prompt_dir_roots=args.prompt_dir_root,
            text_trees=args.text_tree,
            optional_text_trees=args.optional_text_tree,
            required_ids=args.require_id,
        )
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_BACKFILL_SOURCES=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"discovered={total}")
    print(f"inserted={inserted}")
    print(f"already_reserved={existing}")
    print(f"optional_missing={optional_missing}")
    return 0


def prompt_content_sha256(path: Path | str) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def materialize_prompt_id(
    prompt_id: int,
    *,
    content_sha256: str,
    db_path: Path | str | None = None,
) -> None:
    digest = content_sha256.strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("content_sha256 must be exactly 64 lowercase hex characters")
    conn = connect(db_path)
    try:
        with conn:
            changed = conn.execute(
                """
                UPDATE prompt_id_registry
                SET status='materialized',
                    content_sha256=?,
                    materialized_at_utc=strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                WHERE prompt_id=?
                  AND status='allocated'
                  AND source NOT LIKE 'historical-%'
                """,
                (digest, prompt_id),
            ).rowcount
        if changed != 1:
            raise ValueError(f"prompt_id not allocatable for materialization: {prompt_id}")
    finally:
        conn.close()


def mark_prompt_id_used(
    prompt_id: int,
    *,
    db_path: Path | str | None = None,
) -> None:
    conn = connect(db_path)
    try:
        with conn:
            changed = conn.execute(
                """
                UPDATE prompt_id_registry
                SET status='used',
                    used_at_utc=strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                WHERE prompt_id=? AND status='materialized'
                """,
                (prompt_id,),
            ).rowcount
        if changed != 1:
            raise ValueError(f"prompt_id not materialized or already terminal: {prompt_id}")
    finally:
        conn.close()


def cancel_prompt_id(
    prompt_id: int,
    *,
    db_path: Path | str | None = None,
) -> None:
    conn = connect(db_path)
    try:
        with conn:
            changed = conn.execute(
                """
                UPDATE prompt_id_registry
                SET status='cancelled',
                    cancelled_at_utc=strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
                WHERE prompt_id=?
                  AND status IN ('allocated', 'materialized')
                  AND source NOT LIKE 'historical-%'
                """,
                (prompt_id,),
            ).rowcount
        if changed != 1:
            raise ValueError(f"prompt_id not cancellable or already terminal: {prompt_id}")
    finally:
        conn.close()


def smoke_prompt_id(
    *,
    source: str = "activation-smoke",
    project_id: int | None = None,
    db_path: Path | str | None = None,
) -> int:
    prompt_id = allocate_prompt_id(
        db_path,
        source=source,
        project_id=project_id,
    )
    conn = connect(db_path)
    try:
        row = conn.execute(
            "select status from prompt_id_registry where prompt_id=?",
            (prompt_id,),
        ).fetchone()
        if not row or row[0] != "allocated":
            raise RuntimeError(f"PROMPT_ID smoke allocation missing: {prompt_id}")
    finally:
        conn.close()
    cancel_prompt_id(prompt_id, db_path=db_path)
    conn = connect(db_path)
    try:
        row = conn.execute(
            "select status from prompt_id_registry where prompt_id=?",
            (prompt_id,),
        ).fetchone()
        if not row or row[0] != "cancelled":
            raise RuntimeError(f"PROMPT_ID smoke cancellation failed: {prompt_id}")
    finally:
        conn.close()
    return prompt_id


def prompt_id_allocate_command(args: argparse.Namespace) -> int:
    try:
        prompt_id = allocate_prompt_id(
            source=args.source,
            project_id=args.project_id,
            parent_prompt_id=args.parent_prompt_id,
        )
    except (RuntimeError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_ALLOCATE=FAIL {exc}", file=sys.stderr)
        return 1
    print(prompt_id)
    return 0


def prompt_id_backfill_command(args: argparse.Namespace) -> int:
    try:
        values = parse_prompt_id_file(args.ids_file)
        inserted, existing = backfill_prompt_ids(values, source=args.source)
    except (OSError, RuntimeError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_BACKFILL=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"inserted={inserted}")
    print(f"already_reserved={existing}")
    return 0


def prompt_id_materialize_command(args: argparse.Namespace) -> int:
    try:
        digest = prompt_content_sha256(args.content_file)
        materialize_prompt_id(args.prompt_id, content_sha256=digest)
    except (OSError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_MATERIALIZE=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"prompt_id={args.prompt_id}")
    print(f"content_sha256={digest}")
    print("status=materialized")
    return 0


def prompt_id_mark_used_command(args: argparse.Namespace) -> int:
    try:
        mark_prompt_id_used(args.prompt_id)
    except (ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_MARK_USED=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"prompt_id={args.prompt_id}")
    print("status=used")
    return 0


def prompt_id_cancel_command(args: argparse.Namespace) -> int:
    try:
        cancel_prompt_id(args.prompt_id)
    except (ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_CANCEL=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"prompt_id={args.prompt_id}")
    print("status=cancelled")
    return 0


def prompt_id_smoke_command(args: argparse.Namespace) -> int:
    try:
        prompt_id = smoke_prompt_id(
            source=args.source,
            project_id=args.project_id,
        )
    except (RuntimeError, ValueError, sqlite3.Error) as exc:
        print(f"PROMPT_ID_SMOKE=FAIL {exc}", file=sys.stderr)
        return 1
    print(f"prompt_id={prompt_id}")
    print("status=cancelled")
    return 0


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
        raise TagNotFoundError(
            f"tag or alias not found: {name_or_alias!r}; "
            "create it explicitly with 'megavault.py tag'"
        )
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


def ensure_view(conn: sqlite3.Connection, name: str, view_sql: str) -> None:
    current = conn.execute(
        """
        select sql
        from sqlite_master
        where type='view' and name=?
        """,
        (name,),
    ).fetchone()
    if current and normalized_sql(current[0]) == normalized_sql(view_sql):
        return
    conn.execute(f"DROP VIEW IF EXISTS {name}")
    conn.execute(view_sql)


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
    for dependent_view in (
        "codex_work_queue",
        "codex_remote_projects",
        "codex_missing_projects",
        "codex_archived_projects",
    ):
        conn.execute(f"DROP VIEW IF EXISTS {dependent_view}")
    ensure_view(conn, "codex_project_index", view_sql)


def ensure_codex_retrieval_views(conn: sqlite3.Connection) -> None:
    operational_fields = """
          project_id,
          slug,
          project_status,
          canonical_host,
          canonical_worktree,
          runtime_host,
          runtime_path,
          canonical_branch,
          remote_url
    """
    ensure_view(
        conn,
        "codex_work_queue",
        f"""
        CREATE VIEW codex_work_queue AS
        SELECT
{operational_fields}
        FROM codex_project_index
        WHERE project_status IN ('LOCAL', 'REMOTE_ONLY')
        ORDER BY project_id
        """,
    )
    ensure_view(
        conn,
        "codex_remote_projects",
        f"""
        CREATE VIEW codex_remote_projects AS
        SELECT
{operational_fields}
        FROM codex_project_index
        WHERE project_status='REMOTE_ONLY'
        ORDER BY project_id
        """,
    )
    ensure_view(
        conn,
        "codex_missing_projects",
        """
        CREATE VIEW codex_missing_projects AS
        SELECT
          project_id,
          slug,
          project_status
        FROM codex_project_index
        WHERE project_status='MISSING'
        ORDER BY project_id
        """,
    )
    ensure_view(
        conn,
        "codex_archived_projects",
        """
        CREATE VIEW codex_archived_projects AS
        SELECT
          project_id,
          slug,
          project_status
        FROM codex_project_index
        WHERE project_status='ARCHIVED'
        ORDER BY project_id
        """,
    )


PROJECT_CONTEXT_COMPONENTS = (
    (
        8,
        "usage_monitor_entrypoint",
        "python_entrypoint",
        "/home/daniele/projects/codex-usage-monitor/codex_usage_monitor.py",
        "Collects Codex usage limits, persists SQLite snapshots, and dispatches eligible Telegram notifications.",
    ),
    (
        8,
        "session_archive_entrypoint",
        "python_entrypoint",
        "/home/daniele/projects/codex-usage-monitor/codex_session_archive.py",
        "Imports native Codex session JSONL into private raw, normalized, markdown, manifest, and SQLite archive outputs.",
    ),
    (
        8,
        "curated_vault_entrypoint",
        "python_entrypoint",
        "/home/daniele/projects/codex-usage-monitor/codex_curated_vault.py",
        "Builds compact AI-readable session memory from normalized archive records.",
    ),
    (
        8,
        "systemd_units",
        "systemd_config",
        "/home/daniele/projects/codex-usage-monitor/systemd",
        "Defines Oracle quota monitor service/timer and Fedora user session archive service/timer.",
    ),
    (
        23,
        "core_cli_schema_validator",
        "python_module",
        "/home/daniele/MegaVault/ai/megavault_core.py",
        "Owns MegaVault schema migrations, canonical views, validator checks, and CLI commands.",
    ),
    (
        23,
        "strict_tag_wrapper",
        "python_module",
        "/home/daniele/MegaVault/ai/strict_tag_wrapper.py",
        "Wraps incident tag policy and exports the canonical megavault.py command surface.",
    ),
    (
        23,
        "canonical_sqlite",
        "sqlite_database",
        "/home/daniele/MegaVault/megavault.sqlite",
        "Canonical structured facts for projects, repositories, services, incidents, data assets, and Codex context.",
    ),
    (
        23,
        "targeted_tests",
        "test_suite",
        "/home/daniele/MegaVault/tests/test_megavault.py",
        "Focused tests for validation, project routing views, migrations, and compact context retrieval.",
    ),
    (
        49,
        "android_app_module",
        "gradle_module",
        "/home/daniele/projects/PersonalHub/app",
        "Android application shell; reads version.txt for versionCode/versionName and names debug APK as <version>.apk.",
    ),
    (
        49,
        "core_database_module",
        "gradle_module",
        "/home/daniele/projects/PersonalHub/core/database",
        "Single Room database, SAF import/export, rollback, auto-export, and Datasette sync boundary.",
    ),
    (
        49,
        "feature_modules",
        "gradle_modules",
        "/home/daniele/projects/PersonalHub/feature",
        "Included feature modules: luoghi, multitimetracker, sostanze, supercontacts, and wordpulse.",
    ),
    (
        49,
        "operating_rules",
        "project_manifest",
        "/home/daniele/projects/PersonalHub/AGENTS.md",
        "Stable project rules for version increments, single personalhub.db, import/export safety, and APK naming.",
    ),
)


PROJECT_CONTEXT_OPERATIONS = (
    (
        8,
        "monitor_once",
        "/usr/bin/python3 /home/ubuntu/codex-usage-monitor/codex_usage_monitor.py once",
        "Collect one Oracle-hosted Codex usage snapshot and notify only eligible changes.",
        "oracle-vm",
        "/home/ubuntu/codex-usage-monitor",
        "medium",
        "Uses app-server source and runtime SQLite; keep secrets in configured env files, never in chat.",
    ),
    (
        8,
        "monitor_status",
        "python3 codex_usage_monitor.py status",
        "Read latest monitor SQLite state as JSON.",
        "fedora",
        "/home/daniele/projects/codex-usage-monitor",
        "low",
        "Read-oriented status command; initializes schema if needed.",
    ),
    (
        8,
        "session_archive_import",
        "python3 codex_session_archive.py --archive-root /home/daniele/.local/share/codex-session-archive import",
        "Import native Codex sessions into the private Fedora archive.",
        "fedora",
        "/home/daniele/projects/codex-usage-monitor",
        "medium",
        "Systemd user service also runs task costs and curated vault after import.",
    ),
    (
        8,
        "session_archive_verify",
        "python3 codex_session_archive.py --archive-root /home/daniele/.local/share/codex-session-archive verify",
        "Verify archived session hashes and normalized JSONL parsing.",
        "fedora",
        "/home/daniele/projects/codex-usage-monitor",
        "low",
        "Use before trusting archive records for future context.",
    ),
    (
        23,
        "validate",
        "PYTHONDONTWRITEBYTECODE=1 python3 megavault.py validate",
        "Run MegaVault integrity, FK, schema, protocol, registry, and secret-scan checks.",
        "fedora",
        "/home/daniele/MegaVault",
        "low",
        "Required final gate after MegaVault changes.",
    ),
    (
        23,
        "migrate",
        "PYTHONDONTWRITEBYTECODE=1 python3 megavault.py migrate",
        "Apply idempotent SQLite migrations and canonical view refreshes.",
        "fedora",
        "/home/daniele/MegaVault",
        "medium",
        "Run against existing DB only when schema or derived canonical facts changed.",
    ),
    (
        23,
        "unit_tests",
        "PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -q",
        "Run MegaVault standard-library tests.",
        "fedora",
        "/home/daniele/MegaVault",
        "low",
        "Targeted suite covers migration idempotence and CLI retrieval.",
    ),
    (
        23,
        "project_context",
        "PYTHONDONTWRITEBYTECODE=1 python3 megavault.py codex-project-context PROJECT_ID",
        "Print compact routing, component, and operation context for one project_id.",
        "fedora",
        "/home/daniele/MegaVault",
        "low",
        "Use before exploring a governed checkout.",
    ),
    (
        49,
        "unit_tests",
        "./gradlew test",
        "Run JVM/unit tests for PersonalHub modules.",
        "fedora",
        "/home/daniele/projects/PersonalHub",
        "low",
        "Use before Android package or database behavior claims.",
    ),
    (
        49,
        "assemble_debug",
        "./gradlew assembleDebug --no-configuration-cache",
        "Build signed debug APK named from version.txt.",
        "fedora",
        "/home/daniele/projects/PersonalHub",
        "medium",
        "APK/device tasks require canonical Android signing env and no configuration cache.",
    ),
    (
        49,
        "connected_android_tests",
        "./gradlew connectedDebugAndroidTest --no-configuration-cache",
        "Run emulator/device integration tests for DB export/import and app flows.",
        "fedora",
        "/home/daniele/projects/PersonalHub",
        "high",
        "Requires live adb target; do not claim device validation without live evidence.",
    ),
)


def ensure_project_context_schema(conn: sqlite3.Connection) -> bool:
    changed = False
    before = conn.total_changes
    execute_statements(
        conn,
        """
        CREATE TABLE IF NOT EXISTS project_components (
          component_id INTEGER PRIMARY KEY AUTOINCREMENT,
          project_id INTEGER NOT NULL REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE RESTRICT,
          component TEXT NOT NULL,
          type TEXT NOT NULL,
          path TEXT NOT NULL,
          purpose TEXT NOT NULL,
          UNIQUE(project_id, component)
        );
        CREATE INDEX IF NOT EXISTS idx_project_components_project
          ON project_components(project_id, type, component);
        CREATE TABLE IF NOT EXISTS project_operations (
          operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
          project_id INTEGER NOT NULL REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE RESTRICT,
          operation TEXT NOT NULL,
          command TEXT NOT NULL,
          scope TEXT NOT NULL,
          host TEXT,
          workdir TEXT,
          risk_level TEXT NOT NULL CHECK(risk_level IN ('low', 'medium', 'high')),
          notes TEXT,
          UNIQUE(project_id, operation)
        );
        CREATE INDEX IF NOT EXISTS idx_project_operations_project
          ON project_operations(project_id, risk_level, operation);
        """
    )
    changed = changed or conn.total_changes > before
    for row in PROJECT_CONTEXT_COMPONENTS:
        before = conn.total_changes
        conn.execute(
            """
            INSERT INTO project_components(project_id, component, type, path, purpose)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(project_id, component) DO UPDATE SET
              type=excluded.type,
              path=excluded.path,
              purpose=excluded.purpose
            WHERE type IS NOT excluded.type
               OR path IS NOT excluded.path
               OR purpose IS NOT excluded.purpose
            """,
            row,
        )
        changed = changed or conn.total_changes > before
    for row in PROJECT_CONTEXT_OPERATIONS:
        before = conn.total_changes
        conn.execute(
            """
            INSERT INTO project_operations(
              project_id, operation, command, scope, host, workdir, risk_level, notes
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(project_id, operation) DO UPDATE SET
              command=excluded.command,
              scope=excluded.scope,
              host=excluded.host,
              workdir=excluded.workdir,
              risk_level=excluded.risk_level,
              notes=excluded.notes
            WHERE command IS NOT excluded.command
               OR scope IS NOT excluded.scope
               OR host IS NOT excluded.host
               OR workdir IS NOT excluded.workdir
               OR risk_level IS NOT excluded.risk_level
               OR notes IS NOT excluded.notes
            """,
            row,
        )
        changed = changed or conn.total_changes > before
    ensure_view(
        conn,
        "codex_project_context",
        """
        CREATE VIEW codex_project_context AS
        SELECT
          i.project_id,
          i.slug,
          i.project_status,
          i.canonical_host,
          i.canonical_worktree,
          i.runtime_host,
          i.runtime_path,
          i.canonical_branch,
          i.remote_url,
          coalesce((
            SELECT group_concat(component_line, '|')
            FROM (
              SELECT component || ':' || type || ':' || path || ':' || purpose AS component_line
              FROM project_components pc
              WHERE pc.project_id=i.project_id
              ORDER BY component
            )
          ), '') AS components,
          coalesce((
            SELECT group_concat(operation_line, '|')
            FROM (
              SELECT operation || ':' || risk_level || ':' || coalesce(host, '') || ':' ||
                     coalesce(workdir, '') || ':' || command || ':' || scope ||
                     CASE WHEN notes IS NULL OR notes='' THEN '' ELSE ':' || notes END AS operation_line
              FROM project_operations po
              WHERE po.project_id=i.project_id
              ORDER BY operation
            )
          ), '') AS operations
        FROM codex_project_index i
        """
    )
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
    ensure_codex_retrieval_views(conn)
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
    if not current_version or int(current_version[0]) < 7:
        conn.execute(
            "insert or replace into schema_meta(key, value) values ('schema_version', '7')"
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
        "project_components",
        "project_operations",
        "prompt_id_registry",
        "prompt_id_events",
    }
    missing = sorted(table for table in required_tables if not table_exists(conn, table))
    if missing:
        errors.append(f"missing required tables: {missing}")
        return errors
    mutable_historical = conn.execute(
        """
        select prompt_id, status, source
        from prompt_id_registry
        where source like 'historical-%'
          and status<>'allocated'
        order by prompt_id
        """
    ).fetchall()
    if mutable_historical:
        errors.append(
            f"historical PROMPT_ID reservations must remain allocated+immutable: {mutable_historical!r}"
        )

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
        retrieval_view_rules = (
            (
                "codex_work_queue",
                "select count(*) from codex_project_index where project_status in ('LOCAL', 'REMOTE_ONLY')",
                "project_status in ('LOCAL', 'REMOTE_ONLY')",
            ),
            (
                "codex_remote_projects",
                "select count(*) from codex_project_index where project_status='REMOTE_ONLY'",
                "project_status='REMOTE_ONLY'",
            ),
            (
                "codex_missing_projects",
                "select count(*) from codex_project_index where project_status='MISSING'",
                "project_status='MISSING'",
            ),
            (
                "codex_archived_projects",
                "select count(*) from codex_project_index where project_status='ARCHIVED'",
                "project_status='ARCHIVED'",
            ),
        )
        for view_name, expected_sql, status_predicate in retrieval_view_rules:
            if not table_exists(conn, view_name):
                errors.append(f"missing {view_name} view")
                continue
            expected_count = conn.execute(expected_sql).fetchone()[0]
            actual_count = conn.execute(f"select count(*) from {view_name}").fetchone()[0]
            if actual_count != expected_count:
                errors.append(
                    f"{view_name} row count mismatch: expected={expected_count} actual={actual_count}"
                )
            invalid_rows = conn.execute(
                f"""
                select project_id, project_status
                from {view_name}
                where not ({status_predicate})
                order by project_id
                """
            ).fetchall()
            if invalid_rows:
                errors.append(f"{view_name} invalid rows: {invalid_rows!r}")
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
    for table in ("project_components", "project_operations"):
        if table_exists(conn, table):
            unexpected_context_projects = conn.execute(
                f"""
                select distinct project_id
                from {table}
                where project_id not in (8, 23, 49)
                order by project_id
                """
            ).fetchall()
            if unexpected_context_projects:
                errors.append(
                    f"{table} contains out-of-scope project_id rows: {unexpected_context_projects!r}"
                )
    if table_exists(conn, "project_components"):
        component_counts = dict(
            conn.execute(
                """
                select project_id, count(*)
                from project_components
                group by project_id
                """
            ).fetchall()
        )
        for project_id in (8, 23, 49):
            if component_counts.get(project_id, 0) == 0:
                errors.append(f"project_components missing project_id={project_id}")
    if table_exists(conn, "project_operations"):
        operation_counts = dict(
            conn.execute(
                """
                select project_id, count(*)
                from project_operations
                group by project_id
                """
            ).fetchall()
        )
        for project_id in (8, 23, 49):
            if operation_counts.get(project_id, 0) == 0:
                errors.append(f"project_operations missing project_id={project_id}")
    if not table_exists(conn, "codex_project_context"):
        errors.append("missing codex_project_context view")
    else:
        context_count = conn.execute("select count(*) from codex_project_context").fetchone()[0]
        project_count = conn.execute("select count(*) from projects").fetchone()[0]
        if context_count != project_count:
            errors.append(
                f"codex_project_context row count mismatch: projects={project_count} view={context_count}"
            )
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
    if table_exists(conn, "prompt_id_registry"):
        invalid_prompt_ids = conn.execute(
            """
            select prompt_id
            from prompt_id_registry
            where prompt_id < 100000 or prompt_id > 999999
            order by prompt_id
            """
        ).fetchall()
        if invalid_prompt_ids:
            errors.append(f"invalid PROMPT_ID values: {invalid_prompt_ids!r}")
        duplicate_prompt_ids = conn.execute(
            """
            select prompt_id, count(*)
            from prompt_id_registry
            group by prompt_id
            having count(*) > 1
            """
        ).fetchall()
        if duplicate_prompt_ids:
            errors.append(f"duplicate PROMPT_ID values: {duplicate_prompt_ids!r}")
        orphan_parents = conn.execute(
            """
            select child.prompt_id, child.parent_prompt_id
            from prompt_id_registry child
            left join prompt_id_registry parent
              on parent.prompt_id=child.parent_prompt_id
            where child.parent_prompt_id is not null
              and parent.prompt_id is null
            order by child.prompt_id
            """
        ).fetchall()
        if orphan_parents:
            errors.append(f"orphan PROMPT_ID parents: {orphan_parents!r}")
        required_prompt_triggers = {
            "prompt_id_registry_no_delete",
            "prompt_id_identity_immutable",
            "prompt_id_hash_immutable_after_set",
            "prompt_id_state_transition_guard",
            "prompt_id_events_no_update",
            "prompt_id_events_no_delete",
            "prompt_id_event_allocated",
            "prompt_id_event_state_change",
        }
        current_prompt_triggers = {
            row[0]
            for row in conn.execute(
                "select name from sqlite_master where type='trigger' and name like 'prompt_id_%'"
            )
        }
        missing_prompt_triggers = sorted(required_prompt_triggers - current_prompt_triggers)
        if missing_prompt_triggers:
            errors.append(f"missing PROMPT_ID triggers: {missing_prompt_triggers!r}")

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

    tracked_md = {path for path in tracked if path.endswith(".md")}
    extra_md = sorted(tracked_md - ALLOWED_TRACKED_MARKDOWN)
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
            "project_components",
            "project_operations",
            "prompt_id_registry",
            "prompt_id_events",
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


def print_project_retrieval_rows(rows: list[sqlite3.Row | tuple], fields: tuple[str, ...]) -> None:
    for row in rows:
        print(";".join(f"{field}={value if value is not None else ''}" for field, value in zip(fields, row)))


CODEX_WORK_QUEUE_FIELDS = (
    "project_id",
    "slug",
    "project_status",
    "canonical_host",
    "canonical_worktree",
    "runtime_host",
    "runtime_path",
    "canonical_branch",
    "remote_url",
)
CODEX_STATUS_LIST_FIELDS = ("project_id", "slug", "project_status")


def project_view_command(view_name: str, fields: tuple[str, ...]) -> int:
    conn = connect()
    field_sql = ", ".join(fields)
    rows = conn.execute(
        f"""
        select {field_sql}
        from {view_name}
        order by project_id
        """
    ).fetchall()
    print_project_retrieval_rows(rows, fields)
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


CODEX_PROJECT_CONTEXT_FIELDS = (
    "project_id",
    "slug",
    "project_status",
    "canonical_host",
    "canonical_worktree",
    "runtime_host",
    "runtime_path",
    "canonical_branch",
    "remote_url",
    "components",
    "operations",
)


def codex_project_context_command(project_id: int) -> int:
    conn = connect()
    row = conn.execute(
        """
        select project_id, slug, project_status, canonical_host, canonical_worktree,
               runtime_host, runtime_path, canonical_branch, remote_url,
               components, operations
        from codex_project_context
        where project_id=?
        """,
        (project_id,),
    ).fetchone()
    if not row:
        print(f"CODEX_PROJECT_CONTEXT=NOT_FOUND project_id={project_id}", file=sys.stderr)
        return 1
    print_project_retrieval_rows([row], CODEX_PROJECT_CONTEXT_FIELDS)
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


def normalize_github_remote(url: str) -> str:
    text = url.strip()
    if text.startswith("git@github.com:"):
        text = "https://github.com/" + text.removeprefix("git@github.com:")
    text = text.removesuffix(".git").rstrip("/")
    return text.lower()


def repo_slug(owner: str, name: str) -> str:
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    if not slug:
        raise ValueError("empty repository slug")
    return slug


def next_repository_id(conn: sqlite3.Connection) -> str:
    max_id = 0
    for (repository_id,) in conn.execute("select repository_id from repositories"):
        match = re.fullmatch(r"R(\d+)", str(repository_id))
        if match:
            max_id = max(max_id, int(match.group(1)))
    return f"R{max_id + 1:04d}"


def find_registered_github_repo(conn: sqlite3.Connection, *, slug: str, remote_url: str, worktree: str) -> sqlite3.Row | None:
    normalized = normalize_github_remote(remote_url)
    for row in conn.execute(
        """
        select p.project_id, p.slug, r.repository_id, r.remote_url, r.worktree_path
        from projects p
        left join repositories r on r.project_id=p.project_id
        where p.slug=? or r.worktree_path=?
        """,
        (slug, worktree),
    ):
        return row
    for row in conn.execute(
        """
        select p.project_id, p.slug, r.repository_id, r.remote_url, r.worktree_path
        from repositories r
        join projects p on p.project_id=r.project_id
        where r.remote_url is not null
        """
    ):
        if normalize_github_remote(str(row[3])) == normalized:
            return row
    alias_row = conn.execute(
        """
        select p.project_id, p.slug, null as repository_id, null as remote_url, null as worktree_path
        from project_aliases a
        join projects p on p.project_id=a.project_id
        where a.alias in (?, ?)
        """,
        (slug, normalized.removeprefix("https://github.com/")),
    ).fetchone()
    return alias_row


def register_github_repo_command(args: argparse.Namespace) -> int:
    owner = args.owner.strip()
    name = args.name.strip()
    remote_url = args.remote_url.strip()
    default_branch = args.default_branch.strip() or "UNKNOWN"
    worktree = str(Path(args.worktree).expanduser())
    slug = repo_slug(owner, name)
    if normalize_github_remote(remote_url) != f"https://github.com/{owner.lower()}/{name.lower()}":
        print("REGISTER_GITHUB_REPO=FAIL remote_url_owner_name_mismatch", file=sys.stderr)
        return 2
    conn = connect()
    existing = find_registered_github_repo(conn, slug=slug, remote_url=remote_url, worktree=worktree)
    if existing:
        print(f"project_id={existing[0]}")
        print(f"slug={existing[1]}")
        print("status=already_registered")
        return 0
    with conn:
        project_id = int(conn.execute("select coalesce(max(project_id), 0) + 1 from projects").fetchone()[0])
        repository_id = next_repository_id(conn)
        conn.execute(
            """
            insert into projects(project_id, slug, name, status, archived, created_source, notes)
            values(?, ?, ?, 'active', 0, 'github_autosync', ?)
            """,
            (project_id, slug, name, f"Auto-registered from https://github.com/{owner}/{name}; unknown facts intentionally omitted."),
        )
        conn.execute(
            """
            insert into permanent_ids(entity_type, entity_id, canonical_key, created_at_utc)
            values('project', ?, ?, strftime('%Y-%m-%dT%H:%M:%SZ','now'))
            """,
            (project_id, slug),
        )
        conn.execute("insert into project_aliases(alias, project_id) values(?, ?)", (slug, project_id))
        conn.execute(
            """
            insert into repositories(
                repository_id, project_id, location, kind, branch, head, status,
                canonical, repository_kind, host_id, worktree_path, remote_url, runtime_path
            )
            values(?, ?, ?, 'local', ?, null, 'active', 1, 'local_worktree', 'H0001', ?, ?, null)
            """,
            (repository_id, project_id, worktree, None if default_branch == "UNKNOWN" else default_branch, worktree, remote_url.removesuffix(".git")),
        )
    print(f"project_id={project_id}")
    print(f"slug={slug}")
    print(f"repository_id={repository_id}")
    print("status=created")
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
        changed = ensure_project_context_schema(conn) or changed
        changed = ensure_prompt_id_schema(conn) or changed
        conn.execute(
            "insert or replace into schema_meta(key, value) values ('schema_version', ?)",
            (str(SCHEMA_VERSION),),
        )
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
    try:
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
    except TagNotFoundError as exc:
        print(f"INCIDENT_CREATE=TAG_NOT_FOUND {exc}", file=sys.stderr)
        return 1
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
    sub.add_parser("project-work-queue")
    sub.add_parser("project-remote")
    sub.add_parser("project-missing")
    sub.add_parser("project-archived")
    project_context_parser = sub.add_parser("codex-project-context")
    project_context_parser.add_argument("project_id", type=int)
    project_show_parser = sub.add_parser("project-show")
    project_show_parser.add_argument("project_id", type=int)
    project_path_parser = sub.add_parser("project-path")
    project_path_parser.add_argument("--status", action="store_true")
    project_path_parser.add_argument("project_id", type=int)
    prompt_id_parser = sub.add_parser("prompt-id")
    prompt_id_sub = prompt_id_parser.add_subparsers(dest="prompt_id_cmd", required=True)
    prompt_id_allocate = prompt_id_sub.add_parser("allocate")
    prompt_id_allocate.add_argument("--source", required=True)
    prompt_id_allocate.add_argument("--project-id", type=int)
    prompt_id_allocate.add_argument("--parent-prompt-id", type=int)
    prompt_id_backup = prompt_id_sub.add_parser("backup")
    prompt_id_backup.add_argument("--output-dir")
    prompt_id_backfill_sources = prompt_id_sub.add_parser("backfill-sources")
    prompt_id_backfill_sources.add_argument("--source", required=True)
    prompt_id_backfill_sources.add_argument("--git-repo", action="append", default=[])
    prompt_id_backfill_sources.add_argument("--prompt-dir-root", action="append", default=[])
    prompt_id_backfill_sources.add_argument("--text-tree", action="append", default=[])
    prompt_id_backfill_sources.add_argument("--optional-text-tree", action="append", default=[])
    prompt_id_backfill_sources.add_argument("--require-id", type=int, action="append", default=[])
    prompt_id_backfill = prompt_id_sub.add_parser("backfill")
    prompt_id_backfill.add_argument("--source", required=True)
    prompt_id_backfill.add_argument("--ids-file", required=True)
    prompt_id_materialize = prompt_id_sub.add_parser("materialize")
    prompt_id_materialize.add_argument("prompt_id", type=int)
    prompt_id_materialize.add_argument("--content-file", required=True)
    prompt_id_mark_used = prompt_id_sub.add_parser("mark-used")
    prompt_id_mark_used.add_argument("prompt_id", type=int)
    prompt_id_cancel = prompt_id_sub.add_parser("cancel")
    prompt_id_cancel.add_argument("prompt_id", type=int)
    prompt_id_smoke = prompt_id_sub.add_parser("smoke")
    prompt_id_smoke.add_argument("--source", default="activation-smoke")
    prompt_id_smoke.add_argument("--project-id", type=int)
    register_github_parser = sub.add_parser("register-github-repo")
    register_github_parser.add_argument("--owner", required=True)
    register_github_parser.add_argument("--name", required=True)
    register_github_parser.add_argument("--remote-url", required=True)
    register_github_parser.add_argument("--default-branch", required=True)
    register_github_parser.add_argument("--worktree", required=True)
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
    if args.cmd == "project-work-queue":
        return project_view_command("codex_work_queue", CODEX_WORK_QUEUE_FIELDS)
    if args.cmd == "project-remote":
        return project_view_command("codex_remote_projects", CODEX_WORK_QUEUE_FIELDS)
    if args.cmd == "project-missing":
        return project_view_command("codex_missing_projects", CODEX_STATUS_LIST_FIELDS)
    if args.cmd == "project-archived":
        return project_view_command("codex_archived_projects", CODEX_STATUS_LIST_FIELDS)
    if args.cmd == "codex-project-context":
        return codex_project_context_command(args.project_id)
    if args.cmd == "project-show":
        return project_show_command(args.project_id)
    if args.cmd == "project-path":
        return project_path_command(args.project_id, args.status)
    if args.cmd == "prompt-id":
        if args.prompt_id_cmd == "allocate":
            return prompt_id_allocate_command(args)
        if args.prompt_id_cmd == "backup":
            return prompt_id_backup_command(args)
        if args.prompt_id_cmd == "backfill-sources":
            return prompt_id_backfill_sources_command(args)
        if args.prompt_id_cmd == "backfill":
            return prompt_id_backfill_command(args)
        if args.prompt_id_cmd == "materialize":
            return prompt_id_materialize_command(args)
        if args.prompt_id_cmd == "mark-used":
            return prompt_id_mark_used_command(args)
        if args.prompt_id_cmd == "cancel":
            return prompt_id_cancel_command(args)
        if args.prompt_id_cmd == "smoke":
            return prompt_id_smoke_command(args)
        return 2
    if args.cmd == "register-github-repo":
        return register_github_repo_command(args)
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
