#!/usr/bin/env python3
"""Derived operational indexes for Uptime Kuma and Telegram capabilities."""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "megavault.sqlite"

OPERATIONAL_INDEX_VERSION = 1
KUMA_VIEW = "kuma_monitor_index"
TELEGRAM_EVIDENCE_VIEW = "telegram_notification_capability_index"
TELEGRAM_PROJECT_VIEW = "telegram_notification_project_index"

REQUIRED_TABLES = {
    "projects",
    "hosts",
    "services",
    "integrations",
    "project_components",
    "project_operations",
    "schema_meta",
}


def connect(path: Path | str = DB) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def normalized_sql(value: str | None) -> str:
    return " ".join((value or "").split())


def ensure_view(conn: sqlite3.Connection, name: str, view_sql: str) -> bool:
    current = conn.execute(
        "select sql from sqlite_master where type='view' and name=?",
        (name,),
    ).fetchone()
    if current and normalized_sql(current[0]) == normalized_sql(view_sql):
        return False
    conn.execute(f"DROP VIEW IF EXISTS {name}")
    conn.execute(view_sql)
    return True


def missing_required_tables(conn: sqlite3.Connection) -> list[str]:
    existing = {
        row[0]
        for row in conn.execute(
            "select name from sqlite_master where type='table'"
        )
    }
    return sorted(REQUIRED_TABLES - existing)


KUMA_VIEW_SQL = """
CREATE VIEW kuma_monitor_index AS
WITH candidates AS (
  SELECT
    'service' AS entry_kind,
    s.service_id AS entry_id,
    s.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    s.host_id,
    h.name AS host_name,
    s.name AS monitor_name,
    s.scope AS monitor_kind_hint,
    s.unit,
    s.runtime_path,
    s.state AS status,
    s.purpose AS explanation,
    CASE
      WHEN coalesce(trim(s.purpose), '')='' THEN 'MISSING'
      ELSE 'DOCUMENTED'
    END AS explanation_status,
    NULL AS endpoint_ref,
    s.source_ref,
    NULL AS notes
  FROM services s
  LEFT JOIN projects p ON p.project_id=s.project_id
  LEFT JOIN hosts h ON h.host_id=s.host_id
  WHERE lower(
    coalesce(s.name, '') || ' ' ||
    coalesce(s.scope, '') || ' ' ||
    coalesce(s.unit, '') || ' ' ||
    coalesce(s.runtime_path, '') || ' ' ||
    coalesce(s.purpose, '') || ' ' ||
    coalesce(s.source_ref, '')
  ) LIKE '%kuma%'

  UNION ALL

  SELECT
    'integration' AS entry_kind,
    i.integration_id AS entry_id,
    i.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    NULL AS host_id,
    NULL AS host_name,
    i.name AS monitor_name,
    i.type AS monitor_kind_hint,
    NULL AS unit,
    NULL AS runtime_path,
    i.status,
    coalesce(nullif(trim(i.notes), ''), i.name) AS explanation,
    CASE
      WHEN coalesce(trim(i.notes), '')='' THEN 'DERIVED_FROM_NAME'
      ELSE 'DOCUMENTED'
    END AS explanation_status,
    i.endpoint_ref,
    NULL AS source_ref,
    i.notes
  FROM integrations i
  LEFT JOIN projects p ON p.project_id=i.project_id
  WHERE lower(
    coalesce(i.type, '') || ' ' ||
    coalesce(i.name, '') || ' ' ||
    coalesce(i.endpoint_ref, '') || ' ' ||
    coalesce(i.status, '') || ' ' ||
    coalesce(i.notes, '')
  ) LIKE '%kuma%'
)
SELECT
  entry_kind,
  entry_id,
  project_id,
  project_slug,
  project_name,
  project_status,
  project_archived,
  CASE WHEN project_id IS NULL THEN 'UNMAPPED' ELSE 'MAPPED' END AS project_mapping,
  host_id,
  host_name,
  monitor_name,
  monitor_kind_hint,
  unit,
  runtime_path,
  status,
  explanation,
  explanation_status,
  endpoint_ref,
  source_ref,
  notes
FROM candidates
ORDER BY
  CASE WHEN project_id IS NULL THEN 1 ELSE 0 END,
  project_id,
  entry_kind,
  entry_id
"""


