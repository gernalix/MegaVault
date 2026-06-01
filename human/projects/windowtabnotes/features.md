# WindowTabNotes Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/dev/BUG_REGISTRY.md: ## Chrome doppia UI
- dev/legacy/dev/BUG_REGISTRY.md: ## Search launcher apre una UI vuota
- dev/legacy/docs/INSTALLAZIONE.md: sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq
- system/windowtabnotes/__init__.py: from .version import VERSION, version_label
- system/windowtabnotes/active_watch.py: from __future__ import annotations
- system/windowtabnotes/api.py: from __future__ import annotations
- system/windowtabnotes/cli.py: from __future__ import annotations
- system/windowtabnotes/config.py: from __future__ import annotations
- system/windowtabnotes/daemon.py: from __future__ import annotations
- system/windowtabnotes/db.py: from __future__ import annotations
- system/windowtabnotes/gtk_ui.py: from __future__ import annotations
- system/windowtabnotes/logging_setup.py: from __future__ import annotations
- system/windowtabnotes/native_debug.py: from __future__ import annotations
- system/windowtabnotes/native_host.py: from __future__ import annotations

## Useful Limits And Boundaries
- dev/legacy/dev/ARCHITECTURE.md: - Overlay invariant: prima di qualunque autoshow/manual open viene preso `overlay.lock`, vengono chiusi gli overlay `open-note` non correnti, poi viene mostrato solo il target. `overlay-debug --fix` e `overlay-cleanup` riparano 
- dev/legacy/dev/ARCHITECTURE.md: - Search data invariant: backend e debug devono garantire che ogni risultato di query non vuota contenga la query case-insensitive in `notes.text`. Titolo finestra, app, URL, workspace e tab metadata sono solo display/attivazion
- dev/legacy/dev/TEST_PLAN.md: - salvare manualmente una geometry fuori schermo, con width/height <= 0 o sotto la soglia irrecuperabile 16x8 nel database di test, eseguire `overlay-debug --fix-geometry` e confermare che solo quei valori impossibili vengano ripar
- dev/legacy/dev/BUG_REGISTRY.md: - `search-debug QUERY` fallisce se trova risultati in cui `QUERY` non e nel body nota.
- dev/legacy/dev/BUG_REGISTRY.md: - `overlay-debug --fix-geometry` ripara solo dimensioni <= 0, valori non parseabili o coordinate completamente fuori schermo.
- dev/legacy/dev/BUG_REGISTRY.md: - dopo la rimozione dei clamp/min-size aggressivi l'overlay non decorato risultava di fatto non ridimensionabile manualmente.
- dev/legacy/dev/BUG_REGISTRY.md: - `overlay-debug --fix-geometry` ripara solo geometry non parseabili, width/height <= 0, coordinate completamente offscreen o dimensioni irrecuperabili sotto 16x8 px; 17x9 resta valido e non viene ingrandito.
- dev/legacy/dev/BUG_REGISTRY.md: - non usare `overlay-debug --fix-geometry` per normalizzare preferenze piccole ma recuperabili dell'utente.
- dev/legacy/dev/BUG_REGISTRY.md: - il filtro resta body-only: metadati visibili non devono diventare l'unico motivo di match.
- dev/legacy/dev/BUG_REGISTRY.md: - non c'era un blocco esplicito del watcher durante una apertura manuale da search.

## Where The Feature Code Appears To Live
- `system/windowtabnotes/cli.py`
- `system/windowtabnotes/native_host.py`
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
