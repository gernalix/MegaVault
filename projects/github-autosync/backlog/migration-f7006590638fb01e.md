# Avoid routine tested-head drift during C2 integration

<!-- migration-f7006590638fb01e -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 92.

Provenance: `wi:27a7241e16b341278b2359267bfad4f5`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Avoid routine tested-head drift during C2 integration

Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: normal integration flow hit tested_head_drift and required additional reconciliation work. The guard itself is safety-positive, but reaching it during routine supervisor/checkpoint/integration sequencing indicates a possible race or coordination inefficiency between tested head, checkpoint advancement, and integration. Analyze how to prevent avoidable drift without weakening the fail-closed invariant.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "92",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "92"
      ]
    },
    "source": {
      "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
      "parent_id": null,
      "kind": "task",
      "title": "Avoid routine tested-head drift during C2 integration",
      "objective": "Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: normal integration flow hit tested_head_drift and required additional reconciliation work. The guard itself is safety-positive, but reaching it during routine supervisor/checkpoint/integration sequencing indicates a possible race or coordination inefficiency between tested head, checkpoint advancement, and integration. Analyze how to prevent avoidable drift without weakening the fail-closed invariant.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:05:31Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1017,
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "evidence_kind": "issue_inbox",
        "label": "issue:164f804a7b934ab095de248b6d98b2d3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: normal integration flow hit tested_head_drift and required additional reconciliation work. The guard itself is safety-positive, but reaching it during routine supervisor/checkpoint/integration sequencing indicates a possible race or coordination inefficiency between tested head, checkpoint advancement, and integration. Analyze how to prevent avoidable drift without weakening the fail-closed invariant.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:164f804a7b934ab095de248b6d98b2d3\", \"observed_at_ms\": 1790516642871, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:05:31Z"
      },
      {
        "evidence_id": 1699,
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "evidence_kind": "issue_inbox",
        "label": "issue:edaf52952878414e80a591af2f299a4a",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": null, \"description\": \"PR #3777 for prompt 484338 had required test failures; after focused repairs were committed and pushed on its existing task branch, roadmap_finish returned tested_head_drift. The dedicated queue path calls status before its exact-head update branch and cannot refresh the C2-tested-head marker for an explicitly verified newer head.\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:edaf52952878414e80a591af2f299a4a\", \"observed_at_ms\": 1790585165638, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T11:39:01Z"
      },
      {
        "evidence_id": 1892,
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      },
      {
        "evidence_id": 2456,
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "evidence_kind": "issue_inbox",
        "label": "issue:be92034eca7a4c1e8adebba9f91af81a",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 integration optimization from the acceleration chat: PR 7293 had all checks green, but a newer main branch required manual reintegration before completion. Add a standard green-PR refresh operation that updates the isolated worktree to current main, reapplies the already tested change, reruns only impacted checks, preserves provenance, and proceeds automatically when the refresh is clean.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:be92034eca7a4c1e8adebba9f91af81a\", \"observed_at_ms\": 1790784996896, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:edaf52952878414e80a591af2f299a4a",
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "role": "matched",
        "created_at": "2026-09-28T08:46:05Z"
      },
      {
        "issue_id": "issue:164f804a7b934ab095de248b6d98b2d3",
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "role": "decision",
        "created_at": "2026-09-27T13:44:02Z"
      },
      {
        "issue_id": "issue:edaf52952878414e80a591af2f299a4a",
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "role": "decision",
        "created_at": "2026-09-28T08:46:05Z"
      },
      {
        "issue_id": "issue:be92034eca7a4c1e8adebba9f91af81a",
        "work_item_id": "wi:27a7241e16b341278b2359267bfad4f5",
        "role": "decision",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ]
  }
]
```