TELEGRAM_EVIDENCE_VIEW_SQL = """
CREATE VIEW telegram_notification_capability_index AS
WITH candidates AS (
  SELECT
    'integration' AS entry_kind,
    i.integration_id AS entry_id,
    i.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    'CONFIGURED' AS evidence_strength,
    i.name AS mechanism,
    i.type AS mechanism_type,
    i.status,
    i.endpoint_ref,
    NULL AS source_ref,
    i.notes AS explanation
  FROM integrations i
  LEFT JOIN projects p ON p.project_id=i.project_id
  WHERE lower(
    coalesce(i.type, '') || ' ' ||
    coalesce(i.name, '') || ' ' ||
    coalesce(i.endpoint_ref, '') || ' ' ||
    coalesce(i.notes, '')
  ) LIKE '%telegram%'

  UNION ALL

  SELECT
    'service' AS entry_kind,
    s.service_id AS entry_id,
    s.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    'CONFIGURED' AS evidence_strength,
    s.name AS mechanism,
    coalesce(s.scope, 'service') AS mechanism_type,
    s.state AS status,
    NULL AS endpoint_ref,
    s.source_ref,
    s.purpose AS explanation
  FROM services s
  LEFT JOIN projects p ON p.project_id=s.project_id
  WHERE lower(
    coalesce(s.name, '') || ' ' ||
    coalesce(s.scope, '') || ' ' ||
    coalesce(s.unit, '') || ' ' ||
    coalesce(s.runtime_path, '') || ' ' ||
    coalesce(s.purpose, '') || ' ' ||
    coalesce(s.source_ref, '')
  ) LIKE '%telegram%'

  UNION ALL

  SELECT
    'component' AS entry_kind,
    cast(pc.component_id AS TEXT) AS entry_id,
    pc.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    'DOCUMENTED' AS evidence_strength,
    pc.component AS mechanism,
    pc.type AS mechanism_type,
    NULL AS status,
    NULL AS endpoint_ref,
    pc.path AS source_ref,
    pc.purpose AS explanation
  FROM project_components pc
  JOIN projects p ON p.project_id=pc.project_id
  WHERE lower(
    coalesce(pc.component, '') || ' ' ||
    coalesce(pc.type, '') || ' ' ||
    coalesce(pc.path, '') || ' ' ||
    coalesce(pc.purpose, '')
  ) LIKE '%telegram%'

  UNION ALL

  SELECT
    'operation' AS entry_kind,
    cast(po.operation_id AS TEXT) AS entry_id,
    po.project_id,
    p.slug AS project_slug,
    p.name AS project_name,
    p.status AS project_status,
    p.archived AS project_archived,
    'DOCUMENTED' AS evidence_strength,
    po.operation AS mechanism,
    'operation' AS mechanism_type,
    NULL AS status,
    NULL AS endpoint_ref,
    coalesce(po.workdir, '') || CASE
      WHEN coalesce(po.command, '')='' THEN ''
      ELSE ':' || po.command
    END AS source_ref,
    coalesce(po.scope, '') || CASE
      WHEN coalesce(po.notes, '')='' THEN ''
      ELSE ': ' || po.notes
    END AS explanation
  FROM project_operations po
  JOIN projects p ON p.project_id=po.project_id
  WHERE lower(
    coalesce(po.operation, '') || ' ' ||
    coalesce(po.command, '') || ' ' ||
    coalesce(po.scope, '') || ' ' ||
    coalesce(po.host, '') || ' ' ||
    coalesce(po.workdir, '') || ' ' ||
    coalesce(po.notes, '')
  ) LIKE '%telegram%'
)
SELECT
  entry_kind,
  entry_id,
  project_id,
  project_slug,
  project_name,
  project_status,
  project_archived,
  CASE WHEN project_id IS NULL THEN 'UNMAPPED' ELSE 'MAPPED' END AS project_mapping,
  evidence_strength,
  mechanism,
  mechanism_type,
  status,
  endpoint_ref,
  source_ref,
  explanation
FROM candidates
ORDER BY
  CASE WHEN project_id IS NULL THEN 1 ELSE 0 END,
  project_id,
  evidence_strength DESC,
  entry_kind,
  entry_id
"""


TELEGRAM_PROJECT_VIEW_SQL = """
CREATE VIEW telegram_notification_project_index AS
WITH evidence AS (
  SELECT *
  FROM telegram_notification_capability_index
  WHERE project_id IS NOT NULL
)
SELECT
  e.project_id,
  e.project_slug,
  e.project_name,
  e.project_status,
  e.project_archived,
  CASE
    WHEN sum(
      CASE
        WHEN e.evidence_strength='CONFIGURED'
          AND lower(coalesce(e.status, '')) NOT LIKE '%disabled%'
          AND lower(coalesce(e.status, '')) NOT LIKE '%removed%'
          AND lower(coalesce(e.status, '')) NOT LIKE '%not-found%'
          AND lower(coalesce(e.status, '')) NOT LIKE '%inactive%'
        THEN 1
        ELSE 0
      END
    ) > 0 THEN 'CONFIGURED'
    WHEN sum(CASE WHEN e.evidence_strength='DOCUMENTED' THEN 1 ELSE 0 END) > 0
      THEN 'DOCUMENTED'
    ELSE 'DISABLED_OR_HISTORICAL'
  END AS capability_status,
  count(*) AS evidence_count,
  sum(CASE WHEN e.evidence_strength='CONFIGURED' THEN 1 ELSE 0 END)
    AS configured_evidence_count,
  sum(CASE WHEN e.evidence_strength='DOCUMENTED' THEN 1 ELSE 0 END)
    AS documented_evidence_count,
  group_concat(DISTINCT e.entry_kind || ':' || e.entry_id || ':' || e.mechanism)
    AS mechanisms,
  group_concat(DISTINCT coalesce(e.status, '')) AS statuses,
  group_concat(DISTINCT coalesce(e.endpoint_ref, '')) AS endpoint_refs,
  group_concat(DISTINCT coalesce(e.source_ref, '')) AS source_refs
FROM evidence e
GROUP BY
  e.project_id,
  e.project_slug,
  e.project_name,
  e.project_status,
  e.project_archived
ORDER BY e.project_id
"""


