# amici_fb Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: ## Main Commands
- dev/legacy/docs/TROUBLESHOOTING.md: ## Service Path or Unit Wrong
- dev/legacy/docs/OPERATIONS.md: ## Service and Timer
- dev/legacy/AGENTS.md: ## Standard Workflow
- dev/legacy/AGENTS.md: ## Git Workflow
- dev/legacy/README.md: `amici_fb` is a Linux Mint user-level automation that opens Facebook with
- dev/legacy/CHANGELOG.md: - Repaired the Linux Mint user-level `amici_fb.service` and
- amici_fb.py: from urllib.parse import urlparse, parse_qs, unquote, urlencode

## Useful Limits And Boundaries
- dev/legacy/README.md: Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts,
- dev/legacy/docs/ARCHITECTURE.md: - `.env.example`: safe placeholder env file. Real `.env` is private and ignored.
- dev/legacy/docs/ARCHITECTURE.md: 10. Save snapshot CSV, update SQLite, select a safe previous CSV for comparison,
- dev/legacy/docs/ARCHITECTURE.md: - `fb_storage_state.json` is the saved login/session file. Do not commit or
- dev/legacy/docs/ARCHITECTURE.md: - Push errors are logged as warnings and never fail the scraper.
- dev/legacy/docs/TROUBLESHOOTING.md: Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`,
- dev/legacy/docs/TROUBLESHOOTING.md: Never print the real URL.
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: do not delete state files. If a service process is genuinely stale and no
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: preserve the database and CSVs; use `AMICI_FB_DB` only for an explicit test
- dev/legacy/docs/OPERATIONS.md: Do not paste token values into logs or reports.
- dev/legacy/docs/OPERATIONS.md: Safe test through the runner helper:
- dev/legacy/docs/OPERATIONS.md: Safe raw curl test without printing the URL:

## Where The Feature Code Appears To Live
- `_shared/telegram_notify.py`
- `amici_fb.py`
- `amici_fb_task_runner.py`
- `telegram_notify.py`
- `.gitignore`
- `_shared/__init__.py`
- `amici-fb.service`
- `amici-fb.timer`
- `amici_fb.service`
- `amici_fb.sqlite3`
- `amici_fb.timer`
- `amici_fb.zip`
- `amici_fb_daily.cmd`
