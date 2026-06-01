# system_watchdog Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: ## Commands
- requirements.txt: # No third-party Python packages are required.
- dev/legacy/README.md: Persistent heartbeat sender for a Uptime Kuma push monitor.
- dev/legacy/docs/TROUBLESHOOTING.md: If HTTP push fails, the service continues retrying. Check network reachability to:
- dev/legacy/docs/UPDATE_PROCEDURE.md: sudo systemctl restart system-watchdog.service
- logs.sh: journalctl -u system-watchdog.service -n "${1:-100}" --no-pager
- uninstall.sh: sudo systemctl disable --now system-watchdog.service // true
- watchdog.py: from datetime import datetime, timezone

## Useful Limits And Boundaries
- dev/legacy/docs/ARCHITECTURE.md: - Push failures are recorded but do not stop the loop.
- dev/legacy/docs/TROUBLESHOOTING.md: Run one push manually:
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add local Telegram sending.
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add Docker on Mint.

## Where The Feature Code Appears To Live
- `watchdog.py`
- `install.sh`
- `logs.sh`
- `status.sh`
- `uninstall.sh`