def ensure_operational_indexes(conn: sqlite3.Connection) -> bool:
    missing = missing_required_tables(conn)
    if missing:
        raise RuntimeError(
            "missing required MegaVault tables: " + ",".join(missing)
        )
    changed = False
    changed = ensure_view(conn, KUMA_VIEW, KUMA_VIEW_SQL) or changed
    changed = ensure_view(
        conn, TELEGRAM_EVIDENCE_VIEW, TELEGRAM_EVIDENCE_VIEW_SQL
    ) or changed
    changed = ensure_view(
        conn, TELEGRAM_PROJECT_VIEW, TELEGRAM_PROJECT_VIEW_SQL
    ) or changed
    before = conn.total_changes
    conn.execute(
        """
        insert into schema_meta(key, value)
        values('operational_index_version', ?)
        on conflict(key) do update set value=excluded.value
        where value is not excluded.value
        """,
        (str(OPERATIONAL_INDEX_VERSION),),
    )
    changed = changed or conn.total_changes > before
    return changed


def migrate_operational_indexes(path: Path | str = DB) -> int:
    conn = connect(path)
    try:
        with conn:
            changed = ensure_operational_indexes(conn)
        fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
        if fk_errors:
            print(
                f"OPERATIONAL_INDEX_MIGRATE=FAIL foreign_key_check={fk_errors!r}",
                file=sys.stderr,
            )
            return 1
    except Exception as exc:
        print(f"OPERATIONAL_INDEX_MIGRATE=FAIL {exc}", file=sys.stderr)
        return 1
    finally:
        conn.close()
    print(
        "OPERATIONAL_INDEX_MIGRATE=PASS status="
        + ("changed" if changed else "unchanged")
    )
    return 0


def _read_only_connection(path: Path | str = DB) -> sqlite3.Connection:
    uri = f"file:{Path(path).resolve()}?mode=ro"
    return sqlite3.connect(uri, uri=True)


def _views_exist(conn: sqlite3.Connection) -> bool:
    names = {
        row[0]
        for row in conn.execute(
            """
            select name
            from sqlite_master
            where type='view' and name in (?, ?, ?)
            """,
            (KUMA_VIEW, TELEGRAM_EVIDENCE_VIEW, TELEGRAM_PROJECT_VIEW),
        )
    }
    return names == {KUMA_VIEW, TELEGRAM_EVIDENCE_VIEW, TELEGRAM_PROJECT_VIEW}


