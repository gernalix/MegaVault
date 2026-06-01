# amici_fb Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/docs/OPERATIONS.md` | Status and next run: |
| `dev/legacy/docs/OPERATIONS.md` | - `amici_fb.timer`: `active (waiting)`, next trigger shown. |
| `amici_fb.py` | status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending','accepted','rejected','unknown')), |
| `amici_fb.py` | - pending/unknown + ora tra amici -> accepted (+accepted_at) |
| `amici_fb.py` | WHERE status IN ('pending','unknown') |
| `amici_fb.py` | status = (r["status"] or "pending").strip() |

## Deferred Or Risky Work
- dev/legacy/docs/TROUBLESHOOTING.md: ## SQLite or Data Path Issue
- dev/legacy/docs/OPERATIONS.md: ## Success and Failure Signals
- dev/legacy/AGENTS.md: - `data/browser_diag_*`: failure evidence and screenshots/HTML from Playwright.
- dev/legacy/docs/ARCHITECTURE.md: - `amici_fb.sqlite3`: SQLite history database in the project root when present.
- dev/legacy/docs/ARCHITECTURE.md: 11. Close page/context/browser/database in `finally`.
- dev/legacy/docs/TROUBLESHOOTING.md: Symptom: database errors, missing CSVs, or no previous snapshot found.
- dev/legacy/docs/TROUBLESHOOTING.md: Fix: preserve the database and CSVs; use `AMICI_FB_DB` only for an explicit test
- dev/legacy/docs/TROUBLESHOOTING.md: database:

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
