# owntracks-watcher Overview

OwnTracks Android invia posizioni via HTTP a un ricevitore Flask sulla VM Oracle. Il percorso pubblico verificato e' Cloudflare Tunnel, non la porta Oracle diretta.

## Stato e codice
- Repository placeholder: `/home/daniele/codex-workspace/owntracks-watcher`
- Runtime VM: `ubuntu@150.230.148.128:/home/ubuntu/bots/owntracks_http_server`
- Branch/commit placeholder verificati: `codex/prompt-384917` / `eaac5bc`
- Stack runtime: Python 3.10, Flask, systemd, Cloudflare Tunnel, SQLite WAL

## Configurazione Android
- Modalita': HTTP
- URL: `https://owntracks.danielegalati.com/owntracks`
- Username/password/token: vuoti/non richiesti
- Tracker ID consigliato: `ta`
- Device ID consigliato: `ta` o nome telefono; il server salva soprattutto `tid`
- Monitoring: Significant Changes per uso normale; Move solo per test breve
- Permessi: posizione sempre consentita, posizione precisa, background location, notifiche consentite
- Batteria: disattivare ottimizzazione/restrizioni per OwnTracks

## Link
- AI doc: [AI doc](../../../ai/projects/owntracks-watcher.md)
- Metadata: dev/project.metadata.json (`../../../../owntracks-watcher/dev/project.metadata.json`; status=UNKNOWN)
- Legacy docs: dev/legacy (`../../../../owntracks-watcher/dev/legacy`; status=UNKNOWN)
- Repository: repo path (`../../../../owntracks-watcher`; status=UNKNOWN)
