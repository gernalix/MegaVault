# WindowTabNotes Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/dev/INDEX.md` | - `dev/BUG_REGISTRY.md`: root cause/fix/invarianti storiche per overlay, search, Chrome e Native Messaging. |
| `dev/legacy/dev/TEST_PLAN.md` | - durante cambi focus rapidi, il servizio `windowtabnotes.service` non deve riavviarsi; "nessuna finestra attiva" deve restare evento transitorio, non crash. |
| `dev/legacy/dev/BUG_REGISTRY.md` | # Bug Registry |
| `dev/legacy/dev/BUG_REGISTRY.md` | Root cause: |
| `dev/legacy/dev/BUG_REGISTRY.md` | - i log mostravano contese `sqlite3.OperationalError: database is locked`. |
| `dev/legacy/docs/USO_QUOTIDIANO.md` | - se resta uno stato sporco dopo crash/test, `system/bin/windowtabnotes overlay-cleanup` chiude overlay stale e lascia massimo un overlay |
| `browser-extension/dashboard.js` | const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSearch }).catch((error) => ({ |
| `browser-extension/dashboard.js` | error: String(error), |
| `browser-extension/dashboard.js` | statusEl.textContent = response?.error // "Native Messaging host unavailable."; |
| `system/windowtabnotes/active_watch.py` | except RuntimeError as error: |
| `system/windowtabnotes/active_watch.py` | "active_window": {"error": str(error)}, |
| `system/windowtabnotes/active_watch.py` | except Exception as error: |
| `system/windowtabnotes/active_watch.py` | active = {"error": str(error)} |
| `system/windowtabnotes/api.py` | return {"ok": False, "ignored": True, "error": "Internal focus tab ignored."} |
| `system/windowtabnotes/api.py` | except Exception as error: |
| `system/windowtabnotes/api.py` | return _error("action_failed", str(error)) |
| `system/windowtabnotes/api.py` | return {"ok": False, "error": {"code": code, "message": message}} |
| `system/windowtabnotes/cli.py` | except Exception as error: |
| `system/windowtabnotes/cli.py` | print(f"ERROR: {error}", file=sys.stderr) |
| `system/windowtabnotes/cli.py` | db_ok = f"fail: {error}" |
| `system/windowtabnotes/db.py` | conn = sqlite3.connect(str(target), timeout=0.75) |
| `system/windowtabnotes/db.py` | except sqlite3.OperationalError as error: |
| `system/windowtabnotes/db.py` | if "locked" not in str(error).lower(): |
| `system/windowtabnotes/db.py` | LOG.warning("SQLite WAL pragma skipped while database is locked: %s", target) |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m py_compile $(find system/windowtabnotes -name '*.py') |
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m json.tool browser-extension/manifest.json >/dev/null |
| `dev/legacy/dev/TEST_PLAN.md` | python3 - <<'PY' / system/bin/windowtabnotes-native-host |
| `dev/legacy/docs/TROUBLESHOOTING.md` | systemctl --user restart windowtabnotes.service |
| `dev/legacy/docs/INSTALLAZIONE.md` | sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq |
| `system/scripts/install.sh` | #!/usr/bin/env bash |
| `system/scripts/install.sh` | sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq |
| `system/scripts/install.sh` | python3 - "$CONFIG_DIR/settings.json" "$EXTENSION_ID" <<'PY' |
| `system/scripts/install.sh` | systemctl --user daemon-reload // true |
| `system/scripts/install.sh` | systemctl --user enable --now windowtabnotes.service // true |
| `system/scripts/uninstall.sh` | #!/usr/bin/env bash |
| `system/scripts/uninstall.sh` | systemctl --user disable --now windowtabnotes.service 2>/dev/null // true |
| `system/scripts/uninstall.sh` | systemctl --user daemon-reload 2>/dev/null // true |
| `system/windowtabnotes/active_watch.py` | for snap in snapshots: |
| `system/windowtabnotes/active_watch.py` | context = db.upsert_window_context(conn, snap.as_dict()) |
| `system/windowtabnotes/active_watch.py` | snap = active_window() |
| `system/windowtabnotes/active_watch.py` | return {"ok": True, "active_window": snap.as_dict(), "shown": False, "reason": "own-window", "transient": True} |
| `system/windowtabnotes/active_watch.py` | return {"ok": True, "active_window": snap.as_dict(), "shown": False, "reason": "unmanaged"} |
| `system/windowtabnotes/active_watch.py` | _anchor_note_for_window_if_default(conn, window_note, snap.window_id) |
| `system/windowtabnotes/active_watch.py` | _anchor_note_for_window_if_default(conn, note, snap.window_id) |

## Safety Checks Before Fixing
- dev/legacy/README.md: Versione corrente: vedere `system/bin/windowtabnotes version`.
- dev/legacy/docs/README_UTENTE.md: - un solo database SQLite
- dev/legacy/docs/README_UTENTE.md: Versione: vedere `system/bin/windowtabnotes version`.
- dev/legacy/dev/ARCHITECTURE.md: - Chrome: il service worker invia eventi tab al Native Messaging host su create/update/activate/window-focus. Le note browser sono nel database SQLite, non in un database browser separato.
- dev/legacy/dev/ARCHITECTURE.md: - Manifest Chrome richiede `version` statico. La fonte di verità prodotto resta `system/windowtabnotes/version.py`; manifest e docs vanno sincronizzati quando cambia la versione.
- dev/legacy/dev/AGENT_RULES.md: - non creare database browser separati; `chrome.storage.local` è solo cache temporanea UI.
- dev/legacy/dev/AGENT_RULES.md: - non spostare la versione da `system/windowtabnotes/version.py`.
- dev/legacy/dev/TEST_PLAN.md: system/bin/windowtabnotes version
- dev/legacy/dev/TEST_PLAN.md: - salvare manualmente una geometry fuori schermo, con width/height <= 0 o sotto la soglia irrecuperabile 16x8 nel database di test, eseguire `overlay-debug --fix-geometry` e confermare che solo quei valori impossibili vengano ripar
- dev/legacy/dev/BUG_REGISTRY.md: - il prompt iniziale non riceveva le note reali come righe Rofi, quindi la prima UI sembrava vuota anche con molte note nel database.
