# codex-token-watcher Overview

Monitor locale Mint per leggere la dashboard ChatGPT Codex Analytics, salvare lo storico quota in SQLite/CSV, notificare Telegram quando cambia la percentuale settimanale e fare heartbeat Uptime Kuma remoto sulla VM Oracle.

## Stato e codice
- Runtime autorevole: `/home/daniele/codex-workspace/codex-token-watcher`
- VM Oracle: solo endpoint Uptime Kuma; scraping Codex disabilitato
- Branch runtime: `codex/prompt-384921`
- Stack rilevato: Python, Playwright/Chromium CDP, SQLite, systemd user timer

## Orientamento rapido
- Entrypoint: `/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py`
- Core/data: `extract_dashboard`, `command_once`, `maybe_notify_weekly_change`, SQLite in `~/.local/share/codex-usage-monitor/`
- Test: `python3 -m py_compile`, sample parser, dry-run weekly change
- Script/build: `systemd/codex-usage-monitor.service`, `systemd/codex-usage-monitor.timer`

## Link
- AI doc: [AI doc](../../../ai/projects/codex-token-watcher.md)
- Metadata: [dev/project.metadata.json](../../../../codex-token-watcher/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../codex-token-watcher/dev/legacy)
- Repository: [repo path](../../../../codex-token-watcher)
