# MultiTimeTracker Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/archive/transient/codex log.txt` | - roadmap attiva/storica |
| `dev/legacy/dev/human/INDEX.md` | - `ROADMAP.md`: readable active/later roadmap. |
| `dev/legacy/dev/human/INDEX.md` | - `PLAYSTORE_READINESS_REPORT.md`: Play Store readiness status and pending checks. |
| `dev/legacy/dev/human/INDEX.md` | - `ROADMAP_EXPLAINED.md`: readable roadmap state. |
| `dev/legacy/dev/ai/ARCHITECTURE_LOCK.md` | Future device tests must use only the clone package and must preserve the main app. |
| `dev/legacy/dev/ai/OPERATING_RULES.md` | ## PRIORITY |
| `dev/legacy/dev/ai/BUG_REGISTRY.md` | / TCL_DEVICE / PENDING / no TCL validation device currently confirmed / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / startup_reopen_ANR / WATCH / v521 recovery/startup clone tests PASS; release/main smoke pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / exact_alarm_OEM_behavior / WATCH / v518 copy scoped; device/OEM still pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / fullscreen_policy / WATCH / v518 runtime copy scoped; store/artifact/device still pending / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / screenshot_listing_cleanliness / pending visual pass / |
| `dev/legacy/dev/ai/RISK_REGISTER.md` | / accessibility_static_sanity / pending UI pass / |
| `dev/legacy/en/Troubleshooting/Troubleshooting.md` | If it is a concrete stretch of activity, it is a session. If it is a broader phase that answers “since when,” it probably belongs in [[en/Features/Life Periods/Life Periods]]. |
| `dev/legacy/dev/ROADMAP_ACTIVE.md` | # MOVED: ROADMAP ACTIVE |
| `dev/legacy/dev/ROADMAP_ACTIVE.md` | Active roadmap status moved to `dev/ai/ROADMAP_ACTIVE.md`. |
| `dev/legacy/dev/ROADMAP_HISTORY.md` | Operational roadmap status lives in `dev/ai/ROADMAP_ACTIVE.md`. |

## Deferred Or Risky Work
- dev/legacy/en/Workflows/Common Tracking Workflows.md: Minimal use works best when paired with a small, stable tag set. It is better to track five important blocks clearly than to fail trying to capture everything.
- dev/legacy/dev/ai/TEST_GATES.md: / 524b / connectedDeviceTestAndroidTest clone / BLOCKED_BY_ANDROID_UTP; runner NoClassDefFoundError com.google.common.util.concurrent.AbstractFuture$Failure$1; no main-package reset used /
- dev/legacy/dev/BUG_REGISTRY.md: Current blocker/high/medium/low risk state moved to `dev/ai/RISK_REGISTER.md`.
- dev/legacy/dev/ai/RISK_REGISTER.md: ## BLOCKER
- dev/legacy/dev/ai/RISK_REGISTER.md: / 516 / receiver flag lint blocker fixed /
- dev/legacy/dev/ai/ROADMAP_ACTIVE.md: / connected_clone / BLOCKED_BY_ANDROID_UTP; deviceTest runner crashed with NoClassDefFoundError in com.google.common.util.concurrent.AbstractFuture$Failure$1 after local code fix /
- dev/legacy/dev/human/ROADMAP_EXPLAINED.md: - Closed the v515 static lint blocker for app-open snapshot-change receiver registration.
- dev/legacy/dev/human/CHANGELOG.md: - Fixed the remaining v515 lint blocker by registering the app-open snapshot-change receiver as not exported through AndroidX `ContextCompat`.
- dev/legacy/en/Features/Timed Sessions and Alerts.md: Timed sessions are best when the duration belongs naturally to the tag itself. Examples include focused intervals, standard breaks, review blocks, or routines with a known length. A timed tag can also choose
- dev/legacy/dev/CONTRACT.md: Product, data, UX, and locked runtime invariants moved to `dev/ai/ARCHITECTURE_LOCK.md`.
- dev/legacy/en/Interface/Chronology.md: Gaps are equally important. A gap is not necessarily a bug. It might be untracked life, forgotten capture, or a sign that the day needs reconstruction. Chronology makes those questions visible.
- dev/archive/transient/codex log.txt: - DATABASE TIME

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.
