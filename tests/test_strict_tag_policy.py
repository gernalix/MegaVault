import sqlite3
import unittest

import megavault


class StrictTagPolicyTests(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(
            """
            CREATE TABLE projects (project_id INTEGER PRIMARY KEY);
            CREATE TABLE incidents (
              incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
              project_id INTEGER REFERENCES projects(project_id),
              title TEXT NOT NULL,
              first_seen_utc TEXT,
              last_seen_utc TEXT,
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
            CREATE TABLE tags (
              tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL COLLATE NOCASE UNIQUE,
              description TEXT,
              created_at_utc TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE tag_aliases (
              alias TEXT PRIMARY KEY COLLATE NOCASE,
              tag_id INTEGER NOT NULL REFERENCES tags(tag_id) ON DELETE CASCADE
            );
            CREATE TABLE incident_tags (
              incident_id INTEGER NOT NULL REFERENCES incidents(incident_id) ON DELETE CASCADE,
              tag_id INTEGER NOT NULL REFERENCES tags(tag_id) ON DELETE RESTRICT,
              PRIMARY KEY (incident_id, tag_id)
            );
            """
        )

    def tearDown(self):
        self.conn.close()

    def test_link_rejects_unknown_tag_without_creating_it(self):
        incident_id = megavault.create_incident(
            self.conn, title="test", status="OPEN"
        )
        with self.assertRaises(megavault.TagNotFoundError):
            megavault.link_incident_tag(self.conn, incident_id, "typo_tag")
        self.assertEqual(0, self.conn.execute("SELECT count(*) FROM tags").fetchone()[0])

    def test_existing_alias_can_be_linked(self):
        tag_id, _ = megavault.create_tag(self.conn, "silent")
        megavault.add_tag_alias(self.conn, "muted", tag_id)
        incident_id = megavault.create_incident(
            self.conn, title="test", status="OPEN", tags=["MUTED"]
        )
        self.assertEqual(
            [(incident_id, tag_id)],
            self.conn.execute("SELECT incident_id, tag_id FROM incident_tags").fetchall(),
        )

    def test_alias_prevents_redundant_canonical_tag(self):
        tag_id, _ = megavault.create_tag(self.conn, "silent")
        megavault.add_tag_alias(self.conn, "silent_notification", tag_id)
        self.assertEqual((tag_id, "silent"), megavault.resolve_tag(self.conn, "silent_notification"))
        with self.assertRaises(megavault.TagConflictError):
            megavault.create_tag(self.conn, "silent_notification")

    def test_incident_create_rolls_back_when_any_tag_is_unknown(self):
        megavault.create_tag(self.conn, "known")
        before = self.conn.execute("SELECT count(*) FROM incidents").fetchone()[0]
        with self.assertRaises(megavault.TagNotFoundError):
            with self.conn:
                megavault.create_incident(
                    self.conn,
                    title="must rollback",
                    status="OPEN",
                    tags=["known", "unknown"],
                )
        after = self.conn.execute("SELECT count(*) FROM incidents").fetchone()[0]
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
