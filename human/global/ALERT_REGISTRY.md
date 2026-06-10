# Alert Registry

Registro globale dei monitor Kuma e delle sorgenti Telegram. Il file AI autorevole e' [ALERT_REGISTRY.md](../../ai/global/ALERT_REGISTRY.md).

## Kuma

Kuma vive sulla VM Oracle ed e' usato per storico, alerting e visualizzazione. La notifica Telegram documentata e' `id=1`. Il DB remoto e' stato verificato in sola lettura il 2026-06-10: `/opt/uptime-kuma/data/kuma.db`, integrity `ok`.

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

Gruppo/status page: `Mint Freeze Analysis` id `12`, slug `mint-freeze-analysis`, contiene monitor `13-17`.

## Classificazione operativa

- Critical: backup cloud, backup home, freeze gaps e transfer USB/I/O watchdog.
- Warning: software audit, PSI memory/I/O, guardian, disk usage, retention e amici_fb.
- Info: parcel tracker e monitor obsoleti disabilitati.
- Azione: backup/freeze/storage richiedono investigazione Codex o intervento umano; notifiche spedizione sono principalmente informative.
- False positive risk: alto per monitor obsoleti disabilitati, medio per job timer e push sotto carico, basso per forensics alive e software audit quando il DB e' leggibile.

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
