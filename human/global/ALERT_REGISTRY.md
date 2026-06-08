# Alert Registry

Registro globale dei monitor Kuma e delle sorgenti Telegram. Il file AI autorevole e' [ALERT_REGISTRY.md](../../ai/global/ALERT_REGISTRY.md).

## Kuma

Kuma vive sulla VM Oracle ed e' usato per storico, alerting e visualizzazione. La notifica Telegram documentata e' `id=1`. La verifica live del DB remoto non e' riuscita in questo prompt per timeout SSH.

Monitor attivi documentati:

- `cloud_backup` id `3`, owner `mint-cloud-backup`.
- `mint-home-backup` id `4`, owner `backup_docs`.
- `amici_fb` id `5`, owner `amici-fb`.
- `disk-usage-monitor` id `6`.
- `parcel-tracker` id `7`, owner `parcel-tracker`.
- `mint-home-backup-retention` id `9`, owner `backup_docs`.
- `software_audit_mint` id `11`, owner `mint-update-tracker`.
- Freeze analysis id `13-17`: freeze gaps, PSI memory, PSI IO, guardian alerts, forensics alive.

Monitor obsoleti disabilitati: `mint_heartbeat`, `rsync-transfer`, `codex-token-watcher`.

## Telegram

Helper condiviso: `/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py`.

Sorgenti note:

- `amici-fb`: snapshot, diff ed errori.
- `parcel-tracker`: aggiornamenti spedizione.
- `codex-token-watcher`: notifiche opzionali per quota/errori.
- `surface-recovery-hardening`: watchdog USB/I/O e vecchi guardiani memoria.
- `disk-usage-monitor`: delta spazio e Kuma.

## Vincoli

Non stampare token, chat id sensibili o URL push reali. Kuma non deve avviare remediation.
