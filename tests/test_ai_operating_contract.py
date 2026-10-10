"""Active MegaVault policy ownership and routing; no external calls."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCUMENT = ROOT / "ai/META_INFRASTRUCTURE.md"


class OperatingContractTests(unittest.TestCase):
    def test_normal_operation_scenarios_are_self_contained(self):
        text = DOCUMENT.read_text(encoding="utf-8")
        scenarios = {
            "authority": ("STATUS=SOLE_CROSS_PROJECT_AUTHORITY", "authority_project=MegaVault"),
            "new chat": ("## Read before acting / new-chat takeover", "remote state"),
            "project identity": ("megavault.py project ALIAS", "project-show ID"),
            "PH route": ("personalhubdoc.md", "specialized bootstrap"),
            "Git ownership": ("repo_single_writer.py start", "repo_single_writer.py finish"),
            "commit boundary": ("Commit and push the task branch", "Never manually merge"),
            "PROMPT_ID": ("six-digit", "historical reservations"),
            "retired system": ("retired_orchestrators=C2|C3", "No active C2/C3 writer"),
            "scope": ("least expensive safe mode", "targeted verification"),
            "recovery": ("## Recovery decision tree", "Validator/test failure"),
            "runtime": ("Fedora System Monitor", "live systemd/journal"),
            "stop": ("## Stop conditions", "No optional audit"),
        }
        for scenario, markers in scenarios.items():
            with self.subTest(scenario=scenario):
                for marker in markers:
                    self.assertIn(marker, text)
        self.assertEqual(12, len(scenarios))

    def test_one_authority_for_each_domain(self):
        text = DOCUMENT.read_text(encoding="utf-8")
        for marker in (
            "authority_project=MegaVault",
            "authority_lifecycle=GitHub_issues+Git_task_evidence",
            "authority_prompt_id=retained_Git_reservations",
            "authority_git=github-autosync",
            "authority_observed=Fedora",
            "authority_usage=telemetry_only",
        ):
            self.assertEqual(1, text.count(marker), marker)

    def test_retired_orchestration_is_not_executable_policy(self):
        text = DOCUMENT.read_text(encoding="utf-8")
        for forbidden in (
            "authority_lifecycle=C3",
            "authority_prompt_id=C3",
            "single_c3_writer=required",
            "c3_control.py status",
            "c2_executor_start.py",
        ):
            self.assertNotIn(forbidden, text)

    def test_owner_pointers_do_not_duplicate_operating_rules(self):
        for name in ("BOOTSTRAP.md", "GLOBAL_INDEX.md"):
            text = (ROOT / "ai" / name).read_text(encoding="utf-8")
            self.assertIn("META_INFRASTRUCTURE.md", text)
            self.assertLess(len(text.split()), 90)
        specialist = (ROOT / "ai/MEGAVAULT_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("STATUS=TASK_SPECIFIC_ONLY", specialist)
        self.assertIn("ai/personalhubdoc.md", specialist)
        self.assertNotIn("PH installato", specialist)
        ph = (ROOT / "ai/personalhubdoc.md").read_text(encoding="utf-8")
        self.assertIn("SOURCE=PH_specific_bootstrap", ph)
        self.assertIn("GLOBAL_FALLBACK=ai/META_INFRASTRUCTURE.md+", ph)
        for ph_exclusive in ("PIXEL_NOTIFY:", "FINAL_APK_TELEGRAM:", "version_goal="):
            self.assertIn(ph_exclusive, ph)
            self.assertNotIn(ph_exclusive, specialist)
            self.assertNotIn(ph_exclusive, DOCUMENT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
