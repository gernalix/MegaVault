# Batch RDC temporary prompt file preparation

<!-- migration-adb19f1c359d8f7e -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:23f5aafd9abe4edba5effe14f6af0988`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Batch RDC temporary prompt file preparation

Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: preparing worker prompts through separate RDC write_file calls incurs roughly 9-11 s round-trip per small temporary prompt before worker launch. Multiple worker launches therefore serialize unnecessary preparation latency. Reduce/batch/eliminate these temporary-file write round trips where safe.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:23f5aafd9abe4edba5effe14f6af0988",
      "parent_id": null,
      "kind": "task",
      "title": "Batch RDC temporary prompt file preparation",
      "objective": "Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: preparing worker prompts through separate RDC write_file calls incurs roughly 9-11 s round-trip per small temporary prompt before worker launch. Multiple worker launches therefore serialize unnecessary preparation latency. Reduce/batch/eliminate these temporary-file write round trips where safe.",
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
      "created_at": "2026-09-27T21:05:30Z",
      "updated_at": "2026-09-28T06:45:02Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:23f5aafd9abe4edba5effe14f6af0988",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1015,
        "work_item_id": "wi:23f5aafd9abe4edba5effe14f6af0988",
        "evidence_kind": "issue_inbox",
        "label": "issue:c8881e68146f4e9f99c960097c3390ab",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: preparing worker prompts through separate RDC write_file calls incurs roughly 9-11 s round-trip per small temporary prompt before worker launch. Multiple worker launches therefore serialize unnecessary preparation latency. Reduce/batch/eliminate these temporary-file write round trips where safe.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c8881e68146f4e9f99c960097c3390ab\", \"observed_at_ms\": 1790516613177, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:05:30Z"
      },
      {
        "evidence_id": 1447,
        "work_item_id": "wi:23f5aafd9abe4edba5effe14f6af0988",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:02Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:c8881e68146f4e9f99c960097c3390ab",
        "work_item_id": "wi:23f5aafd9abe4edba5effe14f6af0988",
        "role": "decision",
        "created_at": "2026-09-27T13:43:33Z"
      }
    ]
  }
]
```
