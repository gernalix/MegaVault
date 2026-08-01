# mint-cloud-backup Overview

Linux Mint root backup to Backblaze B2 through restic, with monitor, localhost dashboard, and Uptime Kuma push heartbeat.

## Stato e codice
- Repository: `/home/daniele/codex-projects/mint-cloud-backup`
- Branch/commit verificati: `master` / `8f0fe06`
- Servizio backup: `mint-cloud-backup.service`
- Timer backup: `mint-cloud-backup.timer`
- Monitor: `mint-cloud-backup-monitor.service`
- Dashboard: `mint-cloud-backup-dashboard.service` at `http://127.0.0.1:8765`
- Kuma push: `mint-cloud-backup-kuma-push.service` / `mint-cloud-backup-kuma-push.timer`
- Stato/log principali: `/var/lib/mint-cloud-backup`, `/var/log/mint-cloud-backup`

## Situazione #482917
- Kuma monitor `cloud backup` attivo con finestra piu larga: interval `180s`, timeout `60s`, retries `2`.
- Il pusher usa lock `flock`, timer ogni 2 minuti, messaggi espliciti anche se il dashboard restituisce JSON inatteso.
- Stato verificato 2026-06-06: `backup=idle last_snapshot=cbba8d42 monitor=ok timer=active`.

## Situazione #739284
- Root cause: falso auth da classificazione su JSONL restic; path `authentication.md`/`authorization...` dentro `current_files` venivano scambiati per errore credenziali.
- Errore reale: restic aveva creato snapshot valido ma usciva `3` per sorgente non leggibile `/home/daniele/.gvfs`; era rimasto un lock restic remoto stale.
- Fix: exclude `/home/*/.gvfs`, stato `DEGRADED` per restic exit `3` con snapshot valido, stale lock gestito solo dopo verifica processi, heartbeat Kuma robusto.
- Invariante: non stampare segreti e non modificare credenziali senza prova.

## Link
- AI doc: AI doc (`../../../ai/projects/mint-cloud-backup.md`; status=UNKNOWN)
- Metadata: dev/project.metadata.json (`../../../../../codex-projects/mint-cloud-backup/dev/project.metadata.json`; status=UNKNOWN)
- Repository: repo path (`../../../../../codex-projects/mint-cloud-backup`; status=UNKNOWN)
- Repo docs: docs (`../../../../../codex-projects/mint-cloud-backup/docs`; status=UNKNOWN)
