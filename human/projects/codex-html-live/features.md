# codex-html-live Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `codex_html_live.py`: RenderedSession, iso_from_mtime, safe_name, ensure_output_dir, atomic_write, text_from_content, short_json, message_row
- `tests/test_codex_html_live.py`: CodexHtmlLiveTests

## Confini operativi
- codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }
- codex_html_live.py:348:removed = set(previous) - set(observed)
- codex_html_live.py:349:for path in removed:
- codex_html_live.py:352:if removed or ((set(previous) != set(rendered_state) or changed or not (OUTPUT_DIR / "index.html").exists()) and index_due):
- codex_html_live.py:44:def safe_name(value: str) -> str:
- codex_html_live.py:94:role_class = safe_name(role.lower())
- codex_html_live.py:109:html_path=OUTPUT_DIR / f"{safe_name(fallback_id)}.html",
- codex_html_live.py:145:session.html_path = OUTPUT_DIR / f"{safe_name(session.session_id)}.html"
- codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }
- codex_html_live.py:331:target = cached_session.html_path if cached_session else OUTPUT_DIR / f"{safe_name(path.stem)}.html"
- dev/project.metadata.json:9:"metadata_version": 1,
- preserve metadata, dev/legacy, AI/Human links; no code/DB edits for doc tasks
