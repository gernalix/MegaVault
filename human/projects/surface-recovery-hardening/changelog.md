# surface-recovery-hardening Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01T14:17:44+02:00: `#847392` ha riavviato `rsync-transfer`, montato source BitLocker read-only, corretto `verify-mapping`, corretto il falso down `log_stale` e l'uscita su curl failure del Kuma pusher, aggiornando docs senza creare nuovo slug.
- 2026-06-03T01:37:21+02:00: `#847392` ha corretto il watchdog che pausava rsync su `usb 1-5` WLAN, ripreso lo stesso transfer con `SIGCONT`, e aggiornato docs senza duplicati.

## Evidenza #847392 2026-06-03
- `rsync-transfer.service`: active/running, transient user unit, PID tree invariato `3481045 3481050 3504182`.
- Root cause: pausa watchdog su `usb 1-5` Marvell WLAN, non DEST `sdc`.
- Fix repo: `a7d791d` su `scripts/transfer_usb_io_watchdog.sh`.
- Backup live: `/home/daniele/transfer_usb_io_watchdog.sh.bak-20260603-013451`.
- Health Kuma: `status=up msg=running pid=3481045`.
- Progresso reale: `write_bytes` writer `273024778240 -> 273098440704` in 15s.
- Secondo avvio launcher: `rc=0`, lock held, nessun nuovo rsync target.

## Evidenza #847392 2026-06-01
- `rsync-transfer.service`: active/running, transient user unit.
- PID rsync: `2171819`; secondo processo rsync child presente nello stesso gruppo.
- Health locale Kuma: `status=up msg=running pid=2171819`.
- Health Kuma dopo fix stale-log: service active/running e dry-run `status=up`.
- Test curl failure: `PUSH_URL=http://127.0.0.1:9 RUN_ONCE=1` esce `0` e logga errore non fatale.
- Secondo avvio launcher: `rc=0`, lock held, conteggio rsync invariato.
