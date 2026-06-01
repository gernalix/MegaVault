# maintenance-486 Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | ## Root Cause |
| `dev/legacy/reports/prompt-486-report.md` | Probable root cause: VM starvation during frequent `oracle-backup` local fallback runs. |
| `scripts/ssh_diag_486.sh` | timeout 10 nc -vz "$host" 22 // true |
| `scripts/ssh_diag_486.sh` | timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true |
| `scripts/ssh_diag_486.sh` | timeout 35 ssh \ |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `scripts/ssh_diag_486.sh` | #!/usr/bin/env bash |
| `scripts/ssh_diag_486.sh` | timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true |

## Safety Checks Before Fixing
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
