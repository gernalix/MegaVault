# system_watchdog AI OPERATIONS

PROJECT
- name: system_watchdog
- slug: system-watchdog
- purpose: Persistent heartbeat sender for a Uptime Kuma push monitor.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/system_watchdog`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `d93002d` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: Python tooling
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `watchdog.py`
important_folders:
- `dev`
- `systemd`
important_files:
- `requirements.txt`
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `install.sh`
- `logs.sh`
- `status.sh`
- `uninstall.sh`
- `watchdog.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Persistent heartbeat sender for a Uptime Kuma push monitor.
- dev/legacy/docs/ARCHITECTURE.md: The Mint watchdog is intentionally small:
- dev/legacy/docs/TROUBLESHOOTING.md: If HTTP push fails, the service continues retrying. Check network reachability to:
- dev/legacy/docs/CODEX_CONTEXT.md: `/home/daniele/codex-workspace/system_watchdog`
- dev/legacy/docs/UPDATE_PROCEDURE.md: sudo systemctl restart system-watchdog.service
- requirements.txt: # No third-party Python packages are required.
- install.sh: ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
- logs.sh: journalctl -u system-watchdog.service -n "${1:-100}" --no-pager
- status.sh: ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
- uninstall.sh: sudo systemctl disable --now system-watchdog.service // true
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # Linux Mint System Watchdog |
| `dev/legacy/README.md` | ## Commands |
| `dev/legacy/README.md` | ## Files |
| `dev/legacy/docs/ARCHITECTURE.md` | # Architecture |
| `dev/legacy/docs/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/docs/CODEX_CONTEXT.md` | # Codex Context |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | # Update Procedure |
| `requirements.txt` | # No third-party Python packages are required. |
| `requirements.txt` | # watchdog.py uses only the Python standard library. |
| `install.sh` | #!/usr/bin/env bash |
| `logs.sh` | #!/usr/bin/env bash |
| `status.sh` | #!/usr/bin/env bash |
| `uninstall.sh` | #!/usr/bin/env bash |
| `watchdog.py` | #!/usr/bin/env python3 |
| `dev/legacy/README.md` | Persistent heartbeat sender for a Uptime Kuma push monitor. |
| `dev/legacy/docs/ARCHITECTURE.md` | The Mint watchdog is intentionally small: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | If HTTP push fails, the service continues retrying. Check network reachability to: |
| `dev/legacy/docs/CODEX_CONTEXT.md` | `/home/daniele/codex-workspace/system_watchdog` |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Persistent heartbeat sender for a Uptime Kuma push monitor. |
| `dev/legacy/README.md` | It runs on Linux Mint as `system-watchdog.service`, sends one push every 60 seconds to the remote Kuma endpoint, and records each attempt in local SQLite at: |
| `dev/legacy/README.md` | - `watchdog.sqlite`: runtime database |
| `dev/legacy/docs/ARCHITECTURE.md` | - `watchdog.py` sends an HTTP push to Uptime Kuma every 60 seconds. |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push failures are recorded but do not stop the loop. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Run one push manually: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | If HTTP push fails, the service continues retrying. Check network reachability to: |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Push interval: 60 seconds |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Do not add local Telegram sending. |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Do not add Docker on Mint. |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Verify with `systemctl`, SQLite queries, and a real HTTP push. |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | 4. Commit locally: |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | git commit -m "update system watchdog" |
| `install.sh` | python3 --version >/dev/null |
| `uninstall.sh` | echo "Database and logs left in place: watchdog.sqlite watchdog.log" |
| `watchdog.py` | DEFAULT_PUSH_URL = "http://150.230.148.128:3001/api/push/W1h8mBAnP8?status=up&msg=OK&ping=" |
| `watchdog.py` | id INTEGER PRIMARY KEY AUTOINCREMENT, |
| `watchdog.py` | conn.commit() |
| `watchdog.py` | def push(url, timeout): |
| `watchdog.py` | ok, status, error, response_ms = push(args.push_url, args.timeout) |
| `watchdog.py` | p = argparse.ArgumentParser(description="Linux Mint heartbeat watchdog for Uptime Kuma push monitors") |
| `watchdog.py` | p.add_argument("--push-url", default=os.environ.get("WATCHDOG_PUSH_URL", DEFAULT_PUSH_URL)) |

