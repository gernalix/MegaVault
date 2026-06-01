# system_watchdog Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/docs/ARCHITECTURE.md` | - At process start, the previous heartbeat is compared with current time and boot ID to estimate gaps after freeze, power loss, reboot, or downtime. |
| `watchdog.py` | import urllib.error |
| `watchdog.py` | error TEXT, |
| `watchdog.py` | def push(url, timeout): |
| `watchdog.py` | with urllib.request.urlopen(req, timeout=timeout) as resp: |
| `watchdog.py` | except urllib.error.HTTPError as exc: |
| `watchdog.py` | (utc_ts, local_ts, boot_id, uptime_seconds, push_ok, http_status, error, response_ms) |
| `watchdog.py` | result["error"], |
| `watchdog.py` | ok, status, error, response_ms = push(args.push_url, args.timeout) |
| `watchdog.py` | "error": error, |
| `watchdog.py` | SELECT utc_ts, local_ts, boot_id, uptime_seconds, push_ok, http_status, error, response_ms |
| `watchdog.py` | keys = ["utc_ts", "local_ts", "boot_id", "uptime_seconds", "push_ok", "http_status", "error", "response_ms"] |
| `watchdog.py` | p.add_argument("--timeout", type=int, default=int(os.environ.get("WATCHDOG_TIMEOUT", "20"))) |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/README.md` | sudo systemctl restart system-watchdog.service |
| `dev/legacy/README.md` | sudo systemctl stop system-watchdog.service |
| `dev/legacy/README.md` | python3 watchdog.py once |
| `dev/legacy/README.md` | python3 watchdog.py last |
| `dev/legacy/docs/TROUBLESHOOTING.md` | python3 watchdog.py last |
| `dev/legacy/docs/TROUBLESHOOTING.md` | python3 watchdog.py once |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | git status --short |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | sudo systemctl restart system-watchdog.service |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | python3 watchdog.py last |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | git add . |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | git commit -m "update system watchdog" |
| `install.sh` | #!/usr/bin/env bash |
| `install.sh` | python3 --version >/dev/null |
| `install.sh` | sudo systemctl daemon-reload |
| `install.sh` | sudo systemctl enable --now system-watchdog.service |
| `install.sh` | sudo systemctl --no-pager --full status system-watchdog.service // true |
| `logs.sh` | #!/usr/bin/env bash |
| `logs.sh` | journalctl -u system-watchdog.service -n "${1:-100}" --no-pager |
| `status.sh` | #!/usr/bin/env bash |
| `status.sh` | systemctl --no-pager --full status system-watchdog.service // true |

## Safety Checks Before Fixing
- dev/legacy/README.md: Persistent heartbeat sender for a Uptime Kuma push monitor.
- dev/legacy/README.md: It runs on Linux Mint as `system-watchdog.service`, sends one push every 60 seconds to the remote Kuma endpoint, and records each attempt in local SQLite at:
- dev/legacy/README.md: - `watchdog.sqlite`: runtime database
- dev/legacy/docs/ARCHITECTURE.md: - `watchdog.py` sends an HTTP push to Uptime Kuma every 60 seconds.
- dev/legacy/docs/ARCHITECTURE.md: - Push failures are recorded but do not stop the loop.
- dev/legacy/docs/TROUBLESHOOTING.md: Run one push manually:
- dev/legacy/docs/TROUBLESHOOTING.md: If HTTP push fails, the service continues retrying. Check network reachability to:
- dev/legacy/docs/CODEX_CONTEXT.md: - Push interval: 60 seconds
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add local Telegram sending.
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add Docker on Mint.
- dev/legacy/docs/CODEX_CONTEXT.md: - Verify with `systemctl`, SQLite queries, and a real HTTP push.
- dev/legacy/docs/UPDATE_PROCEDURE.md: 4. Commit locally:
- dev/legacy/docs/UPDATE_PROCEDURE.md: git commit -m "update system watchdog"
- install.sh: python3 --version >/dev/null
