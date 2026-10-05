# Investigate Fedora Service · user:prompt-history-sync.service recurring DOWN incident

<!-- migration-5bb7de146dd66221 -->

Migrated project backlog. Project: **prompt-history**; project_id: 103.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 103.

Provenance: `wi:95fcdd3fdb384eefb877627028a248fb`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate prompt-history-sync.service (id 61) DOWN alert

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:prompt-history-sync.service (id 61)
Heartbeat: 2026-09-30 06:26:25.496 (row 685522)
Failure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "103",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "103"
      ]
    },
    "source": {
      "work_item_id": "wi:95fcdd3fdb384eefb877627028a248fb",
      "parent_id": null,
      "kind": "task",
      "title": "Investigate prompt-history-sync.service (id 61) DOWN alert",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:prompt-history-sync.service (id 61)\nHeartbeat: 2026-09-30 06:26:25.496 (row 685522)\nFailure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": null,
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
        "work_item_id": "wi:95fcdd3fdb384eefb877627028a248fb",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2263,
        "work_item_id": "wi:95fcdd3fdb384eefb877627028a248fb",
        "evidence_kind": "issue_inbox",
        "label": "issue:0c787ef038d38aa4bb5848a0712f4482",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:prompt-history-sync.service (id 61)\\nHeartbeat: 2026-09-30 06:26:25.496 (row 685522)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0c787ef038d38aa4bb5848a0712f4482\", \"observed_at_ms\": 1790749947086, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:0c787ef038d38aa4bb5848a0712f4482",
        "work_item_id": "wi:95fcdd3fdb384eefb877627028a248fb",
        "role": "decision",
        "created_at": "2026-09-30T06:32:27Z"
      }
    ]
  }
]
```
