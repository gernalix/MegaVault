"""Single-document operational coverage; no runtime mutations or external calls."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCUMENT = ROOT / 'ai/META_INFRASTRUCTURE.md'

class OperatingContractTests(unittest.TestCase):
    def test_normal_operation_scenarios_are_self_contained(self):
        text = DOCUMENT.read_text()
        for required in ('request → project backlog/issue', 'when started: local task-state', 'commit/push', 'passive global Inbox', 'no workers', 'No C3 registration', 'Do not allocate PROMPT_ID', 'disabled and masked'):
            self.assertIn(required, text)
        for retired in ('c3_control.py status', 'c3_inbox.py', 'reconcile_issue_batch', 'c2_prepare_codex.py --spec', 'roadmap_start.py'):
            self.assertNotIn(retired, text)

    def test_owner_pointers_do_not_duplicate_operating_rules(self):
        for name in ('BOOTSTRAP.md', 'GLOBAL_INDEX.md'):
            text = (ROOT / 'ai' / name).read_text()
            self.assertIn('META_INFRASTRUCTURE.md', text)
            self.assertLess(len(text.split()), 90)
        specialist = (ROOT / 'ai/MEGAVAULT_PROTOCOL.md').read_text()
        self.assertIn('STATUS=TASK_SPECIFIC_ONLY', specialist)
        for retired in ('prompt-id-command', '## PROMPT_ID canonici',
                        '## Git: single writer per repository', 'Workflowy'):
            self.assertNotIn(retired, specialist)
        self.assertNotIn('PROMPT_IDS:', (ROOT / 'ai/personalhubdoc.md').read_text())

    def test_document_has_one_authority_for_each_domain(self):
        text = DOCUMENT.read_text()
        for marker in ('authority_project=MegaVault', 'authority_backlog=project_GitHub_or_Git',
                       'authority_execution=local_task_state', 'authority_git=github-autosync',
                       'authority_observed=Fedora', 'authority_usage=telemetry_only'):
            self.assertEqual(1, text.count(marker))
        self.assertIn('coverage=90%+_normal_operations_from_this_document_alone', text)

if __name__ == '__main__':
    unittest.main()
