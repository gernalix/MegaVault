#!/usr/bin/env python3
"""Canonical, filesystem-backed SQLite database inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SQLITE_HEADER = b"SQLite format 3\x00"
CLASSIFICATIONS = {
    "canonical", "derived", "cache", "browser", "test", "fixture",
    "backup", "historical", "demo",
}
SKIP_DIRS = {".git", ".gradle", ".idea", ".venv", "node_modules", "__pycache__"}


# Phase C records decisions and child-task inputs only. It intentionally does not
# alter any source database schema.
PHASE_C_SELECTED = {
    "/home/daniele/.local/share/codex-session-archive/index/archive.sqlite": {
        "repo": "gernalix/codex-usage-monitor",
        "needed_changes": [
            "Normalize sessions.prompt_ids into a session_prompt_ids junction table while retaining the raw prompt_ids value for audit.",
            "Add a human-readable session catalog view and indexes for last_timestamp_utc and updated_at_utc.",
        ],
    },
    "/home/daniele/.local/share/codex-usage-monitor/codex_usage_monitor.db": {
        "repo": "gernalix/codex-usage-monitor",
        "needed_changes": [
            "Index quota_snapshots.run_id and notification_events.snapshot_id so Datasette backlinks do not scan the append-only history.",
        ],
    },
    "/home/daniele/MegaVault/megavault.sqlite": {
        "repo": "gernalix/MegaVault",
        "needed_changes": [
            "Add a human-readable database inventory view joining the existing project, repository, and host foreign keys for Datasette navigation.",
        ],
    },
    "/home/ubuntu/sync_root/db/personalhub_read.db": {
        "repo": "gernalix/datasette5",
        "needed_changes": [],
    },
    "/mnt/Seagate6TB/X-Reposts/state/reposts.sqlite": {
        "repo": None,
        "needed_changes": [
            "Add a human-readable repost status view and an index on updated_at while retaining canonical_url and raw timestamp fields.",
        ],
    },
    "/var/lib/fedora-system-monitor/monitor.sqlite3": {
        "repo": "gernalix/fedora-system-monitor",
        "read_source": {
            "kind": "latest_consistent_backup",
            "path_pattern": "/var/lib/fedora-system-monitor/backups/monitor-????????T??????Z.sqlite3",
            "max_age_seconds": 93600,
            "open_mode": "mode=ro&immutable=1",
        },
        "needed_changes": [
            "Add bounded human-readable current-alert and recent-event views over existing keys without dropping details_json or UTC/local timestamps.",
        ],
    },
    "/home/daniele/projects/codex-roadmap/roadmap.sqlite": {
        "repo": "gernalix/codex-roadmap",
        "needed_changes": [],
    },
    "/home/daniele/projects/grindr-web-exporter/data/grindr_export.sqlite3": {
        "repo": None,
        "needed_changes": [
            "Add a human-readable message catalog view joining messages to chats and media through the existing foreign keys while retaining raw_json.",
            "Index messages.timestamp and media.dedupe_hash for chronological browsing and backlinks.",
        ],
    },
    "/home/daniele/projects/salute/salute.db": {
        "repo": "gernalix/salute",
        "needed_changes": [],
    },
}

PHASE_C_BLOCKED = {
    "/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db":
        "No canonical MegaVault project or repository owns the ActivityWatch schema.",
    "/home/daniele/MegaVault/codex_global_timeline.sqlite":
        "Declared canonical database is missing, so its schema and current code owner cannot be verified.",
    "/home/daniele/sync_root/db/incident_registry.sqlite":
        "No canonical MegaVault project or repository owns the legacy global incident registry schema.",
}

PHASE_C_EXCLUDED_PATHS = {
    "/home/daniele/Documents/ChatGPT/Personal Hub/artifacts/731684/final/personalhub.db":
        "Point-in-time import artifact; the active Oracle read projection is the consultable database.",
    "/home/ubuntu/sync_root/db/personalhub.db":
        "Raw PersonalHub sync envelope; expose only the existing human-readable personalhub_read projection.",
}

DEFAULT_EXCLUSION_REASONS = {
    "browser": "Browser profile state is sensitive runtime/cache data, not a consultation database.",
    "cache": "Cache data is derived and rebuildable.",
    "test": "Test output is not canonical personal data.",
    "fixture": "Fixture data is not canonical personal data.",
    "backup": "Backup copies are retained for recovery, not parallel consultation.",
    "demo": "Demo data is not canonical personal data.",
    "historical": "Historical copies are retained for audit, not parallel consultation.",
}


def _table_exists(conn: sqlite3.Connection, name: str) -> bool:
    return conn.execute(
        "select 1 from sqlite_master where type='table' and name=?", (name,)
    ).fetchone() is not None


def _normalize_remote(value: str | None) -> str | None:
    if not value:
        return None
    remote = value.strip().removesuffix(".git").rstrip("/").lower()
    if remote.startswith("git@github.com:"):
        remote = "https://github.com/" + remote.split(":", 1)[1]
    return remote


def _git(path: Path, *args: str) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(path), *args], text=True,
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def _repo_candidate_paths(roots: Iterable[Path]) -> list[Path]:
    candidates: set[Path] = set()
    for raw in roots:
        root = raw.expanduser()
        if not root.is_dir():
            continue
        if (root / ".git").exists():
            candidates.add(root.resolve())
        try:
            children = root.iterdir()
        except OSError:
            continue
        for child in children:
            if child.is_dir() and (child / ".git").exists():
                candidates.add(child.resolve())
    return sorted(candidates, key=str)


def discover_git_repositories(roots: Iterable[Path]) -> list[dict[str, str | None]]:
    """Discover repositories and collapse worktrees/clones by origin, then common dir."""
    unique: dict[str, dict[str, str | None]] = {}
    for path in _repo_candidate_paths(roots):
        common = _git(path, "rev-parse", "--path-format=absolute", "--git-common-dir")
        if not common:
            continue
        origin = _normalize_remote(_git(path, "remote", "get-url", "origin"))
        identity = f"origin:{origin}" if origin else f"gitdir:{Path(common).resolve()}"
        row = {
            "identity": identity,
            "path": str(path),
            "origin": origin,
            "common_git_dir": str(Path(common).resolve()),
        }
        previous = unique.get(identity)
        if previous is None or str(path) < str(previous["path"]):
            unique[identity] = row
    return sorted(unique.values(), key=lambda row: str(row["identity"]))


def is_sqlite_file(path: Path) -> bool:
    try:
        if not path.is_file() or path.is_symlink():
            return False
        with path.open("rb") as stream:
            return stream.read(len(SQLITE_HEADER)) == SQLITE_HEADER
    except OSError:
        return False


def discover_sqlite_files(repo_path: Path) -> list[Path]:
    found: list[Path] = []
    for directory, dirnames, filenames in os.walk(repo_path, followlinks=False):
        dirnames[:] = sorted(name for name in dirnames if name not in SKIP_DIRS)
        base = Path(directory)
        for name in sorted(filenames):
            candidate = base / name
            if is_sqlite_file(candidate):
                found.append(candidate.resolve())
    return found


def classify(path: str, *, declared: bool = False, metadata: str = "") -> str:
    text = path.lower()
    declared_text = metadata.lower()
    parts = {part.lower() for part in Path(path).parts}
    name = Path(path).name.lower()
    if "fixture" in text or "fixtures" in parts:
        return "fixture"
    if "test" in parts or "tests" in parts or name.startswith("test_"):
        return "test"
    if "backup" in text or "backups" in parts or name.endswith((".bak", ".backup")):
        return "backup"
    if "historical" in text or "legacy" in text or "archive" in parts:
        return "historical"
    if "browser" in text or {"chrome", "chromium", "firefox"} & parts:
        return "browser"
    if "cache" in text or ".cache" in parts:
        return "cache"
    if "demo" in text or "sample" in text:
        return "demo"
    if declared and ("historical" in declared_text or "legacy" in declared_text):
        return "historical"
    if declared and ("canonical" in declared_text or "active" in declared_text or "runtime" in declared_text):
        return "canonical"
    return "canonical" if declared else "derived"


def _inventory_id(host_id: str | None, source_path: str) -> str:
    digest = hashlib.sha256(f"{host_id or ''}\0{source_path}".encode()).hexdigest()[:24]
    return f"DBI-{digest}"


def ensure_schema(conn: sqlite3.Connection) -> bool:
    existed = _table_exists(conn, "database_inventory")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS database_inventory (
          inventory_id TEXT PRIMARY KEY,
          project_id INTEGER REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE SET NULL,
          project_slug TEXT,
          repository_id TEXT REFERENCES repositories(repository_id) ON UPDATE CASCADE ON DELETE SET NULL,
          repo_identity TEXT,
          repo_path TEXT,
          repo_origin TEXT,
          git_common_dir TEXT,
          host_id TEXT REFERENCES hosts(host_id) ON UPDATE CASCADE ON DELETE SET NULL,
          db_name TEXT NOT NULL,
          source_path TEXT NOT NULL,
          classification TEXT NOT NULL CHECK(classification IN ('canonical','derived','cache','browser','test','fixture','backup','historical','demo')),
          status TEXT NOT NULL,
          last_seen TEXT,
          canonical INTEGER NOT NULL DEFAULT 0 CHECK(canonical IN (0,1)),
          datasette_expose INTEGER NOT NULL DEFAULT 0 CHECK(datasette_expose IN (0,1)),
          sync_to_oracle INTEGER NOT NULL DEFAULT 0 CHECK(sync_to_oracle IN (0,1)),
          declared INTEGER NOT NULL DEFAULT 0 CHECK(declared IN (0,1)),
          legacy_source TEXT,
          notes TEXT,
          UNIQUE(host_id, source_path)
        )
        """
    )
    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_database_inventory_project
          ON database_inventory(project_id, classification, status)
        """
    )
    conn.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_database_inventory_repo
          ON database_inventory(repo_identity, source_path)
        """
    )
    conn.execute(
        """
        CREATE VIEW IF NOT EXISTS database_inventory_read AS
        SELECT
          i.inventory_id,
          i.project_id,
          p.slug AS project_slug,
          p.name AS project_name,
          i.repository_id,
          r.location AS repository_location,
          r.kind AS repository_kind,
          r.branch AS repository_branch,
          r.head AS repository_head,
          r.status AS repository_status,
          r.canonical AS repository_canonical,
          r.worktree_path AS repository_worktree_path,
          r.remote_url AS repository_remote_url,
          r.runtime_path AS repository_runtime_path,
          i.host_id,
          h.name AS host_name,
          h.kind AS host_kind,
          h.os AS host_os,
          i.db_name,
          i.source_path,
          i.classification,
          i.status,
          i.last_seen,
          i.canonical,
          i.datasette_expose,
          i.sync_to_oracle,
          i.declared,
          i.repo_identity,
          i.repo_path,
          i.repo_origin,
          i.git_common_dir,
          i.legacy_source,
          i.notes
        FROM database_inventory AS i
        LEFT JOIN projects AS p ON p.project_id=i.project_id
        LEFT JOIN repositories AS r ON r.repository_id=i.repository_id
        LEFT JOIN hosts AS h ON h.host_id=i.host_id
        """
    )
    return not existed


