# WindowTabNotes Overview

Root repository: `WindowTabNotes/`.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/WindowTabNotes`
- Branch/commit verificati: `codex/prompt-581472` / `68e0170+dirty_prompt_482719`
- Versione corrente: `v22`
- Servizio utente: `windowtabnotes.service`, installato in `~/.config/systemd/user/windowtabnotes.service`
- DB note: `~/.local/share/windowtabnotes/windowtabnotes.sqlite3`, schema `5`
- Stack rilevato: Python, JavaScript MV3, Shell, SQLite, systemd user, GTK/X11, Chrome Native Messaging

## Orientamento rapido
- Entrypoint: `system/bin/windowtabnotes`, `browser-extension/manifest.json`
- Stato/diagnostica: `system/bin/windowtabnotes-status --json`
- Core/data: `system/windowtabnotes/db.py`, `system/windowtabnotes/active_watch.py`, `system/windowtabnotes/api.py`
- Chrome bridge: `browser-extension/service_worker.js`, `system/bin/windowtabnotes-native-host`
- Test: `PYTHONPATH=system python3 -m unittest tests/test_context_persistence.py`
- Script/install: `system/scripts/install.sh`

## Link
- AI doc: [AI doc](../../../ai/projects/windowtabnotes.md)
- Metadata: [dev/project.metadata.json](../../../../WindowTabNotes/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../WindowTabNotes/dev/legacy)
- Repository: [repo path](../../../../WindowTabNotes)
