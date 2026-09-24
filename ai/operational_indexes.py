#!/usr/bin/env python3
"""Operational indexes for Uptime Kuma monitors and Telegram-capable projects."""
from __future__ import annotations

import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"
VERSION = 3


def conn(path=DB, ro=False):
    p = Path(path).resolve()
    c = sqlite3.connect(f"file:{p}?mode=ro", uri=True) if ro else sqlite3.connect(p)
    if not ro:
        c.execute("PRAGMA foreign_keys=ON")
    return c


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure(c):
    required = {"projects", "hosts", "services", "integrations", "project_components", "project_operations", "schema_meta"}
    existing = {r[0] for r in c.execute("select name from sqlite_master where type='table'")}
    missing = sorted(required - existing)
    if missing:
        raise RuntimeError("missing required tables: " + ",".join(missing))
    c.executescript("""
    CREATE TABLE IF NOT EXISTS operational_inventory_meta(
      inventory_key TEXT PRIMARY KEY, status TEXT NOT NULL, source_ref TEXT,
      last_synced_at TEXT, notes TEXT);
    CREATE TABLE IF NOT EXISTS kuma_monitors(
      monitor_key TEXT PRIMARY KEY,
      integration_id TEXT NOT NULL REFERENCES integrations(integration_id),
      native_monitor_id INTEGER NOT NULL, host_id TEXT REFERENCES hosts(host_id),
      name TEXT NOT NULL, monitor_type TEXT, active INTEGER,
      seen_in_last_sync INTEGER NOT NULL DEFAULT 1, target_ref TEXT,
      purpose TEXT NOT NULL DEFAULT 'UNKNOWN', last_seen_at TEXT,
      source_ref TEXT NOT NULL, notes TEXT,
      UNIQUE(integration_id,native_monitor_id));
    CREATE TABLE IF NOT EXISTS kuma_monitor_projects(
      monitor_key TEXT NOT NULL REFERENCES kuma_monitors(monitor_key) ON DELETE CASCADE,
      project_id INTEGER NOT NULL REFERENCES projects(project_id),
      relationship TEXT NOT NULL DEFAULT 'depends_on_project', notes TEXT,
      PRIMARY KEY(monitor_key,project_id));
    CREATE TABLE IF NOT EXISTS telegram_project_capabilities(
      project_id INTEGER NOT NULL REFERENCES projects(project_id) ON DELETE CASCADE,
      capability_id TEXT NOT NULL, mechanism TEXT NOT NULL, status TEXT NOT NULL,
      source_ref TEXT NOT NULL, explanation TEXT NOT NULL,
      PRIMARY KEY(project_id,capability_id));
    CREATE TABLE IF NOT EXISTS monitoring_targets(
      target_key TEXT PRIMARY KEY,
      project_id INTEGER REFERENCES projects(project_id) ON DELETE SET NULL,
      repository_slug TEXT NOT NULL,
      host_id TEXT REFERENCES hosts(host_id) ON DELETE SET NULL,
      runtime_identity TEXT NOT NULL,
      signal_kind TEXT NOT NULL CHECK(signal_kind IN (
        'systemd_daemon','systemd_job_freshness','http','push','event_job','manual','none')),
      producer TEXT NOT NULL,
      expected_interval_seconds INTEGER CHECK(
        expected_interval_seconds IS NULL OR expected_interval_seconds > 0),
      desired_state TEXT NOT NULL CHECK(desired_state IN ('MONITORED','EXCLUDED','PENDING')),
      kuma_monitor_key TEXT REFERENCES kuma_monitors(monitor_key) ON DELETE SET NULL,
      rationale TEXT NOT NULL,
      source_ref TEXT NOT NULL,
      last_verified_at TEXT,
      notes TEXT,
      UNIQUE(repository_slug,runtime_identity,signal_kind));
    INSERT OR IGNORE INTO operational_inventory_meta
      VALUES('kuma_monitors','NOT_SYNCED','integration:INT0002',NULL,
      'Sync from the live Uptime Kuma SQLite database before claiming completeness.');
    INSERT OR IGNORE INTO operational_inventory_meta
      VALUES('monitoring_targets','EMPTY','code:ai/operational_indexes.py',NULL,
      'Canonical cross-repository monitoring plan; populate from verified runtime evidence.');
    """)
    p56 = c.execute("select slug from projects where project_id=56").fetchone()
    if p56 and p56[0] == "android-build-telegram-watch-v1":
        c.execute("""INSERT OR IGNORE INTO telegram_project_capabilities VALUES(
          56,'gradle_build_watch','telegram_notify.py','VERIFIED_CODE',
          'repo:gernalix/android_build_telegram_watch_v1/android_build_telegram_watch.py',
          'Watches Gradle daemon logs and sends Telegram notifications when Android builds succeed or fail.')""")
    for view in ("kuma_monitor_index", "monitoring_target_index", "telegram_notification_capability_index", "telegram_notification_project_index", "telegram_shared_infrastructure_index"):
        c.execute(f"DROP VIEW IF EXISTS {view}")
    c.executescript("""
    CREATE VIEW kuma_monitor_index AS
    SELECT km.monitor_key,km.integration_id,i.name AS kuma_instance,km.native_monitor_id,
      km.name AS monitor_name,km.monitor_type,km.active,km.seen_in_last_sync,
      CASE WHEN km.seen_in_last_sync=0 THEN 'REMOVED_OR_NOT_SEEN'
           WHEN km.active=1 THEN 'ACTIVE' WHEN km.active=0 THEN 'INACTIVE' ELSE 'UNKNOWN' END AS monitor_state,
      km.target_ref,km.purpose AS explanation,
      CASE WHEN trim(coalesce(km.purpose,''))='' OR upper(trim(km.purpose))='UNKNOWN' THEN 'MISSING' ELSE 'DOCUMENTED' END AS explanation_status,
      km.host_id,h.name AS host_name,count(DISTINCT kmp.project_id) AS project_count,
      group_concat(DISTINCT kmp.project_id) AS project_ids,group_concat(DISTINCT p.slug) AS project_slugs,
      CASE WHEN count(DISTINCT kmp.project_id)=0 THEN 'UNMAPPED' ELSE 'MAPPED' END AS project_mapping,
      km.last_seen_at,km.source_ref,km.notes
    FROM kuma_monitors km
    LEFT JOIN integrations i ON i.integration_id=km.integration_id
    LEFT JOIN hosts h ON h.host_id=km.host_id
    LEFT JOIN kuma_monitor_projects kmp ON kmp.monitor_key=km.monitor_key
    LEFT JOIN projects p ON p.project_id=kmp.project_id
    GROUP BY km.monitor_key;

    CREATE VIEW monitoring_target_index AS
    SELECT mt.target_key,mt.project_id,p.slug AS project_slug,mt.repository_slug,
      mt.host_id,h.name AS host_name,mt.runtime_identity,mt.signal_kind,mt.producer,
      mt.expected_interval_seconds,mt.desired_state,mt.kuma_monitor_key,
      km.name AS kuma_monitor_name,
      CASE
        WHEN mt.desired_state='EXCLUDED' THEN 'EXCLUDED'
        WHEN mt.kuma_monitor_key IS NULL THEN 'UNBOUND'
        WHEN km.seen_in_last_sync=0 THEN 'STALE_MONITOR'
        WHEN km.active=1 THEN 'BOUND_ACTIVE'
        WHEN km.active=0 THEN 'BOUND_INACTIVE'
        ELSE 'BOUND_UNKNOWN'
      END AS binding_state,
      mt.rationale,mt.source_ref,mt.last_verified_at,mt.notes
    FROM monitoring_targets mt
    LEFT JOIN projects p ON p.project_id=mt.project_id
    LEFT JOIN hosts h ON h.host_id=mt.host_id
    LEFT JOIN kuma_monitors km ON km.monitor_key=mt.kuma_monitor_key;

    CREATE VIEW telegram_notification_capability_index AS
    WITH x AS (
      SELECT 'explicit' kind,tc.capability_id entry_id,tc.project_id,p.slug project_slug,p.name project_name,p.status project_status,p.archived,
        'VERIFIED' strength,tc.mechanism,'telegram' mechanism_type,tc.status,NULL endpoint_ref,tc.source_ref,tc.explanation
      FROM telegram_project_capabilities tc JOIN projects p ON p.project_id=tc.project_id
      UNION ALL
      SELECT 'integration',i.integration_id,i.project_id,p.slug,p.name,p.status,p.archived,'CONFIGURED',i.name,i.type,i.status,i.endpoint_ref,NULL,i.notes
      FROM integrations i LEFT JOIN projects p ON p.project_id=i.project_id
      WHERE lower(coalesce(i.type,'')||' '||coalesce(i.name,'')||' '||coalesce(i.endpoint_ref,'')||' '||coalesce(i.notes,'')) LIKE '%telegram%'
      UNION ALL
      SELECT 'service',s.service_id,s.project_id,p.slug,p.name,p.status,p.archived,'CONFIGURED',s.name,coalesce(s.scope,'service'),s.state,NULL,s.source_ref,s.purpose
      FROM services s LEFT JOIN projects p ON p.project_id=s.project_id
      WHERE lower(coalesce(s.name,'')||' '||coalesce(s.scope,'')||' '||coalesce(s.unit,'')||' '||coalesce(s.runtime_path,'')||' '||coalesce(s.purpose,'')||' '||coalesce(s.source_ref,'')) LIKE '%telegram%'
      UNION ALL
      SELECT 'component',cast(pc.component_id AS TEXT),pc.project_id,p.slug,p.name,p.status,p.archived,'DOCUMENTED',pc.component,pc.type,NULL,NULL,pc.path,pc.purpose
      FROM project_components pc JOIN projects p ON p.project_id=pc.project_id
      WHERE lower(coalesce(pc.component,'')||' '||coalesce(pc.type,'')||' '||coalesce(pc.path,'')||' '||coalesce(pc.purpose,'')) LIKE '%telegram%'
      UNION ALL
      SELECT 'operation',cast(po.operation_id AS TEXT),po.project_id,p.slug,p.name,p.status,p.archived,'DOCUMENTED',po.operation,'operation',NULL,NULL,
        coalesce(po.workdir,'')||CASE WHEN coalesce(po.command,'')='' THEN '' ELSE ':'||po.command END,
        coalesce(po.scope,'')||CASE WHEN coalesce(po.notes,'')='' THEN '' ELSE ': '||po.notes END
      FROM project_operations po JOIN projects p ON p.project_id=po.project_id
      WHERE lower(coalesce(po.operation,'')||' '||coalesce(po.command,'')||' '||coalesce(po.scope,'')||' '||coalesce(po.host,'')||' '||coalesce(po.workdir,'')||' '||coalesce(po.notes,'')) LIKE '%telegram%'
    )
    SELECT kind AS entry_kind,entry_id,project_id,project_slug,project_name,project_status,archived AS project_archived,
      CASE WHEN project_id IS NULL THEN 'SHARED_OR_UNMAPPED_INFRASTRUCTURE' ELSE 'PROJECT_SCOPED' END project_mapping,
      strength AS evidence_strength,mechanism,mechanism_type,status,endpoint_ref,source_ref,explanation FROM x;

    CREATE VIEW telegram_notification_project_index AS
    SELECT project_id,project_slug,project_name,project_status,project_archived,
      CASE WHEN sum(evidence_strength='VERIFIED')>0 THEN 'VERIFIED'
           WHEN sum(evidence_strength='CONFIGURED' AND lower(coalesce(status,'')) NOT LIKE '%disabled%' AND lower(coalesce(status,'')) NOT LIKE '%removed%' AND lower(coalesce(status,'')) NOT LIKE '%not-found%' AND lower(coalesce(status,'')) NOT LIKE '%inactive%')>0 THEN 'CONFIGURED'
           WHEN sum(evidence_strength='DOCUMENTED')>0 THEN 'DOCUMENTED' ELSE 'DISABLED_OR_HISTORICAL' END capability_status,
      count(*) evidence_count,sum(evidence_strength='VERIFIED') verified_evidence_count,
      sum(evidence_strength='CONFIGURED') configured_evidence_count,sum(evidence_strength='DOCUMENTED') documented_evidence_count,
      group_concat(DISTINCT entry_kind||':'||entry_id||':'||mechanism) mechanisms,
      group_concat(DISTINCT coalesce(status,'')) statuses,group_concat(DISTINCT coalesce(endpoint_ref,'')) endpoint_refs,
      group_concat(DISTINCT coalesce(source_ref,'')) source_refs
    FROM telegram_notification_capability_index WHERE project_id IS NOT NULL
    GROUP BY project_id,project_slug,project_name,project_status,project_archived;

    CREATE VIEW telegram_shared_infrastructure_index AS
    SELECT entry_kind,entry_id,evidence_strength,mechanism,mechanism_type,status,endpoint_ref,source_ref,explanation
    FROM telegram_notification_capability_index WHERE project_id IS NULL;
    """)
    c.execute("""INSERT INTO schema_meta(key,value) VALUES('operational_index_version',?)
      ON CONFLICT(key) DO UPDATE SET value=excluded.value""", (str(VERSION),))


