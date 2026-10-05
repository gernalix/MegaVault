# Investigate C2 recurring DOWN incident

<!-- migration-86c00edde6df0893 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:031e649cff744f1897e09702a69e3c2a`, `issue:127f80b17e27564b37e278ddd53fe124`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Diagnose C2 degraded publisher monitor

Uptime Kuma monitor transitioned to DOWN.
Monitor: C2 (id 73)
Heartbeat: 2026-09-30 09:43:23.894 (row 691877)
Failure context: C2 degraded: publisher

status: pending

### issue:127f80b17e27564b37e278ddd53fe124

Uptime Kuma monitor transitioned to DOWN.
Monitor: C2 (id 73)
Heartbeat: 2026-10-01 15:30:46.567 (row 749748)
Failure context: No heartbeat in the time window

state: pending

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
      "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Diagnose C2 degraded publisher monitor",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: C2 (id 73)\nHeartbeat: 2026-09-30 09:43:23.894 (row 691877)\nFailure context: C2 degraded: publisher",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 1000,
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
      "created_at": "2026-09-30T12:21:51Z",
      "updated_at": "2026-09-30T12:21:51Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "to_work_item_id": "wi:8767be7ce13647a98a91b6d76c863b8d",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T12:21:51Z",
        "actor": "c2-issue-triage",
        "note": "issue:2644c3921a17d34a953d2716151bde37"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2297,
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "evidence_kind": "issue_inbox",
        "label": "issue:2644c3921a17d34a953d2716151bde37",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: C2 (id 73)\\nHeartbeat: 2026-09-30 09:43:23.894 (row 691877)\\nFailure context: C2 degraded: publisher\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:2644c3921a17d34a953d2716151bde37\", \"observed_at_ms\": 1790761489446, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      },
      {
        "evidence_id": 2439,
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "evidence_kind": "issue_inbox",
        "label": "issue:4079fd517623aefadfbf3fafb13e5d3b",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: C2 (id 73)\\nHeartbeat: 2026-09-30 15:07:52.184 (row 702411)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4079fd517623aefadfbf3fafb13e5d3b\", \"observed_at_ms\": 1790780985212, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:26:58Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:2644c3921a17d34a953d2716151bde37",
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "role": "decision",
        "created_at": "2026-09-30T09:44:49Z"
      },
      {
        "issue_id": "issue:4079fd517623aefadfbf3fafb13e5d3b",
        "work_item_id": "wi:031e649cff744f1897e09702a69e3c2a",
        "role": "decision",
        "created_at": "2026-09-30T16:26:58Z"
      }
    ]
  },
  {
    "routing": {
      "project": "51",
      "reason": "monitor/service ownership from explicit source text",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "issue_id": "issue:127f80b17e27564b37e278ddd53fe124",
      "description": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: C2 (id 73)\nHeartbeat: 2026-10-01 15:30:46.567 (row 749748)\nFailure context: No heartbeat in the time window",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790868728428,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:32:08Z"
    },
    "issue_work_item_links": []
  }
]
```
