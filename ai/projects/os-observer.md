PROJECT: os-observer
SLUG: os-observer
PATH: /home/daniele/codex-workspace/os-observer
REMOTE: none
BRANCH: codex/prompt-914582

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 25
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- shell scripts

TEST:
- tests

VERSIONING:
- git_branch: codex/prompt-914582
- git_remote: none
- preexisting_status_count: 12

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
-  M codex_freeze_runner.py
-  M config/codex-resource-presets.json
-  M dev/INDEX.md
-  M dev/TEST_PLAN.md
-  M tests/test_codex_freeze_runner.py
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118

KNOWN_BUGS:
- dev/legacy/TROUBLESHOOTING.md

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- AGENTS.md -> dev/legacy/AGENTS.md
- ARCHITECTURE.md -> dev/legacy/ARCHITECTURE.md
- OPERATIONS.md -> dev/legacy/OPERATIONS.md
- PATCH_WORKFLOW.md -> dev/legacy/PATCH_WORKFLOW.md
- README.md -> dev/legacy/README.md
- RETENTION_POLICY.md -> dev/legacy/RETENTION_POLICY.md
- TROUBLESHOOTING.md -> dev/legacy/TROUBLESHOOTING.md
- dev/AGENT_RULES.md -> dev/legacy/dev/AGENT_RULES.md
- dev/ARCHITECTURE.md -> dev/legacy/dev/ARCHITECTURE.md
- dev/AUTOFIX_ALLOWLIST.md -> dev/legacy/dev/AUTOFIX_ALLOWLIST.md
- dev/BOOT_SEQUENCE.md -> dev/legacy/dev/BOOT_SEQUENCE.md
- dev/CHANGELOG.md -> dev/legacy/dev/CHANGELOG.md
- dev/FALSE_POSITIVE_STRATEGY.md -> dev/legacy/dev/FALSE_POSITIVE_STRATEGY.md
- dev/MONITOR_MAPPING.md -> dev/legacy/dev/MONITOR_MAPPING.md
- dev/RECOVERY_POLICY.md -> dev/legacy/dev/RECOVERY_POLICY.md
- dev/ROLLBACK.md -> dev/legacy/dev/ROLLBACK.md
- dev/SAFETY.md -> dev/legacy/dev/SAFETY.md
- dev/SQLITE_SCHEMA_NOTES.md -> dev/legacy/dev/SQLITE_SCHEMA_NOTES.md
- dev/ai-diagnostics/SCHEMA.md -> dev/legacy/dev/ai-diagnostics/SCHEMA.md
- docs/prompt_731_seagate_usb_diagnosis.md -> dev/legacy/docs/prompt_731_seagate_usb_diagnosis.md
- docs/prompt_734_seagate_recovery_report.md -> dev/legacy/docs/prompt_734_seagate_recovery_report.md
- docs/prompt_735_recovery_and_v7_report.md -> dev/legacy/docs/prompt_735_recovery_and_v7_report.md
- docs/registro_soluzioni.md -> dev/legacy/docs/registro_soluzioni.md
- dev/INDEX.md -> dev/legacy/dev/INDEX.md
- dev/TEST_PLAN.md -> dev/legacy/dev/TEST_PLAN.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