def migrate(path=DB):
    try:
        c = conn(path)
        with c: ensure(c)
        bad = c.execute("PRAGMA foreign_key_check").fetchall()
        c.close()
        if bad: raise RuntimeError(f"foreign_key_check={bad!r}")
        print("OPERATIONAL_INDEX_MIGRATE=PASS")
        return 0
    except Exception as e:
        print(f"OPERATIONAL_INDEX_MIGRATE=FAIL {e}", file=sys.stderr); return 1


def validate(path=DB):
    c = conn(path, True)
    try:
        ver = c.execute("select value from schema_meta where key='operational_index_version'").fetchone()
        meta = c.execute("select status from operational_inventory_meta where inventory_key='kuma_monitors'").fetchone()
        if not ver or ver[0] != str(VERSION) or not meta:
            print("OPERATIONAL_INDEX_VALIDATE=FAIL schema_not_migrated", file=sys.stderr); return 1
        status = meta[0]
        current = c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1").fetchone()[0]
        unmapped = c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1 and project_mapping='UNMAPPED'").fetchone()[0]
        missing = c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1 and explanation_status='MISSING'").fetchone()[0]
        tproj = c.execute("select count(*) from telegram_notification_project_index").fetchone()[0]
        shared = c.execute("select count(*) from telegram_shared_infrastructure_index").fetchone()[0]
        targets = c.execute("select count(*) from monitoring_target_index").fetchone()[0]
        monitored_unbound = c.execute("select count(*) from monitoring_target_index where desired_state='MONITORED' and binding_state='UNBOUND'").fetchone()[0]
        target_missing = c.execute("select count(*) from monitoring_target_index where trim(coalesce(rationale,''))='' or trim(coalesce(source_ref,''))=''").fetchone()[0]
        if status == 'COMPLETE' and (not current or unmapped or missing):
            print(f"OPERATIONAL_INDEX_VALIDATE=FAIL kuma_status={status} current={current} unmapped={unmapped} missing_explanation={missing}", file=sys.stderr); return 1
        label = "PASS" if status == 'COMPLETE' and not monitored_unbound and not target_missing else "PASS_WITH_WARNINGS"
        print(f"OPERATIONAL_INDEX_VALIDATE={label} kuma_inventory_status={status} kuma_entries={current} kuma_unmapped={unmapped} kuma_missing_explanation={missing} monitoring_targets={targets} monitoring_unbound={monitored_unbound} monitoring_missing_metadata={target_missing} telegram_projects={tproj} telegram_shared_infrastructure={shared}")
        return 0
    finally: c.close()


