# mint-manual-updates Overview

Servizio user systemd v9 con un solo updater ufficiale per Linux Mint: sistema, venv Python locali, tool di sviluppo, Android Studio e Android SDK.

## Stato e codice

- Repository: `/home/daniele/codex-workspace/mint-manual-updates`
- Branch/commit verificati: `master` / `pending prompt #618472`
- Comando ufficiale unico: `bin/mint-manual-updates --run`
- Guardrail v9: default balanced; `rsync`, load alto e PSI CPU alta sono consentiti/non bloccanti; memoria/swap/PSI memoria/PSI I/O estrema/root disk/freeze/apt/batteria critica restano bloccanti.
- Script duplicato rimosso: `removed duplicate script`
- Unit duplicate rimosse: `removed duplicate service`, `removed duplicate timer`

## Orientamento rapido

- Entrypoint: `bin/mint-manual-updates`
- Stato: `~/.local/state/mint-manual-updates/`
- Log venv: `~/.local/state/mint-manual-updates/venv-logs/`
- Storico Android: `~/.local/state/mint-manual-updates/android-sdk-history/`
- Test: `bash -n bin/mint-manual-updates`, `shellcheck bin/mint-manual-updates` se disponibile

## Link

- AI doc: [AI doc](../../../ai/projects/mint-manual-updates.md)
- Metadata: [dev/project.metadata.json](../../../../mint-manual-updates/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../mint-manual-updates/dev/legacy)
- Repository: [repo path](../../../../mint-manual-updates)
