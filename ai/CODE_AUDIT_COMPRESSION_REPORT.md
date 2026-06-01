# CODE_AUDIT_COMPRESSION_REPORT

Prompt: #604927
Generated: 2026-06-01T13:36:08+02:00
Projects analyzed: 23
Code files audited: 550 / 550
AI docs compressed: 23
Line reduction: 5633 -> 2803 (50.2%)
Word/token proxy reduction: 50046 -> 20538 (59.0%)

| slug | old_lines | new_lines | old_words | new_words | code_files | tests |
|---|---:|---:|---:|---:|---:|---:|
| supercontacts | 392 | 206 | 4250 | 2394 | 96 | 80 |
| windowtabnotes | 334 | 155 | 3341 | 1200 | 32 | 0 |
| android-sdk-auto-update | 228 | 120 | 1803 | 937 | 2 | 0 |
| aw-converter | 109 | 65 | 347 | 226 | 1 | 0 |
| chatgpt-chrome-debug | 253 | 140 | 2269 | 1120 | 12 | 0 |
| codex-html-live | 198 | 125 | 1578 | 831 | 3 | 10 |
| codex-token-watcher | 109 | 79 | 358 | 404 | 1 | 0 |
| codex-wrapper | 109 | 65 | 349 | 228 | 1 | 0 |
| facebook-video-archiver | 280 | 142 | 2545 | 953 | 6 | 0 |
| installa-app | 109 | 65 | 349 | 228 | 1 | 0 |
| linux-mint-service-dashboard | 314 | 143 | 3248 | 1095 | 11 | 11 |
| mint-manual-updates | 230 | 89 | 2298 | 561 | 5 | 0 |
| os-observer | 365 | 166 | 5082 | 1344 | 29 | 20 |
| owntracks-watcher | 109 | 65 | 349 | 228 | 1 | 0 |
| parcel-tracker | 211 | 102 | 1531 | 588 | 5 | 0 |
| multitimetracker | 513 | 198 | 5570 | 2186 | 224 | 80 |
| maintenance-486 | 195 | 77 | 1626 | 451 | 2 | 0 |
| oracle-backup-service | 297 | 148 | 3084 | 1026 | 19 | 0 |
| remote-opt-oracle-backup | 203 | 141 | 1175 | 958 | 7 | 0 |
| remote-codex-phone | 129 | 65 | 514 | 235 | 1 | 0 |
| amici-fb | 335 | 143 | 2734 | 999 | 53 | 0 |
| surface-recovery-hardening | 371 | 169 | 4037 | 1445 | 31 | 0 |
| system-watchdog | 240 | 135 | 1609 | 901 | 7 | 0 |

## New Invariant Sources
- supercontacts: inv=90, data=80, risks=70, bugs=70
- windowtabnotes: inv=90, data=80, risks=57, bugs=70
- android-sdk-auto-update: inv=9, data=10, risks=8, bugs=8
- aw-converter: inv=1, data=0, risks=0, bugs=0
- chatgpt-chrome-debug: inv=26, data=16, risks=12, bugs=38
- codex-html-live: inv=15, data=17, risks=4, bugs=8
- codex-token-watcher: inv=1, data=0, risks=5, bugs=0
- codex-wrapper: inv=1, data=0, risks=0, bugs=0
- facebook-video-archiver: inv=18, data=26, risks=17, bugs=24
- installa-app: inv=1, data=0, risks=0, bugs=0
- linux-mint-service-dashboard: inv=43, data=32, risks=24, bugs=39
- mint-manual-updates: inv=5, data=0, risks=0, bugs=2
- os-observer: inv=90, data=80, risks=70, bugs=70
- owntracks-watcher: inv=1, data=0, risks=0, bugs=0
- parcel-tracker: inv=9, data=10, risks=0, bugs=9
- multitimetracker: inv=90, data=80, risks=70, bugs=70
- maintenance-486: inv=5, data=0, risks=0, bugs=5
- oracle-backup-service: inv=79, data=80, risks=41, bugs=49
- remote-opt-oracle-backup: inv=40, data=45, risks=23, bugs=20
- remote-codex-phone: inv=1, data=0, risks=0, bugs=0
- amici-fb: inv=50, data=63, risks=39, bugs=54
- surface-recovery-hardening: inv=90, data=65, risks=70, bugs=70
- system-watchdog: inv=8, data=12, risks=7, bugs=14

## Open Questions
- windowtabnotes: code_files=32, tests_detected=0; keep UNKNOWN where evidence is thin.
- android-sdk-auto-update: code_files=2, tests_detected=0; keep UNKNOWN where evidence is thin.
- aw-converter: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- chatgpt-chrome-debug: code_files=12, tests_detected=0; keep UNKNOWN where evidence is thin.
- codex-token-watcher: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- codex-wrapper: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- facebook-video-archiver: code_files=6, tests_detected=0; keep UNKNOWN where evidence is thin.
- installa-app: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- mint-manual-updates: code_files=5, tests_detected=0; keep UNKNOWN where evidence is thin.
- owntracks-watcher: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- parcel-tracker: code_files=5, tests_detected=0; keep UNKNOWN where evidence is thin.
- maintenance-486: code_files=2, tests_detected=0; keep UNKNOWN where evidence is thin.
- oracle-backup-service: code_files=19, tests_detected=0; keep UNKNOWN where evidence is thin.
- remote-opt-oracle-backup: code_files=7, tests_detected=0; keep UNKNOWN where evidence is thin.
- remote-codex-phone: code_files=1, tests_detected=0; keep UNKNOWN where evidence is thin.
- amici-fb: code_files=53, tests_detected=0; keep UNKNOWN where evidence is thin.
- surface-recovery-hardening: code_files=31, tests_detected=0; keep UNKNOWN where evidence is thin.
- system-watchdog: code_files=7, tests_detected=0; keep UNKNOWN where evidence is thin.

## Validation Targets
- AI format META/PURPOSE/STACK/MAP/ARCH/FLOW/INV/BUILD/TEST/DATA/DNB/BUG/RISK/ROAD/LINK/OPEN
- active code map excludes dev/legacy and .codex_patch snapshots
- BUILD commands limited to build/script/CI/tool files
- long MAP lines wrapped into repeated key=value rows
- no project code/db/build touched
- Human docs rewritten with code-audit orientation

## Validation Result
- PASS: 23 AI docs use compact required section set.
- PASS: each AI doc has INV, DNB, BUILD, TEST, DATA, ROAD, LINK, OPEN.
- PASS: markdown links and metadata targets resolve.
- PASS: long AI lines over 180 chars = 0 after MAP wrapping.
- PASS: active code map excludes `dev/legacy/` and `.codex_patch_*` snapshots.
- PASS: no build executed; no project code or database files modified by this prompt.
- NOTE: current project repos still have unrelated preexisting dirty files; they were not staged or committed here.
- NOTE: untracked `ai/MEGAVAULT_PROTOCOL.md` was left uncommitted because it was not produced by this audit.
