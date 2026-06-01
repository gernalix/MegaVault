# codex-html-live Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: ## Quick Use
- dev/legacy/README.md: ## Commands
- dev/legacy/README.md: Live HTML archive for Codex JSONL sessions without tmux.
- dev/legacy/dev/CHANGELOG.md: - Fixed dashboard UX so session IDs and an explicit `Open` column link to chat HTML files, with full-row hover and pointer affordance.
- codex_html_live.py: from dataclasses import dataclass, field

## Useful Limits And Boundaries
- dev/legacy/README.md: - Original Codex sessions, read-only: `~/.codex/sessions/**/*.jsonl`
- dev/legacy/README.md: Generated HTML and Codex JSONL session files are not source files and must not be committed.
- dev/legacy/dev/ARCHITECTURE.md: - Original JSONL files are opened read-only by the daemon.
- dev/legacy/dev/ARCHITECTURE.md: Do not edit or commit:
- dev/legacy/dev/AGENT_RULES.md: ## Safety
- dev/legacy/dev/AGENT_RULES.md: - Treat `~/.codex/sessions/**/*.jsonl` as source data owned by Codex. The daemon must only read those files.
- dev/legacy/dev/AGENT_RULES.md: - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data.
- dev/legacy/dev/AGENT_RULES.md: - Keep the project portable. Do not hardcode `/home/daniele` in source files; resolve paths at runtime with `Path.home()`.
- dev/legacy/dev/AGENT_RULES.md: - Avoid heavy mandatory dependencies. The default path must work with Python 3 standard library and systemd user services.
- dev/legacy/dev/AGENT_RULES.md: - The daemon must detect new JSONL files after startup without manual intervention.
- dev/legacy/dev/AGENT_RULES.md: - The daemon must refresh changed session HTML and the index automatically.
- dev/legacy/dev/AGENT_RULES.md: - Low CPU/I/O behavior: do not reread unchanged JSONL files in every poll, debounce changed active sessions, and avoid rewriting identical HTML.

## Where The Feature Code Appears To Live
- `codex_html_live.py`
- `tests/test_codex_html_live.py`
