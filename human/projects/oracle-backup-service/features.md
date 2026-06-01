# oracle-backup-service Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: # oracle-backup-service
- dev/legacy/README.md: ## Backup Flow
- dev/legacy/docs/TROUBLESHOOTING.md: ## Useful Commands
- dev/legacy/docs/TROUBLESHOOTING.md: ## SSH Banner Timeouts During Backup
- dev/legacy/docs/CHANGELOG.md: ### Prompt #739 running backup healthcheck noise
- dev/legacy/docs/CHANGELOG.md: ### Prompt #483 degraded backup freshness state
- dev/legacy/docs/OPERATIONS.md: ## Quick Checklist
- scripts/backup.sh: # Use sqlite online backup API
- scripts/backup.sh: # Now run restic backup to each repo
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/docs/TROUBLESHOOTING.md: - `[oracle-backup] Healthcheck`
- dev/legacy/docs/OPERATIONS.md: last=$(sudo cat /var/lib/oracle_backup/last_any_success_epoch 2>/dev/null // sudo cat /var/lib/oracle_backup/last_successful_epoch)
- scripts/backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/check_backup_health.py: ENV_FILE = os.environ.get("ORACLE_BACKUP_ENV_FILE", "/etc/oracle_backup/oracle_backup.env")

## Useful Limits And Boundaries
- dev/legacy/README.md: # oracle-backup-service
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/README.md: - `scripts/backup.sh`: main oneshot job for `oracle-backup.service`.
- dev/legacy/README.md: - `scripts/prune.sh`: restic retention job for `oracle-backup-prune.service`.
- dev/legacy/README.md: - `scripts/check_backup_health.py`: freshness monitor used by `oracle-backup-monitor.service`.
- dev/legacy/README.md: - `scripts/oracle-backup-healthcheck.sh`: preventive read-only healthcheck used by `oracle-backup-healthcheck.service`.
- dev/legacy/README.md: - Any successful backup marker: `/var/lib/oracle_backup/last_any_success_epoch`
- dev/legacy/README.md: - Last backup status: `/var/lib/oracle_backup/last_backup_status`
- dev/legacy/README.md: - Healthcheck alert lock: `/run/oracle-backup-healthcheck-alert.lock`
- dev/legacy/README.md: - Freshness monitor alert lock: `/run/lock/oracle-backup-monitor-alert.lock`
- dev/legacy/README.md: The VM runtime is a flat install, not a git checkout. Deploy `scripts/backup.sh`
- dev/legacy/README.md: to `/opt/oracle_backup/backup.sh`, `scripts/check_backup_health.py` to

## Where The Feature Code Appears To Live
- `scripts/check_backup_health.py`
- `scripts/check_remote_quota.py`
- `scripts/backup.sh`
- `scripts/oracle-backup-healthcheck.sh`
- `scripts/prune.sh`
- `scripts/prune_local_snapshots.sh`
