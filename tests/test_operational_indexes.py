import io
import sqlite3
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from ai import operational_indexes


class OperationalIndexTests(unittest.TestCase):
    def make_db(self, root: Path) -> Path:
        db = root / "megavault.sqlite"
        c = sqlite3.connect(db)
        c.executescript("""
        PRAGMA foreign_keys=ON;
        CREATE TABLE projects(project_id INTEGER PRIMARY KEY,slug TEXT NOT NULL,name TEXT NOT NULL,status TEXT NOT NULL,archived INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE hosts(host_id TEXT PRIMARY KEY,name TEXT NOT NULL,kind TEXT NOT NULL);
        CREATE TABLE services(service_id TEXT PRIMARY KEY,project_id INTEGER REFERENCES projects(project_id),host_id TEXT REFERENCES hosts(host_id),name TEXT NOT NULL,scope TEXT,unit TEXT,runtime_path TEXT,state TEXT,purpose TEXT,source_ref TEXT);
        CREATE TABLE integrations(integration_id TEXT PRIMARY KEY,project_id INTEGER REFERENCES projects(project_id),type TEXT NOT NULL,name TEXT NOT NULL,endpoint_ref TEXT,status TEXT,notes TEXT);
        CREATE TABLE project_components(component_id INTEGER PRIMARY KEY AUTOINCREMENT,project_id INTEGER NOT NULL REFERENCES projects(project_id),component TEXT NOT NULL,type TEXT NOT NULL,path TEXT NOT NULL,purpose TEXT NOT NULL);
        CREATE TABLE project_operations(operation_id INTEGER PRIMARY KEY AUTOINCREMENT,project_id INTEGER NOT NULL REFERENCES projects(project_id),operation TEXT NOT NULL,command TEXT NOT NULL,scope TEXT NOT NULL,host TEXT,workdir TEXT,risk_level TEXT NOT NULL,notes TEXT);
        CREATE TABLE schema_meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
        INSERT INTO projects VALUES(8,'codex-usage-monitor','Codex Usage Monitor','active',0);
        INSERT INTO projects VALUES(56,'android-build-telegram-watch-v1','Android Build Telegram Watch','active',0);
        INSERT INTO hosts VALUES('H0002','oracle-vm','remote_server');
        INSERT INTO integrations VALUES('INT0001',NULL,'telegram','telegram_shared','/safe/telegram.env','active','shared infrastructure');
        INSERT INTO integrations VALUES('INT0002',NULL,'uptime_kuma','oracle_kuma','remote:example','active','values_not_stored');
        INSERT INTO services VALUES('S1',8,'H0002','usage Telegram notifier','systemd','usage.service','/srv/usage','active','Sends usage alerts to Telegram','repo:usage');
        INSERT INTO services VALUES('S2',NULL,'H0002','telegram-media-monitor.service','systemd','telegram-media-monitor.service',NULL,'oneshot_last_result_success',NULL,'registry');
        """)
        c.commit(); c.close(); return db

    def make_kuma_source(self, root: Path) -> Path:
        db = root / "kuma.db"
        c = sqlite3.connect(db)
        c.executescript("""
        CREATE TABLE monitor(id INTEGER PRIMARY KEY,name TEXT NOT NULL,type TEXT,active INTEGER,hostname TEXT,port INTEGER,url TEXT);
        INSERT INTO monitor VALUES(1,'HTTP API','http',1,NULL,NULL,'https://api.example/private/path?token=SECRET_VALUE');
        INSERT INTO monitor VALUES(2,'Push heartbeat','push',1,NULL,NULL,'https://kuma.example/api/push/SECRET_PUSH_TOKEN?status=up');
        """)
        c.commit(); c.close(); return db

    def test_migration_and_telegram_indexes(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            self.assertEqual(0, operational_indexes.migrate_operational_indexes(db))
            c = sqlite3.connect(db)
            self.assertEqual(('NOT_SYNCED',), c.execute("select status from operational_inventory_meta where inventory_key='kuma_monitors'").fetchone())
            rows = c.execute("select project_id,capability_status from telegram_notification_project_index order by project_id").fetchall()
            self.assertIn((8,'CONFIGURED'), rows)
            self.assertIn((56,'VERIFIED'), rows)
            self.assertEqual(2, c.execute("select count(*) from telegram_shared_infrastructure_index").fetchone()[0])
            c.close()

    def test_not_synced_is_warning_not_false_complete(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp)); operational_indexes.migrate_operational_indexes(db)
            out = io.StringIO()
            with redirect_stdout(out): result = operational_indexes.validate_operational_indexes(db)
            self.assertEqual(0, result)
            self.assertIn('PASS_WITH_WARNINGS', out.getvalue())
            self.assertIn('kuma_inventory_status=NOT_SYNCED', out.getvalue())

    def test_kuma_sync_sanitizes_and_requires_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); db = self.make_db(root); source = self.make_kuma_source(root)
            operational_indexes.migrate_operational_indexes(db)
            self.assertEqual(0, operational_indexes.sync_kuma_sqlite(source,'INT0002','H0002',db))
            c = sqlite3.connect(db)
            rows = c.execute("select monitor_key,target_ref,purpose from kuma_monitors order by native_monitor_id").fetchall()
            self.assertEqual('DISCOVERED_NEEDS_MAPPING', c.execute("select status from operational_inventory_meta where inventory_key='kuma_monitors'").fetchone()[0])
            c.close()
            self.assertEqual('url:https://api.example', rows[0][1])
            self.assertEqual('url:https://kuma.example', rows[1][1])
            self.assertNotIn('SECRET_VALUE', repr(rows)); self.assertNotIn('SECRET_PUSH_TOKEN', repr(rows))
            err = io.StringIO()
            with redirect_stderr(err): self.assertEqual(1, operational_indexes.finalize_kuma_inventory(db))
            self.assertIn('KUMA_FINALIZE=FAIL', err.getvalue())
            for key,pid,purpose in (
                ('INT0002:1',8,'Checks the Codex usage API endpoint.'),
                ('INT0002:2',56,'Receives Android build watcher health pushes.'),
            ):
                self.assertEqual(0, operational_indexes.map_kuma_monitor(key,pid,path=db))
                self.assertEqual(0, operational_indexes.describe_kuma_monitor(key,purpose,path=db))
            self.assertEqual(0, operational_indexes.finalize_kuma_inventory(db))
            self.assertEqual(0, operational_indexes.validate_operational_indexes(db))


if __name__ == '__main__':
    unittest.main()
