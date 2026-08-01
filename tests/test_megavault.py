import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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


if __name__ == "__main__":
    unittest.main()
