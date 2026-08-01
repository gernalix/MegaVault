import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
V16_BLOB = "16f9503cef9cba1c74e00e5ad43747fbab569554"

SEMANTIC_MAP = {
    "VERSION": ("VERSION",),
    "FORMAT": ("FORMAT",),
    "P1": ("AI_SOURCE",),
    "P2": ("HUMAN_SOURCE",),
    "P3": ("LEGACY_SOURCE",),
    "P4": ("PROJECT_DOC_RULE",),
    "P5": ("INFO_DENSITY", "FORMAT"),
    "P6": ("DUPLICATE_TRUTH",),
    "P7": ("INVENT_FACTS",),
    "P8": ("DOC_DEBT",),
    "P9": ("CODE_DOC_PRIORITY",),
    "P10": ("PRODUCTIVE_CONTEXT",),
    "P11": ("CLEAN_REQUIRED",),
    "P12": ("DOCS_BEFORE_FINAL",),
    "P13": ("REUSE", "REWRITE"),
    "P14": ("ARCHIVE_DEFAULT",),
    "P15": ("TOOLING_AUTONOMY",),
    "P16": ("BRANCH_DOC_REQUIRED",),
    "P17": ("LARGE_ARTIFACT_LOCATION",),
    "P18": ("UNKNOWN_RULE",),
    "P19": ("HUMAN_SOURCE_FORBID",),
    "P20": ("SYNC_REQUIRED",),
    "P21": ("HOST_PROFILE",),
    "P22": ("CLEAN_REQUIRED", "REMOTE_REQUIRED", "PUSH_REQUIRED", "SYNC_REQUIRED"),
    "P23": ("INCIDENT_REGISTRY",),
    "P24": ("MEGAVAULT_FORBID", "PROJECT_DOCS_IN_MEGAVAULT"),
    "P25": ("GLOBAL_TIMELINE",),
    "P26": ("EXECUTION_INSIGHTS",),
    "READ_ORDER": ("ENTRY_ORDER",),
    "CANONICAL_CODEX_TIMELINE_DB": ("TIMELINE_DB",),
    "CANONICAL_CODEX_TIMELINE_REPORT": ("TIMELINE_REPORT",),
    "CANONICAL_CODEX_TIMELINE_AI": ("TIMELINE_AI_REPORT",),
    "ANDROID_READ_ORDER": ("ENTRY_ORDER",),
    "ENTRY_ORDER": ("ENTRY_ORDER",),
    "TIMELINE_SCRIPT_REQ": ("TIMELINE_SCRIPT_REQ",),
    "REPORT_ALL_BLOCKERS": ("INSIGHT_SCOPE",),
    "REPORT_ALL_WORKAROUNDS": ("INSIGHT_SCOPE",),
    "REPORT_RESOLVED_BLOCKERS": ("INSIGHT_SCOPE",),
    "REPORT_UNRESOLVED_BLOCKERS": ("INSIGHT_SCOPE",),
    "REPORT_GENERIC_BLOCKERS": ("GENERIC_BLOCKER",),
    "FINAL_REPORT_REQ": ("FINAL_REPORT_REQ",),
    "VALIDATE": ("VALIDATE",),
}

PROSE_MAP = {
    "Kuma:": ("SECRET_KUMA_FILE",),
    "GitHub:": ("SECRET_GITHUB_AUTH",),
    "Telegram:": ("SECRET_TELEGRAM_FILE",),
    "Quando un task": ("SECRET_READ", "SECRET_PATH_REPROMPT", "SECRET_EXPOSURE"),
}