def _phase_c_exclusion_reason(source_path: str, classification: str) -> str | None:
    if source_path in PHASE_C_EXCLUDED_PATHS:
        return PHASE_C_EXCLUDED_PATHS[source_path]
    if classification in DEFAULT_EXCLUSION_REASONS:
        return DEFAULT_EXCLUSION_REASONS[classification]
    if "/exports/sync-test-" in source_path:
        return "End-to-end sync test output is not canonical personal data."
    if source_path.endswith("/datasette5/output.db"):
        return "Generated Datasette output is not a canonical source database."
    if source_path.endswith("/exports/orchestrator/channel_catalog.sqlite"):
        return "Derived exporter orchestration catalog is not useful for personal consultation."
    if source_path.endswith("/exports/orchestrator/telegram_notify_state.sqlite"):
        return "Derived notification delivery state is not useful for personal consultation."
    return None


def apply_phase_c_decisions(conn: sqlite3.Connection) -> tuple[dict[str, int], list[dict[str, object]]]:
    """Set existing selection flags and fail closed if any inventory row is undecided."""
    counts = {"selected": 0, "excluded": 0, "blocked": 0}
    decisions: list[dict[str, object]] = []
    rows = conn.execute(
        "select inventory_id,source_path,classification,host_id from database_inventory order by inventory_id"
    ).fetchall()
    for inventory_id, source_path, classification, host_id in rows:
        selected = PHASE_C_SELECTED.get(source_path)
        blocked = PHASE_C_BLOCKED.get(source_path)
        excluded = _phase_c_exclusion_reason(source_path, classification)
        if selected:
            decision = "selected"
            reason = "Canonical or personal database useful for private consultation."
            expose, sync = 1, int(host_id != "H0002")
        elif blocked:
            decision, reason, expose, sync = "blocked", blocked, 0, 0
        elif excluded:
            decision, reason, expose, sync = "excluded", excluded, 0, 0
        else:
            raise RuntimeError(f"undecided database inventory row: {inventory_id} {source_path}")
        conn.execute(
            """update database_inventory set datasette_expose=?,sync_to_oracle=?
                where inventory_id=? and (datasette_expose<>? or sync_to_oracle<>?)""",
            (expose, sync, inventory_id, expose, sync),
        )
        counts[decision] += 1
        decisions.append({
            "inventory_id": inventory_id, "decision": decision,
            "datasette_expose": bool(expose), "sync_to_oracle": bool(sync), "reason": reason,
        })
    return counts, decisions


