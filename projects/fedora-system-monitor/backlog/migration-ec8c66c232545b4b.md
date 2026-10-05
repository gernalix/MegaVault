# Investigate Fedora Service · user:espanso.service recurring DOWN incident

<!-- migration-ec8c66c232545b4b -->

Migrated project backlog. Project: **fedora-system-monitor**; project_id: 15.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 15.

Provenance: `wi:2036610c7e9b460fbf2e82e615bdf128`, `issue:0af3a26f7f5b4c8c80670ae4c873558e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate espanso.service (id 52) DOWN alert

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:espanso.service (id 52)
Heartbeat: 2026-09-30 06:26:25.001 (row 685519)
Failure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.

status: pending

### issue:0af3a26f7f5b4c8c80670ae4c873558e

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:espanso.service (id 52)
Heartbeat: 2026-10-01 12:11:48.648 (row 743233)
Failure context: user:espanso.service: inactive/dead

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "15",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "15"
      ]
    },
    "source": {
      "work_item_id": "wi:2036610c7e9b460fbf2e82e615bdf128",
      "parent_id": null,
      "kind": "task",
      "title": "Investigate espanso.service (id 52) DOWN alert",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:espanso.service (id 52)\nHeartbeat: 2026-09-30 06:26:25.001 (row 685519)\nFailure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.",
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
        "work_item_id": "wi:2036610c7e9b460fbf2e82e615bdf128",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2260,
        "work_item_id": "wi:2036610c7e9b460fbf2e82e615bdf128",
        "evidence_kind": "issue_inbox",
        "label": "issue:33bc915fd494597e7934123e4acd2973",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:espanso.service (id 52)\\nHeartbeat: 2026-09-30 06:26:25.001 (row 685519)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:33bc915fd494597e7934123e4acd2973\", \"observed_at_ms\": 1790749946447, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:33bc915fd494597e7934123e4acd2973",
        "work_item_id": "wi:2036610c7e9b460fbf2e82e615bdf128",
        "role": "decision",
        "created_at": "2026-09-30T06:32:26Z"
      }
    ]
  },
  {
    "routing": {
      "project": "15",
      "reason": "monitor/service ownership from explicit source text",
      "related_projects": [
        "15"
      ]
    },
    "source": {
      "issue_id": "issue:0af3a26f7f5b4c8c80670ae4c873558e",
      "description": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:espanso.service (id 52)\nHeartbeat: 2026-10-01 12:11:48.648 (row 743233)\nFailure context: user:espanso.service: inactive/dead",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790856910044,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T12:15:10Z"
    },
    "issue_work_item_links": []
  }
]
```
