# mint-manual-updates Troubleshooting

## Problemi e sintomi rilevati nel codice
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
- Se `--upgrade-venvs` salta tutto con `status=skipped_guardrail`, controllare `~/.local/state/mint-manual-updates/last-report.txt` e i dettagli `guardrail-detail` nel log.
- Se un singolo venv fallisce, gli altri continuano; controllare il file specifico in `~/.local/state/mint-manual-updates/venv-logs/`.

## Comandi/verifiche utili trovati
- `bin/mint-manual-updates --upgrade-venvs-report-only`
- `bin/mint-manual-updates --upgrade-venvs`
- `bin/mint-manual-updates --status`
- `tail -n 220 ~/.local/state/mint-manual-updates/mint-manual-updates.log`

## Safety prima di correggere
- dev/project.metadata.json:9:"metadata_version": 1,
- Non usare `sudo pip`, `pip` globale o `pip3` globale per aggiornamenti Python di sistema.
- Il root venv default e `/home/daniele/codex-workspace`; usare `--venvs-root PATH` solo se si vuole esplicitamente uscire da quel perimetro.
- systemd/user/mint-manual-updates.service:2:Description=Linux Mint manual safe updates v5
- systemd/user/mint-manual-updates.timer:2:Description=Weekly Linux Mint manual safe updates v5
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
