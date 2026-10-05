# Route web executor C2 intake through the canonical writer

<!-- migration-be43276e244474cb -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:1c989b834905489993c3ab03f88ba06c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Route web executor C2 intake through the canonical writer

Prevent web/ChatGPT executors from directly mutating local roadmap.sqlite for new C2 work items. Submit intake through the fenced single writer, wait for applied receipt, read back the canonical work_item_id, then use that ID for executor_started and manual order. Preserve/recover local-only task content and test the rejected-dispatch path without overwriting local data.

status: pending

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
      "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
      "parent_id": null,
      "kind": "task",
      "title": "Route web executor C2 intake through the canonical writer",
      "objective": "Prevent web/ChatGPT executors from directly mutating local roadmap.sqlite for new C2 work items. Submit intake through the fenced single writer, wait for applied receipt, read back the canonical work_item_id, then use that ID for executor_started and manual order. Preserve/recover local-only task content and test the rejected-dispatch path without overwriting local data.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 20,
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
      "created_at": "2026-09-27T23:05:09Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "c2"
      },
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "intake"
      },
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "single-writer"
      },
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1262,
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "evidence_kind": "issue_inbox",
        "label": "issue:2895b40450234a85b2b11f41af208ae0",
        "uri": "codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"code_location\": null, \"description\": \"A ChatGPT web executor used local c2_intake to add wi:b1f32409733b4978baacdd41ba4698f5 (Codex human view unread messages) directly into canonical checkout roadmap.sqlite without a writer receipt. Git main became dirty/behind and guarded pull blocked; its executor_started Issue #3232 then rejected work_item_not_found, and global order #3234 rejected that local-only ID. Preserved exact local DB at /home/daniele/.local/share/c2-recovery-20260928/roadmap-local-before-3234.sqlite. Intake/executor UI must route through fenced single writer and verify canonical ID before dispatch.\", \"executor\": null, \"executor_ref\": \"01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"issue_id\": \"issue:2895b40450234a85b2b11f41af208ae0\", \"observed_at_ms\": 1790550149553, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T23:05:09Z"
      },
      {
        "evidence_id": 1380,
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "evidence_kind": "issue_inbox",
        "label": "issue:e660537df802440eb014454e745260f0",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"tools/c2_intake.py\", \"description\": \"c2_intake.py add mutates roadmap.sqlite locally even though the C2 contract requires canonical roadmap mutations through the single writer. A work item created this way is invisible to the GitHub writer, causing a subsequent c2_executor_start mutation to fail with executor_start_work_item_not_found. The intake path should either submit through the writer or clearly prevent direct canonical use.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:e660537df802440eb014454e745260f0\", \"observed_at_ms\": 1790564993588, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-28T03:16:58Z"
      },
      {
        "evidence_id": 1895,
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:e660537df802440eb014454e745260f0",
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "role": "matched",
        "created_at": "2026-09-28T03:09:53Z"
      },
      {
        "issue_id": "issue:2895b40450234a85b2b11f41af208ae0",
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "role": "decision",
        "created_at": "2026-09-27T23:02:29Z"
      },
      {
        "issue_id": "issue:e660537df802440eb014454e745260f0",
        "work_item_id": "wi:1c989b834905489993c3ab03f88ba06c",
        "role": "decision",
        "created_at": "2026-09-28T03:09:53Z"
      }
    ]
  }
]
```
