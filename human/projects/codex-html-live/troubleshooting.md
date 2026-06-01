# codex-html-live Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `dev/legacy/dev/AGENT_RULES.md` | ## Regression Areas |
| `dev/legacy/dev/TEST_PLAN.md` | ## Permission Regression Test |
| `codex_html_live.py` | return message_row("tool", "", f"JSON parse error: {exc}\n{raw[:1000]}") |
| `codex_html_live.py` | print(f"codex-html-live error: {exc}", file=sys.stderr, flush=True) |

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/legacy/README.md` | python3 codex_html_live.py install |
| `dev/legacy/README.md` | systemctl --user is-active codex-html-live.service |
| `dev/legacy/README.md` | journalctl --user -u codex-html-live.service -n 80 --no-pager |
| `dev/legacy/dev/ARCHITECTURE.md` | systemctl --user status codex-html-live.service |
| `dev/legacy/dev/ARCHITECTURE.md` | journalctl --user -u codex-html-live.service -n 120 --no-pager |
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m py_compile codex_html_live.py |
| `dev/legacy/dev/TEST_PLAN.md` | python3 codex_html_live.py install |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user is-active codex-html-live.service |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user status codex-html-live.service --no-pager |
| `dev/legacy/dev/TEST_PLAN.md` | journalctl --user -u codex-html-live.service -n 120 --no-pager |
| `codex_html_live.py` | #!/usr/bin/env python3 |
| `codex_html_live.py` | wrapper.write_text(f"#!/bin/sh\nexec /usr/bin/env python3 {Path(__file__).resolve()} \"$@\"\n", encoding="utf-8") |

## Safety Checks Before Fixing
- dev/legacy/README.md: - Original Codex sessions, read-only: `~/.codex/sessions/**/*.jsonl`
- dev/legacy/README.md: Generated HTML and Codex JSONL session files are not source files and must not be committed.
- dev/legacy/dev/ARCHITECTURE.md: - Original JSONL files are opened read-only by the daemon.
- dev/legacy/dev/ARCHITECTURE.md: Do not edit or commit:
- dev/legacy/dev/AGENT_RULES.md: ## Safety
- dev/legacy/dev/AGENT_RULES.md: - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data.
- dev/legacy/dev/AGENT_RULES.md: - Keep the project portable. Do not hardcode `/home/daniele` in source files; resolve paths at runtime with `Path.home()`.
- dev/legacy/dev/AGENT_RULES.md: - Low CPU/I/O behavior: do not reread unchanged JSONL files in every poll, debounce changed active sessions, and avoid rewriting identical HTML.
- dev/legacy/dev/AGENT_RULES.md: - Use clear commit messages that describe the operator-visible change.
- codex_html_live.py: <meta name="viewport" content="width=device-width, initial-scale=1">
