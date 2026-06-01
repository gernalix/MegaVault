PROJECT: SuperContacts
SLUG: supercontacts
PATH: /home/daniele/codex-workspace/SuperContacts
REMOTE: https://github.com/gernalix/SuperContacts.git
BRANCH: codex/prompt-xxx

STACK:
- gradle/android-or-jvm

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 3
- dirty_docs_skipped: 0

DB:
- tmp/pixel719/super_contacts_debug.db

BUILD:
- ./gradlew <task>

TEST:
- app/src/test
- app/src/androidTest
- gradle test/check tasks if needed

VERSIONING:
- git_branch: codex/prompt-xxx
- git_remote: https://github.com/gernalix/SuperContacts.git
- preexisting_status_count: 8

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
- ?? apps_installate_mint.txt

KNOWN_BUGS:
- not indexed; inspect legacy if needed

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- apps_installate_mint.txt -> dev/legacy/apps_installate_mint.txt
- dev/INDEX.md -> dev/legacy/dev/INDEX.md
- dev/NEODOC.md -> dev/legacy/dev/NEODOC.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
