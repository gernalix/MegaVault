# mint-manual-updates Overview

Servizio user systemd v5 per controllare e applicare aggiornamenti prudenti su Linux Mint 22.3 / Ubuntu noble, inclusi report e upgrade espliciti dei venv Python locali.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/mint-manual-updates`
- Branch/commit verificati: `master` / `pending prompt #482917`
- File codice/config/test/script analizzati: 5 su 5
- Stack rilevato: UNKNOWN, UNKNOWN, UNKNOWN

## Orientamento rapido
- Entrypoint manuale: `bin/mint-manual-updates`
- Entrypoint extra: `bin/mint-extra-updater`
- Stato manuale: `~/.local/state/mint-manual-updates/`
- Log venv: `~/.local/state/mint-manual-updates/venv-logs/`
- Test: `bash -n bin/mint-manual-updates`, `shellcheck bin/mint-manual-updates` se disponibile

## Link
- AI doc: [AI doc](../../../ai/projects/mint-manual-updates.md)
- Metadata: [dev/project.metadata.json](../../../../mint-manual-updates/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../mint-manual-updates/dev/legacy)
- Repository: [repo path](../../../../mint-manual-updates)
