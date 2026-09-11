import io
import sqlite3
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from ai import operational_indexes


class OperationalIndexTests(unittest.TestCase):
    def make_db(self, root: Path) -> Path:
        db = root / "megavault.sqlite"
        conn = sqlite3.connect(db)
        conn.executescript(
            """
            PRAGMA foreign_keys=ON;
            CREATE TABLE projects(
              project_id INTEGER PRIMARY KEY,
              slug TEXT NOT NULL,
              name TEXT NOT NULL,
              status TEXT NOT NULL,
              archived INTEGER NOT NULL DEFAULT 0
            );
            CREATE TABLE hosts(
              host_id TEXT PRIMARY KEY,
              name TEXT NOT NULL,
              kind TEXT NOT NULL
            );
            CREATE TABLE services(
              service_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id),
              host_id TEXT REFERENCES hosts(host_id),
              name TEXT NOT NULL,
              scope TEXT,
              unit TEXT,
              runtime_path TEXT,
              state TEXT,
              purpose TEXT,
              source_ref TEXT
            );
            CREATE TABLE integrations(
              integration_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id),
              type TEXT NOT NULL,
              name TEXT NOT NULL,
              endpoint_ref TEXT,
              status TEXT,
              notes TEXT
            );
            CREATE TABLE project_components(
              component_id INTEGER PRIMARY KEY AUTOINCREMENT,
              project_id INTEGER NOT NULL REFERENCES projects(project_id),
              component TEXT NOT NULL,
              type TEXT NOT NULL,
              path TEXT NOT NULL,
              purpose TEXT NOT NULL
            );
            CREATE TABLE project_operations(
              operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
              project_id INTEGER NOT NULL REFERENCES projects(project_id),
              operation TEXT NOT NULL,
              command TEXT NOT NULL,
              scope TEXT NOT NULL,
              host TEXT,
              workdir TEXT,
              risk_level TEXT NOT NULL,
              notes TEXT
            );
            CREATE TABLE schema_meta(
              key TEXT PRIMARY KEY,
              value TEXT NOT NULL
            );

            INSERT INTO projects(project_id, slug, name, status, archived)
            VALUES(8, 'codex-usage-monitor', 'Codex Usage Monitor', 'active', 0);

            INSERT INTO hosts(host_id, name, kind)
            VALUES('H0002', 'oracle-vm', 'remote_server');

            INSERT INTO services(
              service_id, project_id, host_id, name, scope, unit,
              runtime_path, state, purpose, source_ref
            ) VALUES(
              'S_TEST_KUMA', 8, 'H0002', 'usage health pusher', 'systemd',
              'usage-kuma.service', '/srv/usage-kuma', 'active',
              'Pushes Codex usage health to Uptime Kuma',
              'repo:codex-usage-monitor'
            );

            INSERT INTO integrations(
              integration_id, project_id, type, name, endpoint_ref, status, notes
            ) VALUES(
              'I_TEST_TELEGRAM', 8, 'notification', 'Telegram notifier',
              'secret_refs:telegram', 'active',
              'Sends eligible Codex usage alerts to Telegram'
            );

            INSERT INTO project_components(
              project_id, component, type, path, purpose
            ) VALUES(
              8, 'telegram_dispatch', 'python',
              '/srv/codex-usage-monitor/notifier.py',
              'Dispatches Telegram notifications'
            );
            """
        )
        conn.commit()
        conn.close()
        return db

    def test_migration_is_idempotent_and_creates_views(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            self.assertEqual(0, operational_indexes.migrate_operational_indexes(db))
            self.assertEqual(0, operational_indexes.migrate_operational_indexes(db))
            conn = sqlite3.connect(db)
            views = {
                row[0]
                for row in conn.execute(
                    """
                    select name from sqlite_master
                    where type='view' and name in (
                      'kuma_monitor_index',
                      'telegram_notification_capability_index',
                      'telegram_notification_project_index'
                    )
                    """
                )
            }
            version = conn.execute(
                "select value from schema_meta where key='operational_index_version'"
            ).fetchone()
            conn.close()
            self.assertEqual(
                {
                    "kuma_monitor_index",
                    "telegram_notification_capability_index",
                    "telegram_notification_project_index",
                },
                views,
            )
            self.assertEqual(("1",), version)

    def test_kuma_index_exposes_project_and_explanation(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            operational_indexes.migrate_operational_indexes(db)
            conn = sqlite3.connect(db)
            row = conn.execute(
                """
                select project_id, project_slug, host_name, monitor_name,
                       explanation, explanation_status
                from kuma_monitor_index
                where entry_id='S_TEST_KUMA'
                """
            ).fetchone()
            conn.close()
            self.assertEqual(
                (
                    8,
                    "codex-usage-monitor",
                    "oracle-vm",
                    "usage health pusher",
                    "Pushes Codex usage health to Uptime Kuma",
                    "DOCUMENTED",
                ),
                row,
            )

    def test_telegram_project_index_collapses_multiple_evidence_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            operational_indexes.migrate_operational_indexes(db)
            conn = sqlite3.connect(db)
            row = conn.execute(
                """
                select project_id, capability_status, evidence_count,
                       configured_evidence_count, documented_evidence_count
                from telegram_notification_project_index
                """
            ).fetchone()
            conn.close()
            self.assertEqual((8, "CONFIGURED", 2, 1, 1), row)

    def test_operational_validate_passes_for_complete_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            operational_indexes.migrate_operational_indexes(db)
            output = io.StringIO()
            with redirect_stdout(output):
                result = operational_indexes.validate_operational_indexes(db)
            self.assertEqual(0, result)
            self.assertIn("OPERATIONAL_INDEX_VALIDATE=PASS", output.getvalue())


if __name__ == "__main__":
    unittest.main()
