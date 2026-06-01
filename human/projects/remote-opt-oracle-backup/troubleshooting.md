# remote_opt_oracle_backup Troubleshooting

## Problemi e sintomi rilevati nel codice
- backup.sh:2:set -euo pipefail
- backup.sh:49:cleanup_failed_snapshot() {
- backup.sh:55:trap cleanup_failed_snapshot EXIT
- backup.sh:66:sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- backup.sh:84:repo_fail=0
- backup.sh:85:failed_repos=()
- backup.sh:98:echo "[!] repo write preflight failed: $repo"
- backup.sh:128:repo_fail=$((repo_fail + 1))
- check_backup_health.py:20:except FileNotFoundError:
- check_backup_health.py:38:f"Probabile che i backup non siano mai partiti o che ci sia un errore di permessi.\n"
- check_backup_health.py:61:except Exception as e:
- check_backup_health.py:63:notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error")
- check_backup_health.py:64:except Exception:
- prune_local_snapshots.sh:2:set -euo pipefail
- prune.sh:2:set -euo pipefail
- prune.sh:37:repo_fail=0
- prune.sh:52:repo_fail=$((repo_fail + 1))
- prune.sh:53:echo "[!] prune failed for repo=$repo"

## Comandi/verifiche utili trovati
- prune.sh:1:#!/usr/bin/env bash
- prune.sh:7:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- prune.sh:41:if restic -r "$repo" unlock && \
- prune.sh:43:restic -r "$repo" forget \
- prune.sh:48:restic -r "$repo" prune \

## Safety prima di correggere
- backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
- backup.sh:37:if ! flock -n 9; then
- backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
- backup.sh:52:rm -rf -- "$snap_run_dir"
- backup.sh:102:rclone deletefile "$remote_path/.oracle-backup-write-test" // true
- backup.sh:110:restic -r "$repo" unlock
- backup.sh:4:ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- backup.sh:5:STATE_DIR="/var/lib/oracle_backup"
- backup.sh:6:LOG_DIR="/var/log/oracle_backup"
- backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
