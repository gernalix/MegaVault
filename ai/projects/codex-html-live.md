# codex-html-live AI OPERATIONS

PROJECT
- name: codex-html-live
- slug: codex-html-live
- purpose: Live HTML archive for Codex JSONL sessions: watches session files and renders browser-readable chat archives without relying on tmux.
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/codex-html-live`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `1e8ecaa` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- `codex_html_live.py`
important_folders:
- `dev`
- `tests`
important_files:
- `dev/README.md`
tests:
- `tests/test_codex_html_live.py`
scripts:
- `codex_html_live.py`
- `tests/test_codex_html_live.py`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Live HTML archive for Codex JSONL sessions without tmux.
- dev/legacy/dev/ARCHITECTURE.md: - `codex_html_live.py`: Python standard-library CLI, renderer, daemon loop, installer.
- dev/legacy/dev/AGENT_RULES.md: These rules are binding for future Codex sessions working on this project.
- dev/legacy/dev/TEST_PLAN.md: python3 -m py_compile codex_html_live.py
- dev/legacy/dev/CHANGELOG.md: - Fixed dashboard UX so session IDs and an explicit `Open` column link to chat HTML files, with full-row hover and pointer affordance.
- codex_html_live.py: from dataclasses import dataclass, field
- tests/test_codex_html_live.py: ROOT = Path(__file__).resolve().parents[1]
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # codex-html-live |
| `dev/legacy/README.md` | ## Quick Use |
| `dev/legacy/README.md` | ## What It Watches And Writes |
| `dev/legacy/README.md` | ## Install |
| `dev/legacy/README.md` | ## Commands |
| `dev/legacy/README.md` | ## Verify |
| `dev/legacy/README.md` | ## Troubleshooting |
| `dev/legacy/README.md` | ## Source Files |
| `dev/legacy/dev/ARCHITECTURE.md` | # Architecture |
| `dev/legacy/dev/ARCHITECTURE.md` | ## Components |
| `dev/legacy/dev/ARCHITECTURE.md` | ## Data Flow |
| `dev/legacy/dev/ARCHITECTURE.md` | ## JSONL Rendering |
| `dev/legacy/dev/ARCHITECTURE.md` | ## systemd |
| `dev/legacy/dev/ARCHITECTURE.md` | ## Security |
| `dev/legacy/dev/ARCHITECTURE.md` | ## Generated Files |
| `dev/legacy/dev/AGENT_RULES.md` | # Agent Rules |
| `dev/legacy/dev/AGENT_RULES.md` | ## Safety |
| `dev/legacy/dev/AGENT_RULES.md` | ## Operational Contract |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - Original Codex sessions, read-only: `~/.codex/sessions/**/*.jsonl` |
| `dev/legacy/README.md` | Generated HTML and Codex JSONL session files are not source files and must not be committed. |
| `dev/legacy/dev/ARCHITECTURE.md` | All dynamic content is HTML-escaped. Tool output is rendered in `<pre>` blocks to preserve stdout/stderr formatting. |
| `dev/legacy/dev/ARCHITECTURE.md` | - Original JSONL files are opened read-only by the daemon. |
| `dev/legacy/dev/ARCHITECTURE.md` | Do not edit or commit: |
| `dev/legacy/dev/AGENT_RULES.md` | ## Safety |
| `dev/legacy/dev/AGENT_RULES.md` | - Treat `~/.codex/sessions/**/*.jsonl` as source data owned by Codex. The daemon must only read those files. |
| `dev/legacy/dev/AGENT_RULES.md` | - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data. |
| `dev/legacy/dev/AGENT_RULES.md` | - Keep the project portable. Do not hardcode `/home/daniele` in source files; resolve paths at runtime with `Path.home()`. |
| `dev/legacy/dev/AGENT_RULES.md` | - Avoid heavy mandatory dependencies. The default path must work with Python 3 standard library and systemd user services. |
| `dev/legacy/dev/AGENT_RULES.md` | - The daemon must detect new JSONL files after startup without manual intervention. |
| `dev/legacy/dev/AGENT_RULES.md` | - The daemon must refresh changed session HTML and the index automatically. |
| `dev/legacy/dev/AGENT_RULES.md` | When editing, explicitly protect: |
| `dev/legacy/dev/AGENT_RULES.md` | - Low CPU/I/O behavior: do not reread unchanged JSONL files in every poll, debounce changed active sessions, and avoid rewriting identical HTML. |
| `dev/legacy/dev/AGENT_RULES.md` | - Use clear commit messages that describe the operator-visible change. |
| `dev/legacy/dev/CHANGELOG.md` | - Added live polling of `~/.codex/sessions/**/*.jsonl` with metadata caching to avoid reparsing unchanged sessions. |
| `codex_html_live.py` | <meta name="viewport" content="width=device-width, initial-scale=1"> |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
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
test_targets:
- `tests/test_codex_html_live.py`
known_test_flakiness_or_requirements:
- dev/legacy/dev/TEST_PLAN.md: ## Permission Regression Test

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Generated HTML and Codex JSONL session files are not source files and must not be committed. |
| `dev/legacy/dev/ARCHITECTURE.md` | All dynamic content is HTML-escaped. Tool output is rendered in `<pre>` blocks to preserve stdout/stderr formatting. |
| `dev/legacy/dev/ARCHITECTURE.md` | Do not edit or commit: |
| `dev/legacy/dev/AGENT_RULES.md` | - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data. |
| `dev/legacy/dev/AGENT_RULES.md` | - Use clear commit messages that describe the operator-visible change. |
| `dev/legacy/dev/CHANGELOG.md` | - Added strict generated-output permissions: output directory `700`, HTML files `600`. |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/dev/AGENT_RULES.md` | - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data. |
| `dev/legacy/dev/CHANGELOG.md` | - Added live polling of `~/.codex/sessions/**/*.jsonl` with metadata caching to avoid reparsing unchanged sessions. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/dev/AGENT_RULES.md` | ## Regression Areas |
| `dev/legacy/dev/TEST_PLAN.md` | ## Permission Regression Test |
| `codex_html_live.py` | return message_row("tool", "", f"JSON parse error: {exc}\n{raw[:1000]}") |
| `codex_html_live.py` | print(f"codex-html-live error: {exc}", file=sys.stderr, flush=True) |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: Generated HTML and Codex JSONL session files are not source files and must not be committed.
- dev/legacy/dev/ARCHITECTURE.md: All dynamic content is HTML-escaped. Tool output is rendered in `<pre>` blocks to preserve stdout/stderr formatting.
- dev/legacy/dev/ARCHITECTURE.md: Do not edit or commit:
- dev/legacy/dev/AGENT_RULES.md: ## Safety
- dev/legacy/dev/AGENT_RULES.md: - Treat `~/.codex/sessions/**/*.jsonl` as source data owned by Codex. The daemon must only read those files.
- dev/legacy/dev/AGENT_RULES.md: - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data.
- dev/legacy/dev/AGENT_RULES.md: - Keep the project portable. Do not hardcode `/home/daniele` in source files; resolve paths at runtime with `Path.home()`.
- dev/legacy/dev/AGENT_RULES.md: - Avoid heavy mandatory dependencies. The default path must work with Python 3 standard library and systemd user services.
- dev/legacy/dev/AGENT_RULES.md: - The daemon must detect new JSONL files after startup without manual intervention.
- dev/legacy/dev/AGENT_RULES.md: - The daemon must refresh changed session HTML and the index automatically.
- dev/legacy/dev/AGENT_RULES.md: When editing, explicitly protect:
- dev/legacy/dev/AGENT_RULES.md: - Low CPU/I/O behavior: do not reread unchanged JSONL files in every poll, debounce changed active sessions, and avoid rewriting identical HTML.
- dev/legacy/dev/CHANGELOG.md: - Added live polling of `~/.codex/sessions/**/*.jsonl` with metadata caching to avoid reparsing unchanged sessions.

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/CHANGELOG.md` | ## 2026-05-10 |
| `dev/legacy/dev/CHANGELOG.md` | - Fixed dashboard UX so session IDs and an explicit `Open` column link to chat HTML files, with full-row hover and pointer affordance. |
| `dev/legacy/dev/CHANGELOG.md` | - Created `codex_html_live.py` with daemon, renderer, CLI, installer, and systemd user-service support. |
| `dev/legacy/dev/CHANGELOG.md` | - Added live polling of `~/.codex/sessions/**/*.jsonl` with metadata caching to avoid reparsing unchanged sessions. |
| `dev/legacy/dev/CHANGELOG.md` | - Added dark HTML session pages with user, assistant, and tool separation. |
| `dev/legacy/dev/CHANGELOG.md` | - Added live `index.html` sorted by recent activity. |
| `dev/legacy/dev/CHANGELOG.md` | - Added strict generated-output permissions: output directory `700`, HTML files `600`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added codex-friendly project documentation and Git ignore rules. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - `dev/AGENT_RULES.md`: binding rules for future Codex work. |
| `dev/legacy/dev/AGENT_RULES.md` | These rules are binding for future Codex sessions working on this project. |

LEGACY_SUMMARY
- legacy_docs_read_count: 8
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/dev/ARCHITECTURE.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/dev/TEST_PLAN.md`
- `dev/legacy/dev/CHANGELOG.md`
- `codex_html_live.py`
- `tests/test_codex_html_live.py`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../codex-html-live/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/codex-html-live/overview.md)
- human_folder: [human folder](../../human/projects/codex-html-live)
- legacy_docs: [dev/legacy](../../../codex-html-live/dev/legacy)
- repo_path: [repo](../../../codex-html-live)

OPEN_QUESTIONS
- none detected in extracted sources
