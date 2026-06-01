# oracle-backup-service Overview

oracle-backup-service is documented in the MegaVault because local project docs were consolidated and archived under `dev/legacy`. Verified purpose from the source corpus: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least on

## Why It Exists
- dev/legacy/README.md: Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot directory, then records a success marker only after at least 
- dev/legacy/docs/TROUBLESHOOTING.md: - `[oracle-backup] Healthcheck`
- dev/legacy/docs/CHANGELOG.md: ### Prompt #739 running backup healthcheck noise
- dev/legacy/docs/OPERATIONS.md: last=$(sudo cat /var/lib/oracle_backup/last_any_success_epoch 2>/dev/null // sudo cat /var/lib/oracle_backup/last_successful_epoch)
- scripts/backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- scripts/check_backup_health.py: ENV_FILE = os.environ.get("ORACLE_BACKUP_ENV_FILE", "/etc/oracle_backup/oracle_backup.env")
- scripts/check_remote_quota.py: ENV_PATH = Path("/etc/oracle_backup/oracle_backup.env")

## Current State
- Repository: `/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service`
- Branch at enrichment: `fix/degraded-healthcheck-state`
- Latest local commit at enrichment: `058c59b`
- Stack signals: Python, Shell, UNKNOWN, UNKNOWN
- Documentation quality: enriched from legacy docs and repository structure

## How To Use This Documentation
Start with the AI doc for operational work, then read these Human pages for explanation. Legacy docs are historical context, not the primary operating source after this enrichment.

## Links
- AI doc: [AI doc](../../../ai/projects/oracle-backup-service.md)
- Metadata: [dev/project.metadata.json](../../../../projects/vm_oracle/oracle-backup-service/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/vm_oracle/oracle-backup-service/dev/legacy)
- Repository: [repo path](../../../../projects/vm_oracle/oracle-backup-service)
