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

Do not run R8/minification, ABI stripping, APK post-processing or manual re-signing solely because a transport rejects the APK size. Transport constraints must be fixed at the delivery layer. After final gates pass, the artifact is immutable: the exact same bytes are installed on the Pixel and delivered to Telegram.

## Telegram delivery architecture

Do not create a dedicated repository just for large APK delivery.

Ownership:

- shared `telegram_notify`: cloud Bot API notification client;
- PersonalHub: APK delivery policy and GitHub Release fallback for large APKs;
- `gernalix/vm_oracle`: no self-hosted Telegram Bot API service for this workflow.

Keep Telegram on the standard cloud Bot API. If the final APK is at or below
50 MB, deliver it directly as a Telegram document. If it is larger, publish it
as the current APK asset on the stable PersonalHub development prerelease and
send the GitHub Release link through Telegram. PersonalHub is private, so that
link requires GitHub authentication unless repository visibility changes.

Secrets such as bot token and chat/destination remain outside Git.

The shared notifier should accept/configure one base endpoint, send documents through it, and preserve the existing destination/config semantics. A runtime acceptance test must send a temporary file larger than the cloud 50 MB limit and then delete the temporary file.

## Release workflow

Preferred PersonalHub release sequence:

1. targeted tests and source/UI gates;
2. one final signed debug build after the code is stable;
3. verify version/signature/hash once;
4. install that exact APK on Pixel;
5. deliver the APK through `telegram_notify` if it is at or below 50 MB, otherwise publish it to the stable GitHub prerelease and send that link through `telegram_notify`;
6. perform required MegaVault/roadmap terminal writes;
7. stop.

No release/universal/arm64/re-sign fallback ladder is allowed merely to fit Telegram.

## Roadmap/token discipline

For a sequence of PersonalHub tasks, use a campaign: intermediate phases perform only targeted compile/tests and push code; one final phase performs the single version bump, broad final build/device QA, Pixel install and Telegram delivery. Avoid rebuilding/installing/delivering after every independent subtask.

GPT-5.5 medium is the default for pre-localized implementation/verification. GPT-5.6 Sol medium remains appropriate for schema migration/data-safety work or genuinely cross-module architectural failures.

`roadmap_guard.py complete` returning `push_verified=git_push_exit_0` is terminal proof for the roadmap push; do not spend tool calls on follow-up status/rev-parse/fetch checks.
