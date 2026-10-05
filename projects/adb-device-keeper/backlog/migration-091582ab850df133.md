# Investigate Fedora Service · user:adb-device-keeper.service recurring DOWN incident

<!-- migration-091582ab850df133 -->

Migrated project backlog. Project: **adb-device-keeper**; project_id: 95.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 95.

Provenance: `wi:75b9dbade6c74a869c0a6278492833ee`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate adb-device-keeper.service (id 54) DOWN alert

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:adb-device-keeper.service (id 54)
Heartbeat: 2026-09-30 06:26:24.191 (row 685515)
Failure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "95",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "95"
      ]
    },
    "source": {
      "work_item_id": "wi:75b9dbade6c74a869c0a6278492833ee",
      "parent_id": null,
      "kind": "task",
      "title": "Investigate adb-device-keeper.service (id 54) DOWN alert",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:adb-device-keeper.service (id 54)\nHeartbeat: 2026-09-30 06:26:24.191 (row 685515)\nFailure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.",
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
        "work_item_id": "wi:75b9dbade6c74a869c0a6278492833ee",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2257,
        "work_item_id": "wi:75b9dbade6c74a869c0a6278492833ee",
        "evidence_kind": "issue_inbox",
        "label": "issue:75acbdbb03332865de5052abb26c77df",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:adb-device-keeper.service (id 54)\\nHeartbeat: 2026-09-30 06:26:24.191 (row 685515)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:75acbdbb03332865de5052abb26c77df\", \"observed_at_ms\": 1790749945048, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:75acbdbb03332865de5052abb26c77df",
        "work_item_id": "wi:75b9dbade6c74a869c0a6278492833ee",
        "role": "decision",
        "created_at": "2026-09-30T06:32:25Z"
      }
    ]
  }
]
```
