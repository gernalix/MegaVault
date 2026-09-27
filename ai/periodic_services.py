#!/usr/bin/env python3
"""Canonical periodic-systemd evidence attached to MegaVault services."""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"
SNAPSHOT_TOOL = ROOT / "tools/systemd_periodic_snapshot.py"
ORACLE_SSH = Path("/home/daniele/projects/vm_oracle/scripts/oracle_ssh.sh")
HOSTS = {"fedora": "H0001", "oracle": "H0002"}
INTERNAL_HELPERS = (
    "watchdog", "notify-retry", "telegram-notify", "live-status",
    "callback-bridge", "time-triggers", "healthcheck",
)


def now_sql(c: sqlite3.Connection) -> str:
    return c.execute("select strftime('%Y-%m-%dT%H:%M:%SZ','now')").fetchone()[0]


def ensure_schema(c: sqlite3.Connection) -> None:
    c.executescript("""
    CREATE TABLE IF NOT EXISTS periodic_service_evidence(
      service_id TEXT PRIMARY KEY REFERENCES services(service_id) ON DELETE CASCADE,
      timer_unit TEXT NOT NULL, service_unit TEXT NOT NULL,
      enabled_semantics TEXT NOT NULL, active_semantics TEXT NOT NULL,
      defining_path TEXT NOT NULL, source_line_start INTEGER, source_line_end INTEGER,
      source_sha256 TEXT, source_kind TEXT NOT NULL,
      present INTEGER NOT NULL CHECK(present IN (0,1)),
      monitoring_decision TEXT NOT NULL CHECK(monitoring_decision IN ('MONITORED','EXCLUDED','PENDING')),
      monitoring_status TEXT NOT NULL, monitoring_rationale TEXT NOT NULL,
      monitoring_target_key TEXT REFERENCES monitoring_targets(target_key) ON DELETE SET NULL,
      reconciled_at TEXT NOT NULL,
      UNIQUE(timer_unit, service_id));
    CREATE TABLE IF NOT EXISTS periodic_service_reconciliations(
      host_id TEXT NOT NULL REFERENCES hosts(host_id), scope TEXT NOT NULL,
      evidence_hash TEXT NOT NULL, reconciled_at TEXT NOT NULL, timer_count INTEGER NOT NULL,
      PRIMARY KEY(host_id,scope));
    DROP VIEW IF EXISTS periodic_service_registry;
    CREATE VIEW periodic_service_registry AS
    SELECT e.service_id,s.name,s.project_id,p.slug AS project_slug,s.host_id,h.name AS host_name,
      s.scope,e.timer_unit,e.service_unit,e.enabled_semantics,e.active_semantics,
      e.defining_path,e.source_line_start,e.source_line_end,e.source_kind,e.present,
      e.monitoring_decision,e.monitoring_status,e.monitoring_rationale,
      e.monitoring_target_key,mt.kuma_monitor_key,e.reconciled_at
    FROM periodic_service_evidence e JOIN services s ON s.service_id=e.service_id
    LEFT JOIN projects p ON p.project_id=s.project_id LEFT JOIN hosts h ON h.host_id=s.host_id
    LEFT JOIN monitoring_targets mt ON mt.target_key=e.monitoring_target_key;
    INSERT INTO operational_inventory_meta(inventory_key,status,source_ref,last_synced_at,notes)
      VALUES('periodic_services','EMPTY','systemd-live+registered-repositories',NULL,
             'Run periodic-service-reconcile for Fedora system/user and Oracle system scopes.')
      ON CONFLICT(inventory_key) DO NOTHING;
    """)
    columns = {row[1] for row in c.execute("pragma table_info(periodic_service_evidence)")}
    if "source_repository_id" not in columns:
        c.execute("alter table periodic_service_evidence add column source_repository_id TEXT")
    if "source_relative_path" not in columns:
        c.execute("alter table periodic_service_evidence add column source_relative_path TEXT")
    c.execute("drop view if exists periodic_service_registry")
    c.execute("""create view periodic_service_registry as
    select e.service_id,s.name,s.project_id,p.slug as project_slug,s.host_id,h.name as host_name,
      s.scope,e.timer_unit,e.service_unit,e.enabled_semantics,e.active_semantics,
      e.defining_path,e.source_line_start,e.source_line_end,e.source_kind,
      e.source_repository_id,e.source_relative_path,e.present,
      e.monitoring_decision,e.monitoring_status,e.monitoring_rationale,
      e.monitoring_target_key,mt.kuma_monitor_key,e.reconciled_at
    from periodic_service_evidence e join services s on s.service_id=e.service_id
    left join projects p on p.project_id=s.project_id left join hosts h on h.host_id=s.host_id
    left join monitoring_targets mt on mt.target_key=e.monitoring_target_key""")
    _backfill_repository_references(c)