def safe_target(row, cols):
    if 'hostname' in cols and row['hostname']:
        return f"host:{row['hostname']}" + (f":{row['port']}" if 'port' in cols and row['port'] else '')
    if 'url' in cols and row['url']:
        try:
            u = urlsplit(str(row['url']))
            if u.scheme and u.netloc: return f"url:{u.scheme}://{u.netloc}"
        except ValueError: pass
    if 'type' in cols and str(row['type'] or '').lower() == 'push': return 'push:token_redacted'
    return None


def kuma_sync(source_db, integration_id='INT0002', host_id=None, path=DB):
    srcp = Path(source_db).expanduser().resolve()
    if not srcp.exists(): print(f"KUMA_SYNC=FAIL source_not_found={srcp}", file=sys.stderr); return 1
    d = conn(path)
    try:
        with d: ensure(d)
        if not d.execute("select 1 from integrations where integration_id=?",(integration_id,)).fetchone():
            print(f"KUMA_SYNC=FAIL integration_not_found={integration_id}",file=sys.stderr); return 1
        s = sqlite3.connect(f"file:{srcp}?mode=ro", uri=True); s.row_factory=sqlite3.Row
        cols={r[1] for r in s.execute("pragma table_info(monitor)")}
        if not {'id','name'} <= cols: s.close(); print("KUMA_SYNC=FAIL invalid_monitor_table",file=sys.stderr); return 1
        selected=['id','name']+[x for x in ('type','active','hostname','port','url') if x in cols]
        rows=s.execute(f"select {','.join(selected)} from monitor order by id").fetchall(); s.close(); stamp=now()
        with d:
            d.execute("update kuma_monitors set seen_in_last_sync=0 where integration_id=?",(integration_id,))
            for r in rows:
                key=f"{integration_id}:{int(r['id'])}"; typ=str(r['type']) if 'type' in cols and r['type'] is not None else None
                active=int(bool(r['active'])) if 'active' in cols and r['active'] is not None else None
                d.execute("""INSERT INTO kuma_monitors(monitor_key,integration_id,native_monitor_id,host_id,name,monitor_type,active,seen_in_last_sync,target_ref,purpose,last_seen_at,source_ref)
                  VALUES(?,?,?,?,?,?,?,1,?,'UNKNOWN',?,?)
                  ON CONFLICT(monitor_key) DO UPDATE SET host_id=coalesce(excluded.host_id,kuma_monitors.host_id),name=excluded.name,monitor_type=excluded.monitor_type,active=excluded.active,seen_in_last_sync=1,target_ref=excluded.target_ref,last_seen_at=excluded.last_seen_at,source_ref=excluded.source_ref""",
                  (key,integration_id,int(r['id']),host_id,str(r['name']),typ,active,safe_target(r,cols),stamp,f"uptime-kuma-sqlite:monitor:{int(r['id'])}"))
            current=d.execute("select count(*) from kuma_monitors where integration_id=? and seen_in_last_sync=1",(integration_id,)).fetchone()[0]
            unmapped=d.execute("select count(*) from kuma_monitors km where integration_id=? and seen_in_last_sync=1 and not exists(select 1 from kuma_monitor_projects k where k.monitor_key=km.monitor_key)",(integration_id,)).fetchone()[0]
            missing=d.execute("select count(*) from kuma_monitors where integration_id=? and seen_in_last_sync=1 and (trim(coalesce(purpose,''))='' or upper(trim(purpose))='UNKNOWN')",(integration_id,)).fetchone()[0]
            status='DISCOVERED_EMPTY' if current==0 else ('DISCOVERED_NEEDS_MAPPING' if unmapped or missing else 'READY_TO_FINALIZE')
            d.execute("""UPDATE operational_inventory_meta SET status=?,source_ref=?,last_synced_at=?,notes=? WHERE inventory_key='kuma_monitors'""",
              (status,f"sqlite:{srcp.name}",stamp,f"current={current};unmapped={unmapped};missing_explanation={missing}"))
        print(f"KUMA_SYNC=PASS current={current} unmapped={unmapped} missing_explanation={missing} status={status}"); return 0
    except Exception as e:
        print(f"KUMA_SYNC=FAIL {e}",file=sys.stderr); return 1
    finally: d.close()


