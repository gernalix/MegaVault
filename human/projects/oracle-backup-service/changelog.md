# oracle-backup-service Changelog

## Eventi MegaVault
- 2026-06-13: `#918472` ha eseguito cleanup sicuro e solo locale del fallback restic `/var/lib/oracle_backup/emergency_repo`. Snapshot locali: 82 -> 11; repo fisico: 14G -> 3.9G; `/`: 98%/1.2G liberi -> 75%/12G liberi. Comandi restic puntati sempre a `-r /var/lib/oracle_backup/emergency_repo`; nessun backup remoto cancellato o modificato. Healthcheck finale coerente: WARNING/`REMOTE_DEGRADED`, quota fallback OK, OCI ancora `StorageLimitExceeded`.
- 2026-06-13: `#486219` ha aggiunto quota hard al fallback locale. Default: `LOCAL_FALLBACK_MAX_GB=5`, soglia soft 80%, riserva pre-write 1G, floor root 1G. Stato live: `emergency_repo` e' 13.95 GiB, quindi il preflight quota registra `BACKUP_BLOCKED_FALLBACK_QUOTA` ed esce non-zero prima di scrivere altri backup locali. Nessun backup remoto o locale e' stato cancellato.
- 2026-06-12: `#914721` ha liberato spazio sulla VM Oracle senza toccare `emergency_repo`: lo snapshot SQLite statico `/var/lib/oracle_backup/sqlite_snapshots/20260608_180131` e' stato copiato su Seagate 6TB, verificato con manifest e sha256, poi rimosso dalla VM. Root e' passata da 100%/0B liberi a 82%/8.3G liberi dopo il successivo backup fallback automatico. Il remoto OCI resta `StorageLimitExceeded`, quindi `emergency_repo` resta indispensabile.
- 2026-06-10: `#492837` ha risolto il CRITICAL di freschezza backup: il job falliva per spazio durante lo snapshot SQLite locale di `strano_anello.db`; ora in low-space i dump SQLite vengono compressi e inviati direttamente al fallback restic locale. Il remoto OCI resta pieno (`StorageLimitExceeded`) e lo spazio root resta in alert, ma il fallback locale recente e' di nuovo valido.
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.

## Evidenza audit
- File codice/config/test/script analizzati: 19 / 19.
- Invarianti estratte: 79; data/storage facts: 80; rischi: 41; bug markers: 49.
