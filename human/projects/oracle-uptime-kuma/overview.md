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

Status page:

- `Mint Freeze Analysis`, slug `mint-freeze-analysis`
- URL: `http://150.230.148.128:3001/status/mint-freeze-analysis`
- Monitor associati: 13-17
- Refresh: 60s

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

- Kuma è solo scatola nera, cronologia, alerting e visualizzazione.
- Nessun reboot/restart/kill deve partire da Kuma.
- Nessuna modifica distruttiva ai monitor o al DB senza backup recente.
- Gli URL push `/api/push/<token>` non vanno stampati nei report e non vanno committati.

## Come vengono gestiti i monitor

- I monitor push sono usati da servizi locali Mint o Oracle per inviare un heartbeat a Kuma.
- Ogni servizio conserva il token push fuori da Git, di solito in un file env locale.
- Il pusher deve essere leggero, con timeout curl breve, e non deve far fallire il servizio principale solo perché Kuma non risponde.
- Se un monitor diventa rumoroso, prima si verifica se segnala un guasto reale; poi si corregge il pusher o si allargano intervallo/timeout/retry.
- I monitor obsoleti si disattivano o si marcano come obsoleti, conservando storico e dati.
- Ogni nuovo monitor o cambio importante va registrato nei registri globali AI `SERVICE_REGISTRY.md` e `ALERT_REGISTRY.md`.
