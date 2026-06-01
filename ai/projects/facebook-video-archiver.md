PROJECT: facebook-video-archiver
SLUG: facebook-video-archiver
PATH: /home/daniele/codex-workspace/facebook-video-archiver
REMOTE: none
BRANCH: work/v4-deep-discovery

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 8
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- shell scripts

TEST:
- not detected

VERSIONING:
- git_branch: work/v4-deep-discovery
- git_remote: none
- preexisting_status_count: 16

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
-  M .env.example
-  M .gitignore
-  M README.md
-  M dev/OPERATIONS.md
-  M facebook_video_archiver.sh
-  M state/discovered_urls.txt
-  M state/downloaded.txt
-  M systemd/user/facebook-video-archiver.service
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118
- ?? facebook_archive_dashboard.py

KNOWN_BUGS:
- not indexed; inspect legacy if needed

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- dev/AGENT_RULES.md -> dev/legacy/dev/AGENT_RULES.md
- dev/ARCHITECTURE.md -> dev/legacy/dev/ARCHITECTURE.md
- dev/CHANGELOG.md -> dev/legacy/dev/CHANGELOG.md
- dev/INDEX.md -> dev/legacy/dev/INDEX.md
- dev/LEGAL_AND_SAFETY.md -> dev/legacy/dev/LEGAL_AND_SAFETY.md
- dev/TEST_PLAN.md -> dev/legacy/dev/TEST_PLAN.md
- README.md -> dev/legacy/README.md
- dev/OPERATIONS.md -> dev/legacy/dev/OPERATIONS.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
