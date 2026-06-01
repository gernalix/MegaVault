PROJECT: oracle-backup-service
SLUG: oracle-backup-service
PATH: /home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service
REMOTE: https://github.com/gernalix/oracle-backup-service.git
BRANCH: fix/degraded-healthcheck-state

STACK:
- unknown/local-tooling

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 4
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- not declared

TEST:
- not detected

VERSIONING:
- git_branch: fix/degraded-healthcheck-state
- git_remote: https://github.com/gernalix/oracle-backup-service.git
- preexisting_status_count: 15

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
-  M config/oracle_backup.env.example
-  M scripts/backup.sh
-  M scripts/check_backup_health.py
-  M scripts/oracle-backup-healthcheck.sh
-  M systemd/oracle-backup.timer
- ?? .codexmeta
- ?? .codexmeta.bak.20260528_191731
- ?? .codexmeta.bak.20260528_191758
- ?? .codexmeta.bak.20260528_191912
- ?? .codexmeta.bak.20260528_193715
- ?? .codexmeta.bak.20260528_193944
- ?? .codexmeta.bak.20260528_194118
- ?? scripts/check_remote_quota.py
- ?? systemd/oracle-backup-remote-quota.service
- ?? systemd/oracle-backup-remote-quota.timer

KNOWN_BUGS:
- dev/legacy/docs/TROUBLESHOOTING.md

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- README.md -> dev/legacy/README.md
- docs/CHANGELOG.md -> dev/legacy/docs/CHANGELOG.md
- docs/OPERATIONS.md -> dev/legacy/docs/OPERATIONS.md
- docs/TROUBLESHOOTING.md -> dev/legacy/docs/TROUBLESHOOTING.md

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
