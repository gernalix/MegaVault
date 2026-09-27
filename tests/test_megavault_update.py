from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("megavault_update", ROOT / "tools" / "megavault_update.py")
assert SPEC and SPEC.loader
updater = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(updater)


class CanonicalUpdateTests(unittest.TestCase):
    def git(self, repo: Path | None, *args: str) -> subprocess.CompletedProcess[str]:
        command = ["git"]
        if repo is not None:
            command += ["-C", str(repo)]
        command += list(args)
        return subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        bare = root / "remote.git"
        seed = root / "seed"
        local = root / "canonical"
        self.git(None, "init", "--bare", "--initial-branch=master", str(bare))
        self.git(None, "clone", str(bare), str(seed))
        self.git(seed, "config", "user.email", "test@example.invalid")
        self.git(seed, "config", "user.name", "Test")
        (seed / "megavault.py").write_text("print('VALIDATE=PASS')\n", encoding="utf-8")
        import sqlite3

        sqlite3.connect(seed / "megavault.sqlite").close()
        self.git(seed, "add", ".")
        self.git(seed, "commit", "-m", "seed")
        self.git(seed, "push", "origin", "master")
        self.git(None, "clone", str(bare), str(local))
        return temporary, seed, local

    def test_dirty_state_blocks_before_fetch_or_mutation(self) -> None:
        temporary, _seed, local = self.fixture()
        self.addCleanup(temporary.cleanup)
        before = self.git(local, "rev-parse", "HEAD").stdout.strip()
        (local / "dirty.txt").write_text("preserve\n", encoding="utf-8")
        with self.assertRaisesRegex(updater.UpdateBlocked, "dirty_worktree"):
            updater.update(local, expected_repo=local)
        self.assertEqual(before, self.git(local, "rev-parse", "HEAD").stdout.strip())
        self.assertEqual("preserve\n", (local / "dirty.txt").read_text(encoding="utf-8"))

    def test_clean_checkout_fast_forwards_and_validates(self) -> None:
        temporary, seed, local = self.fixture()
        self.addCleanup(temporary.cleanup)
        (seed / "next.txt").write_text("next\n", encoding="utf-8")
        self.git(seed, "add", "next.txt")
        self.git(seed, "commit", "-m", "next")
        self.git(seed, "push", "origin", "master")
        result = updater.update(local, expected_repo=local)
        self.assertEqual("PASS", result["status"])
        self.assertEqual("true", result["changed"])
        self.assertEqual(
            self.git(seed, "rev-parse", "HEAD").stdout.strip(),
            self.git(local, "rev-parse", "HEAD").stdout.strip(),
        )


if __name__ == "__main__":
    unittest.main()
