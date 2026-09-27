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
    return not existed


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


def dispatch(argv: list[str], *, db_path: Path) -> int | None:
    if not argv or argv[0] != "database-inventory-reconcile":
        return None
    parser = argparse.ArgumentParser(prog="megavault.py database-inventory-reconcile")
    parser.add_argument("--root", action="append", default=[])
    parser.add_argument("--host-id", default="H0001")
    args = parser.parse_args(argv[1:])
    return reconcile_command(db_path, args.root, args.host_id)
