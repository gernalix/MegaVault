# Improve roadmap command failure diagnostics

<!-- migration-6e61fc074ce36caa -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:0575e6982b1e4c32978bb76c45796f1e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Improve roadmap command failure diagnostics

Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: command sequence roadmap_pull.py --repo . followed by sqlite3 failed with exit code 2 and no useful output, forcing a later retry using the SQLite query directly. Capture as avoidable retry/diagnostic friction; improve command construction/error surfacing so failures explain the exact cause and do not require redundant reruns.

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
      "work_item_id": "wi:0575e6982b1e4c32978bb76c45796f1e",
      "parent_id": null,
      "kind": "task",
      "title": "Improve roadmap command failure diagnostics",
      "objective": "Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: command sequence roadmap_pull.py --repo . followed by sqlite3 failed with exit code 2 and no useful output, forcing a later retry using the SQLite query directly. Capture as avoidable retry/diagnostic friction; improve command construction/error surfacing so failures explain the exact cause and do not require redundant reruns.",
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
        "work_item_id": "wi:0575e6982b1e4c32978bb76c45796f1e",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1013,
        "work_item_id": "wi:0575e6982b1e4c32978bb76c45796f1e",
        "evidence_kind": "issue_inbox",
        "label": "issue:0b61a34019e746b0ae6715fb416e284a",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Retrospective friction from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: command sequence roadmap_pull.py --repo . followed by sqlite3 failed with exit code 2 and no useful output, forcing a later retry using the SQLite query directly. Capture as avoidable retry/diagnostic friction; improve command construction/error surfacing so failures explain the exact cause and do not require redundant reruns.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0b61a34019e746b0ae6715fb416e284a\", \"observed_at_ms\": 1790516612789, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:05:30Z"
      },
      {
        "evidence_id": 1446,
        "work_item_id": "wi:0575e6982b1e4c32978bb76c45796f1e",
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
        "issue_id": "issue:0b61a34019e746b0ae6715fb416e284a",
        "work_item_id": "wi:0575e6982b1e4c32978bb76c45796f1e",
        "role": "decision",
        "created_at": "2026-09-27T13:43:32Z"
      }
    ]
  }
]
```
