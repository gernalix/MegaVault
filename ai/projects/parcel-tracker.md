# parcel-tracker AI OPERATIONS

PROJECT
- name: parcel-tracker
- slug: parcel-tracker
- purpose: Servizio leggero user-level per monitorare la spedizione `XT329499807TS`.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/parcel-tracker`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `0fea1eb` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `parcel_tracker.py`
important_folders:
- `dev`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `parcel_tracker.py`
- `parcel_tracker.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `logs`

ARCH
summary:
- dev/legacy/dev/INDEX.md: Servizio leggero user-level per monitorare la spedizione `XT329499807TS`.
- dev/legacy/dev/TROUBLESHOOTING.md: ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi
- dev/legacy/dev/CHANGELOG.md: - Creato tracker permanente per `XT329499807TS`.
- dev/legacy/dev/OPERATIONS.md: mkdir -p ~/.config/systemd/user
- parcel_tracker.py: from __future__ import annotations
- parcel_tracker.sh: BASE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/dev/INDEX.md` | # Parcel Tracker |
| `dev/legacy/dev/INDEX.md` | ## File principali |
| `dev/legacy/dev/INDEX.md` | ## Comandi |
| `dev/legacy/dev/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/dev/TROUBLESHOOTING.md` | ## Parsing ParcelsApp |
| `dev/legacy/dev/TROUBLESHOOTING.md` | ## Nessuna notifica Telegram |
| `dev/legacy/dev/TROUBLESHOOTING.md` | ## Systemd user non raggiungibile |
| `dev/legacy/dev/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/CHANGELOG.md` | ## v1 |
| `dev/legacy/dev/OPERATIONS.md` | # Operations |
| `dev/legacy/dev/OPERATIONS.md` | ## Installazione timer |
| `dev/legacy/dev/OPERATIONS.md` | ## Verifiche |
| `dev/legacy/dev/OPERATIONS.md` | ## Telegram |
| `dev/legacy/dev/OPERATIONS.md` | ## Uptime Kuma |
| `parcel_tracker.py` | #!/usr/bin/env python3 |
| `parcel_tracker.sh` | # v1 |
| `parcel_tracker.sh` | #!/usr/bin/env bash |
| `dev/legacy/dev/INDEX.md` | Servizio leggero user-level per monitorare la spedizione `XT329499807TS`. |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi |
| `dev/legacy/dev/TROUBLESHOOTING.md` | Il fallback evita crash e mantiene Kuma aggiornato, ma puo notificare solo cambiamenti del testo leggibile, non necessariamente eventi logistici puliti. Controllare `last_source` con: |
| `dev/legacy/dev/TROUBLESHOOTING.md` | La prima esecuzione inizializza lo stato e non notifica, per evitare duplicati. Le notifiche partono solo da un cambio successivo di `last_event_key`. |
| `dev/legacy/dev/TROUBLESHOOTING.md` | ## Systemd user non raggiungibile |
| `dev/legacy/dev/TROUBLESHOOTING.md` | In shell non interattive puo servire: |
| `dev/legacy/dev/CHANGELOG.md` | - Push Uptime Kuma a ogni controllo riuscito. |
| `dev/legacy/dev/OPERATIONS.md` | Non contiene token Telegram hardcoded. |
| `dev/legacy/dev/OPERATIONS.md` | A ogni controllo riuscito invia push all'URL fornito nel prompt. |
| `parcel_tracker.py` | KUMA_PUSH_URL = "http://150.230.148.128:3001/api/push/M1O23ekcPKlx5oZ2dPVSviYhJ0q3TwXX?status=up&msg=OK&ping=" |
| `parcel_tracker.py` | key TEXT PRIMARY KEY, |
| `parcel_tracker.py` | id INTEGER PRIMARY KEY AUTOINCREMENT, |
| `parcel_tracker.py` | conn.commit() |
| `parcel_tracker.py` | log(f"kuma.push OK msg={message}") |
| `parcel_tracker.py` | parser.add_argument("--test-kuma", action="store_true", help="Push one successful heartbeat to Uptime Kuma.") |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
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
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/dev/TROUBLESHOOTING.md: Il fallback evita crash e mantiene Kuma aggiornato, ma puo notificare solo cambiamenti del testo leggibile, non necessariamente eventi logistici puliti. Controllare `last_source` con:
- parcel_tracker.py: def fetch_url(url: str, timeout: int = 30) -> str:
- parcel_tracker.py: with urllib.request.urlopen(req, timeout=timeout) as resp:
- parcel_tracker.py: timeout=40,
- parcel_tracker.py: log(f"telegram.test ERROR helper_missing path={TELEGRAM_HELPER}")
- parcel_tracker.py: subprocess.run([sys.executable, str(TELEGRAM_HELPER), "--check"], check=True, timeout=20)
- parcel_tracker.py: urllib.request.urlopen(KUMA_PUSH_URL, timeout=20).read()

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | - Push Uptime Kuma a ogni controllo riuscito. |
| `dev/legacy/dev/OPERATIONS.md` | A ogni controllo riuscito invia push all'URL fornito nel prompt. |
| `parcel_tracker.py` | KUMA_PUSH_URL = "http://150.230.148.128:3001/api/push/M1O23ekcPKlx5oZ2dPVSviYhJ0q3TwXX?status=up&msg=OK&ping=" |
| `parcel_tracker.py` | conn.commit() |
| `parcel_tracker.py` | log(f"kuma.push OK msg={message}") |
| `parcel_tracker.py` | parser.add_argument("--test-kuma", action="store_true", help="Push one successful heartbeat to Uptime Kuma.") |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | Il fallback evita crash e mantiene Kuma aggiornato, ma puo notificare solo cambiamenti del testo leggibile, non necessariamente eventi logistici puliti. Controllare `last_source` con: |
| `dev/legacy/dev/CHANGELOG.md` | - Push Uptime Kuma a ogni controllo riuscito. |
| `parcel_tracker.py` | log(f"kuma.push OK msg={message}") |
| `parcel_tracker.py` | import sqlite3 |
| `parcel_tracker.py` | def db() -> sqlite3.Connection: |
| `parcel_tracker.py` | conn = sqlite3.connect(STATE_DB) |
| `parcel_tracker.py` | def get_state(conn: sqlite3.Connection, key: str) -> str / None: |
| `parcel_tracker.py` | def set_state(conn: sqlite3.Connection, key: str, value: str) -> None: |
| `parcel_tracker.py` | import urllib.error |
| `parcel_tracker.py` | log(f"telegram.test ERROR helper_missing path={TELEGRAM_HELPER}") |
| `parcel_tracker.py` | log(f"run ERROR {type(exc).__name__}: {exc}") |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
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

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- UNKNOWN: no verified do-not-break rules found in read sources.

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/CHANGELOG.md` | ## v1 |
| `dev/legacy/dev/CHANGELOG.md` | - Creato tracker permanente per `XT329499807TS`. |
| `dev/legacy/dev/CHANGELOG.md` | - Stato e cronologia controlli in SQLite. |
| `dev/legacy/dev/CHANGELOG.md` | - Notifica Telegram solo su nuovo evento. |
| `dev/legacy/dev/CHANGELOG.md` | - Push Uptime Kuma a ogni controllo riuscito. |
| `dev/legacy/dev/CHANGELOG.md` | - Timer systemd user ogni 30 minuti. |
| `dev/legacy/dev/CHANGELOG.md` | - Documentazione operativa codex-friendly. |
| `dev/legacy/dev/TROUBLESHOOTING.md` | ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi |
| `parcel_tracker.py` | status = clean_text(next((x for x in text_fields if clean_text(x)), "")) |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi |
| `parcel_tracker.py` | status = clean_text(next((x for x in text_fields if clean_text(x)), "")) |

LEGACY_SUMMARY
- legacy_docs_read_count: 7
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/dev/TROUBLESHOOTING.md`
- `dev/legacy/dev/CHANGELOG.md`
- `dev/legacy/dev/OPERATIONS.md`
- `parcel_tracker.py`
- `parcel_tracker.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../parcel-tracker/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/parcel-tracker/overview.md)
- human_folder: [human folder](../../human/projects/parcel-tracker)
- legacy_docs: [dev/legacy](../../../parcel-tracker/dev/legacy)
- repo_path: [repo](../../../parcel-tracker)

OPEN_QUESTIONS
- parcel_tracker.py: with urllib.request.urlopen(req, timeout=timeout) as resp:
- parcel_tracker.py: log(f"telegram.test ERROR helper_missing path={TELEGRAM_HELPER}")
- parcel_tracker.py: urllib.request.urlopen(KUMA_PUSH_URL, timeout=20).read()
