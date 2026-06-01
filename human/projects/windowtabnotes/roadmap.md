# WindowTabNotes Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
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

## Deferred Or Risky Work
- dev/legacy/dev/BUG_REGISTRY.md: - i log mostravano contese `sqlite3.OperationalError: database is locked`.
- system/windowtabnotes/db.py: LOG.warning("SQLite WAL pragma skipped while database is locked: %s", target)
- dev/legacy/docs/README_UTENTE.md: - un solo database SQLite
- dev/legacy/dev/ARCHITECTURE.md: - Chrome: il service worker invia eventi tab al Native Messaging host su create/update/activate/window-focus. Le note browser sono nel database SQLite, non in un database browser separato.
- dev/legacy/dev/ARCHITECTURE.md: - Overlay invariant: prima di qualunque autoshow/manual open viene preso `overlay.lock`, vengono chiusi gli overlay `open-note` non correnti, poi viene mostrato solo il target. `overlay-debug --fix` e `overlay-cleanup` riparano 
- dev/legacy/dev/ARCHITECTURE.md: - Search data invariant: backend e debug devono garantire che ogni risultato di query non vuota contenga la query case-insensitive in `notes.text`. Titolo finestra, app, URL, workspace e tab metadata sono solo display/attivazion
- dev/legacy/dev/ARCHITECTURE.md: 3. `api.py` upserta `browser_tabs`, riassocia eventuali note per `normalized_url`, non crea note vuote e aggiorna `metadata.active_browser_tab`.
- dev/legacy/dev/ARCHITECTURE.md: 6. Se non ci sono match, Rofi mostra "Nessun risultato" o esce pulito; non deve riempire con metadata non pertinenti.
- dev/legacy/dev/AGENT_RULES.md: - non creare database browser separati; `chrome.storage.local` è solo cache temporanea UI.
- dev/legacy/dev/TEST_PLAN.md: - salvare manualmente una geometry fuori schermo, con width/height <= 0 o sotto la soglia irrecuperabile 16x8 nel database di test, eseguire `overlay-debug --fix-geometry` e confermare che solo quei valori impossibili vengano ripar
- dev/legacy/dev/TEST_PLAN.md: - verificare che search non mostri `[window]`, note scollegate, note vuote o risultati da metadata.
- dev/legacy/dev/BUG_REGISTRY.md: - dopo la rimozione dei clamp/min-size aggressivi l'overlay non decorato risultava di fatto non ridimensionabile manualmente.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
