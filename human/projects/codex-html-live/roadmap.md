# codex-html-live Roadmap

## Segnali dal codice
- codex_html_live.py:315:next_cache: dict[Path, RenderedSession] = {}
- codex_html_live.py:328:next_cache[path] = cache[path]
- codex_html_live.py:336:next_cache[path] = cached_session
- codex_html_live.py:346:next_cache[path] = session
- codex_html_live.py:353:changed = atomic_write(OUTPUT_DIR / "index.html", render_index(list(next_cache.values()))) or changed
- codex_html_live.py:355:return rendered_state, changed, next_cache, render_times, last_index_render

## Debito/rischi da considerare
- codex_html_live.py:56:if path.exists() and path.read_text(encoding="utf-8", errors="replace") == content:
- codex_html_live.py:58:except OSError:
- codex_html_live.py:118:with path.open("r", encoding="utf-8", errors="replace") as handle:
- codex_html_live.py:132:except json.JSONDecodeError as exc:
- codex_html_live.py:133:return message_row("tool", "", f"JSON parse error: {exc}\n{raw[:1000]}")
- codex_html_live.py:322:except FileNotFoundError:
- codex_html_live.py:380:except Exception as exc:
- codex_html_live.py:381:print(f"codex-html-live error: {exc}", file=sys.stderr, flush=True)
- codex_html_live.py:199:@media (max-width: 720px) { .top { display: block; } th:nth-child(3), td:nth-child(3) { display: none; } .wrap { padding: 14px; } }
- codex_html_live.py:348:removed = set(previous) - set(observed)
- codex_html_live.py:349:for path in removed:
- codex_html_live.py:352:if removed or ((set(previous) != set(rendered_state) or changed or not (OUTPUT_DIR / "index.html").exists()) and index_due):