def _backfill_repository_references(c: sqlite3.Connection) -> None:
    repositories = c.execute("""select repository_id,worktree_path from repositories
      where canonical=1 and worktree_path is not null order by repository_id""").fetchall()
    for service_id, source_path in c.execute("""select service_id,defining_path from periodic_service_evidence
      where source_kind='repository_exact_hash' and source_repository_id is null""").fetchall():
        path = Path(source_path)
        matches = []
        for repository_id, root_text in repositories:
            try:
                relative = path.relative_to(Path(root_text))
            except ValueError:
                continue
            matches.append((repository_id, relative.as_posix()))
        if len(matches) == 1:
            c.execute("""update periodic_service_evidence set source_repository_id=?,source_relative_path=?
              where service_id=?""", (*matches[0], service_id))


def _sha(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def _repository_sources(c: sqlite3.Connection) -> dict[tuple[str, str], list[tuple[str, int, str, Path, Path]]]:
    index: dict[tuple[str, str], list[tuple[str, int, str, Path, Path]]] = {}
    rows = c.execute("""select r.repository_id,r.project_id,p.slug,r.worktree_path from repositories r
      join projects p on p.project_id=r.project_id
      where r.canonical=1 and r.worktree_path is not null and p.archived=0""").fetchall()
    for repository_id, project_id, slug, root_text in rows:
        root = Path(root_text)
        if not root.is_dir():
            continue
        for pattern in ("*.timer", "*.service"):
            try:
                paths = root.rglob(pattern)
                for path in paths:
                    if ".git" in path.parts:
                        continue
                    digest = _sha(path)
                    if digest:
                        index.setdefault((path.name, digest), []).append(
                            (repository_id, project_id, slug, root, path)
                        )
            except OSError:
                continue
    return index


def _existing_service(c: sqlite3.Connection, host_id: str, scope: str, timer: str, service: str) -> tuple[str, int | None] | None:
    matches: list[tuple[int, str, int | None]] = []
    for service_id, project_id, unit, name in c.execute(
        """select service_id,project_id,coalesce(unit,''),name from services
        where host_id=? and (scope=? or scope is null or scope='')
        order by case when scope=? then 0 else 1 end,service_id""",
        (host_id, scope, scope),
    ):
        units = {item.strip() for item in unit.split("+")}
        if timer in units or name == timer:
            matches.append((0, service_id, project_id))
        elif service in units or name == service:
            matches.append((1, service_id, project_id))
    if not matches:
        return None
    _, service_id, project_id = min(matches)
    return service_id, project_id


def _existing_project(c: sqlite3.Connection, host_id: str, timer: str, service: str) -> int | None:
    for project_id, unit, name in c.execute(
        "select project_id,coalesce(unit,''),name from services where host_id=? and project_id is not null", (host_id,)
    ):
        if timer in {item.strip() for item in unit.split("+")} or service in unit.split("+") or name in (timer, service):
            return int(project_id)
    return None


def _matching_target(c: sqlite3.Connection, host_id: str, scope: str, service: str) -> sqlite3.Row | None:
    identity = f"user:{service}" if scope == "user" else service
    rows = c.execute("""select mt.target_key,mt.runtime_identity,mt.desired_state,mt.kuma_monitor_key,mt.rationale,
      case when mt.kuma_monitor_key is null then 'MISSING_TARGET'
           when km.seen_in_last_sync=0 then 'STALE_MONITOR'
           when km.active=1 then 'BOUND_ACTIVE' when km.active=0 then 'BOUND_INACTIVE' else 'BOUND_UNKNOWN' end
      from monitoring_targets mt left join kuma_monitors km on km.monitor_key=mt.kuma_monitor_key
      where mt.host_id=? order by mt.target_key""", (host_id,)).fetchall()
    stem = service.removesuffix(".service")
    exact = [row for row in rows if row[1] in (identity, service)]
    if exact:
        return exact[0]
    combined = [row for row in rows if any(
        stem == part.strip() or (len(part.strip()) > 5 and stem.endswith("-" + part.strip()))
        for part in row[1].split("+")
    )]
    return combined[0] if len(combined) == 1 else None


def monitor_decision(*, target: sqlite3.Row | None, defining_path: str, timer_unit: str,
                     enabled_state: str = "enabled", project_covered: bool = False) -> tuple[str, str, str]:
    if target is not None:
        desired = target[2]
        if desired == "EXCLUDED":
            return "EXCLUDED", "EXCLUDED", str(target[4])
        status = str(target[5])
        return desired, status, str(target[4])
    if defining_path.startswith(("/usr/lib/systemd/", "/lib/systemd/")):
        return "EXCLUDED", "SYSTEM_FACILITY", "Distribution-owned timer is covered by host health and is not an independent custom failure domain."
    if any(token in timer_unit for token in INTERNAL_HELPERS):
        return "EXCLUDED", "INTERNAL_HELPER", "Transient/internal helper has no independently actionable failure domain."
    if "personalhub" in timer_unit.lower():
        return "EXCLUDED", "EXTERNAL_OWNER", "PersonalHub runtime is externally owned and is not changed or provisioned by this reconciliation."
    if enabled_state in {"disabled", "masked"}:
        return "EXCLUDED", "NOT_ENABLED", "Timer is not enabled, so no periodic runtime is expected."
    if project_covered:
        return "EXCLUDED", "SHARED_FAILURE_DOMAIN", "A canonical monitor already covers the owning project's actionable periodic failure domain."
    return "PENDING", "MISSING_TARGET", "Custom periodic job has no deterministic monitoring target; no Kuma success is claimed."


def reconcile_snapshot(snapshot: dict[str, Any], host_id: str, c: sqlite3.Connection) -> dict[str, int]:
    ensure_schema(c)
    c.row_factory = sqlite3.Row
    sources = _repository_sources(c)
    stamp = now_sql(c)
    scopes = sorted({str(row["scope"]) for row in snapshot.get("timers", [])})
    c.execute("""update periodic_service_evidence set present=0,reconciled_at=? where service_id in
      (select service_id from services where host_id=?)""", (stamp, host_id))
    counts = {"timers": 0, "monitored": 0, "excluded": 0, "pending": 0}
    for row in sorted(snapshot.get("timers", []), key=lambda item: (item["scope"], item["timer_unit"])):
        scope, timer, service = str(row["scope"]), str(row["timer_unit"]), str(row["service_unit"])
        source = dict(row.get("timer_source") or {})
        installed_path = str(source.get("path") or "")
        digest = source.get("sha256")
        candidates = sources.get((timer, str(digest)), []) if digest else []
        candidate = candidates[0] if len(candidates) == 1 else None
        existing = _existing_service(c, host_id, scope, timer, service)
        project_id = candidate[1] if candidate else (existing[1] if existing else _existing_project(c, host_id, timer, service))
        service_id = existing[0] if existing else "PER-" + hashlib.sha256(f"{host_id}|{scope}|{timer}".encode()).hexdigest()[:16]
        defining_path = str(candidate[4]) if candidate else installed_path
        source_kind = "repository_exact_hash" if candidate else ("installed_fragment" if digest else "installed_fragment_unreadable")
        line_start = 1 if candidate else source.get("line_start")
        line_end = (len(candidate[4].read_bytes().splitlines()) or 1) if candidate else source.get("line_end")
        source_repository_id = candidate[0] if candidate else None
        source_relative_path = candidate[4].relative_to(candidate[3]).as_posix() if candidate else None
        state = f"enabled={row.get('enabled_state','unknown')};timer={row.get('active_state','unknown')}/{row.get('sub_state','unknown')};service={row.get('service_active_state','unknown')};result={row.get('service_result','unknown')}"
        if existing is None:
            c.execute("""insert into services(service_id,project_id,host_id,name,scope,unit,state,purpose,source_ref)
              values(?,?,?,?,?,?,?,?,?)""", (service_id, project_id, host_id, service, scope, f"{service}+{timer}", state,
              "Automatically discovered periodic systemd job.", defining_path))
        else:
            c.execute("""update services set project_id=coalesce(?,project_id),scope=?,unit=?,state=?,source_ref=?
              where service_id=?""", (project_id, scope, f"{service}+{timer}", state, defining_path, service_id))
        target = _matching_target(c, host_id, scope, service)
        project_covered = bool(project_id and c.execute("""select 1 from monitoring_targets
          where project_id=? and host_id=? and desired_state='MONITORED' limit 1""", (project_id, host_id)).fetchone())
        decision, monitor_status, rationale = monitor_decision(
            target=target, defining_path=defining_path, timer_unit=timer,
            enabled_state=str(row.get("enabled_state", "unknown")), project_covered=project_covered)
        c.execute("""insert into periodic_service_evidence(
          service_id,timer_unit,service_unit,enabled_semantics,active_semantics,
          defining_path,source_line_start,source_line_end,source_sha256,source_kind,present,
          monitoring_decision,monitoring_status,monitoring_rationale,monitoring_target_key,reconciled_at,
          source_repository_id,source_relative_path) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
          on conflict(service_id) do update set timer_unit=excluded.timer_unit,service_unit=excluded.service_unit,
          enabled_semantics=excluded.enabled_semantics,active_semantics=excluded.active_semantics,
          defining_path=excluded.defining_path,source_line_start=excluded.source_line_start,
          source_line_end=excluded.source_line_end,source_sha256=excluded.source_sha256,
          source_kind=excluded.source_kind,present=1,monitoring_decision=excluded.monitoring_decision,
          monitoring_status=excluded.monitoring_status,monitoring_rationale=excluded.monitoring_rationale,
          monitoring_target_key=excluded.monitoring_target_key,reconciled_at=excluded.reconciled_at,
          source_repository_id=excluded.source_repository_id,source_relative_path=excluded.source_relative_path""",
          (service_id,timer,service,str(row.get("enabled_state","unknown")),state,defining_path,
           line_start,line_end,digest,source_kind,1,decision,monitor_status,rationale,
           target[0] if target else None,stamp,source_repository_id,source_relative_path))
        counts["timers"] += 1
        counts[decision.lower()] += 1
    c.execute("""delete from services where host_id=? and service_id like 'PER-%' and
      exists(select 1 from periodic_service_evidence e where e.service_id=services.service_id and e.present=0)""", (host_id,))
    for scope in scopes:
        canonical = json.dumps([row for row in snapshot["timers"] if row["scope"] == scope], sort_keys=True, separators=(",", ":"))
        count = sum(1 for row in snapshot["timers"] if row["scope"] == scope)
        c.execute("""insert into periodic_service_reconciliations values(?,?,?,?,?)
          on conflict(host_id,scope) do update set evidence_hash=excluded.evidence_hash,
          reconciled_at=excluded.reconciled_at,timer_count=excluded.timer_count""",
          (host_id,scope,hashlib.sha256(canonical.encode()).hexdigest(),stamp,count))
    total = c.execute("select count(*) from periodic_service_evidence where present=1").fetchone()[0]
    pending = c.execute("select count(*) from periodic_service_evidence where present=1 and monitoring_decision='PENDING'").fetchone()[0]
    c.execute("""update operational_inventory_meta set status='COMPLETE',last_synced_at=?,notes=?
      where inventory_key='periodic_services'""", (stamp, f"present={total};pending={pending}"))
    return counts


def capture_snapshot(host: str, scope: str, oracle_ssh: Path = ORACLE_SSH) -> dict[str, Any]:
    if host == "fedora":
        env = os.environ.copy()
        if scope in ("user", "all"):
            uid = os.getuid()
            env.setdefault("XDG_RUNTIME_DIR", f"/run/user/{uid}")
            env.setdefault("DBUS_SESSION_BUS_ADDRESS", f"unix:path=/run/user/{uid}/bus")
        command = [sys.executable, str(SNAPSHOT_TOOL), "--scope", scope]
        result = subprocess.run(command, text=True, capture_output=True, env=env, timeout=120, check=False)
    else:
        if scope != "system":
            raise ValueError("Oracle discovery supports system scope only")
        result = subprocess.run([str(oracle_ssh), "python3 - --scope system"], input=SNAPSHOT_TOOL.read_text(),
                                text=True, capture_output=True, timeout=120, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip().splitlines()[-1] or "snapshot failed")
    return json.loads(result.stdout)


def reconcile_command(host: str, scope: str, snapshot_file: str | None = None, path: Path = DB) -> int:
    try:
        snapshot = json.loads(Path(snapshot_file).read_text()) if snapshot_file else capture_snapshot(host, scope)
        c = sqlite3.connect(path)
        c.execute("pragma foreign_keys=on")
        with c:
            counts = reconcile_snapshot(snapshot, HOSTS[host], c)
        c.close()
        print("PERIODIC_SERVICE_RECONCILE=PASS " + " ".join(f"{key}={value}" for key, value in counts.items()))
        return 0
    except Exception as exc:
        print(f"PERIODIC_SERVICE_RECONCILE=FAIL {exc}", file=sys.stderr)
        return 1


def validate(c: sqlite3.Connection) -> tuple[bool, str]:
    tables = {row[0] for row in c.execute("select name from sqlite_master where type='table'")}
    if "periodic_service_evidence" not in tables:
        return False, "schema_missing=1"
    status_row = c.execute("select status from operational_inventory_meta where inventory_key='periodic_services'").fetchone()
    if status_row and status_row[0] == "EMPTY":
        return True, "not_reconciled=1"
    required = {("H0001", "system"), ("H0001", "user"), ("H0002", "system")}
    reconciled = {tuple(row) for row in c.execute("select host_id,scope from periodic_service_reconciliations")}
    missing = sorted(required - reconciled)
    bad = c.execute("""select count(*) from periodic_service_evidence where present=1 and
      (defining_path='' or
       ((source_line_start is null or source_line_end is null) and source_kind!='installed_fragment_unreadable') or
       monitoring_rationale='' or monitoring_status='')""").fetchone()[0]
    stale = 0
    rows = c.execute("""select e.defining_path,e.source_sha256,e.source_repository_id,
      e.source_relative_path,r.worktree_path,p.slug
      from periodic_service_evidence e
      left join repositories r on r.repository_id=e.source_repository_id
      left join projects p on p.project_id=r.project_id
      where e.present=1 and e.source_kind='repository_exact_hash'""").fetchall()
    for source_path, digest, repository_id, relative_path, worktree_path, project_slug in rows:
        absolute = Path(source_path)
        candidate: Path | None = absolute if absolute.exists() else None
        repository_root: Path | None = None
        if repository_id and relative_path:
            if str(project_slug or "").lower() == "megavault":
                repository_root = ROOT
            elif worktree_path:
                repository_root = Path(worktree_path)
            relocated = repository_root / relative_path if repository_root is not None else None
            if candidate is None and relocated is not None and relocated.exists():
                candidate = relocated
            if candidate is None and repository_root is not None and repository_root.exists():
                stale += 1
                continue
        if candidate is not None and _sha(candidate) != digest:
            stale += 1
    ok = not missing and not bad and not stale
    return ok, f"missing_scopes={len(missing)} invalid={bad} stale_sources={stale}"


def show(path: Path = DB) -> int:
    c = sqlite3.connect(f"file:{Path(path).resolve()}?mode=ro", uri=True)
    for row in c.execute("""select host_name,scope,timer_unit,service_unit,coalesce(project_slug,''),
      enabled_semantics,active_semantics,defining_path,source_line_start,source_line_end,
      monitoring_decision,monitoring_status,monitoring_rationale from periodic_service_registry
      where present=1 order by host_name,scope,timer_unit"""):
        print(";".join(str(item or "") for item in row))
    c.close()
    return 0
