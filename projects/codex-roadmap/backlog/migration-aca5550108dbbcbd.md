# Review C2 workflow simplification audit

<!-- migration-aca5550108dbbcbd -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:3476c751c7734c9fb11ae4d737143ee3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Review C2 workflow simplification audit

https://github.com/gernalix/codex-roadmap/blob/85fd430f72cb593306e9332c976898a3650a1b73/audits/2026-09-27-c2-workflow-simplification-audit.md

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
      "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
      "parent_id": null,
      "kind": "task",
      "title": "Review C2 workflow simplification audit",
      "objective": "https://github.com/gernalix/codex-roadmap/blob/85fd430f72cb593306e9332c976898a3650a1b73/audits/2026-09-27-c2-workflow-simplification-audit.md",
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
      "created_at": "2026-09-27T21:03:12Z",
      "updated_at": "2026-09-28T06:45:03Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 987,
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "evidence_kind": "issue_inbox",
        "label": "issue:a71f3e2d9b4c48c58b5d9e1f3a7c6d20",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"https://github.com/gernalix/codex-roadmap/blob/85fd430f72cb593306e9332c976898a3650a1b73/audits/2026-09-27-c2-workflow-simplification-audit.md\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:a71f3e2d9b4c48c58b5d9e1f3a7c6d20\", \"observed_at_ms\": 1790534157412, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/codex-roadmap\"}",
        "created_at": "2026-09-27T21:03:12Z"
      },
      {
        "evidence_id": 1252,
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "evidence_kind": "issue_inbox",
        "label": "issue:36b451d40cd14ff5aa02d36e04306215",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Separare dipendenze reali e burocrazia\\nRidurre il task al minimo\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:36b451d40cd14ff5aa02d36e04306215\", \"observed_at_ms\": 1790549314668, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T22:50:48Z"
      },
      {
        "evidence_id": 1449,
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:03Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:36b451d40cd14ff5aa02d36e04306215",
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "role": "matched",
        "created_at": "2026-09-27T22:48:34Z"
      },
      {
        "issue_id": "issue:a71f3e2d9b4c48c58b5d9e1f3a7c6d20",
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "role": "decision",
        "created_at": "2026-09-27T18:35:57Z"
      },
      {
        "issue_id": "issue:36b451d40cd14ff5aa02d36e04306215",
        "work_item_id": "wi:3476c751c7734c9fb11ae4d737143ee3",
        "role": "decision",
        "created_at": "2026-09-27T22:48:34Z"
      }
    ]
  }
]
```
