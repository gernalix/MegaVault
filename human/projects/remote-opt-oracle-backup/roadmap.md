# remote_opt_oracle_backup Roadmap

## Segnali dal codice
- no tests detected by static scan

## Debito/rischi da considerare
- backup.sh:2:set -euo pipefail
- backup.sh:49:cleanup_failed_snapshot() {
- backup.sh:55:trap cleanup_failed_snapshot EXIT
- backup.sh:66:sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- backup.sh:84:repo_fail=0
- backup.sh:85:failed_repos=()
- backup.sh:98:echo "[!] repo write preflight failed: $repo"
- backup.sh:128:repo_fail=$((repo_fail + 1))
- backup.sh:8:RESTIC_RUN_LOCK="$STATE_DIR/restic-job.lock"
- backup.sh:15:export RESTIC_PASSWORD
- backup.sh:36:exec 9>"$RESTIC_RUN_LOCK"
- backup.sh:37:if ! flock -n 9; then
- backup.sh:42:ORACLE_BACKUP_LOCK_HELD=1 KEEP_LOCAL_SNAPSHOTS=3 MAX_LOCAL_SNAPSHOT_GB=8 MIN_FREE_GB=8 \
- backup.sh:52:rm -rf -- "$snap_run_dir"
