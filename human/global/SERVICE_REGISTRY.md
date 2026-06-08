# Service Registry

Mappa globale dei servizi e timer infrastrutturali verificati sul host Mint il 2026-06-08. Il file AI autorevole e' [SERVICE_REGISTRY.md](../../ai/global/SERVICE_REGISTRY.md).

## Dashboard locali

- `system-service-dashboard.service`: user service attivo su `http://127.0.0.1:8788`, dashboard locale read-only dei servizi.
- `mint-cloud-backup-dashboard.service`: system service attivo su `http://127.0.0.1:8765`, dashboard del backup cloud Mint.

## Servizi user principali

- Attivi: `adb-wifi-autoconnect`, `aw-watcher-media-player`, `chatgpt-chrome-live-logger`, `codex-html-live`, `mint-freeze-forensics`, `mint-update-tracker`, `system-service-dashboard`, `terminal-logger-codex`, `transfer-vecchio-disco-adaptive-throttle`, `windowtabnotes`, `x11vnc-real-display`.
- Timer attivi: `amici_fb`, `android-sdk-auto-update`, `home-backup-kuma-push`, `home-backup-retention-kuma-push`, `home-incremental-backup`, `mint-manual-updates`, `mint-resource-guardian`, `mint-update-tracker`, `mint-xfce-layout-guard`, `parcel-tracker`, `terminal-logger-codex-snapshot`, `terminal-logger-maintenance`.
- Falliti al momento della discovery: `amici_fb.service`, `android-sdk-auto-update.service`, `terminal-logger-maintenance.service`.

## Servizi system principali

- Attivi: `mint-cloud-backup-dashboard`, `mint-cloud-backup-monitor`, `remote-recovery-tmux`, `surface-no-suspend`, `transfer-usb-io-watchdog`.
- Timer system attivi: `disk-usage-monitor`, `dpkg-db-backup`, `mint-cloud-backup`, `mint-cloud-backup-kuma-push`, `mintupdate-automation-autoremove`, `mintupdate-automation-upgrade`.

## Vincoli

- I servizi desktop/autostart e i servizi di pacchetti generici non sono elencati come infrastruttura di progetto salvo relazione diretta.
- Le unita' Oracle VM non sono state verificate live: SSH verso la VM e' andato in timeout.
