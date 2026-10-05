# Project-centric operational contract
VERSION=62
STATUS=SOLE_CROSS_PROJECT_AUTHORITY

The user's request defines scope. Make the minimum change, preserve unrelated work,
start with targeted verification and stop when acceptance passes.

## Sources of authority

- Each project's Git/GitHub owns its code, history and backlog. Prefer its GitHub
  Issues; update an equivalent issue instead of duplicating it.
- MegaVault `megavault.sqlite` owns project IDs, aliases, repositories and desired
  infrastructure inventory. Resolve supplied project_id exclusively there; never
  invent or reassign one. Archive historical IDs permanently.
- systemd, Fedora System Monitor and Uptime Kuma own observed runtime/health.
- codex-usage-monitor owns usage telemetry only.
- C3 is a frozen historical archive. Its databases, code, source prompts and IDs
  are retained, but no active task needs its services, CLI, router or lifecycle.

## Normal task flow

request → project backlog/issue → when started: local task-state → Codex → test →
commit/push → close issue after verified acceptance and integration.

If the project cannot be identified: request → passive global Inbox → project backlog.
The sole global passive Inbox is `/home/daniele/MegaVault/inbox/`; it has no workers,
promotion, automatic reconciliation, timers or orchestration.
Projects without an accessible user-owned GitHub tracker use the Git-owned
`/home/daniele/MegaVault/projects/<slug>/backlog/`. These folders contain backlog,
not operational task-state. Known projects never go to the global Inbox.

Preserve source provenance, unique requirements, priority, dependencies and explicit
conflicts when reconciling backlog. Cross-project requests have one owning issue
with explicit related project IDs and links. Do not execute backlog during triage.
Do not allocate PROMPT_ID or execution state for an unstarted task. Historical
PROMPT_ID reservations are immutable archival references, not a new-task gate.

## Execution and Git

Read only the named project's entrypoint and relevant files. For PersonalHub use
`/home/daniele/MegaVault/ai/personalhubdoc.md`.
Create local task-state only when work starts; use a task-local file/worktree and
reference the project issue. Persist complex work through commit + push.
Use isolated Git worktrees and the existing Git single writer where configured:
`python3 /home/daniele/projects/github-autosync/repo_single_writer.py start --repo PATH --task-id LOCAL_TASK_ID`
and its `finish` operation for queued integration. This is repository integration,
not a global task orchestrator. No C3 registration, ownership lease, executor
receipt or completion callback is required. Existing worker/worktree ownership
must be preserved; never duplicate an executor, reset/stash user work or force-push.
Confirm acceptance, actual Git state and required runtime readback before closure;
queued integration alone is not completed integration. Keep blocked work with its
evidence and a concrete next action; no model polling loop.

## Infrastructure and archive

C3 writer/web/runtime/path/timer/ingress/Symphony and its Kuma-to-Inbox bridge are
disabled and masked. No automatic consumer inserts or promotes C3 work. Do not
unmask, reinstall or run archived C3 installers/dispatchers to start a task.
Independent monitoring, personal Workflowy, Git integration, browser utilities and
usage telemetry remain project-owned; none may use C3 as a runtime dependency.
Archived roadmap references can be read as history, never as current backlog or
permission to run old recovery/checkpoint instructions.

Migration evidence: `gernalix/codex-roadmap/archive/retirement-2026-10-05/` contains
the complete canonical SQLite/JSON/Markdown export, reconciliation, source-to-target
mapping and verification. Repository and database history must not be deleted.
Secrets remain references only; use systemd credentials or native Secret Service
at point of use. Never store secret values in Git, logs, exports or chat.

Machine-readable invariants:

authority_project=MegaVault; authority_backlog=project_GitHub_or_Git; authority_execution=local_task_state; authority_git=github-autosync; authority_observed=Fedora; authority_usage=telemetry_only
project_ids=archive_only_never_reuse; prompt_ids=reserved_forever; global_inbox=passive_only; inbox_is_not_work_item=true; projections_are_not_authority=true
coverage=90%+_normal_operations_from_this_document_alone
