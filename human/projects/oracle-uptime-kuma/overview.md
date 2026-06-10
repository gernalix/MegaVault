# Oracle Uptime Kuma

Kuma vive sulla VM Oracle `ubuntu@150.230.148.128`, hostname `instance-20260201-1126`, ed e' raggiungibile su `http://150.230.148.128:3001`.

Runtime verificato il 2026-06-10:

- systemd reale: `docker.service`, attivo e abilitato.
- compose service: `uptime-kuma`.
- container: `uptime-kuma`, image `louislam/uptime-kuma:2.3.2`, stato `running/healthy`.
- compose: `/opt/uptime-kuma/docker-compose.yml`.
- dati: `/opt/uptime-kuma/data`.
- DB: `/opt/uptime-kuma/data/kuma.db`, con WAL/SHM presenti.
- backup: `/opt/uptime-kuma/backups`.
- log: `/opt/uptime-kuma/data/error.log` e Docker JSON log.
- non esiste un `uptime-kuma.service` dedicato: si opera via Docker Compose/container.

Stato operativo:

- DB `PRAGMA integrity_check`: `ok`.
- Root VM: 93% usata al controllo 2026-06-10; prima di backup/restore o crescita log va ricontrollato lo spazio.
- Telegram: notifica `id=1`, nome `Notifica Telegram (1)`, attiva/default. I valori token/chat id non vanno stampati.

Monitor principali:

| ID | Nome | Stato | Ruolo |
|---:|---|---|---|
| 3 | cloud backup | attivo | backup cloud Mint |
| 4 | mint-home-backup | attivo | backup home |
| 5 | amici_fb | attivo | snapshot amici Facebook |
| 6 | disk-usage-monitor | attivo | spazio disco |
| 7 | parcel-tracker | attivo | tracking spedizione |
| 9 | mint-home-backup-retention | attivo | retention/report backup |
| 11 | software audit mint | attivo | audit software Mint |
| 12 | Mint Freeze Analysis | attivo | gruppo status page |
| 13-17 | Freeze/PSI/Guardian/Alive | attivi | freeze analysis |

Monitor disattivati/obsoleti:

- `1 mint heartbeat`: heartbeat generico sostituito da monitor specifici.
- `2 rsync-transfer`: disattivato per assenza di runner transfer live verificato.
- `10 codex-token-watcher`: disattivato/obsoleto per runtime legacy non affidabile.

Regole:

- Kuma e' storico, alerting e visualizzazione; non deve avviare reboot, restart, kill o remediation.
- Un rosso Kuma e' un segnale, non una prova: prima si verifica lo stato locale del servizio monitorato.
- Nessuna modifica distruttiva a monitor o DB senza backup recente.
- I monitor obsoleti si disattivano, non si cancellano, per conservare storico e motivazione.
- Ogni cambio monitor va riflesso nei registri AI globali e in un report.
