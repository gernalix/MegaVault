# mint-manual-updates Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `bin/mint-manual-updates --run`: aggiorna superfici prudenti e mantiene pip globale/AppImage/Docker in report-only.
- `bin/mint-manual-updates --dry-run`: simula/reporta senza applicare aggiornamenti.
- `bin/mint-manual-updates --upgrade-venvs-report-only`: scopre venv locali e genera report `python -m pip list --outdated`.
- `bin/mint-manual-updates --upgrade-venvs`: aggiorna esplicitamente solo pacchetti dentro i venv trovati.
- Discovery venv default: `/home/daniele/codex-workspace`, pattern `*/venv/bin/python`, `*/.venv/bin/python`, `*/env/bin/python`.
- Directory escluse dalla discovery venv: `.git`, `node_modules`, `build`, `dist`, `.gradle`, `.cache`, `__pycache__`.
- Log venv: `~/.local/state/mint-manual-updates/venv-logs/`.

## Confini operativi
- dev/project.metadata.json:9:"metadata_version": 1,
- Python globale: solo report `pip3 list --outdated`; niente `sudo pip`, `pip` globale o `pip3` globale per aggiornare pacchetti di sistema.
- Venv fuori `/home/daniele/codex-workspace`: esclusi salvo `--venvs-root PATH` esplicito.
- systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v5
- systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v5
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
