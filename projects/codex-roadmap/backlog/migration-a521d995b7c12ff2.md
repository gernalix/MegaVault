# C2 dashboard reads legacy semantic-watcher state instead of current Master Watcher schema

<!-- migration-a521d995b7c12ff2 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:64ddc28d325c4e3da453bc822f27066f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 dashboard reads legacy semantic-watcher state instead of current Master Watcher schema

La dashboard legge file e stati superati e può mostrare un allarme mentre il Master Watcher si sta riprendendo. Occorre allineare la lettura allo stato attuale per evitare informazioni fuorvianti.

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
      "work_item_id": "wi:64ddc28d325c4e3da453bc822f27066f",
      "parent_id": null,
      "kind": "task",
      "title": "C2 dashboard reads legacy semantic-watcher state instead of current Master Watcher schema",
      "objective": "La dashboard legge file e stati superati e può mostrare un allarme mentre il Master Watcher si sta riprendendo. Occorre allineare la lettura allo stato attuale per evitare informazioni fuorvianti.",
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
      "created_at": "2026-09-30T04:48:27Z",
      "updated_at": "2026-09-30T04:48:27Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:64ddc28d325c4e3da453bc822f27066f",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:64ddc28d325c4e3da453bc822f27066f",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2009,
        "work_item_id": "wi:64ddc28d325c4e3da453bc822f27066f",
        "evidence_kind": "issue_inbox",
        "label": "issue:0178710fadcb4e2a92894611b943a86d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Dashboard C2 runtime incompatibile col Master Watcher: /home/daniele/.local/bin/c2-roadmap-status legge ancora c2-roadmap-semantic-watcher/{semantic-state,heartbeat}.json e usa stati legacy (waiting_gate/complete_wait), mentre il watcher attivo usa /home/daniele/.local/share/c2-master-watcher/state.json e schema working/recovering/waiting_external/stalled/needs_user/degraded/globally_quiescent/stopped. Evidenza: alle 11:33 il Master Watcher ha prodotto status=recovering, wake_result=started, ma la dashboard alle 11:34 mostrava rosso RICHIEDE CONTROLLO e watcher AI non disponibile. Impatto: stato utente fuorviante e possibili falsi allarmi.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0178710fadcb4e2a92894611b943a86d\", \"observed_at_ms\": 1790674500815, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T04:48:27Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:0178710fadcb4e2a92894611b943a86d",
        "work_item_id": "wi:64ddc28d325c4e3da453bc822f27066f",
        "role": "decision",
        "created_at": "2026-09-29T09:35:00Z"
      }
    ]
  }
]
```
