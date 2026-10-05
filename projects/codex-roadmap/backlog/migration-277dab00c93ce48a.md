# Aggiungere una priorità canonica per i batch C2

<!-- migration-277dab00c93ce48a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:5f106b5f31c6446a87499a70c6b18d40`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Aggiungere una priorità canonica per i batch C2

Definire una priorità first-class a livello batch che governi lo scheduling dei membri, mantenendo coerenti dipendenze e preemption.

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
      "work_item_id": "wi:5f106b5f31c6446a87499a70c6b18d40",
      "parent_id": null,
      "kind": "task",
      "title": "Aggiungere una priorità canonica per i batch C2",
      "objective": "Definire una priorità first-class a livello batch che governi lo scheduling dei membri, mantenendo coerenti dipendenze e preemption.",
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
      "created_at": "2026-09-30T10:23:46Z",
      "updated_at": "2026-09-30T10:23:46Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:5f106b5f31c6446a87499a70c6b18d40",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2162,
        "work_item_id": "wi:5f106b5f31c6446a87499a70c6b18d40",
        "evidence_kind": "issue_inbox",
        "label": "issue:07af1c3c0879482b87ce3c42d9110075",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"La C2 non ha ancora una priorità P0 first-class a livello di batch: priority:p0 è per-work-item e drain_first è un override per selector. Per la nuova dashboard batch-centric serve un'entità/priorità canonica di batch che propaghi correttamente lo scheduling senza dover taggare manualmente ogni membro, preservando dipendenze e preemption.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:07af1c3c0879482b87ce3c42d9110075\", \"observed_at_ms\": 1790720597013, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T10:23:46Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:07af1c3c0879482b87ce3c42d9110075",
        "work_item_id": "wi:5f106b5f31c6446a87499a70c6b18d40",
        "role": "decision",
        "created_at": "2026-09-29T22:23:17Z"
      }
    ]
  }
]
```