EXPECTED_TARGET_VALUES = {
    "VERSION": "17",
    "FORMAT": "ultracompressed_key_value",
    "AI_SOURCE": "authoritative",
    "HUMAN_SOURCE": "derived",
    "LEGACY_SOURCE": "historical",
    "INFO_DENSITY": "max",
    "DUPLICATE_TRUTH": "forbidden",
    "DOC_DEBT": "tech_debt",
    "CODE_DOC_PRIORITY": "code>docs",
    "PRODUCTIVE_CONTEXT": "metadata+ai_doc",
    "DOCS_BEFORE_FINAL": "required",
    "ARCHIVE_DEFAULT": "yes",
    "BRANCH_DOC_REQUIRED": "yes",
    "LARGE_ARTIFACT_LOCATION": "outside_vault",
    "SECRET_KUMA_FILE": "/home/daniele/.config/codex/secrets/kuma.env",
    "SECRET_GITHUB_AUTH": "gh_or_/home/daniele/.config/codex/secrets/github.env",
    "SECRET_TELEGRAM_FILE": "/home/daniele/.config/codex/secrets/telegram.env",
    "SECRET_READ": "only_when_current_task_requires_service",
    "SECRET_PATH_REPROMPT": "forbidden",
    "SECRET_EXPOSURE": "forbidden_in_prompt,visible_commands,output,logs,reports,repository",
    "OPTIMIZATION_OPPORTUNITIES": "mandatory_final_report_section",
}


def parse_key_values(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.replace("_", "").isalnum() and key == key.upper():
            result[key] = value
    return result


class ProtocolSemanticCoverageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.v16_text = subprocess.check_output(
            ["git", "cat-file", "blob", V16_BLOB], cwd=ROOT, text=True
        )
        cls.v17_text = PROTOCOL.read_text(encoding="utf-8")
        cls.v16 = parse_key_values(cls.v16_text)
        cls.v17 = parse_key_values(cls.v17_text)

    def test_v17_is_unique_key_value_only(self) -> None:
        lines = [line for line in self.v17_text.splitlines() if line]
        keys = []
        for line in lines:
            self.assertRegex(line, r"^[A-Z0-9_]+=.+$")
            keys.append(line.split("=", 1)[0])
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(self.v17["VERSION"], "17")

    def test_every_v16_directive_is_covered(self) -> None:
        covered = 0
        unchanged = 0
        missing: list[str] = []
        for key, old_value in self.v16.items():
            if self.v17.get(key) == old_value:
                covered += 1
                unchanged += 1
                continue
            targets = SEMANTIC_MAP.get(key, ())
            if targets and all(target in self.v17 for target in targets):
                covered += 1
            else:
                missing.append(key)
        self.assertEqual(missing, [])
        self.assertEqual(len(self.v16), 184)
        self.assertEqual(covered, len(self.v16))
        self.assertEqual(unchanged, 142)
        for prefix, targets in PROSE_MAP.items():
            self.assertTrue(any(line.startswith(prefix) for line in self.v16_text.splitlines()))
            self.assertTrue(all(target in self.v17 for target in targets))

    def test_mapped_targets_have_expected_semantics(self) -> None:
        for key, expected in EXPECTED_TARGET_VALUES.items():
            self.assertEqual(self.v17.get(key), expected, key)

    def test_read_order_and_required_reporting_contract(self) -> None:
        self.assertEqual(
            self.v17["ENTRY_ORDER"],
            "MEGAVAULT_PROTOCOL>GLOBAL_INDEX>clean_check>HOST_PROFILE_if_required>ANDROID_PROTOCOL_if_required>project.metadata.json>docs/ai>targeted_inspection>reuse>implementation",
        )
        required_fields = {
            "root_cause",
            "impact",
            "estimated_future_savings",
            "one_time_fix",
            "priority",
            "confidence",
            "status",
        }
        self.assertEqual(set(self.v17["INSIGHT_ITEM_FIELDS"].split(",")), required_fields)
        self.assertEqual(set(self.v17["OPTIMIZATION_ITEM_FIELDS"].split(",")), required_fields)
        self.assertIn("optimization_opportunities", self.v17["FINAL_REPORT_REQ"].split(","))
        self.assertEqual(self.v17["OPTIMIZATION_OPPORTUNITIES"], "mandatory_final_report_section")


if __name__ == "__main__":
    unittest.main()
