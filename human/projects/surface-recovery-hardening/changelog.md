# surface-recovery-hardening Changelog

## Eventi MegaVault
- 2026-06-01: `#739482` ha migrato docs locali in `dev/legacy` e creato metadata/MegaVault.
- 2026-06-01: `#842915` ha arricchito AI/Human docs da legacy e repo structure.
- 2026-06-01T13:39:31+02:00: `#604927` ha auditato codice attivo, arricchito Human docs e compresso AI doc.
- 2026-06-01T14:17:44+02:00: `#847392` ha riavviato `rsync-transfer`, montato source BitLocker read-only, corretto `verify-mapping` e aggiornato docs senza creare nuovo slug.

## Evidenza #847392
- `rsync-transfer.service`: active/running, transient user unit.
- PID rsync: `2171819`; secondo processo rsync child presente nello stesso gruppo.
- Health locale Kuma: `status=up msg=running pid=2171819`.
- Secondo avvio launcher: `rc=0`, lock held, conteggio rsync invariato.
