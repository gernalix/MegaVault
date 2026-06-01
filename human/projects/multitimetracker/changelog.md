# MultiTimeTracker Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
| source | fact |
|---|---|
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | # RELEASE_PROTOCOL |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | ## LOCAL_GATES |
| `dev/legacy/dev/ai/RELEASE_PROTOCOL.md` | ## DEVICE_GATES |
| `dev/legacy/dev/ROADMAP_HISTORY.md` | # MOVED: HUMAN CHANGELOG |
| `dev/legacy/dev/ai/ROADMAP_HISTORY.md` | # ROADMAP_HISTORY |
| `dev/legacy/dev/ai/ROADMAP_HISTORY.md` | ## RECENT_PATCHES |
| `dev/legacy/dev/human/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/human/CHANGELOG.md` | ## v525 |
| `dev/legacy/dev/human/CHANGELOG.md` | - Improved SQLite/runtime performance with query-aligned indexes for sessions, audit events, and Events tables. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Events now refreshes screen data progressively while full exports still read the complete Events state from SQLite. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Made the Events tab denser by removing the redundant intro block, tightening action buttons, and collapsing recent entries by default. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Extended the app report with app version, DB version, active DB path, DB size, core table counts, and backup/import context. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Hardened the backup policy so vault switching/export paths no longer create retained timestamped SQLite autoexports. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Completed the `dev/ai/*` and `dev/human/*` dual-doc structure requested by prompt #581943. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Bumped patch version from `524` to `525`. |
| `dev/legacy/dev/human/CHANGELOG.md` | ## v523 |
| `dev/legacy/dev/human/CHANGELOG.md` | - Renamed the quick-events experience to `Events` / `Eventi`. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Added quick actions with timestamp-only entries, custom fields, and macros that can record multiple actions with the same timestamp. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Moved tag filters behind a collapsed `Filters` control so tags no longer dominate the Events tab on open. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Added unified Timeline markers for event entries and derived session `START` / `STOP` markers without splitting session DB rows. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Extended backup/import/export and SQLite persistence for action fields, field values, macros, macro relations, and entries while preserving v522 data compatibility. |
| `dev/legacy/dev/human/CHANGELOG.md` | - Bumped patch version from `522` to `523`. |
| `dev/legacy/dev/human/CHANGELOG.md` | - `testDebugUnitTest`, `assembleDebug`, hardcoded-string check, Pixel DB tests, Pixel import/export test, and Pixel smoke passed. |
| `dev/legacy/dev/human/CHANGELOG.md` | ## v522 |

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.
