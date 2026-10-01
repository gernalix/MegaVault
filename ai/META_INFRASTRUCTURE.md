# ChatGPT operational contract
VERSION=61
STATUS=SOLE_CROSS_PROJECT_AUTHORITY
Audience=AI_only; coverage=90%+_normal_operations_from_this_document_alone

Paths below are literal. `R=/home/daniele/projects/codex-roadmap`, `M=/home/daniele/MegaVault`, `G=/home/daniele/projects/github-autosync` are notation, not exported environment variables. Expand before executing. User scope overrides automatic intake/reporting; ordinary code tasks need no invented lifecycle item. Read additional documents only for task-specific details.

## Authorities

| Owner | Canonical source | Exclusive responsibility |
|---|---|---|
| MegaVault | `/home/daniele/MegaVault/megavault.sqlite`: projects, project_aliases, repositories, hosts, services, integrations, monitoring_targets | project identity; desired inventory/policy |
| C3 | `/home/daniele/.local/state/c3-control/roadmap.sqlite` | Inbox, work_items, dependencies, priority, prompts/bodies, PROMPT_ID, runs, receipts, lifecycle |
| github-autosync/repo-integrator | `/home/daniele/.local/share/codex-github-autosync`; `G/repo_single_writer.py` | task worktrees/branches, PR, CI, merge, terminal-aware GC |
| fedora-system-monitor | `/var/lib/fedora-system-monitor/monitor.sqlite3`; `/etc/fedora-system-monitor/config.toml`; live systemd/journal and Kuma DB | observed runtime, health, incidents, Kuma |
| codex-usage-monitor | `/home/daniele/projects/codex-usage-monitor` telemetry outputs/native Codex sessions | session/token/cost/usage only; never C3 lifecycle |

C3 primary UI=`http://127.0.0.1:8767`; read API=`GET /api/state`, `GET /api/health`. UI is a DB/API view, not separate authority. C3 project tables are MegaVault-synchronized caches. Git `R/roadmap.sqlite`, Markdown, Obsidian, reports and supervisor task metadata are projections/history: never infer current state from them or restore them over the runtime DB.

## Read before acting / new-chat takeover

1. Read this document; retain only the user's scope. No earlier chat, master goal or checkpoint is required.
2. `python3 R/tools/c3_control.py status`; `curl --fail http://127.0.0.1:8767/api/health`.
3. `systemctl --user show c3-writer.service c3-web.service c3-runtime.service c3-symphony.service -p ActiveState -p SubState -p Result`; inspect only a failed component's bounded journal.
4. For the named item, open the canonical DB read-only (`sqlite3 -readonly /home/daniele/.local/state/c3-control/roadmap.sqlite`): query `work_items`, `work_item_runs`, `work_item_executor_bindings`, `work_item_execution_specs`, `work_item_checkpoints`, `work_item_dependencies` by exact work_item_id/run_id. Live runs are `state IN ('claimed','running','recovering')`; inspect actual `c3-run-<run_id>.service` and executor before recovery. A stale status/lease is not takeover permission.
5. Resolve a supplied project ID only with `python3 M/megavault.py project-show ID`; alias=`python3 M/megavault.py project ALIAS`; path=`python3 M/megavault.py project-path ID`. Check target Git status and exact worktree; preserve dirty/unrelated work.

## Local writer / mutation transport

Single writer=`c3-writer.service`, implementation=`R/tools/c3_local_writer.py`, socket=`/home/daniele/.local/state/c3-control/writer.sock`. Only this process opens canonical C3 writable. WAL, transactions, stable request keys and applied receipts are mandatory. Never invoke internal DB writers/direct intake CLI, Actions writer, or a second writer.

Mutation file envelope: `{"schema":"codex-roadmap.mutation.v1","actor":"chatgpt","operations":[OP]}`. Submit=`python3 R/tools/submit_mutation.py --file FILE --request-key KEY`. Local host uses the Unix socket synchronously; require `submission=applied` plus canonical readback. Retry identical document with identical key; changed payload requires a new key. Collision/invalid mutation is fail-closed, not an excuse to force-write.

For fenced work-item operations, call Python from `R/tools`: `c2_supervisor_lease.load_runtime_identity()` returns `(supervisor_id, fencing_token)`; `c2_control.submit_control(operation=NAME, arguments=ARGS, request_key=KEY, supervisor_id=..., fencing_token=..., canonical_renew=True)`. It routes to the same local writer. Do not acquire/replace ownership manually. `submit_controls` accepts at most 50 independent operations atomically. Prefixes `c2_*` here are supported APIs, not permission to start old daemons.

Remote-only ChatGPT may submit the same immutable `[roadmap-mutation] KEY` Issue to `gernalix/codex-roadmap`; local `c3-remote-ingress.service` consumes bounded prioritized batches. Remote submission is queued, not applied. Verify receipt/readback; do not claim success from Issue creation. GitHub is optional ingress/audit, never a prerequisite on the local host. Do not set `C3_MUTATION_TRANSPORT=github` locally as fallback.

