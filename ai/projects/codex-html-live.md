PROJECT: codex-html-live
SLUG: codex-html-live
PATH: /home/daniele/codex-workspace/codex-html-live
REMOTE: none
BRANCH: master

STACK:
- python

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 5
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- not declared

TEST:
- tests

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
- not indexed; inspect legacy if needed

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- README.md -> dev/legacy/README.md
- dev/AGENT_RULES.md -> dev/legacy/dev/AGENT_RULES.md
- dev/ARCHITECTURE.md -> dev/legacy/dev/ARCHITECTURE.md
- dev/CHANGELOG.md -> dev/legacy/dev/CHANGELOG.md
- dev/TEST_PLAN.md -> dev/legacy/dev/TEST_PLAN.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