def validate_operational_indexes(path: Path | str = DB) -> int:
    conn = _read_only_connection(path)
    try:
        if not _views_exist(conn):
            print(
                "OPERATIONAL_INDEX_VALIDATE=FAIL views_missing; "
                "run 'python3 megavault.py operational-index-migrate'",
                file=sys.stderr,
            )
            return 1
        version = conn.execute(
            "select value from schema_meta where key='operational_index_version'"
        ).fetchone()
        if not version or version[0] != str(OPERATIONAL_INDEX_VERSION):
            print(
                "OPERATIONAL_INDEX_VALIDATE=FAIL "
                f"version={version[0] if version else 'missing'} "
                f"expected={OPERATIONAL_INDEX_VERSION}",
                file=sys.stderr,
            )
            return 1
        unmapped_kuma = conn.execute(
            f"""
            select entry_kind, entry_id
            from {KUMA_VIEW}
            where project_id is null
            order by entry_kind, entry_id
            """
        ).fetchall()
        unmapped_telegram = conn.execute(
            f"""
            select entry_kind, entry_id
            from {TELEGRAM_EVIDENCE_VIEW}
            where project_id is null
            order by entry_kind, entry_id
            """
        ).fetchall()
        duplicate_telegram_projects = conn.execute(
            f"""
            select project_id
            from {TELEGRAM_PROJECT_VIEW}
            group by project_id
            having count(*) <> 1
            """
        ).fetchall()
        missing_kuma_explanation = conn.execute(
            f"""
            select entry_id
            from {KUMA_VIEW}
            where explanation_status='MISSING'
            """
        ).fetchall()
        if duplicate_telegram_projects:
            print(
                "OPERATIONAL_INDEX_VALIDATE=FAIL "
                f"duplicate_telegram_projects={duplicate_telegram_projects!r}",
                file=sys.stderr,
            )
            return 1
        if unmapped_kuma or unmapped_telegram or missing_kuma_explanation:
            print(
                "OPERATIONAL_INDEX_VALIDATE=FAIL "
                f"unmapped_kuma={unmapped_kuma!r} "
                f"unmapped_telegram={unmapped_telegram!r} "
                f"kuma_missing_explanation={missing_kuma_explanation!r}",
                file=sys.stderr,
            )
            return 1
        print(
            "OPERATIONAL_INDEX_VALIDATE=PASS "
            f"kuma_entries={conn.execute(f'select count(*) from {KUMA_VIEW}').fetchone()[0]} "
            f"telegram_projects={conn.execute(f'select count(*) from {TELEGRAM_PROJECT_VIEW}').fetchone()[0]}"
        )
        return 0
    finally:
        conn.close()


def _clean(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).replace(";", ",").split())


def _print_rows(rows: list[sqlite3.Row | tuple], fields: tuple[str, ...]) -> None:
    for row in rows:
        print(
            ";".join(
                f"{field}={_clean(value)}" for field, value in zip(fields, row)
            )
        )


KUMA_FIELDS = (
    "entry_kind",
    "entry_id",
    "project_id",
    "project_slug",
    "project_name",
    "project_mapping",
    "host_name",
    "monitor_name",
    "monitor_kind_hint",
    "unit",
    "runtime_path",
    "status",
    "explanation",
    "explanation_status",
    "endpoint_ref",
    "source_ref",
)

TELEGRAM_FIELDS = (
    "project_id",
    "project_slug",
    "project_name",
    "project_status",
    "project_archived",
    "capability_status",
    "evidence_count",
    "configured_evidence_count",
    "documented_evidence_count",
    "mechanisms",
    "statuses",
    "endpoint_refs",
    "source_refs",
)


def kuma_index_command(
    project_id: int | None = None, path: Path | str = DB
) -> int:
    conn = _read_only_connection(path)
    try:
        if not _views_exist(conn):
            print(
                "KUMA_INDEX=NOT_MIGRATED run 'python3 megavault.py operational-index-migrate'",
                file=sys.stderr,
            )
            return 1
        where = " where project_id=?" if project_id is not None else ""
        params: tuple[object, ...] = (project_id,) if project_id is not None else ()
        fields_sql = ", ".join(KUMA_FIELDS)
        rows = conn.execute(
            f"select {fields_sql} from {KUMA_VIEW}{where} "
            "order by project_id, entry_kind, entry_id",
            params,
        ).fetchall()
        _print_rows(rows, KUMA_FIELDS)
        return 0
    finally:
        conn.close()


def telegram_index_command(
    project_id: int | None = None, path: Path | str = DB
) -> int:
    conn = _read_only_connection(path)
    try:
        if not _views_exist(conn):
            print(
                "TELEGRAM_INDEX=NOT_MIGRATED run 'python3 megavault.py operational-index-migrate'",
                file=sys.stderr,
            )
            return 1
        where = " where project_id=?" if project_id is not None else ""
        params: tuple[object, ...] = (project_id,) if project_id is not None else ()
        fields_sql = ", ".join(TELEGRAM_FIELDS)
        rows = conn.execute(
            f"select {fields_sql} from {TELEGRAM_PROJECT_VIEW}{where} "
            "order by project_id",
            params,
        ).fetchall()
        _print_rows(rows, TELEGRAM_FIELDS)
        return 0
    finally:
        conn.close()


def dispatch(argv: list[str]) -> int | None:
    if not argv:
        return None
    command = argv[0]
    if command not in {
        "operational-index-migrate",
        "operational-index-validate",
        "kuma-index",
        "telegram-index",
    }:
        return None

    parser = argparse.ArgumentParser(prog=f"megavault.py {command}")
    if command in {"kuma-index", "telegram-index"}:
        parser.add_argument("--project-id", type=int)
    args = parser.parse_args(argv[1:])

    if command == "operational-index-migrate":
        return migrate_operational_indexes()
    if command == "operational-index-validate":
        return validate_operational_indexes()
    if command == "kuma-index":
        return kuma_index_command(args.project_id)
    if command == "telegram-index":
        return telegram_index_command(args.project_id)
    return 2
