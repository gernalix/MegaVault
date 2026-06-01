PROJECT: remote_opt_oracle_backup
SLUG: remote-opt-oracle-backup
PATH: /home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup
REMOTE: none
BRANCH: main

STACK:
- python
- shell

ARCH:
- source: legacy docs in dev/legacy; central doc is authoritative after 2026-06-01T07:23:54+02:00
- legacy_archived: 1
- dirty_docs_skipped: 0

DB:
- not detected

BUILD:
- shell scripts

TEST:
- not detected

VERSIONING:
- git_branch: main
- git_remote: none
- preexisting_status_count: 10

RULES:
- Open dev/project.metadata.json first.
- This AI doc is primary. Human docs derive from it.
- Legacy docs are historical only.
- Do not modify app code/db/build for docs-only migration.

ACTIVE_WORK:
-  M backup.sh
-  M prune.sh
-  M prune_local_snapshots.sh
- ?? backup.sh.bak.20260331_220235
- ?? backup.sh.bak.20260502_025422
- ?? oracle-backup.service
- ?? oracle-backup.timer
- ?? prune.sh.bak.20260331_220235
- ?? prune.sh.bak.20260502_032503
- ?? prune_local_snapshots.sh.bak.20260502_025422

KNOWN_BUGS:
- not indexed; inspect legacy if needed

ROADMAP:
- not indexed; inspect legacy if needed

LEGACY_DOCS:
- lib/README.txt -> dev/legacy/lib/README.txt

SKIPPED_DOCS:
- none

LAST_VERIFIED: 2026-06-01T07:23:54+02:00