## Normal operations

- Inbox capture: `python3 R/tools/c3_inbox.py "description" [--repo OWNER/REPO] [--task-id WI] [--run-id RUN]`; stable `--issue-id issue:<32hex>` for retries. Read pending=`v_issue_inbox_pending_ordered`. Observation is not a work item.
- Inbox technical reconciliation: `python3 R/tools/c3_runtime.py --inbox-only` (maximum 25; exact known decisions only; ambiguous remains pending). Semantic disposition: fenced `reconcile_issue_batch` arguments=`batch_id,triaged_by,decisions:[{issue_id,reason,work_item_ids}],new_items`; `new_items` uses intake fields plus `alias`, referenced as `@alias`. Zero work_item_ids discards; otherwise links/promotes. Use one bounded batch, no execution work item/run for triage, no issue about the triage job's own failure.
- Work item: fenced `intake` arguments=`title,objective,acceptance:[...],repo,project,parent_id,depends_on:[...],tags:[...],next_action,execution`. Specify facts/acceptance, explicit dependencies and priority:p0/p1/p2; no inferred execution settings. Normal technical jobs do not become lifecycle items.
- Prepare Codex-backed intake: `python3 R/tools/c2_prepare_codex.py --spec FILE`. Spec requires `work_item_id,prompt_file,source,model,reasoning,activity` (`coding|diagnostic`); optional `resources,max_attempts,readiness_evidence,parent_prompt_id`. This allocates/materializes through C3 and creates a Git-owned worktree; leaves pending, never dispatches. Read returned worktree and canonical state before acting.
- Standalone new/revised prompt: OP=`{"op":"prompt_id_allocate","arguments":{"request_id":"KEY","source":"chatgpt","project_id":ID}}`; use returned six-digit ID. Then submit `register` OP fields=`prompt_id,slug,title,prompt_text,current_path,project_id,model,reasoning` and explicit dependency metadata. `current_path` is compatibility metadata, not body authority. Allocation is C3-only; registration materializes atomically in C3, no MegaVault materialize step. Text/semantic revision needs new ID plus explicit relation; metadata-only change does not. No historic ID reuse, hash-based deduplication or guessed ID. A non-prompt item needs no PROMPT_ID.
- Automatic execution: C3 runtime routes eligible coding to Symphony; GUI/semantic uses on-demand RDC browser utilities. Never dispatch a second executor for a live run. Manual prompt start=`python3 R/tools/roadmap_start.py --repo R --prompt-id ID`; require running/applied readback. Actual executor start=`python3 R/tools/c2_executor_start.py --run-id RUN` (or `--work-item-id WI --executor codex` for authorized manual non-prompt work); enrich binding with `--executor-ref REF --chat-url URL`. Managed workers already emit start; do not duplicate claim/acknowledgment.
- Finish prompt=`python3 R/tools/roadmap_finish.py --repo R --prompt-id ID --result PASS|BLOCKED|FAIL|CANCELLED`. Non-prompt=`python3 R/tools/c2_executor_result.py --run-id RUN --work-item-id WI --result RESULT --payload FILE`; payload keys=`completed:[],remaining:[],evidence:[],blocker:null|string,next_action:null|string`, optional summary. PASS requires complete acceptance and evidence. Integration queued is not completed; return without model polling. Writer/integrator reconcile terminal state asynchronously.
- UI pause/resume/stop/priority/move: preview in C3 UI, apply its precondition-bound action. Cancel/delete requires explicit user confirmation of affected dependents; never manufacture intent or bypass preview.
- Temporary dispatch override=`python3 R/tools/c2_execution_override.py set --selector project|repo|tag --value VALUE`; `read`/`clear`. It changes dispatch only, not semantic priority/dependencies.
- Project/repository registration: `python3 M/megavault.py register-local-repo --worktree PATH` or `register-github-repo --owner OWNER --name NAME --remote-url URL --default-branch BRANCH --worktree PATH`; IDs allocated exclusively in retained MegaVault projects. Archive, never delete/reassign IDs. Desired inventory changes use MegaVault owner CLI; no C3 allocation.
- Git: `python3 G/repo_single_writer.py start --repo PATH --task-id EXISTING_TASK_ID`; edit only returned worktree. Start helper may already allocate it: reuse, do not allocate twice. `status-any --task-id ID [--repo OWNER/REPO]`; `finish --repo PATH --task-id ID` queues PR/integration; `status-all --roadmap-only` reads pipeline. Integrator owns canonical merge and safe hourly GC. Never reset/stash user work, force-push, bypass protected canonical hooks, manually delete dirty/unmerged/active/recovery worktrees, or wait with repeated model calls.
- Monitoring=`fedora-system-monitor status|health|alerts`; `events --since-hours 24`; `context incident ID`; failed unit=`journalctl --user -u UNIT --since '-15 min' -n 100 --no-pager` (system units omit --user). Kuma administration belongs to Fedora's `kuma_admin`; use its task-specific commands only when changing monitors. MegaVault Kuma copies are historical/projections, not observed authority. Deduplicate unresolved failure domains at source; one actionable C3 observation, no storm.

