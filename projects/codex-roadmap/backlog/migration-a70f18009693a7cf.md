# Refresh C2 snapshot before Master Watchdog fingerprint

<!-- migration-a70f18009693a7cf -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:d7e75dd104cb40b692be78ed3c39b6b0`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Refresh C2 snapshot before Master Watchdog fingerprint

Refresh the canonical C2 snapshot before each deterministic Master Watchdog fingerprint, using remote-commit caching, and require the Master Goal to verify the same refreshed canonical state. Prevent false wake decisions caused by stale runtime snapshot or checkout DB. Preserve the supplied observed Inbox/authority mismatch as evidence.

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
      "work_item_id": "wi:d7e75dd104cb40b692be78ed3c39b6b0",
      "parent_id": null,
      "kind": "task",
      "title": "Refresh C2 snapshot before Master Watchdog fingerprint",
      "objective": "Refresh the canonical C2 snapshot before each deterministic Master Watchdog fingerprint, using remote-commit caching, and require the Master Goal to verify the same refreshed canonical state. Prevent false wake decisions caused by stale runtime snapshot or checkout DB. Preserve the supplied observed Inbox/authority mismatch as evidence.",
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
      "created_at": "2026-09-30T07:02:29Z",
      "updated_at": "2026-09-30T07:02:29Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:d7e75dd104cb40b692be78ed3c39b6b0",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2032,
        "work_item_id": "wi:d7e75dd104cb40b692be78ed3c39b6b0",
        "evidence_kind": "issue_inbox",
        "label": "issue:c021c2622739472792f33dae664d6a5f",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Deterministic Master Watchdog can fingerprint a stale runtime snapshot: c2-master-watcher runs every 10s but ~/.local/state/c2-supervisor/roadmap.sqlite3 is refreshed by c2-runtime.service only every ~2 minutes. Live evidence: watchdog snapshot showed Inbox 288 and authority lease expired while origin/main roadmap.sqlite showed Inbox 289 and the same token-189 authority lease valid. Impact: false state-transition wakes and disagreement with the Master Goal. Fix: refresh via c2_snapshot_sync before watchdog fingerprinting (with remote-commit cache) and have the Goal verify the same refreshed snapshot, not a stale checkout DB.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c021c2622739472792f33dae664d6a5f\", \"observed_at_ms\": 1790677937131, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T07:02:29Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:c021c2622739472792f33dae664d6a5f",
        "work_item_id": "wi:d7e75dd104cb40b692be78ed3c39b6b0",
        "role": "decision",
        "created_at": "2026-09-29T10:32:17Z"
      }
    ]
  }
]
```
