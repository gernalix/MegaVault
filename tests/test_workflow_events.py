from __future__ import annotations

from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest import mock

from ai import workflow_events


class WorkflowEventTests(unittest.TestCase):
    def make_db(self, root: Path) -> Path:
        path = root / "megavault.sqlite"
        conn = sqlite3.connect(path)
        conn.executescript(
            """
            PRAGMA foreign_keys=ON;
            create table projects(project_id integer primary key, slug text);
            insert into projects values(23, 'megavault');
            create table events(
              event_id text primary key,
              project_id integer not null references projects(project_id),
              category text not null,
              event_type text not null,
              event_time_utc text not null,
              status text not null,
              summary text not null,
              metadata_json text
            );
            """
        )
        conn.commit()
        conn.close()
        return path

    def test_event_create_and_scoped_validate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            with mock.patch.object(workflow_events, "DB", db):
                rc = workflow_events.dispatch([
                    "event-create", "--project-id", "23", "--category", "code",
                    "--type", "task_complete", "--status", "PASS", "--summary", "done",
                    "--metadata", '{"prompt_id":"418562"}',
                ])
                self.assertEqual(0, rc)
                conn = sqlite3.connect(db)
                event_id = conn.execute("select event_id from events").fetchone()[0]
                conn.close()
                self.assertEqual(0, workflow_events.dispatch(["event-validate", "--event-id", event_id]))
                self.assertEqual(0, workflow_events.dispatch(["event-validate", "--project-id", "23"]))

    def test_invalid_metadata_is_atomic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            with mock.patch.object(workflow_events, "DB", db):
                rc = workflow_events.dispatch([
                    "event-create", "--project-id", "23", "--category", "code",
                    "--type", "task_complete", "--status", "PASS", "--summary", "done",
                    "--metadata", "not-json",
                ])
            self.assertNotEqual(0, rc)
            conn = sqlite3.connect(db)
            self.assertEqual(0, conn.execute("select count(*) from events").fetchone()[0])
            conn.close()

    def test_missing_project_is_atomic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            with mock.patch.object(workflow_events, "DB", db):
                rc = workflow_events.dispatch([
                    "event-create", "--project-id", "999", "--category", "code",
                    "--type", "task_complete", "--status", "PASS", "--summary", "done",
                ])
            self.assertNotEqual(0, rc)
            conn = sqlite3.connect(db)
            self.assertEqual(0, conn.execute("select count(*) from events").fetchone()[0])
            conn.close()

    def test_scoped_validation_ignores_unrelated_global_issue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            db = self.make_db(Path(tmp))
            conn = sqlite3.connect(db)
            conn.execute("PRAGMA foreign_keys=OFF")
            conn.execute(
                "insert into events values(?,?,?,?,?,?,?,?)",
                ("bad", 999, "x", "x", "2026-01-01T00:00:00Z", "PASS", "bad", None),
            )
            conn.execute(
                "insert into events values(?,?,?,?,?,?,?,?)",
                ("good", 23, "x", "x", "2026-01-01T00:00:00Z", "PASS", "good", None),
            )
            conn.commit()
            conn.close()
            with mock.patch.object(workflow_events, "DB", db):
                self.assertEqual(0, workflow_events.dispatch(["event-validate", "--event-id", "good"]))
                self.assertEqual(0, workflow_events.dispatch(["event-validate", "--project-id", "23"]))


if __name__ == "__main__":
    unittest.main()