def build_phase_c_plan(conn: sqlite3.Connection, decisions: list[dict[str, object]]) -> dict[str, object]:
    selected = []
    for row in conn.execute(
        """select i.inventory_id,i.project_id,i.project_slug,i.source_path,
                  i.datasette_expose,i.sync_to_oracle,i.host_id,h.name
             from database_inventory i left join hosts h on h.host_id=i.host_id
            where i.datasette_expose=1 order by i.project_slug,i.source_path"""
    ):
        policy = PHASE_C_SELECTED[row[3]]
        item = {
            "inventory_id": row[0], "project_id": row[1], "project_slug": row[2],
            "repo": policy["repo"], "source_path": row[3],
            "datasette_expose": bool(row[4]), "sync_to_oracle": bool(row[5]),
            "host_id": row[6], "host": row[7],
            "needed_changes": policy["needed_changes"],
        }
        if policy.get("read_source"):
            item["read_source"] = policy["read_source"]
        selected.append(item)
    excluded_summary = []
    for classification, count in conn.execute(
        """select classification,count(*) from database_inventory
             where datasette_expose=0 and source_path not in ({})
             group by classification order by classification""".format(
                 ",".join("?" for _ in PHASE_C_BLOCKED)
             ),
        tuple(PHASE_C_BLOCKED),
    ):
        excluded_summary.append({
            "classification": classification, "count": count,
            "reason": "Excluded by the explicit Phase C decision policy; see decisions for row-level reasons.",
        })
    blocked = [
        {"inventory_id": row[0], "project_id": row[1], "project_slug": row[2],
         "source_path": row[3], "host_id": row[4], "reason": PHASE_C_BLOCKED[row[3]]}
        for row in conn.execute(
            """select inventory_id,project_id,project_slug,source_path,host_id
                 from database_inventory where source_path in ({}) order by source_path""".format(
                     ",".join("?" for _ in PHASE_C_BLOCKED)
                 ),
            tuple(PHASE_C_BLOCKED),
        )
    ]
    grouped_tasks: dict[tuple[int, str | None], dict[str, object]] = {}
    for item in selected:
        if not item["needed_changes"]:
            continue
        key = (int(item["project_id"]), item["repo"])
        task = grouped_tasks.setdefault(key, {
            "task_key": f"phase-c-{item['project_slug']}-datasette-friendly",
            "project_id": item["project_id"], "project_slug": item["project_slug"],
            "repo": item["repo"], "inventory_ids": [], "source_paths": [],
            "needed_changes": [],
            "acceptance": [
                "Implement changes only in the code that creates or migrates the source schema, never by patching a live database.",
                "Preserve useful raw values and timestamps for audit and sorting.",
                "Prove idempotent generation or migration plus SQLite integrity and foreign-key checks.",
            ],
        })
        task["inventory_ids"].append(item["inventory_id"])
        task["source_paths"].append(item["source_path"])
        for change in item["needed_changes"]:
            if change not in task["needed_changes"]:
                task["needed_changes"].append(change)
        if item.get("read_source"):
            task["read_source"] = item["read_source"]
    return {
        "selected": selected, "excluded_summary": excluded_summary,
        "unowned_or_blocked": blocked, "decisions": decisions,
        "repo_tasks": sorted(grouped_tasks.values(), key=lambda task: str(task["task_key"])),
    }