BUILD_TEST
build_files:
- `requirements.txt`
commands_found:
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
| `status.sh` | python3 "$ROOT/watchdog.py" last // true |
| `uninstall.sh` | #!/usr/bin/env bash |
| `uninstall.sh` | sudo systemctl disable --now system-watchdog.service // true |
| `uninstall.sh` | sudo systemctl daemon-reload |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- watchdog.py: def push(url, timeout):
- watchdog.py: with urllib.request.urlopen(req, timeout=timeout) as resp:
- watchdog.py: ok, status, error, response_ms = push(args.push_url, args.timeout)
- watchdog.py: p.add_argument("--timeout", type=int, default=int(os.environ.get("WATCHDOG_TIMEOUT", "20")))

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Persistent heartbeat sender for a Uptime Kuma push monitor. |
| `dev/legacy/README.md` | It runs on Linux Mint as `system-watchdog.service`, sends one push every 60 seconds to the remote Kuma endpoint, and records each attempt in local SQLite at: |
| `dev/legacy/docs/ARCHITECTURE.md` | - `watchdog.py` sends an HTTP push to Uptime Kuma every 60 seconds. |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push failures are recorded but do not stop the loop. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Run one push manually: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | If HTTP push fails, the service continues retrying. Check network reachability to: |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Push interval: 60 seconds |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Verify with `systemctl`, SQLite queries, and a real HTTP push. |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | 4. Commit locally: |
| `dev/legacy/docs/UPDATE_PROCEDURE.md` | git commit -m "update system watchdog" |
| `install.sh` | python3 --version >/dev/null |
| `watchdog.py` | DEFAULT_PUSH_URL = "http://150.230.148.128:3001/api/push/W1h8mBAnP8?status=up&msg=OK&ping=" |
| `watchdog.py` | conn.commit() |
| `watchdog.py` | def push(url, timeout): |
| `watchdog.py` | ok, status, error, response_ms = push(args.push_url, args.timeout) |
| `watchdog.py` | p = argparse.ArgumentParser(description="Linux Mint heartbeat watchdog for Uptime Kuma push monitors") |
| `watchdog.py` | p.add_argument("--push-url", default=os.environ.get("WATCHDOG_PUSH_URL", DEFAULT_PUSH_URL)) |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | It runs on Linux Mint as `system-watchdog.service`, sends one push every 60 seconds to the remote Kuma endpoint, and records each attempt in local SQLite at: |
| `dev/legacy/README.md` | - `watchdog.sqlite`: runtime database |
| `dev/legacy/docs/CODEX_CONTEXT.md` | - Verify with `systemctl`, SQLite queries, and a real HTTP push. |
| `uninstall.sh` | echo "Database and logs left in place: watchdog.sqlite watchdog.log" |
| `logs.sh` | #!/usr/bin/env bash |
| `logs.sh` | journalctl -u system-watchdog.service -n "${1:-100}" --no-pager |
| `watchdog.py` | import sqlite3 |
| `watchdog.py` | conn = sqlite3.connect(path) |
| `watchdog.py` | import urllib.error |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
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

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: - `watchdog.sqlite`: runtime database
- dev/legacy/docs/ARCHITECTURE.md: - Push failures are recorded but do not stop the loop.
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add local Telegram sending.
- dev/legacy/docs/CODEX_CONTEXT.md: - Do not add Docker on Mint.
- install.sh: python3 --version >/dev/null
- uninstall.sh: echo "Database and logs left in place: watchdog.sqlite watchdog.log"

RECENT_DECISIONS
| source | fact |
|---|---|
| `UNKNOWN` | no verified recent decisions found in read sources. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `UNKNOWN` | no verified roadmap found in read sources. |

LEGACY_SUMMARY
- legacy_docs_read_count: 12
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/docs/ARCHITECTURE.md`
- `dev/legacy/docs/TROUBLESHOOTING.md`
- `dev/legacy/docs/CODEX_CONTEXT.md`
- `dev/legacy/docs/UPDATE_PROCEDURE.md`
- `requirements.txt`
- `install.sh`
- `logs.sh`
- `status.sh`
- `uninstall.sh`
- `watchdog.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../system_watchdog/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/system-watchdog/overview.md)
- human_folder: [human folder](../../human/projects/system-watchdog)
- legacy_docs: [dev/legacy](../../../system_watchdog/dev/legacy)
- repo_path: [repo](../../../system_watchdog)

OPEN_QUESTIONS
- watchdog.py: with urllib.request.urlopen(req, timeout=timeout) as resp:
