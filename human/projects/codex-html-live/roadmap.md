# codex-html-live Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/README.md` | - `dev/AGENT_RULES.md`: binding rules for future Codex work. |
| `dev/legacy/dev/AGENT_RULES.md` | These rules are binding for future Codex sessions working on this project. |

## Deferred Or Risky Work
- dev/legacy/dev/ARCHITECTURE.md: All dynamic content is HTML-escaped. Tool output is rendered in `<pre>` blocks to preserve stdout/stderr formatting.
- dev/legacy/dev/AGENT_RULES.md: - Treat `~/.codex/sessions/**/*.jsonl` as source data owned by Codex. The daemon must only read those files.
- dev/legacy/dev/AGENT_RULES.md: - Do not commit Codex JSONL sessions, generated HTML output, logs, credentials, or private runtime data.
- dev/legacy/dev/AGENT_RULES.md: - The daemon must detect new JSONL files after startup without manual intervention.
- dev/legacy/dev/CHANGELOG.md: - Added live polling of `~/.codex/sessions/**/*.jsonl` with metadata caching to avoid reparsing unchanged sessions.
- codex_html_live.py: <meta name="viewport" content="width=device-width, initial-scale=1">

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
