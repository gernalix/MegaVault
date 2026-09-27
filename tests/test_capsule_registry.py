import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from ai import capsule_registry


class CapsuleRegistryTests(unittest.TestCase):
    def make_conn(self):
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        conn.executescript(
            """
            PRAGMA foreign_keys=ON;
            CREATE TABLE projects (
              project_id INTEGER PRIMARY KEY,
              slug TEXT NOT NULL,
              archived INTEGER NOT NULL
            );
            CREATE TABLE repositories (
              repository_id TEXT PRIMARY KEY,
              project_id INTEGER NOT NULL REFERENCES projects(project_id),
              repository_kind TEXT,
              canonical INTEGER NOT NULL,
              worktree_path TEXT,
              remote_url TEXT,
              runtime_path TEXT
            );
            INSERT INTO projects VALUES (1, 'active-project', 0);
            INSERT INTO projects VALUES (2, 'retired-project', 1);
            INSERT INTO repositories VALUES ('R1', 1, 'local_worktree', 1, NULL, NULL, NULL);
            INSERT INTO repositories VALUES ('R1-OLD', 1, 'legacy', 0, NULL, NULL, NULL);
            INSERT INTO repositories VALUES ('R2', 2, 'local_worktree', 1, NULL, NULL, NULL);
            """
        )
        capsule_registry.ensure_schema(conn)
        self.addCleanup(conn.close)
        return conn

    def test_inventory_is_linked_and_has_explicit_exclusions(self):
        conn = self.make_conn()
        self.assertFalse(capsule_registry.ensure_schema(conn))
        rows = {
            row["repository_id"]: (row["coverage_state"], row["exclusion_reason"])
            for row in capsule_registry.inventory_rows(conn)
        }
        self.assertEqual(("eligible", None), rows["R1"])
        self.assertEqual(("excluded", "obsolete"), rows["R2"])
        self.assertEqual(("excluded", "fully_absorbed"), rows["R1-OLD"])
        conn.execute(
            "insert into capsule_repository_policy values (?, ?, ?, ?, ?)",
            ("R1-OLD", "excluded", "fully_absorbed", "test", "2026-09-27T00:00:00Z"),
        )
        row = conn.execute(
            "select exclusion_reason from capsule_inventory where repository_id='R1-OLD'"
        ).fetchone()
        self.assertEqual("fully_absorbed", row[0])
        self.assertEqual([], capsule_registry.schema_errors(conn))

    def test_fast_discovery_keeps_presence_separate_from_verification(self):
        conn = self.make_conn()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "AGENTS.md").write_text("rules\n", encoding="utf-8")
            (repo / "project-capsule.json").write_text(
                json.dumps(
                    {
                        "artifacts": {"agents": "AGENTS.md"},
                        "validation_hooks": [
                            {"id": "unit", "argv": ["python3", "-V"], "cwd": ".", "safe": True}
                        ],
                        "change_verification": [
                            {"paths": ["src/*.py"], "commands": ["unit"]}
                        ],
                    }
                ),
                encoding="utf-8",
            )
            conn.execute("update repositories set worktree_path=? where repository_id='R1'", (str(repo),))
            row = capsule_registry.inventory_rows(conn, "R1")[0]
            report = capsule_registry.check_repository(
                row, mode="FAST", changed_files=["src/main.py", "docs/readme.md"]
            )
        self.assertEqual("present", report["artifacts"]["agents"]["presence_state"])
        self.assertEqual("unverified", report["artifacts"]["agents"]["verification_state"])
        self.assertEqual("pass", report["artifacts"]["manifest"]["verification_state"])
        self.assertIn("change_verification_mapping_missing:docs/readme.md", report["gaps"])
        self.assertEqual(["unit"], report["changed_file_verification"][1]["commands"])

    def test_full_runs_only_hooks_explicitly_declared_safe(self):
        conn = self.make_conn()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "project-capsule.json").write_text(
                json.dumps(
                    {
                        "validation_hooks": [
                            {"id": "safe", "argv": ["python3", "-c", "raise SystemExit(0)"], "safe": True},
                            {"id": "unsafe", "argv": ["python3", "-c", "raise SystemExit(1)"], "safe": False},
                        ]
                    }
                ),
                encoding="utf-8",
            )
            conn.execute("update repositories set worktree_path=? where repository_id='R1'", (str(repo),))
            row = capsule_registry.inventory_rows(conn, "R1")[0]
            report = capsule_registry.check_repository(row, mode="FULL")
        executed = [item["criterion_id"] for item in report["criteria"] if item["criterion_id"].startswith("validation_hook:")]
        self.assertEqual(["validation_hook:safe"], executed)

    def test_external_standard_adds_raw_unweighted_criteria(self):
        conn = self.make_conn()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / "AGENTS.md").write_text("rules\n", encoding="utf-8")
            conn.execute("update repositories set worktree_path=? where repository_id='R1'", (str(repo),))
            row = capsule_registry.inventory_rows(conn, "R1")[0]
            report = capsule_registry.check_repository(
                row,
                standard={
                    "criteria": [{"id": "operating_rules", "artifact": "agents", "weight": 99}]
                },
            )
        criterion = next(item for item in report["criteria"] if item["criterion_id"] == "operating_rules")
        self.assertEqual("unverified", criterion["state"])
        self.assertNotIn("weight", criterion)

    def test_recording_keeps_discovery_and_verification_separate(self):
        conn = self.make_conn()
        report = {
            "project_id": 1,
            "project_slug": "active-project",
            "repository_id": "R1",
            "coverage_state": "eligible",
            "exclusion_reason": None,
            "mode": "FAST",
            "standard_ref": None,
            "artifacts": {
                "manifest": {
                    "path": "project-capsule.json",
                    "presence_state": "present",
                    "verification_state": "pass",
                    "source_sha256": "a" * 64,
                    "source_timestamp_utc": "2026-09-27T00:00:00+00:00",
                },
                "agents": {
                    "path": "AGENTS.md",
                    "presence_state": "present",
                    "verification_state": "unverified",
                },
            },
            "criteria": [
                {"criterion_id": "artifact:manifest", "state": "pass", "evidence": {}},
                {"criterion_id": "artifact:agents", "state": "unverified", "evidence": {}},
            ],
            "freshness": {
                "repository_head": "b" * 40,
                "checked_at_utc": "2026-09-27T00:00:00+00:00",
            },
            "gaps": [],
        }
        capsule_registry.record_reports(conn, [report])
        row = conn.execute(
            "select discovery_state, verification_state from capsule_registry where repository_id='R1'"
        ).fetchone()
        self.assertEqual(("present", "unverified"), tuple(row))


if __name__ == "__main__":
    unittest.main()
