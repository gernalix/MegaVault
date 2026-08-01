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


class ProtocolV16Test(unittest.TestCase):
    def test_protocol_version_authority_and_read_order(self) -> None:
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertEqual(1, len(re.findall(r"(?m)^VERSION=16$", text)))
        self.assertNotRegex(text, r"(?im)(?:VERSION|PROTOCOL_VERSION)=17\b")
        self.assertIn("READ_ORDER=MEGAVAULT_PROTOCOL>GLOBAL_INDEX>HOST_PROFILE>project.metadata.json>docs/ai", text)
        self.assertIn("ENTRY_ORDER=protocol>global_index>clean_check>host_profile>metadata>docs_ai>targeted_inspection>reuse>implementation", text)
        self.assertIn("SRC_ORDER=HOST_PROFILE>metadata>code_reality>docs_ai>docs_human>legacy", text)
        self.assertIn("P6=no_duplicate_truth", text)
        self.assertIn("P18=unknown_explicit", text)
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
        manifest = json.loads(DELETE_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(7, len(manifest["deleted_paths"]))
        for item in manifest["deleted_paths"]:
            archive = REPO / item["archive_location"]
            self.assertTrue(archive.is_file(), item["archive_location"])
            self.assertRegex(item["blob_sha"], r"^[0-9a-f]{40}$")
            self.assertIn(item["status"], {"ARCHIVE_ONLY_VERIFIED", "ARCHIVED_AND_REVALIDATED"})

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
