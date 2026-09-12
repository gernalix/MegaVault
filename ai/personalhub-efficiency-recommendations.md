# PersonalHub execution and delivery efficiency

Status: design/operating decisions accepted 2026-09-12. This document records cross-repo recommendations that should remain stable across future PersonalHub work.

## Activity Register

Remote PersonalHub now incorporates the following hardening directly in code:

- row snapshots are retained automatically only when an activity is reversible (or explicitly opts in), avoiding full before/after payload growth for non-reversible canonical rows;
- stale Undo outcomes caused by a missing/changed canonical row or missing People event/contact are persisted as `CONFLICT`, so the UI does not keep offering Undo after the conflict is known;
- member-only episode activity receives the real host app version through `HubContextRuntime` instead of hardcoded `0`;
- regression tests cover missing-row stale conflict and absence of snapshots on non-reversible episode activity.

Future work should extend automatic regression coverage before adding manual Android flows. Manual device QA should prove only behavior that unit/integration tests cannot prove.

## PersonalHub serialization

PersonalHub development is serial by default. Do not run independent PersonalHub implementation/release tasks concurrently against `main`. In particular, once a task reaches device QA/release, unrelated commits arriving on `origin/main` are a concurrency blocker rather than work to merge into the already-validated branch and retest.

The desired local tooling is a small task lease/lock used by Codex sessions, with stale-lock recovery, so this rule is enforced rather than merely documented.

## Canonical APK artifact

Default final delivery artifact: canonically signed **debug** APK `<version>.apk` unless a specific task requires release behavior.

Do not run R8/minification, ABI stripping, APK post-processing or manual re-signing solely because a transport rejects the APK size. Transport constraints must be fixed at the delivery layer. After final gates pass, the artifact is immutable: the exact same bytes are installed on the Pixel and delivered either directly through Telegram or through the GitHub Release fallback.

## Telegram delivery architecture

Do not create a dedicated repository just for large APK delivery.

Ownership:

- shared `telegram_notify`: standard cloud Bot API notification/document client;
- PersonalHub: APK delivery policy and GitHub Release fallback for large APKs;
- `gernalix/vm_oracle`: no self-hosted Telegram Bot API service for this workflow.

Keep Telegram on the standard cloud Bot API. If the final APK is at or below 50 MiB, deliver it directly as a Telegram document. If it is larger, publish it as the current APK asset on the stable PersonalHub development prerelease `personalhub-dev-apk` and send the GitHub Release link through Telegram. PersonalHub is private, so that link requires GitHub authentication unless repository visibility changes.

Secrets such as bot token and chat/destination remain outside Git. `telegram_notify` does not need a configurable Local Bot API endpoint for this workflow, and there is no >50 MiB Telegram runtime acceptance test anymore.

For the stable prerelease, upload the replacement APK **before** deleting the previous APK asset. Only after the upload succeeds should old APK assets be removed and release metadata updated. An upload failure must leave the last known-good APK available.

## Release workflow

Preferred PersonalHub release sequence:

1. targeted tests and source/UI gates;
2. one final signed debug build after the code is stable;
3. verify version/signature/hash once;
4. install that exact APK on Pixel;
5. deliver the APK through `telegram_notify` if it is at or below 50 MiB, otherwise publish it to the stable GitHub prerelease and send that link through `telegram_notify`;
6. perform required MegaVault/roadmap terminal writes;
7. stop.

No release/universal/arm64/re-sign fallback ladder is allowed merely to fit Telegram.

## Roadmap/token discipline

For a sequence of PersonalHub tasks, use a campaign: intermediate phases perform only targeted compile/tests and push code; one final phase performs the single version bump, broad final build/device QA, Pixel install and Telegram delivery. Avoid rebuilding/installing/delivering after every independent subtask.

GPT-5.5 medium is the default for pre-localized implementation/verification. GPT-5.6 Sol medium remains appropriate for schema migration/data-safety work or genuinely cross-module architectural failures.

For long-running builds or external processes, prefer one blocking wait or sparse status checks; do not spend model/tool round-trips repeatedly reporting unchanged progress.

`roadmap_guard.py complete` returning `push_verified=git_push_exit_0` is terminal proof for the normal selected-task path. If an implementation is already pushed but the roadmap has advanced and `complete` returns `prompt_identity_mismatch`, use the guard's dedicated `reconcile` flow rather than reproducing its bookkeeping manually. A successful `complete` or `reconcile` push is terminal proof; do not spend tool calls on follow-up status/rev-parse/fetch checks.
