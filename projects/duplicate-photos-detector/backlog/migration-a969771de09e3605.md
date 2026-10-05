# Investigate Fedora Service · user:duplicate-photos-detector-watch.service recurring DOWN incident

<!-- migration-a969771de09e3605 -->

Migrated project backlog. Project: **duplicate-photos-detector**; project_id: 102.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 102, 15.

Provenance: `wi:5ed7c05c167844dc9336a495c2f0f28f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Rendere operativo duplicate-photos-detector su Fedora

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:duplicate-photos-detector-watch.service (id 62)
Heartbeat: 2026-09-30 06:26:24.786 (row 685518)
Failure context: No heartbeat in the time window

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "102",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "102",
        "15"
      ]
    },
    "source": {
      "work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Rendere operativo duplicate-photos-detector su Fedora",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:duplicate-photos-detector-watch.service (id 62)\nHeartbeat: 2026-09-30 06:26:24.786 (row 685518)\nFailure context: No heartbeat in the time window",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": "92",
      "project_name": "github-autosync",
      "repo": "gernalix/duplicate-photos-detector",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T12:10:08Z",
      "updated_at": "2026-09-30T12:10:08Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
        "to_work_item_id": "prompt:817056",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T12:10:08Z",
        "actor": "c2-issue-triage",
        "note": "issue:59073652a7c981ad7539a39068c062d2"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2259,
        "work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
        "evidence_kind": "issue_inbox",
        "label": "issue:59073652a7c981ad7539a39068c062d2",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:duplicate-photos-detector-watch.service (id 62)\\nHeartbeat: 2026-09-30 06:26:24.786 (row 685518)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:59073652a7c981ad7539a39068c062d2\", \"observed_at_ms\": 1790749946275, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:59073652a7c981ad7539a39068c062d2",
        "work_item_id": "wi:5ed7c05c167844dc9336a495c2f0f28f",
        "role": "decision",
        "created_at": "2026-09-30T06:32:26Z"
      }
    ]
  }
]
```
