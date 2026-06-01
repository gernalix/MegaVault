PROJECT: android-sdk-auto-update
SLUG: android-sdk-auto-update
PATH: /home/daniele/codex-workspace/android-sdk-auto-update
REMOTE: none
BRANCH: master

STACK:
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 5
- dirty_docs_skipped: 0

DB:
- logs/android_updates_history.sqlite

BUILD:
- shell scripts

TEST:
- not detected

VERSIONING:
- git_branch: master
- git_remote: none
- preexisting_status_count: 7

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
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
- OPERATIONS.md -> dev/legacy/OPERATIONS.md
- README_ANDROID_SDK_AUTO_UPDATE.md -> dev/legacy/README_ANDROID_SDK_AUTO_UPDATE.md
- TROUBLESHOOTING.md -> dev/legacy/TROUBLESHOOTING.md
- dev/ai/ANDROID_SDK_UPDATE_TOOL.md -> dev/legacy/dev/ai/ANDROID_SDK_UPDATE_TOOL.md
- dev/human/ANDROID_SDK_UPDATE_TOOL.md -> dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
