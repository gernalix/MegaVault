# Regression: Regression: Riparare il finalizer C2 per task su codex-roadmap

<!-- migration-53db8eef4ee97e75 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:e30219c2d6e74fadac68920237d5c105`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Regression: Riparare il finalizer C2 per task su codex-roadmap

C2 worktree wi:3ba130ae55b24bcd869fe92a27367be4 was provisioned on task/wi-3ba130ae-fast-watchdog, but roadmap_repo_integration.py requires task/wi-3ba130ae55b24bcd869fe92a27367be4; queue rejects task_branch_mismatch.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Regression: Riparare il finalizer C2 per task su codex-roadmap",
      "objective": "C2 worktree wi:3ba130ae55b24bcd869fe92a27367be4 was provisioned on task/wi-3ba130ae-fast-watchdog, but roadmap_repo_integration.py requires task/wi-3ba130ae55b24bcd869fe92a27367be4; queue rejects task_branch_mismatch.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": -2100,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T10:08:36Z",
      "updated_at": "2026-09-30T10:08:36Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
        "to_work_item_id": "wi:badf7112fa0547bea990edd6084208e4",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T10:08:36Z",
        "actor": "c2-issue-triage",
        "note": "issue:374f7ae6662f4d579f04a482741d1e00"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2122,
        "work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
        "evidence_kind": "issue_inbox",
        "label": "issue:374f7ae6662f4d579f04a482741d1e00",
        "uri": "codex://threads/01a0ee59-b35c-7b41-b449-73d9a4b9b80b",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ee59-b35c-7b41-b449-73d9a4b9b80b\", \"code_location\": null, \"description\": \"C2 worktree wi:3ba130ae55b24bcd869fe92a27367be4 was provisioned on task/wi-3ba130ae-fast-watchdog, but roadmap_repo_integration.py requires task/wi-3ba130ae55b24bcd869fe92a27367be4; queue rejects task_branch_mismatch.\", \"executor\": null, \"executor_ref\": \"01a0ee59-b35c-7b41-b449-73d9a4b9b80b\", \"issue_id\": \"issue:374f7ae6662f4d579f04a482741d1e00\", \"observed_at_ms\": 1790705633394, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:08:36Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:374f7ae6662f4d579f04a482741d1e00",
        "work_item_id": "wi:e30219c2d6e74fadac68920237d5c105",
        "role": "decision",
        "created_at": "2026-09-29T18:13:53Z"
      }
    ]
  }
]
```
