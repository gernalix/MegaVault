# parcel-tracker Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | Il fallback evita crash e mantiene Kuma aggiornato, ma puo notificare solo cambiamenti del testo leggibile, non necessariamente eventi logistici puliti. Controllare `last_source` con: |
| `parcel_tracker.py` | import urllib.error |
| `parcel_tracker.py` | error TEXT |
| `parcel_tracker.py` | def fetch_url(url: str, timeout: int = 30) -> str: |
| `parcel_tracker.py` | with urllib.request.urlopen(req, timeout=timeout) as resp: |
| `parcel_tracker.py` | timeout=40, |
| `parcel_tracker.py` | log(f"telegram.test ERROR helper_missing path={TELEGRAM_HELPER}") |
| `parcel_tracker.py` | subprocess.run([sys.executable, str(TELEGRAM_HELPER), "--check"], check=True, timeout=20) |
| `parcel_tracker.py` | urllib.request.urlopen(KUMA_PUSH_URL, timeout=20).read() |
| `parcel_tracker.py` | "INSERT INTO checks(checked_at, ok, event_key, status, source, notified, error) VALUES(?, 1, ?, ?, ?, ?, NULL)", |
| `parcel_tracker.py` | "INSERT INTO checks(checked_at, ok, event_key, status, source, notified, error) VALUES(?, 0, NULL, NULL, NULL, 0, ?)", |
| `parcel_tracker.py` | log(f"run ERROR {type(exc).__name__}: {exc}") |
| `parcel_tracker.py` | "SELECT checked_at, ok, source, notified, error FROM checks ORDER BY id DESC LIMIT 1" |
| `parcel_tracker.py` | print(f"last_check: {row[0]} ok={row[1]} source={row[2] or '-'} notified={row[3]} error={row[4] or '-'}") |
| `parcel_tracker.py` | parser.error("choose exactly one command") |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | systemctl --user list-timers --all parcel-tracker.timer |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user daemon-reload |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user enable --now parcel-tracker.timer |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user status parcel-tracker.timer --no-pager |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user list-timers --all parcel-tracker.timer |
| `dev/legacy/dev/OPERATIONS.md` | journalctl --user -u parcel-tracker.service -n 80 --no-pager |
| `parcel_tracker.py` | #!/usr/bin/env python3 |
| `parcel_tracker.py` | import sqlite3 |
| `parcel_tracker.py` | def db() -> sqlite3.Connection: |
| `parcel_tracker.py` | conn = sqlite3.connect(STATE_DB) |
| `parcel_tracker.py` | def get_state(conn: sqlite3.Connection, key: str) -> str / None: |
| `parcel_tracker.py` | def set_state(conn: sqlite3.Connection, key: str, value: str) -> None: |
| `parcel_tracker.sh` | #!/usr/bin/env bash |

## Safety Checks Before Fixing
- dev/legacy/dev/CHANGELOG.md: - Push Uptime Kuma a ogni controllo riuscito.
- dev/legacy/dev/OPERATIONS.md: A ogni controllo riuscito invia push all'URL fornito nel prompt.
- parcel_tracker.py: KUMA_PUSH_URL = "http://150.230.148.128:3001/api/push/M1O23ekcPKlx5oZ2dPVSviYhJ0q3TwXX?status=up&msg=OK&ping="
- parcel_tracker.py: conn.commit()
- parcel_tracker.py: log(f"kuma.push OK msg={message}")
- parcel_tracker.py: parser.add_argument("--test-kuma", action="store_true", help="Push one successful heartbeat to Uptime Kuma.")