def _declared_paths(path: str | None, notes: str | None) -> list[str]:
    values: list[str] = []
    if path and (_looks_like_database_path(path) or is_sqlite_file(Path(path))):
        values.append(path)
    for token in (notes or "").split(";"):
        if "=" not in token:
            continue
        key, value = token.split("=", 1)
        if (
            key.strip().lower() in {"db", "path", "index", "database"}
            and value.startswith("/")
            and (_looks_like_database_path(value) or is_sqlite_file(Path(value)))
        ):
            values.append(value)
    return list(dict.fromkeys(values))


def _looks_like_database_path(value: str) -> bool:
    return Path(value).name.lower().endswith((".db", ".db3", ".sqlite", ".sqlite3"))


def migrate_legacy_inventory(conn: sqlite3.Connection) -> int:
    """Move database-only legacy rows into the canonical inventory and retire them."""
    ensure_schema(conn)
    migrated = 0
    if _table_exists(conn, "data_assets"):
        rows = conn.execute(
            """select data_asset_id, project_id, host_id, name, asset_type, path,
                      coalesce(status,''), coalesce(notes,'') from data_assets"""
        ).fetchall()
        retired: list[str] = []
        for asset_id, project_id, host_id, name, asset_type, path, status, notes in rows:
            marker = f"{name} {asset_type} {path or ''} {notes}".lower()
            if "sqlite" not in marker and not any(
                str(path or "").lower().endswith(ext) for ext in (".db", ".db3", ".sqlite3")
            ):
                continue
            paths = _declared_paths(path, notes)
            if not paths:
                continue
            for source_path in paths:
                metadata = f"{asset_type} {status} {notes}"
                _upsert_declared(
                    conn, source_path, project_id, host_id, name, metadata,
                    legacy_source=f"data_assets:{asset_id}",
                    datasette_expose=int("datasette" in metadata.lower()),
                )
                migrated += 1
            retired.append(asset_id)
        conn.executemany("delete from data_assets where data_asset_id=?", ((x,) for x in retired))
    if _table_exists(conn, "project_components"):
        rows = conn.execute(
            """select component_id, project_id, component, type, path, purpose
                 from project_components
                where lower(type) like '%sqlite%'"""
        ).fetchall()
        for component_id, project_id, component, kind, path, purpose in rows:
            _upsert_declared(
                conn, path, project_id, None, component, f"{kind} {purpose}",
                legacy_source=f"project_components:{component_id}",
            )
            migrated += 1
        conn.executemany("delete from project_components where component_id=?", ((r[0],) for r in rows))
    for inventory_id, source_path, metadata, legacy_source, host_id in conn.execute(
        "select inventory_id,source_path,coalesce(notes,''),coalesce(legacy_source,''),host_id from database_inventory where declared=1"
    ).fetchall():
        if host_id == "H0001" and Path(source_path).is_dir():
            conn.execute("delete from database_inventory where inventory_id=?", (inventory_id,))
            continue
        classification = classify(source_path, declared=True, metadata=metadata)
        normalized_sources = ",".join(dict.fromkeys(filter(None, legacy_source.split(","))))
        conn.execute(
            """update database_inventory
                  set classification=?,canonical=?,legacy_source=?
                where inventory_id=?
                  and (classification<>? or canonical<>? or legacy_source<>?)""",
            (classification, int(classification == "canonical"), normalized_sources, inventory_id,
             classification, int(classification == "canonical"), normalized_sources),
        )
    return migrated