def kuma_map(key, project_id, relationship='depends_on_project', path=DB):
    c=conn(path)
    try:
        with c:
            ensure(c)
            if not c.execute("select 1 from kuma_monitors where monitor_key=?",(key,)).fetchone(): print(f"KUMA_MAP=FAIL monitor_not_found={key}",file=sys.stderr); return 1
            if not c.execute("select 1 from projects where project_id=?",(project_id,)).fetchone(): print(f"KUMA_MAP=FAIL project_not_found={project_id}",file=sys.stderr); return 1
            c.execute("INSERT OR REPLACE INTO kuma_monitor_projects(monitor_key,project_id,relationship) VALUES(?,?,?)",(key,project_id,relationship))
        print(f"KUMA_MAP=PASS monitor_key={key} project_id={project_id}"); return 0
    finally: c.close()


def kuma_describe(key, purpose, path=DB):
    if not purpose.strip() or purpose.strip().upper()=='UNKNOWN': print("KUMA_DESCRIBE=FAIL purpose_required",file=sys.stderr); return 1
    c=conn(path)
    try:
        with c:
            ensure(c); n=c.execute("update kuma_monitors set purpose=? where monitor_key=?",(purpose.strip(),key)).rowcount
        if not n: print(f"KUMA_DESCRIBE=FAIL monitor_not_found={key}",file=sys.stderr); return 1
        print(f"KUMA_DESCRIBE=PASS monitor_key={key}"); return 0
    finally: c.close()


