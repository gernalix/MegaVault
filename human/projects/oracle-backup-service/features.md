# oracle-backup-service Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `scripts/backup.sh`: heartbeat_loop, cleanup_failed_snapshot, cleanup_on_exit, snapshot_one_db, record_remote_failure, record_remote_skip, remote_preflight_cooldown_remaining, run_local_fallback_retention
- `scripts/check_backup_health.py`: load_env_file, read_text, read_epoch, notify, int_cfg, load_json, save_json, service_active
- `scripts/prune_local_snapshots.sh`: bytes_from_gb, snapshot_dirs, count_dirs, total_bytes, free_bytes, delete_oldest
- `scripts/check_remote_quota.py`: load_env, parse_gb, run_rclone_size, read_state, write_state, fmt_gib, main

## Confini operativi
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

## Fallback locale con quota
- Il fallback locale resta `/var/lib/oracle_backup/emergency_repo`, ma `backup.sh` controlla la quota prima della scrittura locale.
- Default live: `LOCAL_FALLBACK_MAX_GB=5`, `LOCAL_FALLBACK_SOFT_PCT=80`, `LOCAL_FALLBACK_PREWRITE_RESERVE_GB=1`, `LOCAL_FALLBACK_ROOT_MIN_FREE_GB=1`.
- Se la quota e' superata, lo stato diventa `BACKUP_BLOCKED_FALLBACK_QUOTA`; restic non parte sul fallback locale e il monitor/healthcheck espone CRITICAL.
