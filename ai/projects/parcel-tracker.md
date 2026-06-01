PROJECT: parcel-tracker
SLUG: parcel-tracker
PATH: /home/daniele/codex-workspace/parcel-tracker
REMOTE: none
BRANCH: master

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 4
- dirty_docs_skipped: 0

DB:
- parcel_tracker.sqlite3

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
- dev/legacy/dev/TROUBLESHOOTING.md

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- dev/CHANGELOG.md -> dev/legacy/dev/CHANGELOG.md
- dev/INDEX.md -> dev/legacy/dev/INDEX.md
- dev/OPERATIONS.md -> dev/legacy/dev/OPERATIONS.md
- dev/TROUBLESHOOTING.md -> dev/legacy/dev/TROUBLESHOOTING.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
