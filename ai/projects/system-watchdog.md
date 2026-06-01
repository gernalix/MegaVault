PROJECT: system_watchdog
SLUG: system-watchdog
PATH: /home/daniele/codex-workspace/system_watchdog
REMOTE: none
BRANCH: master

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 5
- dirty_docs_skipped: 0

DB:
- watchdog.sqlite

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
- dev/legacy/docs/TROUBLESHOOTING.md

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- README.md -> dev/legacy/README.md
- docs/ARCHITECTURE.md -> dev/legacy/docs/ARCHITECTURE.md
- docs/CODEX_CONTEXT.md -> dev/legacy/docs/CODEX_CONTEXT.md
- docs/TROUBLESHOOTING.md -> dev/legacy/docs/TROUBLESHOOTING.md
- docs/UPDATE_PROCEDURE.md -> dev/legacy/docs/UPDATE_PROCEDURE.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
