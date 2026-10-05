# C2 Git guard: commit su branch emette errore pack-refs ambiguo pur riuscendo

<!-- migration-42b0a2ec1faaf20a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:f2d5d81a952b47b1bd4fa4c07d175265`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 Git guard: commit su branch emette errore pack-refs ambiguo pur riuscendo

Ridurre il rumore del reference-transaction hook: durante commit su branch non-main compare 'BLOCKED: codex-roadmap main is guarded' e pack-refs failed, ma il commit procede, rendendo ambiguo l'esito.

Acceptance:

- Commit/push su branch consentiti non emettono falso errore
- Main resta protetto
- Test hook distingue ref main da manutenzione pack-refs/branch

status: waiting

current_action: Prepare deterministic Codex prompt and execution spec in isolated worktree.

next_action: Implement/test a scoped guard diagnostic fix through an isolated C2 branch.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical repository identity",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
      "parent_id": null,
      "kind": "task",
      "title": "C2 Git guard: commit su branch emette errore pack-refs ambiguo pur riuscendo",
      "objective": "Ridurre il rumore del reference-transaction hook: durante commit su branch non-main compare 'BLOCKED: codex-roadmap main is guarded' e pack-refs failed, ma il commit procede, rendendo ambiguo l'esito.",
      "acceptance_json": "[\"Commit/push su branch consentiti non emettono falso errore\", \"Main resta protetto\", \"Test hook distingue ref main da manutenzione pack-refs/branch\"]",
      "status": "waiting",
      "executor_policy": "codex",
      "sort_order": 15,
      "current_action": "Prepare deterministic Codex prompt and execution spec in isolated worktree.",
      "next_action": "Implement/test a scoped guard diagnostic fix through an isolated C2 branch.",
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": "705998",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-25T17:46:28Z",
      "updated_at": "2026-09-27T22:23:04.087114Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "705998",
        "slug": "c2-git-guard-commit-su-branch-emette-errore-pack-705998",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "GPT-5.6 Terra",
        "reasoning": "medium",
        "megavault_mode": "FAST",
        "campaign_id": null,
        "explanation": "",
        "current_path": "prompts/c2-git-guard-commit-su-branch-emette-errore-pack-705998.md",
        "materialization_sha256": "ae3bac0f7567a0130c3e065422639b2f6201eab51e330ea7c0e159e6ee308f09",
        "created_at": "2026-09-26T18:18:59Z",
        "updated_at": "2026-09-27T22:23:05Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "705998",
        "body": "PROMPT_ID=705998\n\n# Goal\nFix the codex-roadmap Git reference-transaction guard so allowed non-main branch work no longer emits the false guard/pack-refs error, while direct mutations of protected main remain blocked.\n\n## Scope\nWork only in this isolated codex-roadmap worktree. Start from the current hook/tests and make the minimum change required. Do not modify roadmap.sqlite directly, C2 scheduling semantics, PersonalHub, or unrelated code.\n\n## Required behavior\n- Allowed commit/push activity on non-main branches must not emit the false guard error.\n- Benign reference maintenance such as pack-refs must not be rejected merely because main exists among refs being inspected.\n- Actual prohibited updates to protected main must still be rejected deterministically.\n- Add or adjust focused automated coverage that distinguishes a real main mutation from branch/ref-maintenance transactions.\n\n## Verification\nRun the narrow hook tests first; expand only if failures or risk require it. Also run git diff --check. Record the exact commands/results. Stop once the acceptance criteria pass.\n\n## Persistence\nCommit the focused fix on the current isolated branch and push it. Open or update a focused PR only if needed to integrate the code change; do not perform unrelated cleanup or refactors.\n",
        "sha256": "ae3bac0f7567a0130c3e065422639b2f6201eab51e330ea7c0e159e6ee308f09",
        "created_at": "2026-09-26T18:18:59Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [
      {
        "execution_id": 400,
        "prompt_id": "705998",
        "cycle_key": "5cf1b2dbd47b00650b57adaa",
        "materialization_sha256": "3e72ab8a9fd03e13c109a36907d67b705536dc2032461af75223a89d6a6b6614",
        "started_at": "2026-09-26T18:22:00Z",
        "ended_at": "2026-09-26T18:22:03Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 2.823,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/f2d5-git-guard",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 16280,
        "cached_input_tokens": 15104,
        "uncached_input_tokens": 1176,
        "output_tokens": 110,
        "reasoning_output_tokens": 44,
        "total_tokens": 16390,
        "source": "codex-usage",
        "recorded_at": "2026-09-26T18:23:14Z"
      },
      {
        "execution_id": 401,
        "prompt_id": "705998",
        "cycle_key": "f2c82cf4ab1265c6d55e950a",
        "materialization_sha256": "ae3bac0f7567a0130c3e065422639b2f6201eab51e330ea7c0e159e6ee308f09",
        "started_at": "2026-09-26T18:20:59Z",
        "ended_at": "2026-09-26T18:22:28Z",
        "outcome": "BLOCKED",
        "duration_seconds": 88.771,
        "model": "gpt-5.6-terra",
        "reasoning": "medium",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/f2d5-git-guard",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 9,
        "input_tokens": 34149,
        "cached_input_tokens": 33536,
        "uncached_input_tokens": 613,
        "output_tokens": 348,
        "reasoning_output_tokens": 109,
        "total_tokens": 34497,
        "source": "codex-usage",
        "recorded_at": "2026-09-26T18:24:20Z"
      },
      {
        "execution_id": 403,
        "prompt_id": "705998",
        "cycle_key": "e00de330c0065fa5e664140b",
        "materialization_sha256": "be0eac64f5dec3edfddc8928088ba8aa742cf7d8105f1bfcfd9397d06a1d31e9",
        "started_at": "2026-09-26T18:22:16Z",
        "ended_at": "2026-09-26T18:22:19Z",
        "outcome": "UNKNOWN",
        "duration_seconds": 3.537,
        "model": "codex-auto-review",
        "reasoning": "low",
        "codex_project": "/home/daniele/.local/share/c2-supervisor/worktrees/f2d5-git-guard",
        "chat_title": null,
        "branch": null,
        "commit_before": null,
        "commit_after": null,
        "tool_call_count": 0,
        "input_tokens": 17593,
        "cached_input_tokens": 16128,
        "uncached_input_tokens": 1465,
        "output_tokens": 142,
        "reasoning_output_tokens": 81,
        "total_tokens": 17735,
        "source": "codex-usage",
        "recorded_at": "2026-09-26T18:58:23Z"
      }
    ],
    "status_history": [
      {
        "history_id": 975,
        "prompt_id": "705998",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-09-26T18:18:59Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 976,
        "prompt_id": "705998",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-09-26T18:20:04Z",
        "actor": "c2-scheduler",
        "note": null
      },
      {
        "history_id": 977,
        "prompt_id": "705998",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-09-26T18:22:35Z",
        "actor": "codex",
        "note": "terminal:roadmap_result:BLOCKED"
      },
      {
        "history_id": 1081,
        "prompt_id": "705998",
        "old_status": "blocked",
        "new_status": "waiting",
        "changed_at": "2026-09-27T22:23:04.087114Z",
        "actor": "c2-blocked-reconcile",
        "note": "Implement/test a scoped guard diagnostic fix through an isolated C2 branch."
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "tag": "c2-discovery"
      },
      {
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "tag": "git-guard"
      },
      {
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "tag": "reliability"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 373,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "classification",
        "label": "codex-roadmap main a5873827 .githooks/reference-transaction still emits guarded-main/pack-refs failure on branch commit;",
        "uri": null,
        "value_json": "\"codex-roadmap main a5873827 .githooks/reference-transaction still emits guarded-main/pack-refs failure on branch commit; reproduced during C2 branch merge/commit.\"",
        "created_at": "2026-09-26T17:12:41Z"
      },
      {
        "evidence_id": 385,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "classification",
        "label": "codex-roadmap main a5873827 c2_scheduler.configure_auto requires structured execution.worktree and materialized prompt/e",
        "uri": null,
        "value_json": "\"codex-roadmap main a5873827 c2_scheduler.configure_auto requires structured execution.worktree and materialized prompt/exact metadata for Codex; this intake has no work_item_execution_specs row.\"",
        "created_at": "2026-09-26T17:18:38Z"
      },
      {
        "evidence_id": 390,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "classification",
        "label": "2026-09-26 recovery under supervisor token 7 found zero active C2 runs and zero resource leases; PersonalHub ownership r",
        "uri": null,
        "value_json": "\"2026-09-26 recovery under supervisor token 7 found zero active C2 runs and zero resource leases; PersonalHub ownership remains external.\"",
        "created_at": "2026-09-26T18:17:23Z"
      },
      {
        "evidence_id": 391,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "classification",
        "label": "gernalix/codex-roadmap remote main is 9b5f4596ebdd7b1919407b6fc636a7970439cd56 and isolated worktree /home/daniele/.loca",
        "uri": null,
        "value_json": "\"gernalix/codex-roadmap remote main is 9b5f4596ebdd7b1919407b6fc636a7970439cd56 and isolated worktree /home/daniele/.local/share/c2-supervisor/worktrees/f2d5-git-guard was created from that exact commit on branch codex/c2-git-guard-f2d5.\"",
        "created_at": "2026-09-26T18:17:23Z"
      },
      {
        "evidence_id": 392,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "classification",
        "label": "Root audit already reproduced the false reference-transaction/pack-refs warning on allowed branch commits and scoped the",
        "uri": null,
        "value_json": "\"Root audit already reproduced the false reference-transaction/pack-refs warning on allowed branch commits and scoped the fix to the Git guard.\"",
        "created_at": "2026-09-26T18:17:23Z"
      },
      {
        "evidence_id": 507,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:b11d618912804f8786e09ae33018a6f9",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"codex-roadmap reference-transaction main guard emits , , and  during a normal commit on isolated branch feature/c2-executor-result-contract. The branch commit still succeeds, but this noisy/failed pack-refs side effect can confuse executors and may indicate the guard is over-blocking non-main ref maintenance.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b11d618912804f8786e09ae33018a6f9\", \"observed_at_ms\": 1790458117733, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T00:49:50Z"
      },
      {
        "evidence_id": 517,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:00f7243db2ef473db2cc53354eaec3e3",
        "uri": "codex://threads/01a0dfe9-31e8-71a1-b81f-21397e535cf8",
        "value_json": "{\"chat_url\": \"codex://threads/01a0dfe9-31e8-71a1-b81f-21397e535cf8\", \"code_location\": null, \"description\": \"Durante un commit riuscito nel worktree task/992303, l'hook reference-transaction di codex-roadmap ha bloccato la fase prepared di un pack-refs con il messaggio che main è guarded; il commit è stato comunque creato.\", \"executor\": \"codex\", \"executor_ref\": \"01a0dfe9-31e8-71a1-b81f-21397e535cf8\", \"issue_id\": \"issue:00f7243db2ef473db2cc53354eaec3e3\", \"observed_at_ms\": 1790463660611, \"origin_run_id\": \"c36e86b1b35d43248d7f0a320104d695\", \"origin_work_item_id\": \"prompt:992303\", \"repo\": null}",
        "created_at": "2026-09-27T00:50:42Z"
      },
      {
        "evidence_id": 531,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:b6579643c5984c3d8db6a75feaf6f1a3",
        "uri": "codex://threads/01a0e018-bc4d-7273-9cbc-1ef0ff79fef4",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e018-bc4d-7273-9cbc-1ef0ff79fef4\", \"code_location\": null, \"description\": \"During C2 #1576 source integration, git fetch and ff-only merge succeeded, but Git background pack-refs emitted a protected-main reference-transaction hook rejection and 'task pack-refs failed'. This nonfatal maintenance error makes successful Git operations appear failed and can obscure true failures.\", \"executor\": \"codex\", \"executor_ref\": \"01a0e018-bc4d-7273-9cbc-1ef0ff79fef4\", \"issue_id\": \"issue:b6579643c5984c3d8db6a75feaf6f1a3\", \"observed_at_ms\": 1790467953005, \"origin_run_id\": null, \"origin_work_item_id\": \"wi:164c72ef2c474ec6bbe2d6d795ab93a0\", \"repo\": null}",
        "created_at": "2026-09-27T01:18:42Z"
      },
      {
        "evidence_id": 557,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:9d2361074d164f6b98e13218e59f92ae",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Creare/pushare un worktree branch codex-roadmap valido ha emesso comunque BLOCKED dal reference-transaction hook durante pack-refs; l'operazione è poi riuscita, ma il guard produce un falso errore/confusione su operazioni Git non-main.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:9d2361074d164f6b98e13218e59f92ae\", \"observed_at_ms\": 1790485750408, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T06:29:45Z"
      },
      {
        "evidence_id": 607,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:bd849e1b8f894f468540214e1efe103d",
        "uri": "codex://threads/01a0e173-23e2-76d0-b9d5-d520ad172f0c",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e173-23e2-76d0-b9d5-d520ad172f0c\", \"code_location\": null, \"description\": \"In task worktrees, ordinary commits/pushes emit a misleading guard failure: 'BLOCKED: codex-roadmap main is guarded. Use roadmap_pull.py' from the reference-transaction hook while pack-refs runs, even though the task-branch commit and push then succeed. Make the main-branch guard silent/non-blocking for ref maintenance on non-main task branches so automation cannot misread successful operations as failures.\", \"executor\": \"codex\", \"executor_ref\": \"01a0e173-23e2-76d0-b9d5-d520ad172f0c\", \"issue_id\": \"issue:bd849e1b8f894f468540214e1efe103d\", \"observed_at_ms\": 1790500538331, \"origin_run_id\": null, \"origin_work_item_id\": \"prompt:660629\", \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-27T09:23:38Z"
      },
      {
        "evidence_id": 983,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:1b9f028cad584d0daf9acff37ece81f0",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"hooks/reference-transaction\", \"description\": \"Git guard friction: running git fetch origin main in the guarded codex-roadmap checkout can trigger the reference-transaction hook during pack-refs and print BLOCKED: codex-roadmap main is guarded, even though fetch is needed only to refresh refs before creating an isolated worktree. The guard should distinguish safe remote-ref maintenance/pack-refs from prohibited canonical main mutations so isolated-worker setup does not spuriously fail or confuse automation.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:1b9f028cad584d0daf9acff37ece81f0\", \"observed_at_ms\": 1790531628271, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-27T21:03:11Z"
      },
      {
        "evidence_id": 989,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:9e4b0db73d9e4f8f8e053a7feada06be",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Git guard emitted a BLOCKED reference-transaction/pack-refs error while creating a normal isolated branch for a documentation-only commit, even though the branch commit and push succeeded; safe branch/ref maintenance should not surface a misleading blocker.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:9e4b0db73d9e4f8f8e053a7feada06be\", \"observed_at_ms\": 1790534700356, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:03:12Z"
      },
      {
        "evidence_id": 993,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:ccbe17eb77dd4d35950eebd640e5334e",
        "uri": "codex://threads/01a0e434-f03d-7131-8d73-41a09cbadecd",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e434-f03d-7131-8d73-41a09cbadecd\", \"code_location\": null, \"description\": \"During commit/rebase in isolated task worktree task/wi-0b2f013b-identity-test, the local reference-transaction guard emitted 'BLOCKED: codex-roadmap main is guarded... task pack-refs failed' while the task branch commit, rebase, and push still completed successfully; output is confusing and may imply an operation failed when it did not.\", \"executor\": null, \"executor_ref\": \"01a0e434-f03d-7131-8d73-41a09cbadecd\", \"issue_id\": \"issue:ccbe17eb77dd4d35950eebd640e5334e\", \"observed_at_ms\": 1790535183593, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:03:59Z"
      },
      {
        "evidence_id": 994,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:85bef1a0eda24078bf15c5d89b9318ba",
        "uri": "codex://threads/01a0e435-6ba1-7ba0-9a84-31531e1cf985",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e435-6ba1-7ba0-9a84-31531e1cf985\", \"code_location\": null, \"description\": \"Isolated codex-roadmap task worktree fast-forward from origin/main was blocked by the reference-transaction hook when roadmap.sqlite changed; git reported 'codex-roadmap main is guarded. Use tools/roadmap_pull.py --repo .' and abort in prepared phase while attempting pack-refs.\", \"executor\": null, \"executor_ref\": \"01a0e435-6ba1-7ba0-9a84-31531e1cf985\", \"issue_id\": \"issue:85bef1a0eda24078bf15c5d89b9318ba\", \"observed_at_ms\": 1790535184573, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:03:59Z"
      },
      {
        "evidence_id": 998,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:b8f46a6ad970453cb15693a1bce8a5f5",
        "uri": "codex://threads/01a0e431-cf7b-7f23-b7f2-d29a0ba8c0fb",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e431-cf7b-7f23-b7f2-d29a0ba8c0fb\", \"code_location\": null, \"description\": \"Creating and pushing the isolated C2 Phase C checkpoint branch emitted a reference-transaction hook rejection for local main during Git pack-refs (guard directs roadmap_pull.py), although the task-branch commit and push succeeded; this can make branch maintenance appear partially failed.\", \"executor\": null, \"executor_ref\": \"01a0e431-cf7b-7f23-b7f2-d29a0ba8c0fb\", \"issue_id\": \"issue:b8f46a6ad970453cb15693a1bce8a5f5\", \"observed_at_ms\": 1790535540790, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:04:00Z"
      },
      {
        "evidence_id": 1002,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:65bd6292e9214d59a0dd46a5629a44e5",
        "uri": "codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"code_location\": null, \"description\": \"Guarded roadmap_pull.py failed after PR #2648 merge: its git merge --ff-only rejected local main with the main reference-transaction hook despite _authorize_merge; index/worktree were left staged at remote tree while HEAD stayed behind 3. This recurs amid noisy pack-refs hook diagnostics and requires guarded recovery, never direct reset/pull.\", \"executor\": null, \"executor_ref\": \"01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"issue_id\": \"issue:65bd6292e9214d59a0dd46a5629a44e5\", \"observed_at_ms\": 1790536782064, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:04:01Z"
      },
      {
        "evidence_id": 1004,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:c7e9615218ca4829b7b7969e0236056b",
        "uri": "codex://threads/01a0e44f-5300-74a2-9190-8d688a243a2a",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e44f-5300-74a2-9190-8d688a243a2a\", \"code_location\": null, \"description\": \"In isolated codex-roadmap Project Capsule task worktree, each successful git commit prints `BLOCKED: codex-roadmap main is guarded. Use: python3 tools/roadmap_pull.py --repo .` followed by `fatal: in prepared phase, update aborted by the reference-transaction hook` and `error: task pack-refs failed`. Commit, push, and PR creation still succeed, but Git maintenance repeatedly invokes the main guard and emits a misleading failure.\", \"executor\": \"codex\", \"executor_ref\": \"01a0e44f-5300-74a2-9190-8d688a243a2a\", \"issue_id\": \"issue:c7e9615218ca4829b7b7969e0236056b\", \"observed_at_ms\": 1790537342364, \"origin_run_id\": null, \"origin_work_item_id\": \"wi:d6185f8fb88d466f907814bf6125890e\", \"repo\": null}",
        "created_at": "2026-09-27T21:04:01Z"
      },
      {
        "evidence_id": 1030,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:207aca3b228641829796ea8ca830d689",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"git-guard\", \"description\": \"Git guard on codex-roadmap blocks or partially interferes with git fetch/pack-refs during clean worktree setup: command emitted 'BLOCKED: codex-roadmap main is guarded' and 'fatal: in prepared phase, update aborted by reference-transaction hook', yet worktree creation continued and printed a path. This creates ambiguous state and slows safe persistence workflows. Guard should clearly allow safe read/fetch/worktree operations or fail atomically with unambiguous status.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:207aca3b228641829796ea8ca830d689\", \"observed_at_ms\": 1790530805041, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:06:30Z"
      },
      {
        "evidence_id": 1055,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:8c7c0fe3a3a54728ba7b5b3047add866",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Il guard Git di codex-roadmap produce attrito ricorrente su operazioni legittime: BLOCKED main guarded, reference-transaction hook, pack-refs e runtime/worktree drift compaiono ripetutamente durante l'orchestrazione. Rendere il percorso guarded più atomico e meno invasivo senza indebolire la protezione del main.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:8c7c0fe3a3a54728ba7b5b3047add866\", \"observed_at_ms\": 1790541648668, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:11:33Z"
      },
      {
        "evidence_id": 1181,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "blocked_reconcile",
        "label": "The Git guard pack-refs warning remains reproducible, but no external prerequisite blocks a focused source fix.",
        "uri": null,
        "value_json": "\"The Git guard pack-refs warning remains reproducible, but no external prerequisite blocks a focused source fix.\"",
        "created_at": "2026-09-27T22:23:04.087114Z"
      },
      {
        "evidence_id": 1232,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:0c698ff35c124287bafcd3b4d1e422d3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"git-hooks\", \"description\": \"Creating and committing an isolated codex-roadmap task branch triggers the main-branch reference-transaction guard during Git pack-refs: it prints “BLOCKED: codex-roadmap main is guarded” and “task pack-refs failed” even though the worktree, commit, and push ultimately succeed. This is noisy and fragile because routine branch/ref maintenance is being intercepted as if it were a protected main update.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0c698ff35c124287bafcd3b4d1e422d3\", \"observed_at_ms\": 1790548234666, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-27T22:32:30Z"
      },
      {
        "evidence_id": 1694,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:ffeef4922e464a5198b6b1dce5b4351a",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": null, \"description\": \"During roadmap reconciliation, git fetch origin main received commit 61f620f5 but the codex-roadmap protected reference-transaction hook rejected the ref update in prepared phase while git fetch returned exit code 0; local main stayed 113 commits behind. Canonical readback had to use FETCH_HEAD directly.\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:ffeef4922e464a5198b6b1dce5b4351a\", \"observed_at_ms\": 1790583833137, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T11:27:01Z"
      },
      {
        "evidence_id": 2055,
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "evidence_kind": "issue_inbox",
        "label": "issue:492328a0665244408f7d30153424224f",
        "uri": "codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"code_location\": null, \"description\": \"Nel worktree isolato chatgpt-rdc-supervisor task/wi-9bed381f-normal-chrome, git fetch origin task/wi-5681590a-normal-chrome viene bloccato dal reference-transaction hook con 'refs/heads/main is single-writer protected' durante pack-refs, anche se il comando non aggiorna main; impedisce il readback sicuro delle modifiche concorrenti.\", \"executor\": null, \"executor_ref\": \"01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"issue_id\": \"issue:492328a0665244408f7d30153424224f\", \"observed_at_ms\": 1790688641584, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T08:09:04Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "df37992017b14cccae43c47d1a1873aa",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "event_key": "c2-schedule-00b0c8955aee2a6bfdaae8c2eb90c17d",
        "attempt": 1,
        "executor": "codex",
        "state": "failed",
        "lease_until": 0.0,
        "worker_ref": null,
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"codex\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"GPT-5.6 Terra\", \"pre_migration_retirement\": {\"checkpoint_commit\": null, \"classification\": \"historical-only\", \"lease_until\": 1790446947.3880148, \"previous_state\": \"failed\", \"worker_ref\": \"c2-run:df37992017b14cccae43c47d1a1873aa\"}, \"project_url\": null, \"prompt_id\": \"705998\", \"reasoning\": \"medium\", \"repo\": \"gernalix/codex-roadmap\", \"resources_json\": \"[\\\"c2-supervision-control-plane\\\"]\", \"work_item_id\": \"wi:f2d5d81a952b47b1bd4fa4c07d175265\", \"worktree\": \"/home/daniele/.local/share/c2-supervisor/worktrees/f2d5-git-guard\"}",
        "created_at": 1790446804.8812366
      }
    ],
    "issue_work_item_links": [
      {
        "issue_id": "issue:b11d618912804f8786e09ae33018a6f9",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-26T21:28:37Z"
      },
      {
        "issue_id": "issue:00f7243db2ef473db2cc53354eaec3e3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-26T23:01:00Z"
      },
      {
        "issue_id": "issue:b6579643c5984c3d8db6a75feaf6f1a3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T00:12:33Z"
      },
      {
        "issue_id": "issue:9d2361074d164f6b98e13218e59f92ae",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T05:09:10Z"
      },
      {
        "issue_id": "issue:bd849e1b8f894f468540214e1efe103d",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T09:15:38Z"
      },
      {
        "issue_id": "issue:207aca3b228641829796ea8ca830d689",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T17:40:05Z"
      },
      {
        "issue_id": "issue:1b9f028cad584d0daf9acff37ece81f0",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T17:53:48Z"
      },
      {
        "issue_id": "issue:9e4b0db73d9e4f8f8e053a7feada06be",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T18:45:00Z"
      },
      {
        "issue_id": "issue:ccbe17eb77dd4d35950eebd640e5334e",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T18:53:03Z"
      },
      {
        "issue_id": "issue:85bef1a0eda24078bf15c5d89b9318ba",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T18:53:04Z"
      },
      {
        "issue_id": "issue:b8f46a6ad970453cb15693a1bce8a5f5",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T18:59:00Z"
      },
      {
        "issue_id": "issue:65bd6292e9214d59a0dd46a5629a44e5",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T19:19:42Z"
      },
      {
        "issue_id": "issue:c7e9615218ca4829b7b7969e0236056b",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T19:29:02Z"
      },
      {
        "issue_id": "issue:8c7c0fe3a3a54728ba7b5b3047add866",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T20:40:48Z"
      },
      {
        "issue_id": "issue:0c698ff35c124287bafcd3b4d1e422d3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-27T22:30:34Z"
      },
      {
        "issue_id": "issue:ffeef4922e464a5198b6b1dce5b4351a",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-28T08:23:53Z"
      },
      {
        "issue_id": "issue:492328a0665244408f7d30153424224f",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "matched",
        "created_at": "2026-09-29T13:30:41Z"
      },
      {
        "issue_id": "issue:b11d618912804f8786e09ae33018a6f9",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-26T21:28:37Z"
      },
      {
        "issue_id": "issue:00f7243db2ef473db2cc53354eaec3e3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-26T23:01:00Z"
      },
      {
        "issue_id": "issue:b6579643c5984c3d8db6a75feaf6f1a3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T00:12:33Z"
      },
      {
        "issue_id": "issue:9d2361074d164f6b98e13218e59f92ae",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T05:09:10Z"
      },
      {
        "issue_id": "issue:bd849e1b8f894f468540214e1efe103d",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T09:15:38Z"
      },
      {
        "issue_id": "issue:207aca3b228641829796ea8ca830d689",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T17:40:05Z"
      },
      {
        "issue_id": "issue:1b9f028cad584d0daf9acff37ece81f0",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T17:53:48Z"
      },
      {
        "issue_id": "issue:9e4b0db73d9e4f8f8e053a7feada06be",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T18:45:00Z"
      },
      {
        "issue_id": "issue:ccbe17eb77dd4d35950eebd640e5334e",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T18:53:03Z"
      },
      {
        "issue_id": "issue:85bef1a0eda24078bf15c5d89b9318ba",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T18:53:04Z"
      },
      {
        "issue_id": "issue:b8f46a6ad970453cb15693a1bce8a5f5",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T18:59:00Z"
      },
      {
        "issue_id": "issue:65bd6292e9214d59a0dd46a5629a44e5",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T19:19:42Z"
      },
      {
        "issue_id": "issue:c7e9615218ca4829b7b7969e0236056b",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T19:29:02Z"
      },
      {
        "issue_id": "issue:8c7c0fe3a3a54728ba7b5b3047add866",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T20:40:48Z"
      },
      {
        "issue_id": "issue:0c698ff35c124287bafcd3b4d1e422d3",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-27T22:30:34Z"
      },
      {
        "issue_id": "issue:ffeef4922e464a5198b6b1dce5b4351a",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-28T08:23:53Z"
      },
      {
        "issue_id": "issue:492328a0665244408f7d30153424224f",
        "work_item_id": "wi:f2d5d81a952b47b1bd4fa4c07d175265",
        "role": "decision",
        "created_at": "2026-09-29T13:30:41Z"
      }
    ]
  }
]
```
