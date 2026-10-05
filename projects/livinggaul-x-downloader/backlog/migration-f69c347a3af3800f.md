# Investigate Fedora Service · user:livinggaul-x-source-availability.service recurring DOWN incident

<!-- migration-f69c347a3af3800f -->

Migrated project backlog. Project: **livinggaul-x-downloader**; project_id: 69.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 69.

Provenance: `wi:95a1a38cba6440c487b056069c5c1787`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: LivingGaul source availability local activation

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:livinggaul-x-source-availability.service (id 70)
Heartbeat: 2026-09-30 06:26:25.386 (row 685521)
Failure context: No heartbeat in the time window

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "69",
      "reason": "canonical repository identity",
      "related_projects": [
        "69"
      ]
    },
    "source": {
      "work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: LivingGaul source availability local activation",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · user:livinggaul-x-source-availability.service (id 70)\nHeartbeat: 2026-09-30 06:26:25.386 (row 685521)\nFailure context: No heartbeat in the time window",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/livinggaul-x-downloader",
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
        "work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
        "to_work_item_id": "prompt:560584",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T12:10:08Z",
        "actor": "c2-issue-triage",
        "note": "issue:656c0120c477f7f9e971dd59584b2cce"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2262,
        "work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
        "evidence_kind": "issue_inbox",
        "label": "issue:656c0120c477f7f9e971dd59584b2cce",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:livinggaul-x-source-availability.service (id 70)\\nHeartbeat: 2026-09-30 06:26:25.386 (row 685521)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:656c0120c477f7f9e971dd59584b2cce\", \"observed_at_ms\": 1790749946790, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:656c0120c477f7f9e971dd59584b2cce",
        "work_item_id": "wi:95a1a38cba6440c487b056069c5c1787",
        "role": "decision",
        "created_at": "2026-09-30T06:32:26Z"
      }
    ]
  }
]
```
