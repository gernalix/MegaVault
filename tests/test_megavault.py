import sqlite3
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
import megavault  # noqa: E402

PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"


class MegaVaultTests(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run(
            ["python3", str(ROOT / "megavault.py"), *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_validate_passes(self):
        result = self.run_tool("validate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("VALIDATE=PASS", result.stdout)

    def test_project_alias_resolves_from_database(self):
        result = self.run_tool("project", "luoghi-app")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("project_id=", result.stdout)
        self.assertIn("slug=luoghi", result.stdout)

    def test_project_id_is_integer_not_prefixed_text(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        value, storage_type = conn.execute(
            "select project_id, typeof(project_id) from projects where slug='luoghi'"
        ).fetchone()
        self.assertIsInstance(value, int)
        self.assertEqual(storage_type, "integer")

    def test_protocol_semantic_guard_detects_critical_removal(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        broken = text.replace("CAPSULIZATION=mandatory_all_projects\n", "", 1)
        errors = megavault.protocol_semantic_errors(broken)
        self.assertIn(
            "protocol_semantic_missing:capsulization:CAPSULIZATION=mandatory_all_projects",
            errors,
        )

    def test_secret_scan_has_zero_hits(self):
        self.assertEqual([], megavault.secret_scan_errors(megavault.git_tracked()))

    def legacy_incident_conn(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.executescript(
            """
            CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            INSERT INTO schema_meta(key, value) VALUES ('schema_version', '2');
            CREATE TABLE projects (
              project_id INTEGER PRIMARY KEY,
              slug TEXT NOT NULL UNIQUE,
              name TEXT NOT NULL,
              status TEXT NOT NULL,
              archived INTEGER NOT NULL DEFAULT 0,
              created_source TEXT NOT NULL,
              notes TEXT
            );
            CREATE TABLE incidents (
              incident_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id),
              title TEXT NOT NULL,
              first_seen_utc TEXT,
              last_seen_utc TEXT,
              occurrence_count TEXT,
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
            CREATE TABLE incident_events (
              incident_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
              incident_id TEXT NOT NULL REFERENCES incidents(incident_id),
              event_time_utc TEXT NOT NULL,
              severity TEXT,
              status TEXT,
              source TEXT,
              detail TEXT
            );
            INSERT INTO incidents(
              incident_id, title, occurrence_count, status, systems, alerts
            ) VALUES (
              'PIXEL_WHATSAPP_SILENT', 'Pixel WhatsApp silent notification', '1',
              'RESOLVED', 'Pixel 8a; Android 17; com.whatsapp',
              'silent_notification; notifications'
            );
            INSERT INTO incident_events(
              incident_id, event_time_utc, status, detail
            ) VALUES (
              'PIXEL_WHATSAPP_SILENT', '2026-08-02T02:16:17Z', 'RESOLVED',
              'legacy event'
            );
            """
        )
        return conn

    def migrated_incident_conn(self):
        conn = self.legacy_incident_conn()
        megavault.migrate_incident_schema(conn)
        conn.commit()
        conn.execute("PRAGMA foreign_keys=ON")
        self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())
        return conn

    def register_tags(self, conn, *names):
        for name in names:
            megavault.create_tag(conn, name)

    def test_migration_preserves_data_and_is_repeatable(self):
        conn = self.migrated_incident_conn()
        row = conn.execute(
            "select incident_id, legacy_incident_key, legacy_occurrence_note from incidents"
        ).fetchone()
        self.assertIsInstance(row[0], int)
        self.assertEqual("PIXEL_WHATSAPP_SILENT", row[1])
        self.assertEqual("1", row[2])
        self.assertEqual(1, conn.execute("select count(*) from incident_events").fetchone()[0])
        before = conn.execute(
            "select count(*), (select count(*) from incident_tags) from incidents"
        ).fetchone()
        self.assertFalse(megavault.migrate_incident_schema(conn))
        after = conn.execute(
            "select count(*), (select count(*) from incident_tags) from incidents"
        ).fetchone()
        self.assertEqual(before, after)

    def test_identical_occurrences_get_distinct_ids(self):
        conn = self.migrated_incident_conn()
        self.register_tags(conn, "whatsapp", "notifications")
        first = megavault.create_incident(
            conn, title="same occurrence", status="OPEN", tags=["whatsapp", "notifications"]
        )
        second = megavault.create_incident(
            conn, title="same occurrence", status="OPEN", tags=["whatsapp", "notifications"]
        )
        self.assertNotEqual(first, second)

    def test_aliases_casing_conflicts_and_idempotent_links(self):
        conn = self.migrated_incident_conn()
        tag_id, canonical = megavault.create_tag(conn, "Silent")
        self.assertEqual((tag_id, canonical), megavault.resolve_or_create_tag(conn, "silent"))
        megavault.add_tag_alias(conn, "no_sound", "SILENT")
        self.assertEqual((tag_id, canonical), megavault.resolve_tag(conn, "NO_SOUND"))
        with self.assertRaises(megavault.TagConflictError):
            megavault.create_tag(conn, "no_SOUND")
        incident_id = megavault.create_incident(
            conn, title="link test", status="OPEN", tags=["no_sound"]
        )
        megavault.link_incident_tag(conn, incident_id, "SILENT")
        self.assertEqual(
            1,
            conn.execute(
                "select count(*) from incident_tags where incident_id=? and tag_id=?",
                (incident_id, tag_id),
            ).fetchone()[0],
        )

    def test_multi_tag_search_uses_and_semantics(self):
        conn = self.migrated_incident_conn()
        self.register_tags(conn, "whatsapp", "notifications", "pixel", "silent")
        whatsapp = megavault.create_incident(
            conn, title="whatsapp only", status="OPEN", tags=["whatsapp"]
        )
        both = megavault.create_incident(
            conn,
            title="whatsapp notifications",
            status="OPEN",
            tags=["whatsapp", "notifications"],
        )
        pixel_silent = megavault.create_incident(
            conn, title="pixel silent", status="OPEN", tags=["pixel", "silent"]
        )
        results = megavault.search_incidents_by_tags(conn, ["WHATSAPP", "notifications"])
        ids = {row[0] for row in results}
        self.assertIn(both, ids)
        self.assertNotIn(whatsapp, ids)
        self.assertNotIn(pixel_silent, ids)
        megavault.add_tag_alias(conn, "muted", "silent")
        self.assertEqual(
            [pixel_silent],
            [row[0] for row in megavault.search_incidents_by_tags(conn, ["PIXEL", "MUTED"])],
        )


if __name__ == "__main__":
    unittest.main()