def _project_slug(conn: sqlite3.Connection, project_id: int | None) -> str | None:
    if project_id is None:
        return None
    row = conn.execute("select slug from projects where project_id=?", (project_id,)).fetchone()
    return row[0] if row else None


def _upsert_declared(
    conn: sqlite3.Connection, source_path: str, project_id: int | None,
    host_id: str | None, name: str, metadata: str, *, legacy_source: str,
    datasette_expose: int = 0,
) -> None:
    host_id = host_id or "H0001"
    local = host_id in (None, "H0001")
    present = local and is_sqlite_file(Path(source_path))
    classification = classify(source_path, declared=True, metadata=metadata)
    status = "present" if present else ("missing" if local else "remote_declared")
    seen = datetime.now(timezone.utc).isoformat() if present else None
    conn.execute(
        """
        INSERT INTO database_inventory(
          inventory_id,project_id,project_slug,host_id,db_name,source_path,
          classification,status,last_seen,canonical,datasette_expose,sync_to_oracle,
          declared,legacy_source,notes
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(host_id,source_path) DO UPDATE SET
          project_id=coalesce(excluded.project_id,database_inventory.project_id),
          project_slug=coalesce(excluded.project_slug,database_inventory.project_slug),
          db_name=excluded.db_name, classification=excluded.classification,
          status=excluded.status, last_seen=coalesce(excluded.last_seen,database_inventory.last_seen),
          canonical=excluded.canonical,
          datasette_expose=max(database_inventory.datasette_expose,excluded.datasette_expose),
          declared=1,
          legacy_source=trim(coalesce(database_inventory.legacy_source||',','')||excluded.legacy_source,','),
          notes=coalesce(database_inventory.notes,excluded.notes)
        """,
        (_inventory_id(host_id, source_path), project_id, _project_slug(conn, project_id),
         host_id, Path(source_path).name or name, source_path, classification, status,
         seen, int(classification == "canonical"), datasette_expose, 0, 1,
         legacy_source, metadata),
    )


