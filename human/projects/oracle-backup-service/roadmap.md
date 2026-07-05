# oracle-backup-service Roadmap

## Segnali dal codice
- scripts/oracle-backup-healthcheck.sh:379:f"/ usage {root_used_pct}% >= {ROOT_USAGE_WARN_PCT}% first observation; warning deferred unless persistent for {ROOT_USAGE_WARN_PERSIST_SEC

## Debito/rischi da considerare
- scripts/backup.sh:2:set -euo pipefail
- scripts/backup.sh:13:LAST_REMOTE_ERROR_FILE="$STATE_DIR/last_remote_error"
- scripts/backup.sh:14:LAST_REMOTE_FAILURE_EPOCH_FILE="$STATE_DIR/last_remote_failure_epoch"
- scripts/backup.sh:36:RESTIC_BACKUP_TIMEOUT_SECONDS="${RESTIC_BACKUP_TIMEOUT_SECONDS:-5400}"
- scripts/backup.sh:37:RESTIC_PRUNE_TIMEOUT_SECONDS="${RESTIC_PRUNE_TIMEOUT_SECONDS:-3600}"
- scripts/backup.sh:38:REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS="${REMOTE_PREFLIGHT_FAILURE_COOLDOWN_SECONDS:-21600}"
- scripts/backup.sh:82:cleanup_failed_snapshot() {
- scripts/backup.sh:96:cleanup_failed_snapshot
- scripts/backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- scripts/backup.sh:24:export RESTIC_PASSWORD
- scripts/backup.sh:59:if [[ "${FORCE_ORACLE_BACKUP:-0}" != "1" && "$last_any_success" =~ ^[0-9]+$ && "$MIN_BACKUP_INTERVAL_SECONDS" -gt 0 ]]; then
- scripts/backup.sh:68:exec 9>"$RESTIC_RUN_LOCK"
- scripts/backup.sh:69:if ! flock -n 9; then
- scripts/backup.sh:85:rm -rf -- "$snap_run_dir"

## Prossimo intervento operativo
- Ripristinare capacita' OCI o approvare un piano esplicito per reset/offload del repo remoto corrotto.
- Non cancellare `/var/lib/oracle_backup/emergency_repo` alla cieca: usare prima `/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt`.
- Soglia corrente fallback: 7G hard, 5.6G soft. Se un run completo futuro supera questa soglia, rivalutare dimensione DB/retention prima di alzare ancora la quota.
