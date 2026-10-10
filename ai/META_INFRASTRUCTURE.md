# ChatGPT operational contract
VERSION=62
STATUS=SOLE_CROSS_PROJECT_AUTHORITY
SCOPE=cross_project_shared_rules
Audience=AI_only

This document owns common execution and ownership rules. The task-specific
[MEGAVAULT_PROTOCOL.md](MEGAVAULT_PROTOCOL.md) supplies specialist policies;
[personalhubdoc.md](personalhubdoc.md) supplies PersonalHub-only exceptions.
Do not copy those exceptions into global policy or create parallel authorities.
Read only the relevant sections for the task; a PersonalHub task starts with
its specialized bootstrap instead of preloading this entire document.

## Authorities

| Domain | Canonical authority |
| --- | --- |
| Projects, aliases, repositories, hosts, integrations and desired services | MegaVault `megavault.sqlite` and verified owner tools |
| Git branches, task worktrees, PRs and integration | `github-autosync/repo_single_writer.py` and Git remote |
| Work requested, decisions and completion | Current user instruction, GitHub issues/task branch evidence; durable Git handoff only when needed |
| Observed runtime and incidents | Fedora System Monitor, live systemd/journal and Kuma |
| Codex token/usage telemetry | codex-usage-monitor, never task lifecycle |

authority_project=MegaVault
authority_lifecycle=GitHub_issues+Git_task_evidence
authority_prompt_id=retained_Git_reservations
authority_git=github-autosync
authority_observed=Fedora
authority_usage=telemetry_only
project_ids=archive_only_never_reuse
prompt_ids=reserved_forever
projections_are_not_authority=true
retired_orchestrators=C2|C3;frozen_history_only;never_start|invoke|restore|dispatch|submit_to_Inbox|allocate_ids_through_retired_helpers

No active C2/C3 writer, Inbox, dispatcher, worker, runtime, allocator, registration
or lifecycle helper is permitted. Old database rows, archived Markdown, old
`Next action` fields and historical test fixtures are evidence, not permission to
resume retired infrastructure. Do not create replacement lifecycle registries.

## Read before acting / new-chat takeover

1. Follow the user's exact requested scope; identify target repository and
   authoritative owner. Use the current remote state, not old chat or stale
   tracking refs, for claims about branches, merges or authoritative documents.
2. For PersonalHub, start with `ai/personalhubdoc.md`; only fetch the relevant
   global/specialist section when required by its fallback contract. Consult
   `PersonalHub/AGENTS.md` and app docs for implementation-specific invariants.
3. For other projects, consult this document plus only the needed specialist
   section and repository `AGENTS.md`/target files. Do not scan every project.
4. Resolve project identity in MegaVault: `python3 /home/daniele/MegaVault/megavault.py project ALIAS`
   or `project-show ID`; verify live state if acting on a service/device.
   Never infer IDs, host identity, secret values, or current operational health.
5. Preserve unrelated edits, active task worktrees and remote advances. If a
   verified prior result is unchanged, reuse it instead of rereading or rerunning.

## Git single writer and durable tasks

- Never edit the canonical checkout directly for an agent code/docs task. Use
  `python3 /home/daniele/projects/github-autosync/repo_single_writer.py start --repo PATH --task-id ID --actor ACTOR`.
  It creates/returns a dedicated task worktree. One task ID across related
  repositories; do not share a working tree with another task.
- Work on the returned task branch; make the smallest coherent change and
  targeted verification. Commit and push the task branch. Finish with
  `python3 /home/daniele/projects/github-autosync/repo_single_writer.py finish --repo PATH --task-id ID`
  to queue the existing single-writer PR/integration pipeline. Verify
  integration separately before calling a canonical-branch change merged.
- The integration owner, not the agent, merges into the protected canonical
  branch. Never manually merge, force-push, reset or stash someone else's work,
  or treat a queued PR as an integrated result.
- For substantial work, checkpoint objective, verified decisions, completed and
  remaining acceptance, blockers, evidence, and one `Next action` in durable Git
  task state when genuinely needed. Commit and push checkpoints. Historical
  codex-roadmap task-state archives are not live execution authority; don't
  create a second task-control database.
- For an explicitly requested Codex prompt, use one immutable six-digit
  PROMPT_ID. Reuse a valid supplied ID; otherwise check current Git issues,
  task branches and historical reservations before choosing an unused ID.
  Propagate the same ID across related repositories. Ordinary manual tasks
  need no PROMPT_ID or retired orchestration acknowledgement. Model/reasoning
  are execution metadata, not prompt body content.

## Execution, validation and recovery

- Use the least expensive safe mode: FAST for localized low-risk changes;
  STANDARD for cross-component changes; STRICT for destructive operations,
  database migrations, security changes or critical infrastructure. Promote
  only for concrete evidence.
- Start with the relevant file/symbol/test and known facts. Batch coherent
  reads and checks; avoid broad scans, duplicate work, speculative changes,
  blind retries and refactors outside scope. No second implementation or
  monitoring mechanism where an existing owner suffices.
- For Python, follow the specialist Python environment policy. Follow the
  project build, security and testing gates, including device-specific
  acceptance when platform behavior is claimed.
- After a failure, examine the minimal discriminating evidence, repair the
  same failure domain if safe and in scope, then resume the original goal.
  An intermediate error, dirty non-overlapping file or delayed PR is not by
  itself a terminal BLOCKED result. Block for true unavailable dependencies,
  unsafe concurrency or essential user authorization.
- Test the smallest sufficient surface first; expand only for failure, material
  risk or release requirements. Report `PASS` only after required evidence;
  integration queued, partial tests and unverified assumptions are not PASS.
  Report material bottlenecks, including ones resolved during the work.

## Secrets, observed runtime and specialist boundaries

- Never put credential values in Git, MegaVault, logs, reports or chat. Resolve
  secrets through the native provider/boundary of the actual runtime and
  validate access without exposing values; see specialist secrets policy.
- MegaVault stores desired inventory and references, not a second observed
  health authority. Use Fedora System Monitor and the actual service/journal
  for runtime evidence. For systemd, Android device identity, SQLite live
  changes, critical network cutovers, Telegram providers and other specialist
  tasks read only the relevant `ai/MEGAVAULT_PROTOCOL.md` section.
- PersonalHub alone owns `PIXEL_NOTIFY`, final APK installation and Telegram
  delivery semantics in `ai/personalhubdoc.md`. Shared Android identity and
  security gates still apply. Project exceptions may specialize a shared
  default but must not silently contradict a shared invariant.

## Recovery decision tree

- Repo or task state unclear: inspect exact Git remote, branch, task worktree,
  PR and latest relevant evidence. Avoid unrelated worktrees or duplicate PRs.
- Integration pending: check the existing single-writer receipt/PR once; fix
  only concrete failed checks in the owned task branch, without polling a model.
- Service or health incident: use live Fedora monitoring, owner systemd status
  and a bounded journal; repair only the demonstrated failure.
- Identity, ownership, current data or consent ambiguous: preserve the state
  and stop the unsafe operation. Do not substitute historical C2/C3 control.
- Validator/test failure: inspect the failing assertion and smallest relevant
  artifact; correct only a demonstrated stale expectation or real regression.

## Stop conditions

Stop when requested acceptance and mandatory readback pass. No optional audit,
duplicate registry, unrelated cleanup, extra prompt or invented notification.
State actual remaining integration or external blockers instead of claiming
completion early.
