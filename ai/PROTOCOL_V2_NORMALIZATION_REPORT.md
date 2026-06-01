# PROTOCOL_V2_NORMALIZATION_REPORT

prompt=#906417
generated_at=2026-06-01T13:59:53+02:00
protocol=MegaVault/ai/MEGAVAULT_PROTOCOL.md VERSION=2
projects_processed=23
ai_docs_normalized=23
line_reduction=2803->1951 (30.4%)
token_proxy_word_reduction=8365->4726 (43.5%)
scope=MegaVault AI docs only; no app code/DB/build touched

## Per Project
| slug | before_lines | after_lines | before_words | after_words | missing_before | missing_after | open |
|---|---:|---:|---:|---:|---|---|---|
| supercontacts | 206 | 99 | 542 | 275 | none | none | none |
| windowtabnotes | 155 | 98 | 464 | 241 | none | none | tests=UNKNOWN_OR_ABSENT |
| android-sdk-auto-update | 120 | 83 | 539 | 241 | none | none | tests=UNKNOWN_OR_ABSENT |
| aw-converter | 65 | 75 | 126 | 96 | none | none | purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| chatgpt-chrome-debug | 140 | 92 | 558 | 271 | none | none | tests=UNKNOWN_OR_ABSENT |
| codex-html-live | 125 | 76 | 431 | 223 | none | none | none |
| codex-token-watcher | 79 | 83 | 164 | 128 | none | none | purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| codex-wrapper | 65 | 75 | 126 | 96 | none | none | purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| facebook-video-archiver | 142 | 78 | 468 | 198 | none | none | tests=UNKNOWN_OR_ABSENT |
| installa-app | 65 | 75 | 126 | 96 | none | none | purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| linux-mint-service-dashboard | 143 | 93 | 410 | 207 | none | none | none |
| mint-manual-updates | 89 | 78 | 202 | 116 | none | none | tests=UNKNOWN_OR_ABSENT |
| os-observer | 166 | 96 | 593 | 418 | none | none | none |
| owntracks-watcher | 65 | 75 | 126 | 96 | none | none | purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| parcel-tracker | 102 | 79 | 268 | 169 | none | none | tests=UNKNOWN_OR_ABSENT |
| multitimetracker | 198 | 99 | 483 | 342 | none | none | none |
| maintenance-486 | 77 | 76 | 255 | 209 | none | none | tests=UNKNOWN_OR_ABSENT |
| oracle-backup-service | 148 | 91 | 378 | 220 | none | none | tests=UNKNOWN_OR_ABSENT |
| remote-opt-oracle-backup | 141 | 89 | 444 | 206 | none | none | tests=UNKNOWN_OR_ABSENT |
| remote-codex-phone | 65 | 74 | 128 | 97 | none | none | tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN |
| amici-fb | 143 | 93 | 446 | 339 | none | none | tests=UNKNOWN_OR_ABSENT |
| surface-recovery-hardening | 169 | 95 | 667 | 299 | none | none | tests=UNKNOWN_OR_ABSENT |
| system-watchdog | 135 | 79 | 421 | 143 | none | none | tests=UNKNOWN_OR_ABSENT |

## Compliance Checks
required_sections=META,PURPOSE,STACK,MAP,ARCH,FLOW,INV,BUILD,TEST,DATA,DNB,BUG,RISK,ROAD,LINK,OPEN
inv_required_keys=arch,data,ux,backup,migration,version,i18n,security,perf
data_required_keys=db,paths,backup,restore,import,export,migration,retention
format=section headers + key=value lines; no markdown prose in project AI docs

## Open Questions
- windowtabnotes: tests=UNKNOWN_OR_ABSENT
- android-sdk-auto-update: tests=UNKNOWN_OR_ABSENT
- aw-converter: purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- chatgpt-chrome-debug: tests=UNKNOWN_OR_ABSENT
- codex-token-watcher: purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- codex-wrapper: purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- facebook-video-archiver: tests=UNKNOWN_OR_ABSENT
- installa-app: purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- mint-manual-updates: tests=UNKNOWN_OR_ABSENT
- owntracks-watcher: purpose=UNKNOWN, tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- parcel-tracker: tests=UNKNOWN_OR_ABSENT
- maintenance-486: tests=UNKNOWN_OR_ABSENT
- oracle-backup-service: tests=UNKNOWN_OR_ABSENT
- remote-opt-oracle-backup: tests=UNKNOWN_OR_ABSENT
- remote-codex-phone: tests=UNKNOWN_OR_ABSENT, flows=UNKNOWN
- amici-fb: tests=UNKNOWN_OR_ABSENT
- surface-recovery-hardening: tests=UNKNOWN_OR_ABSENT
- system-watchdog: tests=UNKNOWN_OR_ABSENT

## Link Validation
status=PASS; ai_docs=23; errors=0; warnings=0
