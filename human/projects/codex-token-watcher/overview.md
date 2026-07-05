# codex-token-watcher Overview

Monitor locale Mint per verificare lo stato Codex CLI, leggere la cache locale quota `token_count`, salvare storico in SQLite e fare heartbeat Uptime Kuma remoto sulla VM Oracle. Il percorso systemd normale e' CLI-only; il backend dashboard Chrome/Playwright resta fallback manuale.

## Stato e codice
- Runtime autorevole: `/home/daniele/codex-workspace/codex-token-watcher`
- VM Oracle: solo endpoint Uptime Kuma; scraping Codex disabilitato
- Branch runtime: `codex/prompt-384921`
- Stack rilevato: Python, Codex CLI, SQLite, systemd user timer, Uptime Kuma push

## Orientamento rapido
- Entrypoint service: `/home/daniele/codex-workspace/codex-token-watcher/codex_cli_status_watcher.py`
- Fallback manuale browser: `/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py`
- Core/data: `cli_status_observations`, `cli_status_deep_observations`, SQLite in `~/.local/share/codex-usage-monitor/`
- Test: `python3 -m py_compile`, sample parser, dry-run weekly change
- Script/build: `systemd/codex-usage-monitor.service`, `systemd/codex-usage-monitor.timer`

## Link
- AI doc: [AI doc](../../../ai/projects/codex-token-watcher.md)
- Metadata: [dev/project.metadata.json](../../../../codex-token-watcher/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../codex-token-watcher/dev/legacy)
- Repository: [repo path](../../../../codex-token-watcher)
