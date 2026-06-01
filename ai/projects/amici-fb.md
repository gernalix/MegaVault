PROJECT: amici_fb
SLUG: amici-fb
PATH: /home/daniele/codex-workspace/scripts/amici_fb
REMOTE: https://github.com/gernalix/amici_fb.git
BRANCH: master

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 6
- dirty_docs_skipped: 0

DB:
- amici_fb.sqlite3

BUILD:
- shell scripts

TEST:
- not detected

VERSIONING:
- git_branch: master
- git_remote: https://github.com/gernalix/amici_fb.git
- preexisting_status_count: 8

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
-  M amici_fb.sqlite3
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
- AGENTS.md -> dev/legacy/AGENTS.md
- CHANGELOG.md -> dev/legacy/CHANGELOG.md
- README.md -> dev/legacy/README.md
- docs/ARCHITECTURE.md -> dev/legacy/docs/ARCHITECTURE.md
- docs/OPERATIONS.md -> dev/legacy/docs/OPERATIONS.md
- docs/TROUBLESHOOTING.md -> dev/legacy/docs/TROUBLESHOOTING.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
