# C2: rendere ripetibile il commit del runbook con checkout sporco

<!-- migration-ee3c1c0d86f2ee89 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:92343c3e9477413b86378a2cc399d05c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2: rendere ripetibile il commit del runbook con checkout sporco

Persisting the roadmap-executor monitoring runbook is blocked by the codex-roadmap main-branch guard while unrelated local modifications already exist. The attempted commit was aborted with: 'BLOCKED: codex-roadmap main is guarded. Use: python3 tools/roadmap_pull.py --repo .' This makes small durable operational documentation changes depend on reconciling unrelated work and risks losing proven recovery procedures.

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
      "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
      "parent_id": null,
      "kind": "task",
      "title": "C2: rendere ripetibile il commit del runbook con checkout sporco",
      "objective": "Persisting the roadmap-executor monitoring runbook is blocked by the codex-roadmap main-branch guard while unrelated local modifications already exist. The attempted commit was aborted with: 'BLOCKED: codex-roadmap main is guarded. Use: python3 tools/roadmap_pull.py --repo .' This makes small durable operational documentation changes depend on reconciling unrelated work and risks losing proven recovery procedures.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 9000,
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
      "created_at": "2026-09-27T21:06:31Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1031,
        "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
        "evidence_kind": "issue_inbox",
        "label": "issue:74cb8442d6a14451a7f5f76174ac581a",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"operations/ROADMAP_EXECUTOR_MONITORING_RUNBOOK.md\", \"description\": \"Persisting the roadmap-executor monitoring runbook is blocked by the codex-roadmap main-branch guard while unrelated local modifications already exist. The attempted commit was aborted with: 'BLOCKED: codex-roadmap main is guarded. Use: python3 tools/roadmap_pull.py --repo .' This makes small durable operational documentation changes depend on reconciling unrelated work and risks losing proven recovery procedures.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:74cb8442d6a14451a7f5f76174ac581a\", \"observed_at_ms\": 1790530842419, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:06:31Z"
      },
      {
        "evidence_id": 1893,
        "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:74cb8442d6a14451a7f5f76174ac581a",
        "work_item_id": "wi:92343c3e9477413b86378a2cc399d05c",
        "role": "decision",
        "created_at": "2026-09-27T17:40:42Z"
      }
    ]
  }
]
```