def kuma_finalize(path=DB):
    c=conn(path)
    try:
        with c:
            ensure(c); current=c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1").fetchone()[0]
            unmapped=c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1 and project_mapping='UNMAPPED'").fetchone()[0]
            missing=c.execute("select count(*) from kuma_monitor_index where seen_in_last_sync=1 and explanation_status='MISSING'").fetchone()[0]
            if not current or unmapped or missing: print(f"KUMA_FINALIZE=FAIL current={current} unmapped={unmapped} missing_explanation={missing}",file=sys.stderr); return 1
            c.execute("update operational_inventory_meta set status='COMPLETE',notes=? where inventory_key='kuma_monitors'",(f"current={current};unmapped=0;missing_explanation=0",))
        print(f"KUMA_FINALIZE=PASS current={current}"); return 0
    finally: c.close()


def show_kuma(path=DB):
    c=conn(path,True)
    try:
        meta=c.execute("select status,last_synced_at,notes from operational_inventory_meta where inventory_key='kuma_monitors'").fetchone()
        print(f"KUMA_INVENTORY={meta[0]};last_synced_at={meta[1] or ''};notes={meta[2] or ''}")
        for r in c.execute("select monitor_key,monitor_name,monitor_type,monitor_state,explanation,project_ids,project_slugs,project_mapping,host_name from kuma_monitor_index order by native_monitor_id"):
            print(";".join(str(x or '') for x in r))
        return 0
    finally:c.close()


