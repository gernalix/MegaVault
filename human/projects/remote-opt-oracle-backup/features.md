# remote_opt_oracle_backup Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `backup.sh`: cleanup_failed_snapshot, snapshot_one_db, run_backup_repo
- `check_backup_health.py`: load_env_file, notify, main
- `prune_local_snapshots.sh`: bytes_from_gb, snapshot_dirs, count_dirs, total_bytes, free_bytes, delete_oldest

## Confini operativi
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
