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
- `kuma.db`: `/opt/uptime-kuma/data/kuma.db` sulla VM Oracle, documentato ma non verificato live in questo prompt.

## Stato non SQLite

- `mint-freeze-forensics`: JSONL e prove freeze sotto `~/.local/state/mint-freeze-forensics`.
- `mint-cloud-backup`: JSON di stato e progresso sotto `/var/lib/mint-cloud-backup`.
- `home-backup`: snapshot su `/media/daniele/Seagate6TB2/home-backups`.
- `surface-recovery-hardening`: destinazione transfer su `/media/daniele/Seagate6TB2/vecchio disco`.

## Esclusioni sensibili

I DB di profili browser, cookie, login e cache di strumenti sono stati riconosciuti come dati sensibili o interni al tool, non come verita' progettuale da centralizzare.
