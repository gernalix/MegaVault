from __future__ import annotations

import hashlib
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BUILDER = REPO / "build_codex_global_timeline.py"
OUTPUTS = (
    "codex_global_timeline.sqlite",
    "codex_global_timeline.md",
    "codex_global_timeline_ai.md",
)


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=True)


def hashes(root: Path) -> dict[str, str]:
    return {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in OUTPUTS}


class DeterministicTimelineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="megavault-timeline-test-")
        self.root = Path(self.temporary.name)
        self.repo = self.root / "repo"
        self.output = self.root / "output"
        self.repo.mkdir()
        self.output.mkdir()
        run(["git", "init", "-q", "-b", "main"], self.repo)
        run(["git", "config", "user.email", "timeline-test@example.invalid"], self.repo)
        run(["git", "config", "user.name", "Timeline Test"], self.repo)
        (self.repo / ".gitignore").write_text("ignored/\nprivate/\nsecrets/\n*.cache\n", encoding="utf-8")
        (self.repo / "tracked.md").write_text("# Stable event 2026-07-31\nstatus=PASS\n", encoding="utf-8")
        (self.repo / "codex_global_timeline.md").write_text("self output", encoding="utf-8")
        run(["git", "add", ".gitignore", "tracked.md", "codex_global_timeline.md"], self.repo)
        run(["git", "commit", "-qm", "fixture"], self.repo)
        (self.repo / "untracked.json").write_text('{"summary":"untracked event 2026-08-01"}\n', encoding="utf-8")
        for directory in ("ignored", "private", "secrets"):
            target = self.repo / directory
            target.mkdir()
            (target / "excluded.md").write_text("# Must never be ingested 2026-08-01\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def build(self, root: Path | None = None, output: Path | None = None) -> subprocess.CompletedProcess[str]:
        return run(
            [
                sys.executable,
                str(BUILDER),
                "--primary-root",
                str(root or self.repo),
                "--output-dir",
                str(output or self.output),
                "--no-git",
            ],
            REPO,
        )

    def test_normal_repo_is_append_only_filtered_and_byte_stable(self) -> None:
        first = self.build()
        first_hashes = hashes(self.output)
        second = self.build()
        self.assertEqual(first_hashes, hashes(self.output))
        self.assertIn("database_changed=no", second.stdout)
        self.assertFalse((self.output / "codex_global_timeline.sqlite-wal").exists())
        self.assertFalse((self.output / "codex_global_timeline.sqlite-shm").exists())

        conn = sqlite3.connect(self.output / "codex_global_timeline.sqlite")
        try:
            self.assertEqual("ok", conn.execute("PRAGMA integrity_check").fetchone()[0])
            self.assertEqual(0, conn.execute("SELECT count(*) FROM (SELECT id FROM timeline_events GROUP BY id HAVING count(*) > 1)").fetchone()[0])
            rows = conn.execute("SELECT event_date,discovered_at,label_short,source_path FROM timeline_events ORDER BY event_date,project,label_short,id").fetchall()
        finally:
            conn.close()
        paths = "\n".join(row[3] for row in rows)
        self.assertIn("tracked.md", paths)
        self.assertIn("untracked.json", paths)
        self.assertNotIn("excluded.md", paths)
        self.assertNotIn("codex_global_timeline.md", paths)
        self.assertTrue(all(row[1].startswith(row[0]) for row in rows))
        self.assertTrue(all(1 <= len(row[2].split()) <= 4 for row in rows))

        before_removal = len(rows)
        (self.repo / "untracked.json").unlink()
        self.build()
        conn = sqlite3.connect(self.output / "codex_global_timeline.sqlite")
        try:
            self.assertEqual(before_removal, conn.execute("SELECT count(*) FROM timeline_events").fetchone()[0])
        finally:
            conn.close()

    def test_linked_worktree_is_supported(self) -> None:
        worktree = self.root / "linked-worktree"
        output = self.root / "worktree-output"
        output.mkdir()
        run(["git", "worktree", "add", "--detach", str(worktree), "HEAD"], self.repo)
        result = self.build(worktree, output)
        self.assertIn("sqlite_integrity=ok", result.stdout)
        first_hashes = hashes(output)
        second = self.build(worktree, output)
        self.assertEqual(first_hashes, hashes(output))
        self.assertIn("database_changed=no", second.stdout)
        self.assertTrue((worktree / ".git").is_file())


if __name__ == "__main__":
    unittest.main()
