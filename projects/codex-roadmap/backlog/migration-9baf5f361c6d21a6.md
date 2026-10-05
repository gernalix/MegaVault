# Separare la presenza dell’executor dallo stato del task C2

<!-- migration-9baf5f361c6d21a6 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:fefff747c8eb419498222d5ea53a7340`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Separare la presenza dell’executor dallo stato del task C2

Evitare che un work item sia mostrato running senza run o executor effettivo e definire una correzione autorevole che consenta di riaccodare il lavoro ancora valido.

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
      "work_item_id": "wi:fefff747c8eb419498222d5ea53a7340",
      "parent_id": null,
      "kind": "task",
      "title": "Separare la presenza dell’executor dallo stato del task C2",
      "objective": "Evitare che un work item sia mostrato running senza run o executor effettivo e definire una correzione autorevole che consenta di riaccodare il lavoro ancora valido.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T10:25:45Z",
      "updated_at": "2026-09-30T10:25:45Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:fefff747c8eb419498222d5ea53a7340",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2174,
        "work_item_id": "wi:fefff747c8eb419498222d5ea53a7340",
        "evidence_kind": "issue_inbox",
        "label": "issue:5926ab5c39d24eeba1e2f84ce8a75aa4",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 lifecycle fragility: a manual/non-run work item can project status=running after executor_started even when no work_item_run, lease or checkpoint exists, but the canonical lifecycle exposes no direct running→pending correction. Recovery currently requires cancelling the false-running shell and recreating/requeuing the still-valid work. C3 should model executor presence separately from task readiness and support an immediate authoritative demotion/requeue path.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:5926ab5c39d24eeba1e2f84ce8a75aa4\", \"observed_at_ms\": 1790726478232, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:5926ab5c39d24eeba1e2f84ce8a75aa4",
        "work_item_id": "wi:fefff747c8eb419498222d5ea53a7340",
        "role": "decision",
        "created_at": "2026-09-30T00:01:18Z"
      }
    ]
  }
]
```
