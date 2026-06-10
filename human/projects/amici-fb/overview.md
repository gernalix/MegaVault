# amici_fb Overview

Linux Mint user-level Facebook automation that opens Facebook with a browser profile, processes friends/URLs, and records local state in SQLite; treat credentials and browser sessi

## Stato e codice
- Repository: `/home/daniele/codex-workspace/scripts/amici_fb`
- Branch/commit verificati: `master` / `0e021f6`
- File codice/config/test/script analizzati: 53 su 53
- Stack rilevato: Python, Shell, Playwright, UNKNOWN

## Orientamento rapido
- Entrypoint: `amici_fb_task_runner.py --headless`
- Core/data: `_shared/__init__.py,_shared/telegram_notify.py,amici_fb.service,amici_fb.timer,fb_storage_state.json`
- Test: `UNKNOWN`
- Script/build: `install_ubuntu_autorun.sh`

## Automazione systemd
- Unità canoniche: `amici_fb.service` e `amici_fb.timer`
- Timer: user systemd, `OnCalendar=09:00`, `Persistent=true`
- Ambiente: `amici_fb.service` carica `/home/daniele/codex-workspace/scripts/amici_fb/.env`
- Obsoleto: non ricreare `amici-fb.service` o `amici-fb.timer`

## Link
- AI doc: [AI doc](../../../ai/projects/amici-fb.md)
- Metadata: [dev/project.metadata.json](../../../../scripts/amici_fb/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../scripts/amici_fb/dev/legacy)
- Repository: [repo path](../../../../scripts/amici_fb)
