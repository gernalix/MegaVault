from __future__ import annotations

import json
import re
import subprocess
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
PROTOCOL = REPO / "ai" / "MEGAVAULT_PROTOCOL.md"
INDEX = REPO / "ai" / "GLOBAL_INDEX.md"
MANIFEST = REPO / "ai" / "V16_RECONCILIATION_MANIFEST.json"
DELETE_MANIFEST = REPO / "ai" / "archive" / "2917AA9_DELETE_MANIFEST.json"


class CanonicalMegaVaultTest(unittest.TestCase):
    def test_protocol_version_authority_and_read_order(self) -> None:
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertEqual(1, len(re.findall(r"(?m)^VERSION=17$", text)))
        self.assertNotRegex(text, r"(?m)^VERSION=16$")
        self.assertIn("FORMAT=ultracompressed_key_value", text)
        self.assertIn("ENTRY_ORDER=MEGAVAULT_PROTOCOL>GLOBAL_INDEX>clean_check>HOST_PROFILE_if_required>ANDROID_PROTOCOL_if_required>project.metadata.json>docs/ai>targeted_inspection>reuse>implementation", text)
        self.assertIn("SRC_ORDER=HOST_PROFILE>metadata>code_reality>docs_ai>docs_human>legacy", text)
        self.assertIn("DUPLICATE_TRUTH=forbidden", text)
        self.assertIn("UNKNOWN_RULE=mark_UNKNOWN", text)
        for path in (
            "global/HOST_PROFILE.md",
            "global/SERVICE_REGISTRY.md",
            "global/DATA_REGISTRY.md",
            "global/NETWORK_TOPOLOGY.md",
            "global/STORAGE_TOPOLOGY.md",
            "global/ALERT_REGISTRY.md",
            "global/INCIDENT_REGISTRY.md",
        ):
            self.assertIn(path, INDEX.read_text(encoding="utf-8"))
            self.assertTrue((REPO / "ai" / path).is_file())

    def test_protocol_v17_lint_and_semantic_coverage(self) -> None:
        result = subprocess.run(
            ["python3", "protocol_lint.py", "--json"],
            cwd=REPO,
            text=True,
            capture_output=True,
            check=True,
        )
        lint = json.loads(result.stdout)
        self.assertEqual("PASS", lint["status"])
        self.assertEqual([], lint["errors"])
        self.assertEqual(214, lint["semantic_coverage"]["covered"])
        self.assertEqual(214, lint["semantic_coverage"]["required"])
        self.assertEqual(100.0, lint["semantic_coverage"]["percent"])
        for field in ("lines", "words", "bytes", "estimated_tokens"):
            self.assertLess(lint["metrics"]["after"][field], lint["metrics"]["before"][field])
        self.assertEqual(
            {
                "duplicate_keys",
                "contradictory_keys",
                "unreachable_rules",
                "missing_required_fields",
                "naming_inconsistency",
                "semantic_coverage",
                "branch_policy_coverage",
            },
            set(lint["checks"]),
        )

    def test_reconciliation_manifest_is_complete_and_machine_verifiable(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(816427, manifest["prompt_id"])
        self.assertEqual(16, manifest["version"])
        self.assertEqual("e5f128bad82dec0597a6394703cf610ac673d837", manifest["base_sha"])
        required = {"semantic_id", "category", "source_refs", "decision", "target_paths", "requires", "supersedes", "conflicts", "invalidates", "archive_refs", "validation", "status", "confidence"}
        include_items = [item for item in manifest["semantic_items"] if item["decision"] == "INCLUDE"]
        self.assertTrue(include_items)
        self.assertEqual(len(include_items), len({item["semantic_id"] for item in include_items}))
        for item in manifest["semantic_items"]:
            self.assertEqual(set(item), required)
            self.assertTrue(0 <= item["confidence"] <= 1)
            for target in item["target_paths"]:
                self.assertTrue((REPO / target).exists(), f"missing target for {item['semantic_id']}: {target}")
        self.assertTrue(all(item["status"] == "VALIDATED" for item in include_items))
        self.assertEqual("PASS", manifest["validation"]["semantic_include_coverage"])

    def test_deleted_blobs_and_archive_pointers_resolve(self) -> None:
        reconciliation = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest = json.loads(DELETE_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual("ai/archive/2917AA9_DELETE_MANIFEST.json", reconciliation["delete_manifest_path"])
        self.assertEqual(7, len(reconciliation["deleted_paths"]))
        self.assertEqual(7, len(manifest["deleted_paths"]))
        reconciliation_by_path = {item["path"]: item for item in reconciliation["deleted_paths"]}
        delete_by_path = {item["path"]: item for item in manifest["deleted_paths"]}
        self.assertEqual(set(delete_by_path), set(reconciliation_by_path))
        for path, item in delete_by_path.items():
            summary = reconciliation_by_path[path]
            for field in ("blob_sha", "archive_location", "status"):
                self.assertEqual(item[field], summary[field], f"{path}: {field}")
            self.assertIs(summary["recovery_verified"], True)
            archive = REPO / item["archive_location"]
            self.assertTrue(archive.is_file(), item["archive_location"])
            self.assertRegex(item["blob_sha"], r"^[0-9a-f]{40}$")
            self.assertIn(item["status"], {"ARCHIVE_ONLY_VERIFIED", "ARCHIVED_AND_REVALIDATED"})
            archive_blob = subprocess.run(
                ["git", "hash-object", str(archive)], cwd=REPO, text=True, capture_output=True, check=True
            ).stdout.strip()
            self.assertEqual(item["blob_sha"], archive_blob, path)

    def test_global_single_developer_trunk_policy(self) -> None:
        text = PROTOCOL.read_text(encoding="utf-8")
        required = {
            "GLOBAL_GIT_MODEL": "trunk_based_single_developer",
            "GIT_POLICY_SCOPE": "all_projects,all_repositories,past_present_future",
            "NEW_REPO_CANONICAL_BRANCH": "main",
            "EXISTING_REPO_CANONICAL_BRANCH": "resolved_operational_branch",
            "OPERATIVE_BRANCH_COUNT": "1",
            "DEFAULT_WORK_BRANCH": "canonical_branch",
            "DIRECT_CANONICAL_WORK": "default",
            "ROLLBACK_MECHANISM": "commit_history",
            "NEW_BRANCH_DEFAULT": "forbidden",
            "NEW_BRANCH_PER_TASK": "forbidden",
            "BRANCH_CHAINING": "forbidden",
            "UNRELATED_BRANCH_REUSE": "forbidden",
            "TEAM_FEATURE_BRANCH_WORKFLOW": "not_default",
            "TEMP_BRANCH": "exception",
            "TEMP_BRANCH_ALLOWED_IF": "explicit_user_request,parallel_work_strictly_required,high_risk_isolation_strictly_required",
            "TEMP_BRANCH_JUSTIFICATION": "mandatory",
            "TEMP_BRANCH_BASE": "canonical_branch",
            "TEMP_BRANCH_FINALIZATION": "integrate_into_canonical+delete",
            "TEMP_BRANCH_LIFETIME": "minimum",
            "UNMERGED_BRANCH_ACCUMULATION": "forbidden",
            "TASK_COMPLETE_REQUIRES": "canonical_branch_updated_or_explicit_user_defer",
            "CANONICAL_SYNC_REQUIRED": "yes",
            "STALE_BRANCH_AUDIT_REQUIRED": "before_branch_creation",
            "FINAL_REPORT_BRANCH_FIELDS": "repository,canonical_branch,current_branch,temporary_branch_reason,integration_status,cleanup_status",
        }
        pairs = dict(
            line.split("=", 1)
            for line in text.splitlines()
            if line and not line.startswith("#") and "=" in line
        )
        for key, value in required.items():
            self.assertEqual(value, pairs.get(key), key)
        self.assertEqual("integrate_into_canonical+delete", pairs["TEMP_BRANCH_FINALIZATION"])
        self.assertIn("canonical_branch_updated", pairs["TASK_COMPLETE_REQUIRES"])
        self.assertEqual("mandatory_final_report_section", pairs["OPTIMIZATION_OPPORTUNITIES"])
        self.assertEqual(
            "root_cause,impact,estimated_future_savings,one_time_fix,priority,confidence,status",
            pairs["INSIGHT_ITEM_FIELDS"],
        )

    def test_git_hygiene_policy(self) -> None:
        text = (REPO / ".gitignore").read_text(encoding="utf-8")
        for rule in ("private/", "secrets/", "**/secrets/", "codex_global_timeline.sqlite-wal", "codex_global_timeline.sqlite-shm", "__pycache__/", ".pytest_cache/"):
            self.assertIn(rule, text)
        for canonical in ("codex_global_timeline.sqlite", "codex_global_timeline.md", "codex_global_timeline_ai.md"):
            self.assertNotIn(f"\n{canonical}\n", f"\n{text}")

    def test_active_internal_markdown_links_resolve_in_checkout(self) -> None:
        raw = subprocess.run(
            ["git", "ls-files", "-co", "--exclude-standard", "-z"],
            cwd=REPO,
            capture_output=True,
            check=True,
        ).stdout
        broken: list[str] = []
        for item in raw.split(b"\0"):
            if not item:
                continue
            path = REPO / item.decode()
            if not path.is_file() or path.suffix != ".md" or "/archive/" in path.as_posix():
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for match in re.finditer(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
                target = match.group(1).strip().split()[0].strip("<>").split("#", 1)[0]
                if not target or target.startswith(("#", "http://", "https://", "mailto:", "git:", "remote:")) or re.match(r"^[A-Za-z]:\\", target):
                    continue
                resolved = (Path(target) if Path(target).is_absolute() else path.parent / target).resolve()
                try:
                    relative = resolved.relative_to(REPO)
                except ValueError:
                    broken.append(f"{path.relative_to(REPO)} -> {target} (outside checkout)")
                    continue
                ignored = subprocess.run(["git", "check-ignore", "-q", str(relative)], cwd=REPO).returncode == 0
                if not resolved.exists() or ignored:
                    broken.append(f"{path.relative_to(REPO)} -> {target}")
        self.assertEqual([], broken)


if __name__ == "__main__":
    unittest.main()
