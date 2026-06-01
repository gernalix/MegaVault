# oracle-backup-service Troubleshooting

## Problemi e sintomi rilevati nel codice
- scripts/backup.sh:2:set -euo pipefail
- scripts/backup.sh:13:LAST_REMOTE_ERROR_FILE="$STATE_DIR/last_remote_error"
- scripts/backup.sh:14:LAST_REMOTE_FAILURE_EPOCH_FILE="$STATE_DIR/last_remote_failure_epoch"
- scripts/backup.sh:36:RESTIC_BACKUP_TIMEOUT_SECONDS="${RESTIC_BACKUP_TIMEOUT_SECONDS:-5400}"
- scripts/backup.sh:37:RESTIC_PRUNE_TIMEOUT_SECONDS="${RESTIC_PRUNE_TIMEOUT_SECONDS:-3600}"
- scripts/backup.sh:38:REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS="${REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS:-21600}"
- scripts/backup.sh:82:cleanup_failed_snapshot() {
- scripts/backup.sh:96:cleanup_failed_snapshot
- scripts/check_backup_health.py:20:LAST_FAILED_REPOS_FILE = STATE_DIR / "last_failed_repos"
- scripts/check_backup_health.py:22:LAST_REMOTE_ERROR_FILE = STATE_DIR / "last_remote_error"
- scripts/check_backup_health.py:37:except FileNotFoundError:
- scripts/check_backup_health.py:45:except Exception:
- scripts/check_backup_health.py:52:except ValueError:
- scripts/check_backup_health.py:69:except ValueError:
- scripts/check_backup_health.py:77:except Exception:
- scripts/check_backup_health.py:87:except Exception as exc:
- scripts/oracle-backup-healthcheck.sh:2:set -euo pipefail
- scripts/oracle-backup-healthcheck.sh:12:LAST_FAILED_REPOS_FILE="/var/lib/oracle_backup/last_failed_repos"

## Comandi/verifiche utili trovati
- scripts/check_remote_quota.py:1:#!/usr/bin/env python3
- scripts/prune.sh:1:#!/usr/bin/env bash
- scripts/prune.sh:7:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/prune.sh:51:if timeout --kill-after=60s "$RESTIC_PRUNE_TIMEOUT_SECONDS" restic -r "$repo" unlock && \
- scripts/prune.sh:53:restic -r "$repo" forget \
- scripts/prune.sh:58:restic -r "$repo" prune \

## Safety prima di correggere
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP_INTERVAL_SECONDS" -gt 0 ]]; then
- scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
- scripts/backup.sh:69:if ! flock -n 9; then
- scripts/backup.sh:85:rm -rf -- "$snap_run_dir"
- scripts/backup.sh:92:kill "$heartbeat_pid" 2>/dev/null // true
- scripts/backup.sh:105:ORACLE_BACKUP_LOCK_HELD=1 /opt/oracle_backup/prune_local_snapshots.sh // true
- scripts/backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- scripts/backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
