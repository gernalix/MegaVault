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


if __name__ == "__main__":
    unittest.main()
