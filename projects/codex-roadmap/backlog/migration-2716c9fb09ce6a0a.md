# C2: aggiungere un comando read-only per lo stato canonico dei work item

<!-- migration-2716c9fb09ce6a0a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:5f95f420c4fa4315a6b7104adb043096`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2: aggiungere un comando read-only per lo stato canonico dei work item

Standardizzare l’accesso read-only allo stato dei task Roadmap per qualsiasi chat via RDC: introdurre un helper unico (es. c2-roadmap task-status <ID>) che nasconda percorso DB/schema/query e restituisca almeno status, progress, current_step, blockers e last_update. Obiettivo: verifica dello stato con un solo comando, senza esplorazione del repo o SQL manuale, riducendo fragilità, round-trip e costo operativo.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

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
      "work_item_id": "wi:5f95f420c4fa4315a6b7104adb043096",
      "parent_id": null,
      "kind": "task",
      "title": "C2: aggiungere un comando read-only per lo stato canonico dei work item",
      "objective": "Standardizzare l’accesso read-only allo stato dei task Roadmap per qualsiasi chat via RDC: introdurre un helper unico (es. c2-roadmap task-status <ID>) che nasconda percorso DB/schema/query e restituisca almeno status, progress, current_step, blockers e last_update. Obiettivo: verifica dello stato con un solo comando, senza esplorazione del repo o SQL manuale, riducendo fragilità, round-trip e costo operativo.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "Parked during roadmap semantic reconciliation.",
      "next_action": "Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.",
      "blocker": "Deferred pending Symphony migration/replacement decision.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:06:30Z",
      "updated_at": "2026-09-28T06:45:05Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:5f95f420c4fa4315a6b7104adb043096",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1027,
        "work_item_id": "wi:5f95f420c4fa4315a6b7104adb043096",
        "evidence_kind": "issue_inbox",
        "label": "issue:afc499a654cc488385afccc438d3264a",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Standardizzare l’accesso read-only allo stato dei task Roadmap per qualsiasi chat via RDC: introdurre un helper unico (es. c2-roadmap task-status <ID>) che nasconda percorso DB/schema/query e restituisca almeno status, progress, current_step, blockers e last_update. Obiettivo: verifica dello stato con un solo comando, senza esplorazione del repo o SQL manuale, riducendo fragilità, round-trip e costo operativo.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:afc499a654cc488385afccc438d3264a\", \"observed_at_ms\": 1790527277740, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:06:30Z"
      },
      {
        "evidence_id": 1457,
        "work_item_id": "wi:5f95f420c4fa4315a6b7104adb043096",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:05Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:afc499a654cc488385afccc438d3264a",
        "work_item_id": "wi:5f95f420c4fa4315a6b7104adb043096",
        "role": "decision",
        "created_at": "2026-09-27T16:41:17Z"
      }
    ]
  }
]
```
