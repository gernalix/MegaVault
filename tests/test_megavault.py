import subprocess
import unittest
import sqlite3
import sys
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
              archived INTEGER NOT NULL DEFAULT 0 CHECK(archived IN (0,1)),
              created_source TEXT NOT NULL,
              notes TEXT
            );
            CREATE TABLE incidents (
              incident_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE SET NULL,
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
              incident_id TEXT NOT NULL REFERENCES incidents(incident_id) ON UPDATE CASCADE ON DELETE CASCADE,
              event_time_utc TEXT NOT NULL,
              severity TEXT,
              status TEXT,
              source TEXT,
              detail TEXT
            );
            """
        )
        conn.execute(
            """
            INSERT INTO incidents(
              incident_id, title, first_seen_utc, last_seen_utc, occurrence_count,
              severity, status, systems, alerts, source_ref
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "PIXEL_WHATSAPP_SUMMARY_CHANNEL_SILENT_NO_SOUND",
                "Pixel WhatsApp silent notification",
                "2026-08-02T02:16:17Z",
                "2026-08-02T02:16:17Z",
                "1",
                "medium",
                "RESOLVED",
                "Pixel 8a; Android 17; com.whatsapp",
                "silent_notification; notifications",
                "legacy",
            ),
        )
        conn.execute(
            """
            INSERT INTO incident_events(incident_id, event_time_utc, severity, status, source, detail)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                "PIXEL_WHATSAPP_SUMMARY_CHANNEL_SILENT_NO_SOUND",
                "2026-08-02T02:16:17Z",
                "medium",
                "RESOLVED",
                "test",
                "legacy event",
            ),
        )
        return conn

    def migrated_incident_conn(self):
        conn = self.legacy_incident_conn()
        megavault.migrate_incident_schema(conn)
        conn.commit()
        conn.execute("PRAGMA foreign_keys=ON")
        self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())
        return conn

    def test_migration_preserves_legacy_incidents_and_is_repeatable(self):
        conn = self.migrated_incident_conn()
        self.assertTrue(megavault.incident_id_is_integer(conn))
        row = conn.execute(
            """
            SELECT incident_id, legacy_incident_key, legacy_occurrence_note
            FROM incidents
            """
        ).fetchone()
        self.assertIsInstance(row[0], int)
        self.assertEqual(
            row[1], "PIXEL_WHATSAPP_SUMMARY_CHANNEL_SILENT_NO_SOUND"
        )
        self.assertEqual(row[2], "1")
        self.assertEqual(1, conn.execute("SELECT count(*) FROM incident_events").fetchone()[0])
        self.assertGreaterEqual(conn.execute("SELECT count(*) FROM tags").fetchone()[0], 5)

        before = conn.execute(
            "SELECT count(*), (SELECT count(*) FROM incident_tags) FROM incidents"
        ).fetchone()
        self.assertFalse(megavault.migrate_incident_schema(conn))
        after = conn.execute(
            "SELECT count(*), (SELECT count(*) FROM incident_tags) FROM incidents"
        ).fetchone()
        self.assertEqual(before, after)

    def test_identical_occurrences_get_distinct_sqlite_ids(self):
        conn = self.migrated_incident_conn()
        first = megavault.create_incident(
            conn,
            title="same observed occurrence",
            status="OPEN",
            first_seen_utc="2026-08-02T10:00:00Z",
            tags=["whatsapp", "notifications"],
        )
        second = megavault.create_incident(
            conn,
            title="same observed occurrence",
            status="OPEN",
            first_seen_utc="2026-08-02T10:00:00Z",
            tags=["whatsapp", "notifications"],
        )
        self.assertNotEqual(first, second)
        self.assertEqual(
            2,
            conn.execute(
                "SELECT count(*) FROM incidents WHERE title='same observed occurrence'"
            ).fetchone()[0],
        )

    def test_tag_resolution_aliases_and_casing_are_case_insensitive(self):
        conn = self.migrated_incident_conn()
        tag_id, canonical = megavault.resolve_or_create_tag(conn, "Silent")
        self.assertEqual("Silent", canonical)
        same_id, same_name = megavault.resolve_or_create_tag(conn, "silent")
        self.assertEqual((tag_id, canonical), (same_id, same_name))
        megavault.add_tag_alias(conn, "no_sound", "SILENT")
        self.assertEqual((tag_id, canonical), megavault.resolve_tag(conn, "NO_SOUND"))
        with self.assertRaises(megavault.TagConflictError):
            megavault.create_tag(conn, "no_SOUND")
        with self.assertRaises(megavault.TagConflictError):
            megavault.add_tag_alias(conn, "silent", "notifications")

    def test_incident_tag_link_is_idempotent_and_referential(self):
        conn = self.migrated_incident_conn()
        incident_id = megavault.create_incident(
            conn, title="link test", status="OPEN", tags=["pixel"]
        )
        megavault.link_incident_tag(conn, incident_id, "PIXEL")
        tag_id = megavault.resolve_tag(conn, "pixel")[0]
        self.assertEqual(
            1,
            conn.execute(
                "SELECT count(*) FROM incident_tags WHERE incident_id=? AND tag_id=?",
                (incident_id, tag_id),
            ).fetchone()[0],
        )
        with self.assertRaises(sqlite3.IntegrityError):
            conn.execute("DELETE FROM tags WHERE tag_id=?", (tag_id,))
        conn.rollback()
        conn.execute("DELETE FROM incidents WHERE incident_id=?", (incident_id,))
        self.assertEqual(
            0,
            conn.execute(
                "SELECT count(*) FROM incident_tags WHERE incident_id=?",
                (incident_id,),
            ).fetchone()[0],
        )
        unused_id, _ = megavault.create_tag(conn, "unused")
        megavault.add_tag_alias(conn, "old_unused", unused_id)
        conn.execute("DELETE FROM tags WHERE tag_id=?", (unused_id,))
        self.assertIsNone(
            conn.execute(
                "SELECT 1 FROM tag_aliases WHERE alias='old_unused'"
            ).fetchone()
        )

    def test_multi_tag_search_uses_and_semantics(self):
        conn = self.migrated_incident_conn()
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
            conn,
            title="pixel silent",
            status="OPEN",
            tags=["pixel", "silent"],
        )
        results = megavault.search_incidents_by_tags(
            conn, ["WHATSAPP", "notifications"]
        )
        self.assertIn(both, {row[0] for row in results})
        self.assertNotIn(whatsapp, {row[0] for row in results})
        self.assertNotIn(pixel_silent, {row[0] for row in results})

        megavault.add_tag_alias(conn, "muted", "silent")
        silent_results = megavault.search_incidents_by_tags(conn, ["PIXEL", "MUTED"])
        self.assertEqual([pixel_silent], [row[0] for row in silent_results])


if __name__ == "__main__":
    unittest.main()