## Invariants / permanently retired

authority_project=MegaVault; authority_lifecycle=C3; authority_prompt_id=C3; authority_git=github-autosync; authority_observed=Fedora; authority_usage=telemetry_only
single_c3_writer=required; project_ids=archive_only_never_reuse; prompt_ids=reserved_forever; inbox_is_not_work_item=true; projections_are_not_authority=true

Model/reasoning are structured execution metadata, never prompt body text; immutable for a running run. Preserve explicit dependencies/resources and permanent ID reservations. Never use telemetry or file titles to start/finish an item.

Retired manual/watch entrypoints also include `c2-roadmap-goal-watchdog`, `c2-roadmap-live-watch`, `c2-roadmap-semantic-watcher`, `c2-personalhub-p0` and `c2-roadmap-status`; their installed services/timers are masked and old scripts reject permanently. They are not recovery tools.

Never reactivate C2 supervisor/watchdog/resume/global discovery/recovery; Workflowy C3 dashboard/sync/manual order/control bridge; snapshot poller/second full roadmap DB; recursive Inbox executor/maintenance timer; MegaVault PROMPT_ID worker/allocator/Issue bridge; usage lifecycle/aggregate C2 health/global CI watcher; dedicated roadmap Git PR writer. Retired checkpoints are historical evidence, never executable recovery points. Never unmask legacy units, reinstall old source/build copies or run an old installer to recover. Personal Workflowy and targeted C3 GUI browser utilities are independent and remain permitted. Manual browser kill switch `/home/daniele/.config/c2/disable-chat-supervisor` is a resource circuit breaker; do not remove without confirming the triggering condition/user authority.

## Recovery decision tree

- Mutation timeout/socket unavailable → inspect `mutation_receipts WHERE request_key=KEY` read-only first; applied means no resend. If absent, check writer unit + bounded journal; repair local failure, retry same immutable request. Writer startup uses systemd readiness; after its restart, start `c3-web.service` if dependency-stop left it inactive and verify HTTP health. Never GitHub/direct-SQL fallback.
- Writer contention/invalid mutation/key conflict → preserve owner; inspect exact receipt/payload/precondition. Correct caller input with a new key only if semantics changed; no repeated identical rejected retries.
- Runtime failure → inspect C3 unit/journal, lease and exact worker; correct the demonstrated fault. Start only current `c3-runtime.service`, never C2. Event trigger=`c3-runtime.path`; one slow `c3-runtime.timer` safety net. Lease expiry alone never authorizes a replacement executor.
- Stale run → verify real worker/executor and existing result/integration evidence. Reconcile through fenced `reconcile_run`/`recover` only after proving ownership is gone; bounded existing recovery, not a new master goal. GUI uncertain delivery → inspect existing run receipt/chat binding; leave quarantined rather than send another prompt.
- PR/CI pending → read Git authority once, fix concrete in-scope failure in task worktree; event-driven integrator handles progress. No model heartbeat loop.
- Project mismatch → resolve MegaVault live; stop allocation and repair source/cache linkage with owner helpers, preserving historical references.
- DB corruption/schema migration → stop sole writer, coherent SQLite backup via `R/tools/c3_storage.py:verified_backup` (SQLite backup API, integrity + SHA manifest), preserve WAL, diagnose/restore latest verified authority backup under writer lock; never replace from stale Git/Markdown/snapshot. Restart current writer, read back required rows/integrity/FK before dependent runtime.
- Browser unavailable/kill switch → do not discover all account chats, take over user's browser or restart global daemon; retain existing run/quarantine and request missing interaction if essential.
- Alert flapping → check Fedora incident/C3 disposition; reuse unresolved incident identity. New observation only after prior incident is genuinely resolved and a distinct actionable occurrence exists.

## Stop conditions

Stop immediately after requested acceptance/readback passes. No optional audit, projection refresh, new registry, redundant checkpoint/report, prompt/task for meta-work, speculative cleanup, repeated retry without new evidence, or model waiting. Keep one minimal canonical handoff only when resumption is needed: architecture/current state/real residuals/exactly one Next action; never require old chat history. Missing authority, unresolved ownership, destructive ambiguity or indispensable user decision → preserve state and ask. Secrets: references only; values never in Git/DB/log/chat; systemd credentials or native Secret Service at point of use. Owner-specific implementation tests/details may be consulted only for the actual task.