def monitoring_target_upsert(
    target_key,
    repository_slug,
    runtime_identity,
    signal_kind,
    producer,
    desired_state,
    rationale,
    source_ref,
    *,
    project_id=None,
    host_id=None,
    expected_interval_seconds=None,
    kuma_monitor_key=None,
    last_verified_at=None,
    notes=None,
    path=DB,
):
    if signal_kind not in {'systemd_daemon','systemd_job_freshness','http','push','event_job','manual','none'}:
        print(f"MONITORING_TARGET_UPSERT=FAIL invalid_signal_kind={signal_kind}", file=sys.stderr); return 1
    if desired_state not in {'MONITORED','EXCLUDED','PENDING'}:
        print(f"MONITORING_TARGET_UPSERT=FAIL invalid_desired_state={desired_state}", file=sys.stderr); return 1
    if expected_interval_seconds is not None and int(expected_interval_seconds) <= 0:
        print("MONITORING_TARGET_UPSERT=FAIL expected_interval_seconds_must_be_positive", file=sys.stderr); return 1
    if not rationale.strip() or not source_ref.strip():
        print("MONITORING_TARGET_UPSERT=FAIL rationale_and_source_ref_required", file=sys.stderr); return 1
    c=conn(path)
    try:
        with c:
            ensure(c)
            if project_id is not None and not c.execute("select 1 from projects where project_id=?",(project_id,)).fetchone():
                print(f"MONITORING_TARGET_UPSERT=FAIL project_not_found={project_id}", file=sys.stderr); return 1
            if host_id is not None and not c.execute("select 1 from hosts where host_id=?",(host_id,)).fetchone():
                print(f"MONITORING_TARGET_UPSERT=FAIL host_not_found={host_id}", file=sys.stderr); return 1
            if kuma_monitor_key is not None and not c.execute("select 1 from kuma_monitors where monitor_key=?",(kuma_monitor_key,)).fetchone():
                print(f"MONITORING_TARGET_UPSERT=FAIL monitor_not_found={kuma_monitor_key}", file=sys.stderr); return 1
            c.execute("""INSERT INTO monitoring_targets(
              target_key,project_id,repository_slug,host_id,runtime_identity,signal_kind,producer,
              expected_interval_seconds,desired_state,kuma_monitor_key,rationale,source_ref,last_verified_at,notes)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
              ON CONFLICT(target_key) DO UPDATE SET
                project_id=excluded.project_id,repository_slug=excluded.repository_slug,host_id=excluded.host_id,
                runtime_identity=excluded.runtime_identity,signal_kind=excluded.signal_kind,producer=excluded.producer,
                expected_interval_seconds=excluded.expected_interval_seconds,desired_state=excluded.desired_state,
                kuma_monitor_key=excluded.kuma_monitor_key,rationale=excluded.rationale,source_ref=excluded.source_ref,
                last_verified_at=excluded.last_verified_at,notes=excluded.notes""",
              (target_key,project_id,repository_slug,host_id,runtime_identity,signal_kind,producer,
               expected_interval_seconds,desired_state,kuma_monitor_key,rationale.strip(),source_ref.strip(),last_verified_at,notes))
            count=c.execute("select count(*) from monitoring_targets").fetchone()[0]
            status='EMPTY' if count==0 else 'PLANNED'
            c.execute("""UPDATE operational_inventory_meta SET status=?,source_ref=?,last_synced_at=?,notes=?
              WHERE inventory_key='monitoring_targets'""",
              (status,'code:ai/operational_indexes.py',now(),f"targets={count}"))
        print(f"MONITORING_TARGET_UPSERT=PASS target_key={target_key}"); return 0
    finally: c.close()


