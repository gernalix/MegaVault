# Progettare la preemption cooperativa dei batch C2

<!-- migration-c1cef5d8aaa006d9 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:7eda9dc5a7c84a1bb18b2987eb447ce1`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Progettare la preemption cooperativa dei batch C2

Definire come gli executor dei batch meno prioritari raggiungono un safe checkpoint, persistono e pubblicano lo stato e rilasciano le risorse prima di lasciare partire un batch prioritario.

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
      "work_item_id": "wi:7eda9dc5a7c84a1bb18b2987eb447ce1",
      "parent_id": null,
      "kind": "task",
      "title": "Progettare la preemption cooperativa dei batch C2",
      "objective": "Definire come gli executor dei batch meno prioritari raggiungono un safe checkpoint, persistono e pubblicano lo stato e rilasciano le risorse prima di lasciare partire un batch prioritario.",
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
        "work_item_id": "wi:7eda9dc5a7c84a1bb18b2987eb447ce1",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2158,
        "work_item_id": "wi:7eda9dc5a7c84a1bb18b2987eb447ce1",
        "evidence_kind": "issue_inbox",
        "label": "issue:b81f2b299f424913b0f0de047475c828",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Progettare la preemption cooperativa dei batch C2: quando l'utente promuove un batch sopra batch già RUNNING, gli executor interessati devono fermarsi al primo safe checkpoint, persistere stato/commit/push e rilasciare le risorse necessarie, così il nuovo batch prioritario può partire senza interrompere operazioni non checkpointabili.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b81f2b299f424913b0f0de047475c828\", \"observed_at_ms\": 1790720088077, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T10:23:46Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:b81f2b299f424913b0f0de047475c828",
        "work_item_id": "wi:7eda9dc5a7c84a1bb18b2987eb447ce1",
        "role": "decision",
        "created_at": "2026-09-29T22:14:48Z"
      }
    ]
  }
]
```
