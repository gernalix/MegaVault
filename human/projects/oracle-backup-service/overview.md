# oracle-backup-service Overview

Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot dir

## Stato e codice
- Repository: `/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service`
- Branch/commit verificati: `fix/degraded-healthcheck-state` / `1a4db9d`
- File codice/config/test/script analizzati: 19 su 19
- Stack rilevato: Python, Shell, UNKNOWN, UNKNOWN

## Stato operativo 2026-06-13
- OCI remoto resta `StorageLimitExceeded`.
- Il fallback locale ha quota hard default 5G e attualmente e' gia' sopra quota: `emergency_repo` 13.95 GiB.
- Nuovi fallback locali vengono bloccati prima della scrittura con `BACKUP_BLOCKED_FALLBACK_QUOTA`; `/` non viene piu' riempita dal fallback automatico.
- Cleanup report non distruttivo: `/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt`.

## Orientamento rapido
- Entrypoint: `UNKNOWN`
- Core/data: `dev/project.metadata.json,scripts/backup.sh,scripts/check_backup_health.py,scripts/oracle-backup-healthcheck.sh`
- Test: `UNKNOWN`
- Script/build: `scripts/check_remote_quota.py,scripts/prune.sh`

## Link
- AI doc: [AI doc](../../../ai/projects/oracle-backup-service.md)
- Metadata: [dev/project.metadata.json](../../../../projects/vm_oracle/oracle-backup-service/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../projects/vm_oracle/oracle-backup-service/dev/legacy)
- Repository: [repo path](../../../../projects/vm_oracle/oracle-backup-service)
