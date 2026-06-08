# Project Index Extended

Mappa relazionale tra progetti, servizi, DB, dashboard, monitor e alert. La lista canonica dei progetti resta [PROJECTS.md](../PROJECTS.md); il file AI autorevole per le relazioni e' [PROJECT_INDEX_EXTENDED.md](../../ai/global/PROJECT_INDEX_EXTENDED.md).

## Relazioni principali

- `android`: `adb-wifi-autoconnect.service`.
- `amici-fb`: `amici_fb.service`, `amici_fb.timer`, `amici_fb.sqlite3`, monitor Kuma `amici_fb`.
- `codex-html-live`: `codex-html-live.service`.
- `codex-token-watcher`: `codex-usage-monitor.service`, `codex-usage-monitor.timer`, `codex_usage.sqlite3`; monitor Kuma obsoleto disabilitato.
- `linux-mint-service-dashboard`: `system-service-dashboard.service`, dashboard `127.0.0.1:8788`.
- `mint-cloud-backup`: servizi backup, monitor, dashboard e push Kuma; dashboard `127.0.0.1:8765`; monitor `cloud_backup`.
- `mint-freeze-forensics`: sampler e guardian, stato JSONL, tab dashboard locale, monitor Kuma freeze `13-17`.
- `mint-update-tracker`: `mint-update-tracker.service`, backfill timer, `software_audit.db`, monitor `software_audit_mint`.
- `oracle-uptime-kuma`: runtime Uptime Kuma remoto, DB `kuma.db`, dashboard Oracle.
- `parcel-tracker`: `parcel-tracker.service`, `parcel-tracker.timer`, `parcel_tracker.sqlite3`, Kuma e Telegram.
- `surface-recovery-hardening`: watchdog/throttle/recovery services, monitor rsync-transfer disabilitato, alert Telegram watchdog.
- `terminal-logger`: servizi/timer user del logger, DB `terminal_logger.sqlite`, repo `/home/daniele/terminal-logger`.
- `windowtabnotes`: `windowtabnotes.service`, `windowtabnotes.sqlite3`.
- `backup_docs`: home backup timers e due monitor Kuma.
- `disk-usage-monitor`: service/timer system, DB `/home/daniele/sync_root/db/disk_usage_monitor.sqlite`, Kuma/Telegram e tab dashboard.
- `x11vnc-real-display`: service user per display fisico, runtime in `/home/daniele/remote_real_display_482`.

## Senza relazione runtime verificata

I progetti Android app-only (`SuperContacts`, `MultiTimeTracker`, `Soldi`) non hanno servizi host verificati in questa discovery. ActivityWatch resta tool locale third-party senza repo MegaVault verificato. Alcuni workspace Oracle o report-only restano `UNKNOWN` perche' SSH verso la VM e' andato in timeout.
