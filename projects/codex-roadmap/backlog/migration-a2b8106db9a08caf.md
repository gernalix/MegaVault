# Regression: Ripristinare C2 dopo crash Chrome e reboot del 30 settembre

<!-- migration-a2b8106db9a08caf -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:1f096c5c7ff3457495db8c6684f9df22`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Ripristinare C2 dopo crash Chrome e reboot del 30 settembre

C2 recovery dopo reboot: c2-master-watcher.timer enabled ma NextElapseUSecMonotonic=infinity, ultimo trigger precedente a riattivazione; runtime bloccato da stale_or_expired_supervisor e triage ricade su CDP Chrome in timeout invece del fallback nativo. Evidenza journal 30 settembre 08:43-08:54 CEST.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Ripristinare C2 dopo crash Chrome e reboot del 30 settembre",
      "objective": "C2 recovery dopo reboot: c2-master-watcher.timer enabled ma NextElapseUSecMonotonic=infinity, ultimo trigger precedente a riattivazione; runtime bloccato da stale_or_expired_supervisor e triage ricade su CDP Chrome in timeout invece del fallback nativo. Evidenza journal 30 settembre 08:43-08:54 CEST.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T11:57:51Z",
      "updated_at": "2026-09-30T11:57:51Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
        "to_work_item_id": "wi:4b72d5af2a32424cb0a5172b19033207",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T11:57:51Z",
        "actor": "c2-issue-triage",
        "note": "issue:1cb875ca19df4d8c9d96c55385f52c95"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2249,
        "work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
        "evidence_kind": "issue_inbox",
        "label": "issue:1cb875ca19df4d8c9d96c55385f52c95",
        "uri": "codex://threads/01a0f113-cf52-75f1-8d72-43d2ebdd0255",
        "value_json": "{\"chat_url\": \"codex://threads/01a0f113-cf52-75f1-8d72-43d2ebdd0255\", \"code_location\": null, \"description\": \"C2 recovery dopo reboot: c2-master-watcher.timer enabled ma NextElapseUSecMonotonic=infinity, ultimo trigger precedente a riattivazione; runtime bloccato da stale_or_expired_supervisor e triage ricade su CDP Chrome in timeout invece del fallback nativo. Evidenza journal 30 settembre 08:43-08:54 CEST.\", \"executor\": null, \"executor_ref\": \"01a0f113-cf52-75f1-8d72-43d2ebdd0255\", \"issue_id\": \"issue:1cb875ca19df4d8c9d96c55385f52c95\", \"observed_at_ms\": 1790751422420, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T11:57:51Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:1cb875ca19df4d8c9d96c55385f52c95",
        "work_item_id": "wi:1f096c5c7ff3457495db8c6684f9df22",
        "role": "decision",
        "created_at": "2026-09-30T06:57:02Z"
      }
    ]
  }
]
```
