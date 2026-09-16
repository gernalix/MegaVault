import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RuntimeBoundaryTests(unittest.TestCase):
    def test_composition_root_has_no_wildcard_or_wrapper_import(self):
        path = ROOT / "megavault.py"
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        wildcard = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
            and any(alias.name == "*" for alias in node.names)
        ]
        self.assertEqual([], wildcard)
        self.assertNotIn("strict_tag_wrapper", source)
        self.assertEqual(
            ["main"],
            [node.name for node in tree.body if isinstance(node, ast.FunctionDef)],
        )

    def test_compatibility_facade_has_no_dynamic_reexport_or_monkeypatch(self):
        path = ROOT / "ai" / "strict_tag_wrapper.py"
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        self.assertNotIn("globals()", source)
        self.assertNotIn("globals().update", source)
        self.assertFalse(
            any(
                isinstance(target, ast.Attribute)
                for node in ast.walk(tree)
                if isinstance(node, (ast.Assign, ast.AnnAssign))
                for target in (node.targets if isinstance(node, ast.Assign) else [node.target])
            )
        )
        wildcard = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
            and any(alias.name == "*" for alias in node.names)
        ]
        self.assertEqual([], wildcard)

    def test_core_owns_repo_paths_and_strict_incident_policy(self):
        source = (ROOT / "ai" / "megavault_core.py").read_text(encoding="utf-8")
        self.assertIn("ROOT = Path(__file__).resolve().parents[1]", source)
        self.assertIn("class TagNotFoundError(ValueError):", source)
        self.assertIn("raise TagNotFoundError(", source)
        self.assertIn("def connect(path: Path | str | None = None)", source)


if __name__ == "__main__":
    unittest.main()
