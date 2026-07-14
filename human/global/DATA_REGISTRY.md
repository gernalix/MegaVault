# Data Registry

Aggiornato: 2026-07-12. Autorita' operativa: [DATA_REGISTRY AI](../../ai/global/DATA_REGISTRY.md).

## Fedora corrente

Il database globale verificato e' `/home/daniele/MegaVault/codex_global_timeline.sqlite`, sorgente canonica della timeline Codex.

Fedora System Monitor usa `/var/lib/fedora-system-monitor/monitor.sqlite3`, schema 2 in WAL, con integrita' e foreign key verificate e backup online sotto `/var/lib/fedora-system-monitor/backups`. Al gate dell'audit 593184 misurava 14.032.896 byte. La retention aggrega soltanto giorni UTC completi prima della cancellazione e conserva permanentemente gli eventi software. Il benchmark sintetico proietta circa 485 MB a 14 giorni, 943 MB a 60, 1,08 GB a 180 e 1,16 GB a un anno; l'upper bound dei backup completi configurati è 39,3 GB prima della compressione filesystem.

Prometheus usa `/var/lib/prometheus/metrics2`, owner `prometheus`, con retention 30 giorni e limite 5 GB. `fedora-diagnostics` non copia questa TSDB: usa l'API ufficiale e crea un singolo ZIP `0600` con CSV, JSON e checksum nella destinazione scelta dall'utente. Gli archivi restano dati manuali dell'utente e non hanno upload o retention automatica.

Il registro incidenti globale previsto dal protocollo e' inizializzato in `/home/daniele/sync_root/db/incident_registry.sqlite`, modo `0600`, con tabelle `incidents` e `incident_events` e integrita' verificata.

Il repository Restic cifrato corrente e' `/mnt/T7_BACKUP/restic-fedora` sul T7.
Contiene 2 snapshot; la lettura integrale storica di 3.955 pack, il controllo
corrente 5% di 198 pack e il restore SHA-256 sono PASS. L'ultimo snapshot
verificato e' `3082eb92`. Prima di ogni snapshot il DB Fedora System Monitor
viene copiato online e verificato nel manifest
`/var/lib/t7-restic-backup/manifest`.

I precedenti path Fedora attesi per codex usage monitor, terminal logger, WindowTabNotes, ActivityWatch, disk usage monitor e git change ledger non esistono al controllo. Questo indica soltanto che i dati non risultano migrati o installati nei path attesi; non prova una perdita dati.

## Regole

Registrare un database come corrente solo dopo verifica di path, owner, schema e backup. Per task documentali non modificare DB di progetto; leggere SQLite in sola lettura quando possibile e trattare profili browser, cookie e note utente come sensibili.
