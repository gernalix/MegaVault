# Oracle Uptime Kuma

Runtime Kuma della VM Oracle, non servizio locale Mint.

Percorsi e stato verificati:

- host: `ubuntu@150.230.148.128`
- container: `uptime-kuma`
- image: `louislam/uptime-kuma:2.3.2`
- DB: `/opt/uptime-kuma/data/kuma.db`
- compose: `/opt/uptime-kuma/docker-compose.yml`
- backup prompt `#847261`: `/opt/uptime-kuma/backups/kuma-pre-847261-freeze-analysis.db`

Gruppo creato:

- `Mint Freeze Analysis`, id `12`

Monitor prompt `#847261`:

| ID | Nome | Tipo | Frequenza | Timeout | Retries |
|---:|---|---|---:|---:|---:|
| 13 | Freeze Gaps | push | 60s | 45s | 1 |
| 14 | PSI Memory | push | 60s | 45s | 1 |
| 15 | PSI IO | push | 60s | 45s | 1 |
| 16 | Guardian Alerts | push | 60s | 45s | 1 |
| 17 | Forensics Alive | push | 60s | 45s | 2 |

Telegram:

- notification id `1` associata ai monitor 13-17.

Regola:

- Kuma e solo scatola nera, cronologia, alerting e visualizzazione.
- Nessun reboot/restart/kill deve partire da Kuma.
