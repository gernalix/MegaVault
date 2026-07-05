# oracle-backup-service Overview

Restic-based backup service for the Oracle VM. It snapshots SQLite databases with the SQLite online backup API, backs up `/home/ubuntu`, `/etc`, and the current SQLite snapshot dir

## Stato e codice
- Repository: `/home/daniele/codex-workspace/projects/vm_oracle/oracle-backup-service`
- Branch/commit verificati: `fix/degraded-healthcheck-state` / `1a4db9d`
- File codice/config/test/script analizzati: 19 su 19
- Stack rilevato: Python, Shell, UNKNOWN, UNKNOWN

## Stato operativo 2026-06-13
- OCI remoto resta `StorageLimitExceeded`: bucket `bucket-20260206-0730` a 22.262 GBytes su limite assunto 22 GiB.
- Il repo remoto `oraclevm` non e' sano: `index/` vuoto, 837 snapshot, `restic check --no-lock` segnala pack non referenziati e tree mancanti.
- Il fallback locale e' ora la protezione funzionante: ultimo backup manuale rc=0 `REMOTE_DEGRADED`, `emergency_repo` 4.8G, hard quota 7G, quota OK, `/` 66%, `sqlite_snapshots` 40K.
- Nuovi fallback locali fanno preflight prima di creare snapshot SQLite; quando OCI non e' scrivibile usano stream-to-restic e non lasciano snapshot on-disk.
- Incident Registry: `/home/ubuntu/sync_root/db/incident_registry.sqlite`, incidenti principali `OCI_STORAGE_LIMIT_EXCEEDED`, `OCI_REMOTE_REPOSITORY_CORRUPT`, `ORACLE_ROOT_DISK_PRESSURE`.
- Report cleanup locale: `/home/ubuntu/maintenance-918472/`; inventario precedente non distruttivo: `/home/ubuntu/maintenance-486219/reports/fallback_inventory_20260613T000454Z.txt`.

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