def show_monitoring_targets(repository_slug=None,path=DB):
    c=conn(path,True)
    try:
        q="""select target_key,coalesce(project_id,''),repository_slug,coalesce(host_name,''),runtime_identity,
          signal_kind,producer,coalesce(expected_interval_seconds,''),desired_state,coalesce(kuma_monitor_key,''),
          binding_state,rationale,source_ref,coalesce(last_verified_at,'') from monitoring_target_index"""
        args=()
        if repository_slug is not None:
            q+=" where repository_slug=?"; args=(repository_slug,)
        for r in c.execute(q+" order by repository_slug,target_key",args):
            print(";".join(str(x or '') for x in r))
        return 0
    finally:c.close()


def show_telegram(project_id=None,path=DB):
    c=conn(path,True)
    try:
        q="select project_id,project_slug,capability_status,evidence_count,mechanisms from telegram_notification_project_index"; args=()
        if project_id is not None: q+=" where project_id=?"; args=(project_id,)
        for r in c.execute(q+" order by project_id",args): print(";".join(str(x or '') for x in r))
        return 0
    finally:c.close()


# Stable names used by the root CLI wrapper and tests.
migrate_operational_indexes = migrate
validate_operational_indexes = validate
sync_kuma_sqlite = kuma_sync
map_kuma_monitor = kuma_map
describe_kuma_monitor = kuma_describe
finalize_kuma_inventory = kuma_finalize
kuma_index_command = show_kuma
telegram_index_command = show_telegram
monitoring_target_upsert_command = monitoring_target_upsert
monitoring_target_index_command = show_monitoring_targets