def _registered_repositories(conn: sqlite3.Connection) -> list[dict[str, object]]:
    cursor = conn.execute(
        """select r.repository_id,r.project_id,p.slug,r.host_id,r.worktree_path,r.remote_url,r.canonical
             from repositories r join projects p on p.project_id=r.project_id
            where r.worktree_path is not null"""
    )
    columns = [item[0] for item in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def reconcile(conn: sqlite3.Connection, roots: Iterable[Path] | None = None, host_id: str = "H0001") -> dict[str, int]:
    ensure_schema(conn)
    registered = _registered_repositories(conn)
    configured = [Path(str(row["worktree_path"])) for row in registered]
    scan_roots = list(roots or [Path("/home/daniele/projects"), *configured])
    discovered_repos = discover_git_repositories(scan_roots)
    by_path = {str(Path(str(r["worktree_path"])).resolve()): r for r in registered if Path(str(r["worktree_path"])).exists()}
    by_origin = {_normalize_remote(str(r["remote_url"])): r for r in registered if r["remote_url"]}
    now = datetime.now(timezone.utc).isoformat()
    seen_ids: set[str] = set()
    for repo in discovered_repos:
        mapping = by_path.get(str(repo["path"])) or by_origin.get(repo["origin"])
        project_id = int(mapping["project_id"]) if mapping else None
        repository_id = str(mapping["repository_id"]) if mapping else None
        project_slug = str(mapping["slug"]) if mapping else None
        row_host = str(mapping["host_id"] or host_id) if mapping else host_id
        for db_path in discover_sqlite_files(Path(str(repo["path"]))):
            source_path = str(db_path)
            inventory_id = _inventory_id(row_host, source_path)
            classification = classify(source_path)
            conn.execute(
                """
                INSERT INTO database_inventory(
                  inventory_id,project_id,project_slug,repository_id,repo_identity,repo_path,
                  repo_origin,git_common_dir,host_id,db_name,source_path,classification,status,
                  last_seen,canonical,datasette_expose,sync_to_oracle,declared
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0)
                ON CONFLICT(host_id,source_path) DO UPDATE SET
                  project_id=excluded.project_id,project_slug=excluded.project_slug,
                  repository_id=excluded.repository_id,repo_identity=excluded.repo_identity,
                  repo_path=excluded.repo_path,repo_origin=excluded.repo_origin,
                  git_common_dir=excluded.git_common_dir,db_name=excluded.db_name,
                  status='present',last_seen=excluded.last_seen
                WHERE database_inventory.project_id IS NOT excluded.project_id
                   OR database_inventory.project_slug IS NOT excluded.project_slug
                   OR database_inventory.repository_id IS NOT excluded.repository_id
                   OR database_inventory.repo_identity IS NOT excluded.repo_identity
                   OR database_inventory.repo_path IS NOT excluded.repo_path
                   OR database_inventory.repo_origin IS NOT excluded.repo_origin
                   OR database_inventory.git_common_dir IS NOT excluded.git_common_dir
                   OR database_inventory.db_name IS NOT excluded.db_name
                   OR database_inventory.status<>'present'
                """,
                (inventory_id, project_id, project_slug, repository_id, repo["identity"],
                 repo["path"], repo["origin"], repo["common_git_dir"], row_host,
                 db_path.name, source_path, classification, "present", now,
                 int(classification == "canonical"), 0, 0),
            )
            seen_ids.add(inventory_id)
    if seen_ids:
        placeholders = ",".join("?" for _ in seen_ids)
        conn.execute(
            f"update database_inventory set status='missing' where declared=0 and host_id=? and status<>'missing' and inventory_id not in ({placeholders})",
            (host_id, *sorted(seen_ids)),
        )
    else:
        conn.execute("update database_inventory set status='missing' where declared=0 and host_id=? and status<>'missing'", (host_id,))
    declared = conn.execute("select count(*) from database_inventory where declared=1").fetchone()[0]
    return {"repositories": len(discovered_repos), "sqlite_files": len(seen_ids), "declared": declared}


def reconcile_command(db_path: Path, roots: list[str], host_id: str) -> int:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN IMMEDIATE")
        migrated = migrate_legacy_inventory(conn)
        result = reconcile(conn, [Path(root) for root in roots] if roots else None, host_id)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    print(json.dumps({"status": "PASS", "migrated": migrated, **result}, sort_keys=True))
    return 0


def selection_command(db_path: Path, output: Path) -> int:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        conn.execute("BEGIN IMMEDIATE")
        counts, decisions = apply_phase_c_decisions(conn)
        plan = build_phase_c_plan(conn, decisions)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
    output.write_text(json.dumps(plan, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", **counts, "output": str(output)}, sort_keys=True))
    return 0


def dispatch(argv: list[str], *, db_path: Path) -> int | None:
    if not argv or argv[0] not in {"database-inventory-reconcile", "database-inventory-select"}:
        return None
    if argv[0] == "database-inventory-select":
        parser = argparse.ArgumentParser(prog="megavault.py database-inventory-select")
        parser.add_argument("--output", type=Path, default=Path("/tmp/c2-phase-c-plan.json"))
        args = parser.parse_args(argv[1:])
        return selection_command(db_path, args.output)
    parser = argparse.ArgumentParser(prog="megavault.py database-inventory-reconcile")
    parser.add_argument("--root", action="append", default=[])
    parser.add_argument("--host-id", default="H0001")
    args = parser.parse_args(argv[1:])
    return reconcile_command(db_path, args.root, args.host_id)
