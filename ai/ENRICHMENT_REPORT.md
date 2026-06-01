# ENRICHMENT_REPORT

Prompt: #842915
Generated: 2026-06-01T13:20:29+02:00
Projects analyzed: 23
Projects enriched: 23
AI files updated: 23
Human files updated/created: 115
Legacy/source files read: 426
Projects with insufficient information: 5

## Quality Summary
| slug | sources_read | commands | invariants | bugs | roadmap | source_quality |
|---|---:|---:|---:|---:|---:|---|
| supercontacts | 36 | 70 | 89 | 22 | 14 | OK |
| windowtabnotes | 35 | 70 | 89 | 55 | 10 | OK |
| android-sdk-auto-update | 7 | 14 | 30 | 12 | 6 | OK |
| aw-converter | 1 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| chatgpt-chrome-debug | 17 | 18 | 22 | 25 | 0 | OK |
| codex-html-live | 8 | 12 | 17 | 4 | 2 | OK |
| codex-token-watcher | 1 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| codex-wrapper | 1 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| facebook-video-archiver | 12 | 38 | 67 | 6 | 0 | OK |
| installa-app | 1 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| linux-mint-service-dashboard | 18 | 14 | 89 | 46 | 6 | OK |
| mint-manual-updates | 7 | 22 | 39 | 10 | 0 | OK |
| os-observer | 38 | 70 | 89 | 70 | 70 | OK |
| owntracks-watcher | 1 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| parcel-tracker | 7 | 13 | 14 | 15 | 2 | OK |
| multitimetracker | 140 | 70 | 89 | 70 | 63 | OK |
| maintenance-486 | 3 | 2 | 37 | 5 | 1 | OK |
| oracle-backup-service | 11 | 70 | 89 | 36 | 4 | OK |
| remote-opt-oracle-backup | 6 | 6 | 21 | 2 | 0 | OK |
| remote-codex-phone | 4 | 2 | 0 | 0 | 0 | OK |
| amici-fb | 17 | 50 | 49 | 47 | 6 | OK |
| surface-recovery-hardening | 43 | 70 | 89 | 70 | 13 | OK |
| system-watchdog | 12 | 27 | 22 | 13 | 0 | OK |

## Insufficient Projects
- aw-converter: thin source corpus; AI/Human docs contain UNKNOWN/OPEN QUESTION where facts were missing.
- codex-token-watcher: thin source corpus; AI/Human docs contain UNKNOWN/OPEN QUESTION where facts were missing.
- codex-wrapper: thin source corpus; AI/Human docs contain UNKNOWN/OPEN QUESTION where facts were missing.
- installa-app: thin source corpus; AI/Human docs contain UNKNOWN/OPEN QUESTION where facts were missing.
- owntracks-watcher: thin source corpus; AI/Human docs contain UNKNOWN/OPEN QUESTION where facts were missing.

## Validation Targets
- one AI file per project
- human overview/features/roadmap/changelog/troubleshooting per project
- AI->Human/metadata/legacy/repo links present
- Human overview->AI/metadata/legacy/repo links present
- indexes link AI/Human/metadata
- no project repo writes required for enrichment

## Validation Result
- PASS: 23 AI docs present and non-skeletal.
- PASS: 23 Human project folders include overview/features/roadmap/changelog/troubleshooting.
- PASS: bidirectional AI/Human/metadata/legacy/repo links exist and resolve.
- PASS: metadata targets exist.
- PASS: no project repo documentation entrypoint or legacy paths changed during enrichment.
- PASS: no build executed; no database or application code modified for this prompt.
