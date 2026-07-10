# Data Registry

Aggiornato: 2026-07-09. Autorita' operativa: [DATA_REGISTRY AI](../../ai/global/DATA_REGISTRY.md).

## Fedora corrente

Il database globale verificato e' `/home/daniele/MegaVault/codex_global_timeline.sqlite`, sorgente canonica della timeline Codex.

Fedora System Monitor usa `/var/lib/fedora-system-monitor/monitor.sqlite3`, schema 2 in WAL, con integrita' verificata e backup online sotto `/var/lib/fedora-system-monitor/backups`. Dopo il primo inventario completo misurava 4.136.960 byte. Le metriche scadute sono aggregate prima della cancellazione; gli eventi software restano permanenti.

Il registro incidenti globale previsto dal protocollo e' inizializzato in `/home/daniele/sync_root/db/incident_registry.sqlite`, modo `0600`, con tabelle `incidents` e `incident_events` e integrita' verificata.

I precedenti path Fedora attesi per codex usage monitor, terminal logger, WindowTabNotes, ActivityWatch, disk usage monitor e git change ledger non esistono al controllo. Questo indica soltanto che i dati non risultano migrati o installati nei path attesi; non prova una perdita dati.

I nuovi log live Codex sono file privati sotto `/home/daniele/.local/state/codex-session-logger/sessions`; non hanno cancellazione automatica. Dettagli e recupero: [Log live Codex](CODEX_SESSION_LOGGING.md).

## Regole

Registrare un database come corrente solo dopo verifica di path, owner, schema e backup. Per task documentali non modificare DB di progetto; leggere SQLite in sola lettura quando possibile e trattare profili browser, cookie e note utente come sensibili.
