# Allineare c2_control alle operazioni execution override

<!-- migration-7dd6682a391a6fdd -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:b30b76a7df1e4ffb9b9f2945fbbefe5e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Allineare c2_control alle operazioni execution override

Aggiungere set_execution_override e clear_execution_override all’elenco OPERATIONS del client tools/c2_control.py quando risultano già supportate e fenced da tools/c2_mutations.py. Verificare che il percorso ufficiale non richieda mutation costruite manualmente.

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
      "work_item_id": "wi:b30b76a7df1e4ffb9b9f2945fbbefe5e",
      "parent_id": null,
      "kind": "task",
      "title": "Allineare c2_control alle operazioni execution override",
      "objective": "Aggiungere set_execution_override e clear_execution_override all’elenco OPERATIONS del client tools/c2_control.py quando risultano già supportate e fenced da tools/c2_mutations.py. Verificare che il percorso ufficiale non richieda mutation costruite manualmente.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
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
      "created_at": "2026-09-30T10:16:35Z",
      "updated_at": "2026-09-30T10:16:35Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:b30b76a7df1e4ffb9b9f2945fbbefe5e",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2154,
        "work_item_id": "wi:b30b76a7df1e4ffb9b9f2945fbbefe5e",
        "evidence_kind": "issue_inbox",
        "label": "issue:b98a0ebc363a45999035c82b355a5fbf",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 control helper tools/c2_control.py non espone set_execution_override/clear_execution_override tra OPERATIONS, mentre tools/c2_mutations.py li supporta e li tratta come operazioni supervisor-fenced. Questo obbliga i client a costruire mutation manuali proprio per il meccanismo ufficiale di priorità drain_first. Allineare il helper alle operazioni canoniche per ridurre attrito/errore.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b98a0ebc363a45999035c82b355a5fbf\", \"observed_at_ms\": 1790714823948, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T10:16:35Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:b98a0ebc363a45999035c82b355a5fbf",
        "work_item_id": "wi:b30b76a7df1e4ffb9b9f2945fbbefe5e",
        "role": "decision",
        "created_at": "2026-09-29T20:47:03Z"
      }
    ]
  }
]
```
