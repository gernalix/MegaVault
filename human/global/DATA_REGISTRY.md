# Data Registry

Registro leggibile dei database e degli stati locali rilevanti. Il file AI autorevole e' [DATA_REGISTRY.md](../../ai/global/DATA_REGISTRY.md).

## SQLite principali

- `software_audit.db`: `/home/ubuntu/sync_root/db/software_audit.db`, owner `mint-update-tracker`, con WAL/SHM presenti.
- `codex_usage.sqlite3`: `~/.local/share/codex-usage-monitor/codex_usage.sqlite3`, owner `codex-token-watcher`.
- `terminal_logger.sqlite`: `~/.local/share/terminal-logger/db/terminal_logger.sqlite`, owner `terminal-logger`.
- `windowtabnotes.sqlite3`: `~/.local/share/windowtabnotes/windowtabnotes.sqlite3`, owner `windowtabnotes`.
- `amici_fb.sqlite3`: `/home/daniele/codex-workspace/scripts/amici_fb/amici_fb.sqlite3`, owner `amici-fb`.
- `parcel_tracker.sqlite3`: `/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.sqlite3`, owner `parcel-tracker`.
- `peewee-sqlite.v2.db`: `~/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db`, owner `activitywatch`.
- `disk_usage_monitor.sqlite`: `/home/daniele/sync_root/db/disk_usage_monitor.sqlite`, owner `disk-usage-monitor`.
- `kuma.db`: `/opt/uptime-kuma/data/kuma.db` sulla VM Oracle, verificato live in sola lettura il 2026-06-10 con WAL/SHM presenti e integrity `ok`.

## Stato non SQLite

- `mint-freeze-forensics`: JSONL e prove freeze sotto `~/.local/state/mint-freeze-forensics`.
- `mint-cloud-backup`: JSON di stato e progresso sotto `/var/lib/mint-cloud-backup`.
- `home-backup`: snapshot su `/media/daniele/Seagate6TB2/home-backups`.
- `surface-recovery-hardening`: destinazione transfer su `/media/daniele/Seagate6TB2/vecchio disco`.

## Esclusioni sensibili

I DB di profili browser, cookie, login e cache di strumenti sono stati riconosciuti come dati sensibili o interni al tool, non come verita' progettuale da centralizzare.

## Data loss

- High impact: `windowtabnotes.sqlite3`, `kuma.db`, snapshot home e destinazione transfer.
- Medium impact: `software_audit.db`, `terminal_logger.sqlite`, `amici_fb.sqlite3`, ActivityWatch, disk monitor e stati backup/freeze.
- Low impact: `codex_usage.sqlite3`, `parcel_tracker.sqlite3`, storici Android update.
- Secrets: non verificati nei DB live; `terminal_logger.sqlite`, note utente, ActivityWatch, Kuma e dati home/transfer restano `UNKNOWN` o sensibili per contenuto possibile.
