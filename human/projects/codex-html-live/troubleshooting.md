# codex-html-live Troubleshooting

## Problemi e sintomi rilevati nel codice
- codex_html_live.py:56:if path.exists() and path.read_text(encoding="utf-8", errors="replace") == content:
- codex_html_live.py:58:except OSError:
- codex_html_live.py:118:with path.open("r", encoding="utf-8", errors="replace") as handle:
- codex_html_live.py:132:except json.JSONDecodeError as exc:
- codex_html_live.py:133:return message_row("tool", "", f"JSON parse error: {exc}\n{raw[:1000]}")
- codex_html_live.py:322:except FileNotFoundError:
- codex_html_live.py:380:except Exception as exc:
- codex_html_live.py:381:print(f"codex-html-live error: {exc}", file=sys.stderr, flush=True)

## Comandi/verifiche utili trovati
- UNKNOWN: nessun comando rilevato in build/script/CI.

## Safety prima di correggere
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
