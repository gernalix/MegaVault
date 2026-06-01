# maintenance-486 AI OPERATIONS

PROJECT
- name: maintenance-486
- slug: maintenance-486
- purpose: Oracle VM maintenance/report workspace for prompt 486; source material is mostly reports and logs, so operational details are limited and should be verified before remote changes.
- current_status: Working tree has 1 non-clean entries; do not mix unrelated changes. First entries: ?? logs/20260510T205813Z_prompt739_readonly_diag.log
- repo_path: `/home/daniele/codex-workspace/projects/vm_oracle/maintenance-486`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `ed9de94` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- UNKNOWN
important_folders:
- `dev`
- `logs`
- `scripts`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `scripts/ssh_diag_486.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `logs`

ARCH
summary:
- dev/legacy/reports/prompt-486-report.md: # Prompt #486 Oracle VM Recovery Report
- scripts/ssh_diag_486.sh: key="${2:-../ssh-key-2026-02-01.key}"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | # Prompt #486 Oracle VM Recovery Report |
| `dev/legacy/reports/prompt-486-report.md` | ## Root Cause |
| `dev/legacy/reports/prompt-486-report.md` | ## Commands Executed |
| `dev/legacy/reports/prompt-486-report.md` | ## Files Modified On VM |
| `dev/legacy/reports/prompt-486-report.md` | ## Services Restarted Or Stopped |
| `dev/legacy/reports/prompt-486-report.md` | ## Final SSH State |
| `dev/legacy/reports/prompt-486-report.md` | ## Final Telegram Bot State |
| `dev/legacy/reports/prompt-486-report.md` | ## Final Backup And Healthcheck State |
| `dev/legacy/reports/prompt-486-report.md` | ## Residual Risks |
| `dev/legacy/reports/prompt-486-report.md` | ## Related Code Commit |
| `scripts/ssh_diag_486.sh` | #!/usr/bin/env bash |
| `scripts/ssh_diag_486.sh` | key="${2:-../ssh-key-2026-02-01.key}" |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | Probable root cause: VM starvation during frequent `oracle-backup` local fallback runs. |
| `dev/legacy/reports/prompt-486-report.md` | - A repeated `oracle-backup.service` run was active shortly after a successful local fallback and was driving heavy SQLite/restic IO. |
| `dev/legacy/reports/prompt-486-report.md` | - Applied runtime `CPUWeight=10 IOWeight=10 CPUQuota=50%` to `oracle-backup.service`. |
| `dev/legacy/reports/prompt-486-report.md` | - Reniced and ioniced active backup/restic processes. |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped `oracle-backup.timer`. |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped one active backup run after confirming a recent successful fallback existed. |
| `dev/legacy/reports/prompt-486-report.md` | - Copied `oracle-backup-service` payload to `/tmp/oracle486-payload.tgz`. |
| `dev/legacy/reports/prompt-486-report.md` | - Enabled/restarted oracle backup timers. |
| `dev/legacy/reports/prompt-486-report.md` | - Ran monitor and healthcheck in dry-run/safe mode. |
| `dev/legacy/reports/prompt-486-report.md` | - Observed a subsequent timer run skip because `last_any_success_epoch` was still inside `MIN_BACKUP_INTERVAL_SECONDS=900`. |
| `dev/legacy/reports/prompt-486-report.md` | - `/opt/oracle_backup/backup.sh` |
| `dev/legacy/reports/prompt-486-report.md` | - `/usr/local/bin/oracle-backup-healthcheck.sh` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-monitor.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-monitor.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-healthcheck.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-healthcheck.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-prune.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-prune.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-localprune.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-localprune.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/ssh.service.d/10-oracle-backup-responsiveness.conf` |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped `oracle-backup.timer` during recovery. |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped one active `oracle-backup.service` run after diagnosis. |
| `dev/legacy/reports/prompt-486-report.md` | - Enabled/started oracle backup timers. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `scripts/ssh_diag_486.sh` | #!/usr/bin/env bash |
| `scripts/ssh_diag_486.sh` | timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- scripts/ssh_diag_486.sh: timeout 10 nc -vz "$host" 22 // true
- scripts/ssh_diag_486.sh: timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true
- scripts/ssh_diag_486.sh: timeout 35 ssh \

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | ## Related Code Commit |
| `dev/legacy/reports/prompt-486-report.md` | `oracle-backup-service` commit deployed: |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | Probable root cause: VM starvation during frequent `oracle-backup` local fallback runs. |
| `dev/legacy/reports/prompt-486-report.md` | - A repeated `oracle-backup.service` run was active shortly after a successful local fallback and was driving heavy SQLite/restic IO. |
| `dev/legacy/reports/prompt-486-report.md` | - Applied runtime `CPUWeight=10 IOWeight=10 CPUQuota=50%` to `oracle-backup.service`. |
| `dev/legacy/reports/prompt-486-report.md` | - Reniced and ioniced active backup/restic processes. |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped `oracle-backup.timer`. |
| `dev/legacy/reports/prompt-486-report.md` | - Stopped one active backup run after confirming a recent successful fallback existed. |
| `dev/legacy/reports/prompt-486-report.md` | - Copied `oracle-backup-service` payload to `/tmp/oracle486-payload.tgz`. |
| `dev/legacy/reports/prompt-486-report.md` | - Enabled/restarted oracle backup timers. |
| `dev/legacy/reports/prompt-486-report.md` | - Observed a subsequent timer run skip because `last_any_success_epoch` was still inside `MIN_BACKUP_INTERVAL_SECONDS=900`. |
| `dev/legacy/reports/prompt-486-report.md` | - `/opt/oracle_backup/backup.sh` |
| `dev/legacy/reports/prompt-486-report.md` | - `/usr/local/bin/oracle-backup-healthcheck.sh` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-monitor.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-monitor.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-healthcheck.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-healthcheck.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-prune.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-prune.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-localprune.service` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/oracle-backup-localprune.timer` |
| `dev/legacy/reports/prompt-486-report.md` | - `/etc/systemd/system/ssh.service.d/10-oracle-backup-responsiveness.conf` |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | ## Root Cause |
| `dev/legacy/reports/prompt-486-report.md` | Probable root cause: VM starvation during frequent `oracle-backup` local fallback runs. |
| `scripts/ssh_diag_486.sh` | timeout 10 nc -vz "$host" 22 // true |
| `scripts/ssh_diag_486.sh` | timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true |
| `scripts/ssh_diag_486.sh` | timeout 35 ssh \ |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/reports/prompt-486-report.md: Probable root cause: VM starvation during frequent `oracle-backup` local fallback runs.
- dev/legacy/reports/prompt-486-report.md: - A repeated `oracle-backup.service` run was active shortly after a successful local fallback and was driving heavy SQLite/restic IO.
- dev/legacy/reports/prompt-486-report.md: - Applied runtime `CPUWeight=10 IOWeight=10 CPUQuota=50%` to `oracle-backup.service`.
- dev/legacy/reports/prompt-486-report.md: - Reniced and ioniced active backup/restic processes.
- dev/legacy/reports/prompt-486-report.md: - Stopped `oracle-backup.timer`.
- dev/legacy/reports/prompt-486-report.md: - Stopped one active backup run after confirming a recent successful fallback existed.
- dev/legacy/reports/prompt-486-report.md: - Copied `oracle-backup-service` payload to `/tmp/oracle486-payload.tgz`.
- dev/legacy/reports/prompt-486-report.md: - Enabled/restarted oracle backup timers.
- dev/legacy/reports/prompt-486-report.md: - Ran monitor and healthcheck in dry-run/safe mode.
- dev/legacy/reports/prompt-486-report.md: - Observed a subsequent timer run skip because `last_any_success_epoch` was still inside `MIN_BACKUP_INTERVAL_SECONDS=900`.
- dev/legacy/reports/prompt-486-report.md: - `/opt/oracle_backup/backup.sh`
- dev/legacy/reports/prompt-486-report.md: - `/usr/local/bin/oracle-backup-healthcheck.sh`
- dev/legacy/reports/prompt-486-report.md: - `/etc/systemd/system/oracle-backup.service`
- dev/legacy/reports/prompt-486-report.md: - `/etc/systemd/system/oracle-backup.timer`
- dev/legacy/reports/prompt-486-report.md: - `/etc/systemd/system/oracle-backup-monitor.service`
- dev/legacy/reports/prompt-486-report.md: - `/etc/systemd/system/oracle-backup-monitor.timer`

RECENT_DECISIONS
| source | fact |
|---|---|
| `UNKNOWN` | no verified recent decisions found in read sources. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | `ssh.service` was not restarted; it received runtime and persistent resource priority settings. |

LEGACY_SUMMARY
- legacy_docs_read_count: 3
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/reports/prompt-486-report.md`
- `scripts/ssh_diag_486.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../projects/vm_oracle/maintenance-486/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/maintenance-486/overview.md)
- human_folder: [human folder](../../human/projects/maintenance-486)
- legacy_docs: [dev/legacy](../../../projects/vm_oracle/maintenance-486/dev/legacy)
- repo_path: [repo](../../../projects/vm_oracle/maintenance-486)

OPEN_QUESTIONS
- none detected in extracted sources
