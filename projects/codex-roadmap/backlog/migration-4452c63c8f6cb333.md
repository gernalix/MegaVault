# Ordinare i batch C2 rispettando le dipendenze

<!-- migration-4452c63c8f6cb333 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:4dcb24e3bbe4418984d8d6760033ea5b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Ordinare i batch C2 rispettando le dipendenze

Calcolare il riordino topologico valido più vicino all’ordine preferito dall’utente e spiegare le correzioni necessarie.

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
      "work_item_id": "wi:4dcb24e3bbe4418984d8d6760033ea5b",
      "parent_id": null,
      "kind": "task",
      "title": "Ordinare i batch C2 rispettando le dipendenze",
      "objective": "Calcolare il riordino topologico valido più vicino all’ordine preferito dall’utente e spiegare le correzioni necessarie.",
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
        "work_item_id": "wi:4dcb24e3bbe4418984d8d6760033ea5b",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2159,
        "work_item_id": "wi:4dcb24e3bbe4418984d8d6760033ea5b",
        "evidence_kind": "issue_inbox",
        "label": "issue:6932461b62074774b23586d4ce929cab",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Definire il motore di riordino batch C2 dependency-aware con best effort: il drag esprime un ordine preferito, ma il sistema deve calcolare automaticamente il più vicino ordine topologico valido, spostando davanti le dipendenze necessarie e mostrando un warning esplicativo delle correzioni effettuate.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:6932461b62074774b23586d4ce929cab\", \"observed_at_ms\": 1790720088300, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T10:23:46Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:6932461b62074774b23586d4ce929cab",
        "work_item_id": "wi:4dcb24e3bbe4418984d8d6760033ea5b",
        "role": "decision",
        "created_at": "2026-09-29T22:14:48Z"
      }
    ]
  }
]
```
