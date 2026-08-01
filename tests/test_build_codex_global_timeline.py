import argparse
import contextlib
import hashlib
import io
import tempfile
import unittest
from pathlib import Path

import build_codex_global_timeline as timeline


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class TimelineIdempotenceTest(unittest.TestCase):
    def test_two_consecutive_builds_are_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as raw_tmp:
            root = Path(raw_tmp)
            (root / "source.md").write_text(
                "# Stable event\nstatus=PASS\nupdated=2026-08-01\n",
                encoding="utf-8",
            )
            original = (
                timeline.BASE_DIR,
                timeline.DB_PATH,
                timeline.REPORT_PATH,
                timeline.AI_REPORT_PATH,
            )
            timeline.BASE_DIR = root
            timeline.DB_PATH = root / "codex_global_timeline.sqlite"
            timeline.REPORT_PATH = root / "codex_global_timeline.md"
            timeline.AI_REPORT_PATH = root / "codex_global_timeline_ai.md"
            args = argparse.Namespace(source_root=[], no_git=True, max_git_commits=10)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(timeline.build(args), 0)
                first = tuple(digest(path) for path in (timeline.DB_PATH, timeline.REPORT_PATH, timeline.AI_REPORT_PATH))
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(timeline.build(args), 0)
                second = tuple(digest(path) for path in (timeline.DB_PATH, timeline.REPORT_PATH, timeline.AI_REPORT_PATH))
            finally:
                (
                    timeline.BASE_DIR,
                    timeline.DB_PATH,
                    timeline.REPORT_PATH,
                    timeline.AI_REPORT_PATH,
                ) = original
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
