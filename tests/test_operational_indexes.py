import io
import hashlib
import sqlite3
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from ai import operational_indexes
from ai import periodic_services


class OperationalIndexTests(unittest.TestCase):
    def make_db(self, root: Path) -> Path:
        db = root / "megavault.sqlite"
        c = sqlite3.connect(db)
        c.executescript("""
        PRAGMA foreign_keys=ON;
        CREATE TABLE projects(project_id INTEGER PRIMARY KEY,slug TEXT NOT NULL,name TEXT NOT NULL,status TEXT NOT NULL,archived INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE repositories(repository_id TEXT PRIMARY KEY,project_id INTEGER NOT NULL REFERENCES projects(project_id),canonical INTEGER NOT NULL,worktree_path TEXT);
        CREATE TABLE hosts(host_id TEXT PRIMARY KEY,name TEXT NOT NULL,kind TEXT NOT NULL);
        CREATE TABLE services(service_id TEXT PRIMARY KEY,project_id INTEGER REFERENCES projects(project_id),host_id TEXT REFERENCES hosts(host_id),name TEXT NOT NULL,scope TEXT,unit TEXT,runtime_path TEXT,state TEXT,purpose TEXT,source_ref TEXT);
        CREATE TABLE integrations(integration_id TEXT PRIMARY KEY,project_id INTEGER REFERENCES projects(project_id),type TEXT NOT NULL,name TEXT NOT NULL,endpoint_ref TEXT,status TEXT,notes TEXT);
        CREATE TABLE project_components(component_id INTEGER PRIMARY KEY AUTOINCREMENT,project_id INTEGER NOT NULL REFERENCES projects(project_id),component TEXT NOT NULL,type TEXT NOT NULL,path TEXT NOT NULL,purpose TEXT NOT NULL);
        CREATE TABLE project_operations(operation_id INTEGER PRIMARY KEY AUTOINCREMENT,project_id INTEGER NOT NULL REFERENCES projects(project_id),operation TEXT NOT NULL,command TEXT NOT NULL,scope TEXT NOT NULL,host TEXT,workdir TEXT,risk_level TEXT NOT NULL,notes TEXT);
        CREATE TABLE schema_meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
        INSERT INTO projects VALUES(8,'codex-usage-monitor','Codex Usage Monitor','active',0);
        INSERT INTO projects VALUES(56,'android-build-telegram-watch-v1','Android Build Telegram Watch','active',0);
        INSERT INTO hosts VALUES('H0002','oracle-vm','remote_server');
        INSERT INTO hosts VALUES('H0001','fedora','local_workstation');
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

    def test_monitoring_target_registry_tracks_cross_repo_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            self.assertEqual(0, operational_indexes.migrate_operational_indexes(db))
            self.assertEqual(
                0,
                operational_indexes.monitoring_target_upsert_command(
                    "repo:codex-usage-monitor",
                    "gernalix/codex-usage-monitor",
                    "user:codex-usage-monitor.service",
                    "systemd_job_freshness",
                    "fedora-system-monitor",
                    "MONITORED",
                    "Quota acquisition must complete on schedule.",
                    "repo:gernalix/codex-usage-monitor/systemd/codex-usage-monitor.service",
                    project_id=8,
                    expected_interval_seconds=1800,
                    path=db,
                ),
            )
            c = sqlite3.connect(db)
            row = c.execute(
                "select repository_slug,signal_kind,producer,desired_state,binding_state "
                "from monitoring_target_index where target_key='repo:codex-usage-monitor'"
            ).fetchone()
            self.assertEqual(
                ("gernalix/codex-usage-monitor","systemd_job_freshness","fedora-system-monitor","MONITORED","UNBOUND"),
                row,
            )
            self.assertEqual(
                ("PLANNED",),
                c.execute("select status from operational_inventory_meta where inventory_key='monitoring_targets'").fetchone(),
            )
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

    def test_kuma_sanitized_json_sync_is_idempotent_and_rejects_secret_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); db = self.make_db(root); source = root / "monitors.json"
            operational_indexes.migrate_operational_indexes(db)
            source.write_text('{"monitors":[{"id":7,"name":"Job","type":"push","active":1}]}')
            self.assertEqual(0, operational_indexes.kuma_sync_json(source, "INT0002", "H0002", db))
            self.assertEqual(0, operational_indexes.kuma_sync_json(source, "INT0002", "H0002", db))
            c = sqlite3.connect(db)
            self.assertEqual((1, "push:token_redacted"), c.execute(
                "select count(*),target_ref from kuma_monitors where monitor_key='INT0002:7'").fetchone())
            c.close()
            source.write_text('{"monitors":[{"id":7,"name":"Job","type":"push","active":1,"pushToken":"secret"}]}')
            self.assertEqual(1, operational_indexes.kuma_sync_json(source, "INT0002", "H0002", db))

    def test_periodic_discovery_reconciliation_and_source_staleness(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); db = self.make_db(root)
            unit_dir = root / "repo" / "systemd"; unit_dir.mkdir(parents=True)
            timer_path = unit_dir / "critical-sync.timer"
            timer_path.write_text("[Timer]\nOnCalendar=*:0/15\nPersistent=true\n")
            digest = hashlib.sha256(timer_path.read_bytes()).hexdigest()
            c = sqlite3.connect(db)
            c.execute("insert into repositories values('R1',8,1,?)", (str(root / "repo"),))
            c.commit(); c.close()
            operational_indexes.migrate_operational_indexes(db)
            operational_indexes.monitoring_target_upsert_command(
                "critical-sync", "gernalix/codex-usage-monitor", "critical-sync.service",
                "systemd_job_freshness", "fedora-system-monitor", "MONITORED",
                "Independent durable synchronization freshness.", "test:critical-sync.timer",
                project_id=8, host_id="H0001", expected_interval_seconds=1800, path=db,
            )
            snapshot = {"schema": 1, "timers": [
                self.periodic_row("critical-sync", "/etc/systemd/system/critical-sync.timer", digest),
                self.periodic_row("dnf-makecache", "/usr/lib/systemd/system/dnf-makecache.timer", "a" * 64),
                self.periodic_row("worker-watchdog", "/etc/systemd/system/worker-watchdog.timer", "b" * 64),
            ]}
            c = sqlite3.connect(db)
            with c:
                first = periodic_services.reconcile_snapshot(snapshot, "H0001", c)
                second = periodic_services.reconcile_snapshot(snapshot, "H0001", c)
                c.execute("insert into periodic_service_reconciliations values('H0001','user','x','now',0)")
                c.execute("insert into periodic_service_reconciliations values('H0002','system','x','now',0)")
            self.assertEqual(first, second)
            self.assertEqual(3, c.execute("select count(*) from periodic_service_registry where present=1").fetchone()[0])
            decisions = dict(c.execute("select timer_unit,monitoring_decision from periodic_service_registry"))
            self.assertEqual("MONITORED", decisions["critical-sync.timer"])
            self.assertEqual("EXCLUDED", decisions["dnf-makecache.timer"])
            self.assertEqual("EXCLUDED", decisions["worker-watchdog.timer"])
            self.assertTrue(periodic_services.validate(c)[0])
            timer_path.write_text(timer_path.read_text() + "RandomizedDelaySec=1m\n")
            self.assertFalse(periodic_services.validate(c)[0])
            c.close()

    @staticmethod
    def periodic_row(name, path, digest):
        return {
            "scope": "system", "timer_unit": f"{name}.timer", "service_unit": f"{name}.service",
            "enabled_state": "enabled", "active_state": "active", "sub_state": "waiting",
            "service_active_state": "inactive", "service_result": "success", "service_exec_status": "0",
            "last_trigger": "now", "next_trigger": "later",
            "timer_source": {"path": path, "sha256": digest, "line_start": 1, "line_end": 3},
            "service_source": {"path": path.replace(".timer", ".service"), "sha256": None, "line_start": None, "line_end": None},
        }

    def test_monitor_decision_does_not_create_completeness_monitors(self):
        decision = periodic_services.monitor_decision(
            target=None, defining_path="/usr/lib/systemd/system/fstrim.timer", timer_unit="fstrim.timer")
        self.assertEqual(("EXCLUDED", "SYSTEM_FACILITY"), decision[:2])
        decision = periodic_services.monitor_decision(
            target=None, defining_path="/etc/systemd/system/c2-watchdog.timer", timer_unit="c2-watchdog.timer")
        self.assertEqual(("EXCLUDED", "INTERNAL_HELPER"), decision[:2])
        decision = periodic_services.monitor_decision(
            target=None, defining_path="/etc/systemd/system/new-backup.timer", timer_unit="new-backup.timer")
        self.assertEqual(("PENDING", "MISSING_TARGET"), decision[:2])


if __name__ == '__main__':
    unittest.main()