def dispatch(argv):
    if not argv or argv[0] not in {'operational-index-migrate','operational-index-validate','kuma-index','kuma-sync-sqlite','kuma-map','kuma-describe','kuma-finalize','monitoring-target-upsert','monitoring-target-index','telegram-index'}: return None
    cmd=argv[0]; p=argparse.ArgumentParser(prog=f"megavault.py {cmd}")
    if cmd=='kuma-sync-sqlite': p.add_argument('--source-db',required=True); p.add_argument('--integration-id',default='INT0002'); p.add_argument('--host-id')
    elif cmd=='kuma-map': p.add_argument('--monitor-key',required=True); p.add_argument('--project-id',required=True,type=int); p.add_argument('--relationship',default='depends_on_project')
    elif cmd=='kuma-describe': p.add_argument('--monitor-key',required=True); p.add_argument('--purpose',required=True)
    elif cmd=='monitoring-target-upsert':
        p.add_argument('--target-key',required=True); p.add_argument('--repository-slug',required=True)
        p.add_argument('--runtime-identity',required=True); p.add_argument('--signal-kind',required=True)
        p.add_argument('--producer',required=True); p.add_argument('--desired-state',required=True)
        p.add_argument('--rationale',required=True); p.add_argument('--source-ref',required=True)
        p.add_argument('--project-id',type=int); p.add_argument('--host-id')
        p.add_argument('--expected-interval-seconds',type=int); p.add_argument('--kuma-monitor-key')
        p.add_argument('--last-verified-at'); p.add_argument('--notes')
    elif cmd=='monitoring-target-index': p.add_argument('--repository-slug')
    elif cmd=='telegram-index': p.add_argument('--project-id',type=int)
    a=p.parse_args(argv[1:])
    if cmd=='operational-index-migrate': return migrate()
    if cmd=='operational-index-validate': return validate()
    if cmd=='kuma-index': return show_kuma()
    if cmd=='kuma-sync-sqlite': return kuma_sync(a.source_db,a.integration_id,a.host_id)
    if cmd=='kuma-map': return kuma_map(a.monitor_key,a.project_id,a.relationship)
    if cmd=='kuma-describe': return kuma_describe(a.monitor_key,a.purpose)
    if cmd=='kuma-finalize': return kuma_finalize()
    if cmd=='monitoring-target-upsert': return monitoring_target_upsert(
        a.target_key,a.repository_slug,a.runtime_identity,a.signal_kind,a.producer,a.desired_state,
        a.rationale,a.source_ref,project_id=a.project_id,host_id=a.host_id,
        expected_interval_seconds=a.expected_interval_seconds,kuma_monitor_key=a.kuma_monitor_key,
        last_verified_at=a.last_verified_at,notes=a.notes)
    if cmd=='monitoring-target-index': return show_monitoring_targets(a.repository_slug)
    return show_telegram(a.project_id)
