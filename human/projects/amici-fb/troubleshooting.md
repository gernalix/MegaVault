# amici_fb Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
- dev/legacy/README.md: Privacy: do not commit `.env`, `fb_storage_state.json`, browser artifacts,
- dev/legacy/README.md: cookies, Telegram tokens, or the real Uptime Kuma Push URL.
- dev/legacy/docs/ARCHITECTURE.md: - `.env.example`: safe placeholder env file. Real `.env` is private and ignored.
- dev/legacy/docs/ARCHITECTURE.md: - `amici_fb.sqlite3`: SQLite history database in the project root when present.
- dev/legacy/docs/ARCHITECTURE.md: 10. Save snapshot CSV, update SQLite, select a safe previous CSV for comparison,
- dev/legacy/docs/ARCHITECTURE.md: 11. Close page/context/browser/database in `finally`.
- dev/legacy/docs/ARCHITECTURE.md: - `fb_storage_state.json` is the saved login/session file. Do not commit or
- dev/legacy/docs/ARCHITECTURE.md: ## Uptime Kuma Push
- dev/legacy/docs/ARCHITECTURE.md: - Push errors are logged as warnings and never fail the scraper.
- dev/legacy/docs/TROUBLESHOOTING.md: Use conservative fixes. Do not remove `.env`, `fb_storage_state.json`,
- dev/legacy/docs/TROUBLESHOOTING.md: .venv/bin/python -m playwright --version
- dev/legacy/docs/TROUBLESHOOTING.md: Never print the real URL.
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: do not delete state files. If a service process is genuinely stale and no
- dev/legacy/docs/TROUBLESHOOTING.md: Symptom: database errors, missing CSVs, or no previous snapshot found.
