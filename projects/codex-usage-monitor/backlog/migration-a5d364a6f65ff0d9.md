# Diagnose codex-usage-monitor service failure and stale heartbeat

<!-- migration-a5d364a6f65ff0d9 -->

Migrated project backlog. Project: **codex-usage-monitor**; project_id: 8.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 8.

Provenance: `wi:0ae5cc40737b4548bd4cff4251f8d757`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Diagnose codex-usage-monitor service failure and stale heartbeat

Investigate Kuma monitor 60 DOWN at 2026-09-28 14:47:27.782 for user:codex-usage-monitor.service failed/failed and stale job freshness. Verify current service and monitor state, determine cause, apply a scoped recovery if needed, and record live readback.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "8",
      "reason": "canonical repository identity",
      "related_projects": [
        "8"
      ]
    },
    "source": {
      "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
      "parent_id": null,
      "kind": "task",
      "title": "Diagnose codex-usage-monitor service failure and stale heartbeat",
      "objective": "Investigate Kuma monitor 60 DOWN at 2026-09-28 14:47:27.782 for user:codex-usage-monitor.service failed/failed and stale job freshness. Verify current service and monitor state, determine cause, apply a scoped recovery if needed, and record live readback.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-usage-monitor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-29T13:32:00Z",
      "updated_at": "2026-09-29T13:32:00Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1740,
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "evidence_kind": "issue_inbox",
        "label": "issue:0607062d9726d6fb8abf659b92819f45",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:codex-usage-monitor.service (id 60)\\nHeartbeat: 2026-09-28 14:47:27.782 (row 608027)\\nFailure context: user:codex-usage-monitor.service: failed/failed; job freshness stale age=missings threshold=2400s\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0607062d9726d6fb8abf659b92819f45\", \"observed_at_ms\": 1790606892273, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T13:32:00Z"
      },
      {
        "evidence_id": 2241,
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "evidence_kind": "issue_inbox",
        "label": "issue:e52850eec3b12b4231615c13c6cd700c",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:codex-usage-monitor.service (id 60)\\nHeartbeat: 2026-09-30 06:26:24.383 (row 685516)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:e52850eec3b12b4231615c13c6cd700c\", \"observed_at_ms\": 1790749945558, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T11:54:00Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:e52850eec3b12b4231615c13c6cd700c",
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "role": "matched",
        "created_at": "2026-09-30T06:32:25Z"
      },
      {
        "issue_id": "issue:0607062d9726d6fb8abf659b92819f45",
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "role": "decision",
        "created_at": "2026-09-28T14:48:12Z"
      },
      {
        "issue_id": "issue:e52850eec3b12b4231615c13c6cd700c",
        "work_item_id": "wi:0ae5cc40737b4548bd4cff4251f8d757",
        "role": "decision",
        "created_at": "2026-09-30T06:32:25Z"
      }
    ]
  }
]
```
