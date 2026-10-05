# Avoid checking out main when merging C2 PRs from task worktrees

<!-- migration-4dc881f0c3dcc1e2 -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 92.

Provenance: `wi:d29b347667534ba6b5fd635f3bf59f51`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Avoid checking out main when merging C2 PRs from task worktrees

C2 integration helpers invoking gh pr merge from a secondary codex-roadmap worktree fail because main is already checked out in the canonical worktree. Use an explicit repository/API merge path or another safe approach that does not check out main in the task worktree.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "92",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "92"
      ]
    },
    "source": {
      "work_item_id": "wi:d29b347667534ba6b5fd635f3bf59f51",
      "parent_id": null,
      "kind": "task",
      "title": "Avoid checking out main when merging C2 PRs from task worktrees",
      "objective": "C2 integration helpers invoking gh pr merge from a secondary codex-roadmap worktree fail because main is already checked out in the canonical worktree. Use an explicit repository/API merge path or another safe approach that does not check out main in the task worktree.",
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
      "created_at": "2026-09-30T07:54:41Z",
      "updated_at": "2026-09-30T07:54:41Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:d29b347667534ba6b5fd635f3bf59f51",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:d29b347667534ba6b5fd635f3bf59f51",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2051,
        "work_item_id": "wi:d29b347667534ba6b5fd635f3bf59f51",
        "evidence_kind": "issue_inbox",
        "label": "issue:47ba601c3ca34aa2a8e4614ee9605bbd",
        "uri": "chatgpt-web",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"gh pr merge invoked from a secondary codex-roadmap worktree fails with fatal: main is already used by worktree at /home/daniele/projects/codex-roadmap. C2 integration helpers should merge via explicit --repo/API or otherwise avoid checking out main from a task worktree.\", \"executor\": \"chatgpt\", \"executor_ref\": \"chatgpt-web\", \"issue_id\": \"issue:47ba601c3ca34aa2a8e4614ee9605bbd\", \"observed_at_ms\": 1790684958938, \"origin_run_id\": null, \"origin_work_item_id\": \"wi:c2b1264824d748d0b828e02468ae1089\", \"repo\": null}",
        "created_at": "2026-09-30T07:54:41Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:47ba601c3ca34aa2a8e4614ee9605bbd",
        "work_item_id": "wi:d29b347667534ba6b5fd635f3bf59f51",
        "role": "decision",
        "created_at": "2026-09-29T12:29:18Z"
      }
    ]
  }
]
```
