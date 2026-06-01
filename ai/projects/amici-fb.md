# amici_fb AI OPERATIONS

PROJECT
- name: amici_fb
- slug: amici-fb
- purpose: Linux Mint user-level Facebook automation that opens Facebook with a browser profile, processes friends/URLs, and records local state in SQLite; treat credentials and browser session data as sensitive.
- current_status: Working tree has 8 non-clean entries; do not mix unrelated changes. First entries: M amici_fb.sqlite3, ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912
- repo_path: `/home/daniele/codex-workspace/scripts/amici_fb`
- remote: `https://github.com/gernalix/amici_fb.git`
- branch: `master`
- last_verified_commit/date: `0e021f6` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: Python tooling, playwright, requests
- DB: SQLite
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `_shared/telegram_notify.py`
- `amici_fb.py`
- `amici_fb_task_runner.py`
- `telegram_notify.py`
important_folders:
- `_shared`
- `data`
- `dev`
important_files:
- `requirements.txt`
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `.gitignore`
- `_shared/__init__.py`
- `_shared/telegram_notify.py`
- `amici-fb.service`
- `amici-fb.timer`
- `amici_fb.py`
- `amici_fb.service`
- `amici_fb.sqlite3`
- `amici_fb.timer`
- `amici_fb.zip`
- `amici_fb_daily.cmd`
- `amici_fb_task_runner.py`
- `data/.~lock.amici_2025-11-24.csv#`
- `data/amici_2025-11-24.csv`
- `data/amici_2025-11-28.csv`
- `data/amici_2025-11-29.csv`
- `data/amici_2025-11-30.csv`
- `data/amici_2025-12-16.csv`
- `data/amici_2025-12-21.csv`
- `data/amici_2025-12-24.csv`
- `data/amici_2025-12-27.csv`
- `data/amici_2025-12-28.csv`
- `data/amici_2025-12-30.csv`
- `data/amici_2025-12-31.csv`
- `data/amici_2026-01-01.csv`
- `data/amici_2026-01-02.csv`
- `data/amici_2026-01-05.csv`
- `data/amici_2026-01-06.csv`
- `data/amici_2026-01-07.csv`
- `data/amici_2026-01-08.csv`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `*.db/*.sqlite user/runtime data`

