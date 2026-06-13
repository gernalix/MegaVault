# oracle-backup-service Changelog

## Eventi MegaVault
- 2026-06-13: `#847261` ha introdotto Incident Registry SQLite (`/home/ubuntu/sync_root/db/incident_registry.sqlite`) e ha corretto la causa locale degli alert ricorrenti: preflight remoto/fallback prima degli snapshot SQLite, streaming forzato quando OCI non e' scrivibile, retention locale a un run completo, hard quota fallback 7G. Validazione: backup manuale rc=0 `REMOTE_DEGRADED`, fallback valido, `/` 66%, `sqlite_snapshots` 40K, `emergency_repo` 4.8G, healthcheck/monitor rc=0 WARNING. Remoto OCI resta `StorageLimitExceeded` e repo remoto risulta corrotto/unindexed.
- 2026-06-13: `#918472` ha eseguito cleanup sicuro e solo locale del fallback restic `/var/lib/oracle_backup/emergency_repo`. Snapshot locali: 82 -> 11; repo fisico: 14G -> 3.9G; `/`: 98%/1.2G liberi -> 75%/12G liberi. Comandi restic puntati sempre a `-r /var/lib/oracle_backup/emergency_repo`; nessun backup remoto cancellato o modificato. Healthcheck finale coerente: WARNING/`REMOTE_DEGRADED`, quota fallback OK, OCI ancora `StorageLimitExceeded`.
- 2026-06-13: `#486219` ha aggiunto quota hard al fallback locale. Default iniziale: `LOCAL_FALLBACK_MAX_GB=5`, poi superato da `#847261` a 7G dopo misura di un run completo in streaming. Stato live prima cleanup: `emergency_repo` 13.95 GiB, quindi il preflight quota registrava `BACKUP_BLOCKED_FALLBACK_QUOTA` ed usciva non-zero prima di scrivere altri backup locali. Nessun backup remoto o locale e' stato cancellato.
- 2026-06-12: `#914721` ha liberato spazio sulla VM Oracle senza toccare `emergency_repo`: lo snapshot SQLite statico `/var/lib/oracle_backup/sqlite_snapshots/20260608_180131` e' stato copiato su Seagate 6TB, verificato con manifest e sha256, poi rimosso dalla VM. Root e' passata da 100%/0B liberi a 82%/8.3G liberi dopo il successivo backup fallback automatico. Il remoto OCI resta `StorageLimitExceeded`, quindi `emergency_repo` resta indispensabile.
- 2026-06-10: `#492837` ha risolto il CRITICAL di freschezza backup: il job falliva per spazio durante lo snapshot SQLite locale di `strano_anello.db`; ora in low-space i dump SQLite vengono compressi e inviati direttamente al fallback restic locale. Il remoto OCI resta pieno (`StorageLimitExceeded`) e lo spazio root resta in alert, ma il fallback locale recente e' di nuovo valido.
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.

## Evidenza audit
- File codice/config/test/script analizzati: 19 / 19.
- Invarianti estratte: 79; data/storage facts: 80; rischi: 41; bug markers: 49.
