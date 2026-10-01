"""Single-document operational coverage; no runtime mutations or external calls."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DOCUMENT = ROOT / 'ai/META_INFRASTRUCTURE.md'

class OperatingContractTests(unittest.TestCase):
    def test_normal_operation_scenarios_are_self_contained(self):
        text = DOCUMENT.read_text()
        scenarios = {
            'new chat': ('## Read before acting / new-chat takeover', 'c3_control.py status'),
            'state readback': ('/api/state', 'work_item_executor_bindings'),
            'Inbox capture': ('c3_inbox.py', '--issue-id'),
            'Inbox decisions': ('reconcile_issue_batch', 'work_item_ids', '@alias'),
            'technical Inbox': ('c3_runtime.py --inbox-only', 'maximum 25'),
            'work intake': ('`intake`', 'depends_on', 'execution'),
            'prepare': ('c2_prepare_codex.py --spec', 'readiness_evidence'),
            'prompt allocation': ('prompt_id_allocate', 'request_id', 'C3-only'),
            'prompt registration': ('register', 'prompt_text', 'current_path'),
            'project resolve': ('project-show ID', 'project ALIAS'),
            'project register': ('register-local-repo', 'register-github-repo'),
            'executor start/bind': ('c2_executor_start.py', '--executor-ref', '--chat-url'),
            'terminal result': ('roadmap_finish.py', 'c2_executor_result.py', '--payload'),
            'Git integration': ('repo_single_writer.py', 'finish --repo', 'status-any'),
            'monitoring': ('fedora-system-monitor', 'journalctl', 'Kuma administration'),
            'collision': ('request_key=KEY', 'same immutable request', 'fail-closed'),
            'recovery': ('## Recovery decision tree', 'quarantined', 'verified_backup'),
            'stop': ('## Stop conditions', 'Stop immediately', 'No optional audit'),
        }
        for scenario, required in scenarios.items():
            with self.subTest(scenario=scenario):
                for token in required:
                    self.assertIn(token, text)
        self.assertEqual(18, len(scenarios))

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
        for marker in ('authority_project=MegaVault', 'authority_lifecycle=C3',
                       'authority_prompt_id=C3', 'authority_git=github-autosync',
                       'authority_observed=Fedora', 'authority_usage=telemetry_only'):
            self.assertEqual(1, text.count(marker))
        self.assertIn('coverage=90%+_normal_operations_from_this_document_alone', text)

if __name__ == '__main__':
    unittest.main()