ARCH
summary:
- dev/legacy/README.md: `amici_fb` is a Linux Mint user-level automation that opens Facebook with
- dev/legacy/docs/ARCHITECTURE.md: - `amici_fb.py`: main scraper and data pipeline.
- dev/legacy/docs/TROUBLESHOOTING.md: Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`,
- dev/legacy/CHANGELOG.md: - Repaired the Linux Mint user-level `amici_fb.service` and
- dev/legacy/docs/OPERATIONS.md: Use the same runner as systemd:
- dev/legacy/AGENTS.md: This repo runs a real Facebook scraper on the local Linux Mint machine. Treat it
- _shared/__init__.py: """Local shared helpers for amici_fb."""
- _shared/telegram_notify.py: Helper comune per notifiche Telegram.
- amici-fb.service: Description=Snapshot amici Facebook (Playwright) + diff + SQLite + Telegram
- amici-fb.timer: Description=Esecuzione giornaliera amici_fb alle 09:00
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # amici_fb |
| `dev/legacy/README.md` | ## Main Commands |
| `dev/legacy/docs/ARCHITECTURE.md` | # Architecture |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Repository Map |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Runtime Paths |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Entry Points |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Main Scraper Flow |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Playwright State and Diagnostics |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Telegram |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Uptime Kuma Push |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Logs and State |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Locks |
| `dev/legacy/docs/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Timer Not Active |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Service Path or Unit Wrong |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Venv or Python Broken |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Playwright Browser Missing |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Facebook Login Expired |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts, |
| `dev/legacy/README.md` | cookies, Telegram tokens, or the real Uptime Kuma Push URL. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `.env.example`: safe placeholder env file. Real `.env` is private and ignored. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `amici_fb.sqlite3`: SQLite history database in the project root when present. |
| `dev/legacy/docs/ARCHITECTURE.md` | 10. Save snapshot CSV, update SQLite, select a safe previous CSV for comparison, |
| `dev/legacy/docs/ARCHITECTURE.md` | 11. Close page/context/browser/database in `finally`. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `fb_storage_state.json` is the saved login/session file. Do not commit or |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Uptime Kuma Push |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push errors are logged as warnings and never fail the scraper. |
| `dev/legacy/docs/ARCHITECTURE.md` | Primary live logs: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`, |
| `dev/legacy/docs/TROUBLESHOOTING.md` | .venv/bin/python -m playwright --version |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: restore network, then start one run: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Symptom: `Telegram non configurato`, `telegram_notify.failed`, or missing final |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Never print the real URL. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: do not delete state files. If a service process is genuinely stale and no |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Symptom: database errors, missing CSVs, or no previous snapshot found. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: preserve the database and CSVs; use `AMICI_FB_DB` only for an explicit test |
| `dev/legacy/docs/TROUBLESHOOTING.md` | database: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | git restore --staged .env fb_storage_state.json 2>/dev/null // true |
| `dev/legacy/CHANGELOG.md` | faulthandler support, and non-fatal Uptime Kuma Push integration. |
| `dev/legacy/docs/OPERATIONS.md` | Do not paste token values into logs or reports. |
| `dev/legacy/docs/OPERATIONS.md` | Safe test through the runner helper: |
| `dev/legacy/docs/OPERATIONS.md` | Safe raw curl test without printing the URL: |
| `dev/legacy/docs/OPERATIONS.md` | Then check Uptime Kuma UI: the `amici_fb` Push monitor should be UP. |
| `dev/legacy/docs/OPERATIONS.md` | 1. Read logs first; do not delete browser/session state. |

BUILD_TEST
build_files:
- `requirements.txt`
commands_found:
| source | fact |
|---|---|
| `dev/legacy/README.md` | git status --short |
| `dev/legacy/README.md` | systemctl --user status amici_fb.service amici_fb.timer --no-pager |
| `dev/legacy/README.md` | systemctl --user list-timers amici_fb.timer --no-pager |
| `dev/legacy/README.md` | journalctl --user -u amici_fb.service -u amici_fb.timer --since "30 minutes ago" --no-pager |
| `dev/legacy/README.md` | systemctl --user daemon-reload |
| `dev/legacy/docs/ARCHITECTURE.md` | systemctl --user start amici_fb.service |
| `dev/legacy/docs/ARCHITECTURE.md` | journalctl --user -u amici_fb.service -u amici_fb.timer --since "30 minutes ago" --no-pager |
| `dev/legacy/docs/ARCHITECTURE.md` | systemctl --user status amici_fb.service --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user status amici_fb.timer --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user list-timers amici_fb.timer --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user cat amici_fb.timer |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user daemon-reload |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user enable --now amici_fb.timer |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user cat amici_fb.service |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user start amici_fb.service |
| `dev/legacy/docs/TROUBLESHOOTING.md` | .venv/bin/python -c 'import playwright, requests, sqlite3; print("imports ok")' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | python3 -m venv .venv |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl --user -u amici_fb.service --since "3 days ago" --no-pager / grep -Ei 'login/checkpoint/special/Sessione' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl --user -u amici_fb.service --since "3 days ago" --no-pager / grep -Ei 'ERR_/Timeout/DNS/internet' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl --user -u amici_fb.service --since "30 minutes ago" --no-pager / grep -Ei 'telegram' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user status amici_fb.service --no-pager |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user stop amici_fb.service |
| `dev/legacy/docs/TROUBLESHOOTING.md` | import sqlite3 |
| `dev/legacy/docs/TROUBLESHOOTING.md` | conn = sqlite3.connect("amici_fb.sqlite3") |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/docs/TROUBLESHOOTING.md: or navigation timeout.
- dev/legacy/docs/TROUBLESHOOTING.md: journalctl --user -u amici_fb.service --since "3 days ago" --no-pager / grep -Ei 'ERR_/Timeout/DNS/internet'
- dev/legacy/docs/OPERATIONS.md: curl -fsS --get --connect-timeout 2 --max-time 5 \
- _shared/telegram_notify.py: response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20)
- _shared/telegram_notify.py: timeout=20,
- _shared/telegram_notify.py: timeout=60,
- amici_fb.py: self._thread.join(timeout=1.0)
- amici_fb.py: return f"error:{type(e).__name__}:{e}"
- amici_fb.py: return f"<url-error {type(e).__name__}: {e}>"
- amici_fb.py: return f"<title-error {type(e).__name__}: {e}>"

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts, |
| `dev/legacy/README.md` | cookies, Telegram tokens, or the real Uptime Kuma Push URL. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `fb_storage_state.json` is the saved login/session file. Do not commit or |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Uptime Kuma Push |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push errors are logged as warnings and never fail the scraper. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | .venv/bin/python -m playwright --version |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: restore network, then start one run: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | git restore --staged .env fb_storage_state.json 2>/dev/null // true |
| `dev/legacy/CHANGELOG.md` | faulthandler support, and non-fatal Uptime Kuma Push integration. |
| `dev/legacy/docs/OPERATIONS.md` | Then check Uptime Kuma UI: the `amici_fb` Push monitor should be UP. |
| `dev/legacy/AGENTS.md` | Do not delete Playwright browsers, cookies, storage state, CSV history, SQLite |
| `dev/legacy/AGENTS.md` | Never print or commit: |
| `dev/legacy/AGENTS.md` | - Real Uptime Kuma Push URLs or push tokens. |
| `dev/legacy/AGENTS.md` | Use masked log output and placeholder examples only. `.env` must stay ignored. |
| `dev/legacy/AGENTS.md` | 6. Check logs for `status=0/SUCCESS`, `telegram_notify.sent`, and Kuma push |
| `dev/legacy/AGENTS.md` | - Include compatible pre-existing dirty changes in the final commit when the |
| `dev/legacy/AGENTS.md` | - Before commit, scan staged text for real tokens/URLs: |
| `amici_fb.py` | conn.commit() |
| `amici_fb.py` | wait_until="commit", |
| `amici_fb_task_runner.py` | """Thin systemd runner for amici_fb.py with early diagnostics and Kuma push.""" |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts, |
| `dev/legacy/docs/ARCHITECTURE.md` | - `amici_fb.sqlite3`: SQLite history database in the project root when present. |
| `dev/legacy/docs/ARCHITECTURE.md` | 10. Save snapshot CSV, update SQLite, select a safe previous CSV for comparison, |
| `dev/legacy/docs/ARCHITECTURE.md` | 11. Close page/context/browser/database in `finally`. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `fb_storage_state.json` is the saved login/session file. Do not commit or |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push errors are logged as warnings and never fail the scraper. |
| `dev/legacy/docs/ARCHITECTURE.md` | Primary live logs: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`, |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: restore network, then start one run: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: do not delete state files. If a service process is genuinely stale and no |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Symptom: database errors, missing CSVs, or no previous snapshot found. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Fix: preserve the database and CSVs; use `AMICI_FB_DB` only for an explicit test |
| `dev/legacy/docs/TROUBLESHOOTING.md` | database: |
| `dev/legacy/docs/TROUBLESHOOTING.md` | git restore --staged .env fb_storage_state.json 2>/dev/null // true |
| `dev/legacy/CHANGELOG.md` | faulthandler support, and non-fatal Uptime Kuma Push integration. |
| `dev/legacy/docs/OPERATIONS.md` | Do not paste token values into logs or reports. |
| `dev/legacy/docs/OPERATIONS.md` | 1. Read logs first; do not delete browser/session state. |
| `dev/legacy/AGENTS.md` | state is authoritative for runtime. |
| `dev/legacy/AGENTS.md` | Do not delete Playwright browsers, cookies, storage state, CSV history, SQLite |
| `dev/legacy/AGENTS.md` | Use masked log output and placeholder examples only. `.env` must stay ignored. |
| `dev/legacy/AGENTS.md` | 6. Check logs for `status=0/SUCCESS`, `telegram_notify.sent`, and Kuma push |
| `amici_fb.py` | # SQLite DB (creato se non esiste) |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/docs/ARCHITECTURE.md` | sends Uptime Kuma status after success/failure. |
| `dev/legacy/docs/ARCHITECTURE.md` | - Failure: `status=down`, `msg=FAILED:<short reason>`. |
| `dev/legacy/docs/ARCHITECTURE.md` | - Push errors are logged as warnings and never fail the scraper. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Symptom: Python missing, imports fail, or copied venv has broken symlinks. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## Network or DNS Failure |
| `dev/legacy/docs/TROUBLESHOOTING.md` | or navigation timeout. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl --user -u amici_fb.service --since "3 days ago" --no-pager / grep -Ei 'ERR_/Timeout/DNS/internet' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Known evidence: on 2026-05-13 the service failed at |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## SQLite or Data Path Issue |
| `dev/legacy/docs/OPERATIONS.md` | curl -fsS --get --connect-timeout 2 --max-time 5 \ |
| `dev/legacy/docs/OPERATIONS.md` | ## Success and Failure Signals |
| `dev/legacy/docs/OPERATIONS.md` | Failure: |
| `dev/legacy/docs/OPERATIONS.md` | - Journal traceback includes Playwright, network, login, or config failure. |
| `dev/legacy/AGENTS.md` | - `data/browser_diag_*`: failure evidence and screenshots/HTML from Playwright. |
| `_shared/telegram_notify.py` | response = requests.post(_telegram_url("sendMessage"), json=payload, timeout=20) |
| `_shared/telegram_notify.py` | timeout=20, |
| `_shared/telegram_notify.py` | timeout=60, |
| `_shared/telegram_notify.py` | parser.error("title and message are required unless --check is used") |
| `_shared/telegram_notify.py` | print(f"ERROR: {type(exc).__name__}: {exc}", file=sys.stderr) |
| `amici_fb.py` | self._thread.join(timeout=1.0) |
| `amici_fb.py` | return f"error:{type(e).__name__}:{e}" |
| `amici_fb.py` | return f"<url-error {type(e).__name__}: {e}>" |
| `amici_fb.py` | return f"<title-error {type(e).__name__}: {e}>" |
| `amici_fb.py` | logger.log(f"save_artifacts.state_failed label={label} error={type(e).__name__}: {e}") |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts,
- dev/legacy/docs/ARCHITECTURE.md: - `.env.example`: safe placeholder env file. Real `.env` is private and ignored.
- dev/legacy/docs/ARCHITECTURE.md: - `amici_fb.sqlite3`: SQLite history database in the project root when present.
- dev/legacy/docs/ARCHITECTURE.md: 10. Save snapshot CSV, update SQLite, select a safe previous CSV for comparison,
- dev/legacy/docs/ARCHITECTURE.md: 11. Close page/context/browser/database in `finally`.
- dev/legacy/docs/ARCHITECTURE.md: - `fb_storage_state.json` is the saved login/session file. Do not commit or
- dev/legacy/docs/ARCHITECTURE.md: - Push errors are logged as warnings and never fail the scraper.
- dev/legacy/docs/TROUBLESHOOTING.md: Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`,
- dev/legacy/docs/TROUBLESHOOTING.md: .venv/bin/python -m playwright --version
- dev/legacy/docs/TROUBLESHOOTING.md: Never print the real URL.
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: do not delete state files. If a service process is genuinely stale and no
- dev/legacy/docs/TROUBLESHOOTING.md: Symptom: database errors, missing CSVs, or no previous snapshot found.
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: preserve the database and CSVs; use `AMICI_FB_DB` only for an explicit test
- dev/legacy/docs/TROUBLESHOOTING.md: database:
- dev/legacy/docs/OPERATIONS.md: Do not paste token values into logs or reports.
- dev/legacy/docs/OPERATIONS.md: Safe test through the runner helper:

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/CHANGELOG.md` | # Changelog |
| `dev/legacy/CHANGELOG.md` | ## 2026-05-14 |
| `dev/legacy/CHANGELOG.md` | - Repaired the Linux Mint user-level `amici_fb.service` and |
| `dev/legacy/CHANGELOG.md` | - Added `amici_fb_task_runner.py` as the systemd runner with early diagnostics, |
| `dev/legacy/CHANGELOG.md` | - Added project-local `.env` loading through the service and documented |
| `dev/legacy/CHANGELOG.md` | - Verified a live service run: Facebook storage state loaded, 193 friends |
| `dev/legacy/CHANGELOG.md` | - Added Codex-focused project documentation in `AGENTS.md` and `docs/`. |
| `dev/legacy/docs/OPERATIONS.md` | Status and next run: |
| `dev/legacy/docs/OPERATIONS.md` | - `amici_fb.timer`: `active (waiting)`, next trigger shown. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/docs/OPERATIONS.md` | Status and next run: |
| `dev/legacy/docs/OPERATIONS.md` | - `amici_fb.timer`: `active (waiting)`, next trigger shown. |
| `amici_fb.py` | status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','accepted','rejected','unknown')), |
| `amici_fb.py` | - pending/unknown + ora tra amici -> accepted (+accepted_at) |
| `amici_fb.py` | WHERE status IN ('pending','unknown') |
| `amici_fb.py` | status = (r["status"] or "pending").strip() |

LEGACY_SUMMARY
- legacy_docs_read_count: 17
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/docs/ARCHITECTURE.md`
- `dev/legacy/docs/TROUBLESHOOTING.md`
- `dev/legacy/CHANGELOG.md`
- `dev/legacy/docs/OPERATIONS.md`
- `dev/legacy/AGENTS.md`
- `requirements.txt`
- `_shared/__init__.py`
- `_shared/telegram_notify.py`
- `amici-fb.service`
- `amici-fb.timer`
- `amici_fb.py`
- `amici_fb.service`
- `amici_fb.timer`
- `amici_fb_task_runner.py`
- `telegram_notify.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../scripts/amici_fb/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/amici-fb/overview.md)
- human_folder: [human folder](../../human/projects/amici-fb)
- legacy_docs: [dev/legacy](../../../scripts/amici_fb/dev/legacy)
- repo_path: [repo](../../../scripts/amici_fb)

OPEN_QUESTIONS
- dev/legacy/docs/TROUBLESHOOTING.md: Symptom: Python missing, imports fail, or copied venv has broken symlinks.
