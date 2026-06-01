# codex-html-live Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
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

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.
