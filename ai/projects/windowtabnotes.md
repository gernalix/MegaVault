# WindowTabNotes AI OPERATIONS

PROJECT
- name: WindowTabNotes
- slug: windowtabnotes
- purpose: Root repository: `WindowTabNotes/`.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/WindowTabNotes`
- remote: `git@github.com:gernalix/WindowTabNotes.git`
- branch: `codex/prompt-581472`
- last_verified_commit/date: `68e0170` / `2026-06-01T13:20:29+02:00`

STACK
- languages: JavaScript/TypeScript, Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `system/windowtabnotes/cli.py`
- `system/windowtabnotes/native_host.py`
important_folders:
- `browser-extension`
- `dev`
- `system`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `browser-extension/content_script.js`
- `browser-extension/content_style.css`
- `browser-extension/dashboard.css`
- `browser-extension/dashboard.html`
- `browser-extension/dashboard.js`
- `browser-extension/icons/icon128.png`
- `browser-extension/icons/icon16.png`
- `browser-extension/icons/icon32.png`
- `browser-extension/icons/icon48.png`
- `browser-extension/manifest.json`
- `system/bin/windowtabnotes`
- `system/bin/windowtabnotes-native-host`
- `system/scripts/install.sh`
- `system/scripts/uninstall.sh`
- `system/windowtabnotes/__init__.py`
- `system/windowtabnotes/active_watch.py`
- `system/windowtabnotes/api.py`
- `system/windowtabnotes/cli.py`
- `system/windowtabnotes/config.py`
- `system/windowtabnotes/daemon.py`
- `system/windowtabnotes/db.py`
- `system/windowtabnotes/gtk_ui.py`
- `system/windowtabnotes/logging_setup.py`
- `system/windowtabnotes/native_debug.py`
- `system/windowtabnotes/native_host.py`
- `system/windowtabnotes/overlay_runtime.py`
- `system/windowtabnotes/rofi.py`
- `system/windowtabnotes/shortcuts.py`
- `system/windowtabnotes/version.py`
- `system/windowtabnotes/windows.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Repo unico per il sistema locale Linux + Chrome WindowTabNotes.
- dev/legacy/docs/README_UTENTE.md: WindowTabNotes collega note persistenti a:
- dev/legacy/dev/INDEX.md: Root repository: `WindowTabNotes/`.
- dev/legacy/dev/ARCHITECTURE.md: WindowTabNotes è un prodotto locale unico Linux + Chrome.
- dev/legacy/dev/AGENT_RULES.md: - non trattare `browser-extension/` come root progetto.
- dev/legacy/dev/TEST_PLAN.md: system/bin/windowtabnotes version
- dev/legacy/dev/BUG_REGISTRY.md: Registro sintetico per patch future Codex. Obiettivo: evitare re-analisi e regressioni su overlay, search, Chrome e Native Messaging.
- dev/legacy/docs/TROUBLESHOOTING.md: cd /home/daniele/codex-workspace/WindowTabNotes
- dev/legacy/dev/ROADMAP.md: - estensione Chrome MV3 preservata sotto `browser-extension/`
- dev/legacy/dev/VERSIONING.md: Versione corrente: leggere `system/bin/windowtabnotes version`.
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # WindowTabNotes |
| `dev/legacy/docs/README_UTENTE.md` | # WindowTabNotes |
| `dev/legacy/dev/INDEX.md` | # WindowTabNotes Dev Index |
| `dev/legacy/dev/ARCHITECTURE.md` | # Architecture |
| `dev/legacy/dev/AGENT_RULES.md` | # Agent Rules |
| `dev/legacy/dev/TEST_PLAN.md` | # Test Plan |
| `dev/legacy/dev/BUG_REGISTRY.md` | # Bug Registry |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Invarianti |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Search metadata false positive |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Search formato duplicato |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Overlay min-size forzata |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Overlay non ridimensionabile |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Overlay sparisce durante drag/resize |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Overlay multipli |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Chrome doppia UI |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Chrome tab identity |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Shortcut search |
| `dev/legacy/dev/BUG_REGISTRY.md` | ## Search launcher non apre nulla |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Versione corrente: vedere `system/bin/windowtabnotes version`. |
| `dev/legacy/docs/README_UTENTE.md` | - un solo database SQLite |
| `dev/legacy/docs/README_UTENTE.md` | Versione: vedere `system/bin/windowtabnotes version`. |
| `dev/legacy/dev/INDEX.md` | - `browser-extension/service_worker.js`: ponte MV3 verso Native Messaging; non renderizza note nella pagina. |
| `dev/legacy/dev/INDEX.md` | - `browser-extension/content_script.js`: solo cleanup UI legacy Chrome. |
| `dev/legacy/dev/ARCHITECTURE.md` | - `browser-extension/`: ponte Chrome MV3. Traccia tab id, window id, URL, titolo e stato attivo, poi delega UI e storage al backend Linux via Native Messaging. Non renderizza post-it o dashboard nelle pagine. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Ctrl+Alt+P: XFCE avvia `system/bin/windowtabnotes search-launcher`; il launcher apre un prompt Rofi, cerca solo nel body reale delle note, poi mostra risultati compatti. Ctrl+Alt+J, Ctrl+Alt+K e Ctrl+Shift+F non sono usati per |
| `dev/legacy/dev/ARCHITECTURE.md` | - Chrome: il service worker invia eventi tab al Native Messaging host su create/update/activate/window-focus. Le note browser sono nel database SQLite, non in un database browser separato. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Linux -> Chrome tab focus non apre URI browser o pagine ponte. `rofi.py`/dashboard accodano una richiesta SQLite `chrome_focus_request`; `service_worker.js` la consuma via Native Messaging polling e usa `chrome.tabs.update`/`c |
| `dev/legacy/dev/ARCHITECTURE.md` | - Il backend ignora comunque eventuali tab legacy `WindowTabNotes Focus`/`focus.html`, cosi vecchi service worker non creano note. |
| `dev/legacy/dev/ARCHITECTURE.md` | - `profile` è `default` o `incognito`; Chrome MV3 non espone il nome profilo reale. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Manifest Chrome richiede `version` statico. La fonte di verità prodotto resta `system/windowtabnotes/version.py`; manifest e docs vanno sincronizzati quando cambia la versione. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Wayland non è target v1. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Overlay invariant: prima di qualunque autoshow/manual open viene preso `overlay.lock`, vengono chiusi gli overlay `open-note` non correnti, poi viene mostrato solo il target. `overlay-debug --fix` e `overlay-cleanup` riparano  |
| `dev/legacy/dev/ARCHITECTURE.md` | - Le finestre proprie WindowTabNotes sono focus-transient: se l'overlay GTK prende focus durante drag/resize, il watcher non chiude l'overlay e non cambia contesto. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Overlay geometry invariant: default nuove note 360x220, nessun clamp min/max artificiale. L'utente puo rendere un overlay molto piccolo e quella geometry deve persistere dopo focus switch, reopen e restart. L'overlay non decor |
| `dev/legacy/dev/ARCHITECTURE.md` | - Search UI invariant: Rofi usa tema locale largo/alto con font leggibile su Surface/XFCE; non cambiare Ctrl+Alt+P né il log `~/.cache/windowtabnotes/search-launcher.log`. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Search data invariant: backend e debug devono garantire che ogni risultato di query non vuota contenga la query case-insensitive in `notes.text`. Titolo finestra, app, URL, workspace e tab metadata sono solo display/attivazion |
| `dev/legacy/dev/ARCHITECTURE.md` | - Search lifecycle invariant: default solo `ACTIVE`; `--history` puo mostrare `STALE`/`CLOSED`/`HISTORY`, che aprono solo la nota detached/storica. Dopo una apertura da search, il watcher automatico deve riprendere al cambio fin |
| `dev/legacy/dev/ARCHITECTURE.md` | - Focus latency invariant: il path focus non deve eseguire scan pesanti. `active_watch.py` usa `_NET_ACTIVE_WINDOW`, tratta "nessuna finestra attiva" come stato transitorio e calcola la geometria X11 nello scan solo per note nuo |
| `dev/legacy/dev/ARCHITECTURE.md` | - Una finestra/tab senza nota non deve creare overlay automatico. La nota nasce solo da comando esplicito (`note-active-window`, popup/shortcut extension, dashboard). |
| `dev/legacy/dev/ARCHITECTURE.md` | - L'estensione Chrome non deve creare DOM note (`#tab-notes-root`, `#tab-notes-toolbar`, `.tn-note`): l'unico overlay visivo è GTK. |
| `dev/legacy/dev/ARCHITECTURE.md` | - La chiusura overlay salva `hidden=1` solo sulla nota di quella finestra/tab; il daemon non deve riaprirla automaticamente finche Ctrl+Alt+N/search/dashboard non la riattivano. |
| `dev/legacy/dev/ARCHITECTURE.md` | 6. se non esiste una nota o `hidden=1`: `overlay_runtime` chiude stale/non-target e non autoshow. |
| `dev/legacy/dev/ARCHITECTURE.md` | 3. `api.py` upserta `browser_tabs`, riassocia eventuali note per `normalized_url`, non crea note vuote e aggiorna `metadata.active_browser_tab`. |
| `dev/legacy/dev/ARCHITECTURE.md` | 5. `ACTIVE` indica finestra/tab live; `CLOSED` indica finestra X11 non viva; `STALE` indica tab Chrome non nello snapshot live; `HISTORY` indica contesti non runtime. La search default include solo `ACTIVE`; `--history` include  |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
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
| `system/windowtabnotes/active_watch.py` | snap.as_dict(), |
| `system/windowtabnotes/active_watch.py` | "active_window": snap.as_dict(), |
| `system/windowtabnotes/active_watch.py` | return {"window_id": snap.window_id, "own_window": True} |
| `system/windowtabnotes/active_watch.py` | return {"window_id": snap.window_id, "transient": True} |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/dev/TEST_PLAN.md: - durante cambi focus rapidi, il servizio `windowtabnotes.service` non deve riavviarsi; "nessuna finestra attiva" deve restare evento transitorio, non crash.
- dev/legacy/docs/USO_QUOTIDIANO.md: - se resta uno stato sporco dopo crash/test, `system/bin/windowtabnotes overlay-cleanup` chiude overlay stale e lascia massimo un overlay
- system/windowtabnotes/db.py: conn = sqlite3.connect(str(target), timeout=0.75)
- system/windowtabnotes/native_debug.py: timeout=5,
- system/windowtabnotes/native_host.py: timeout=2,
- system/windowtabnotes/windows.py: result = subprocess.run(args, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
- system/windowtabnotes/windows.py: except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as error:

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Versione corrente: vedere `system/bin/windowtabnotes version`. |
| `dev/legacy/docs/README_UTENTE.md` | Versione: vedere `system/bin/windowtabnotes version`. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Manifest Chrome richiede `version` statico. La fonte di verità prodotto resta `system/windowtabnotes/version.py`; manifest e docs vanno sincronizzati quando cambia la versione. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Search data invariant: backend e debug devono garantire che ogni risultato di query non vuota contenga la query case-insensitive in `notes.text`. Titolo finestra, app, URL, workspace e tab metadata sono solo display/attivazion |
| `dev/legacy/dev/AGENT_RULES.md` | - non spostare la versione da `system/windowtabnotes/version.py`. |
| `dev/legacy/dev/TEST_PLAN.md` | system/bin/windowtabnotes version |
| `dev/legacy/dev/BUG_REGISTRY.md` | - il salvataggio layout da resize/move avviene solo se la geometry e valida: interi parseabili, dimensioni almeno 16x8 px e posizione non completamente fuori schermo. |
| `system/windowtabnotes/db.py` | def get_schema_version(conn: sqlite3.Connection) -> int: |
| `system/windowtabnotes/db.py` | def ensure_app_profile(conn: sqlite3.Connection, app_id: str, display_name: str / None = None) -> sqlite3.Row: |
| `system/windowtabnotes/db.py` | def app_display_name(profile: sqlite3.Row / dict[str, Any] / None, fallback: str = "Application") -> str: |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/docs/README_UTENTE.md` | - un solo database SQLite |
| `dev/legacy/dev/INDEX.md` | - `browser-extension/content_script.js`: solo cleanup UI legacy Chrome. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Chrome: il service worker invia eventi tab al Native Messaging host su create/update/activate/window-focus. Le note browser sono nel database SQLite, non in un database browser separato. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Linux -> Chrome tab focus non apre URI browser o pagine ponte. `rofi.py`/dashboard accodano una richiesta SQLite `chrome_focus_request`; `service_worker.js` la consuma via Native Messaging polling e usa `chrome.tabs.update`/`c |
| `dev/legacy/dev/ARCHITECTURE.md` | - Overlay invariant: prima di qualunque autoshow/manual open viene preso `overlay.lock`, vengono chiusi gli overlay `open-note` non correnti, poi viene mostrato solo il target. `overlay-debug --fix` e `overlay-cleanup` riparano  |
| `dev/legacy/dev/ARCHITECTURE.md` | - Search UI invariant: Rofi usa tema locale largo/alto con font leggibile su Surface/XFCE; non cambiare Ctrl+Alt+P né il log `~/.cache/windowtabnotes/search-launcher.log`. |
| `dev/legacy/dev/AGENT_RULES.md` | - non creare database browser separati; `chrome.storage.local` è solo cache temporanea UI. |
| `dev/legacy/dev/AGENT_RULES.md` | - non reintrodurre post-it visuali nel content script: l'overlay unico e GTK, il content script serve solo per cleanup legacy. |
| `dev/legacy/dev/TEST_PLAN.md` | - salvare manualmente una geometry fuori schermo, con width/height <= 0 o sotto la soglia irrecuperabile 16x8 nel database di test, eseguire `overlay-debug --fix-geometry` e confermare che solo quei valori impossibili vengano ripar |
| `dev/legacy/dev/BUG_REGISTRY.md` | - `db.search_index(conn, query)` legge note non vuote e filtra case-insensitive solo su `notes.text`. |
| `dev/legacy/dev/BUG_REGISTRY.md` | - il watcher ignora il focus sull'overlay e non esegue hide/cleanup in quel caso. |
| `dev/legacy/dev/BUG_REGISTRY.md` | - il prompt iniziale non riceveva le note reali come righe Rofi, quindi la prima UI sembrava vuota anche con molte note nel database. |
| `dev/legacy/dev/BUG_REGISTRY.md` | - il launcher logga diagnostica compatta: DB path, note non vuote, candidati, match e campioni esclusi. |
| `dev/legacy/docs/INSTALLAZIONE.md` | sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq |
| `system/scripts/install.sh` | sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq |
| `system/windowtabnotes/active_watch.py` | context = db.upsert_window_context(conn, snap.as_dict()) |
| `system/windowtabnotes/db.py` | import sqlite3 |
| `system/windowtabnotes/db.py` | def connect(path: Path / None = None) -> sqlite3.Connection: |
| `system/windowtabnotes/db.py` | conn = sqlite3.connect(str(target), timeout=0.75) |
| `system/windowtabnotes/db.py` | conn.row_factory = sqlite3.Row |
| `system/windowtabnotes/db.py` | except sqlite3.OperationalError as error: |
| `system/windowtabnotes/db.py` | def migrate(conn: sqlite3.Connection) -> None: |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
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

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
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

RECENT_DECISIONS
| source | fact |
|---|---|
| `system/windowtabnotes/gtk_ui.py` | associated_context = next( |
| `system/windowtabnotes/gtk_ui.py` | context = next((entry for entry in entries if entry["context_id"] == note["context_id"] and entry["context_type"] == note["context_type"]), {}) |
| `system/windowtabnotes/rofi.py` | return next((item for item in items if item.number == number), None) |
| `system/windowtabnotes/rofi.py` | return next((item for item in items if item.label() == choice), None) |
| `system/windowtabnotes/shortcuts.py` | report["search_shortcut_label"] = _shortcut_label(next((key for key, action in selected.items() if action == "search-launcher"), "")) |
| `system/windowtabnotes/shortcuts.py` | search_key = next((key for key, _label in SEARCH_FALLBACKS if not _key_in_use(values, key, "search-launcher")), SEARCH_FALLBACKS[-1][0]) |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/dev/BUG_REGISTRY.md` | Registro sintetico per patch future Codex. Obiettivo: evitare re-analisi e regressioni su overlay, search, Chrome e Native Messaging. |
| `dev/legacy/dev/BUG_REGISTRY.md` | Invarianti future: |
| `dev/legacy/dev/ROADMAP.md` | # Roadmap |
| `dev/legacy/dev/ROADMAP.md` | Idee future: |
| `system/windowtabnotes/gtk_ui.py` | associated_context = next( |
| `system/windowtabnotes/gtk_ui.py` | context = next((entry for entry in entries if entry["context_id"] == note["context_id"] and entry["context_type"] == note["context_type"]), {}) |
| `system/windowtabnotes/rofi.py` | return next((item for item in items if item.number == number), None) |
| `system/windowtabnotes/rofi.py` | return next((item for item in items if item.label() == choice), None) |
| `system/windowtabnotes/shortcuts.py` | report["search_shortcut_label"] = _shortcut_label(next((key for key, action in selected.items() if action == "search-launcher"), "")) |
| `system/windowtabnotes/shortcuts.py` | search_key = next((key for key, _label in SEARCH_FALLBACKS if not _key_in_use(values, key, "search-launcher")), SEARCH_FALLBACKS[-1][0]) |

LEGACY_SUMMARY
- legacy_docs_read_count: 35
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/docs/README_UTENTE.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/dev/ARCHITECTURE.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/dev/TEST_PLAN.md`
- `dev/legacy/dev/BUG_REGISTRY.md`
- `dev/legacy/docs/TROUBLESHOOTING.md`
- `dev/legacy/dev/ROADMAP.md`
- `dev/legacy/dev/VERSIONING.md`
- `dev/legacy/docs/INSTALLAZIONE.md`
- `dev/legacy/docs/USO_QUOTIDIANO.md`
- `dev/legacy/system/migrations/001_schema.md`
- `browser-extension/content_script.js`
- `browser-extension/dashboard.js`
- `browser-extension/manifest.json`
- `system/scripts/install.sh`
- `system/scripts/uninstall.sh`
- `system/windowtabnotes/__init__.py`
- `system/windowtabnotes/active_watch.py`
- `system/windowtabnotes/api.py`
- `system/windowtabnotes/cli.py`
- `system/windowtabnotes/config.py`
- `system/windowtabnotes/daemon.py`
- `system/windowtabnotes/db.py`
- `system/windowtabnotes/gtk_ui.py`
- `system/windowtabnotes/logging_setup.py`
- `system/windowtabnotes/native_debug.py`
- `system/windowtabnotes/native_host.py`
- `system/windowtabnotes/overlay_runtime.py`
- `system/windowtabnotes/rofi.py`
- `system/windowtabnotes/shortcuts.py`
- `system/windowtabnotes/version.py`
- `system/windowtabnotes/windows.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../WindowTabNotes/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/windowtabnotes/overview.md)
- human_folder: [human folder](../../human/projects/windowtabnotes)
- legacy_docs: [dev/legacy](../../../WindowTabNotes/dev/legacy)
- repo_path: [repo](../../../WindowTabNotes)

OPEN_QUESTIONS
- dev/legacy/docs/USO_QUOTIDIANO.md: - se resta uno stato sporco dopo crash/test, `system/bin/windowtabnotes overlay-cleanup` chiude overlay stale e lascia massimo un overlay
- browser-extension/dashboard.js: const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSearch }).catch((error) => ({
- system/windowtabnotes/native_debug.py: return {"ok": False, "error": "host_missing"}
- system/windowtabnotes/native_debug.py: result["error"] = "missing_native_header"
