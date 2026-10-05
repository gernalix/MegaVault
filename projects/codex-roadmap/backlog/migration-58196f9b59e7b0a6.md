# Attribute unexpected concurrent edits in C2 deterministic watchdog worktree

<!-- migration-58196f9b59e7b0a6 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:5c395fad257044489865d3bf1e5fcc76`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Attribute unexpected concurrent edits in C2 deterministic watchdog worktree

Concurrent unexpected edits appeared inside ChatGPT task worktree /home/daniele/projects/codex-roadmap-worktrees/c2-deterministic-watchdog-20260929 while implementing the deterministic watcher: git status shows modifications to tools/c2_master_watchdog.py and tests/test_c2_master_watchdog.py plus untracked tools/c2_inbox_codex_executor.py that were not created by this executor. Impact: risk of mixing independent changes into the watcher checkpoint/PR and violating one-writer-per-worktree assumptions. Preserve and attribute these edits before integration.

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
      "work_item_id": "wi:5c395fad257044489865d3bf1e5fcc76",
      "parent_id": null,
      "kind": "task",
      "title": "Attribute unexpected concurrent edits in C2 deterministic watchdog worktree",
      "objective": "Concurrent unexpected edits appeared inside ChatGPT task worktree /home/daniele/projects/codex-roadmap-worktrees/c2-deterministic-watchdog-20260929 while implementing the deterministic watcher: git status shows modifications to tools/c2_master_watchdog.py and tests/test_c2_master_watchdog.py plus untracked tools/c2_inbox_codex_executor.py that were not created by this executor. Impact: risk of mixing independent changes into the watcher checkpoint/PR and violating one-writer-per-worktree assumptions. Preserve and attribute these edits before integration.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "https://github.com/gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T06:13:20Z",
      "updated_at": "2026-09-30T06:13:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:5c395fad257044489865d3bf1e5fcc76",
        "tag": "priority:p2"
      },
      {
        "work_item_id": "wi:5c395fad257044489865d3bf1e5fcc76",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2029,
        "work_item_id": "wi:5c395fad257044489865d3bf1e5fcc76",
        "evidence_kind": "issue_inbox",
        "label": "issue:924f79fa18494fd69c53865c7c8bab0b",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Concurrent unexpected edits appeared inside ChatGPT task worktree /home/daniele/projects/codex-roadmap-worktrees/c2-deterministic-watchdog-20260929 while implementing the deterministic watcher: git status shows modifications to tools/c2_master_watchdog.py and tests/test_c2_master_watchdog.py plus untracked tools/c2_inbox_codex_executor.py that were not created by this executor. Impact: risk of mixing independent changes into the watcher checkpoint/PR and violating one-writer-per-worktree assumptions. Preserve and attribute these edits before integration.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:924f79fa18494fd69c53865c7c8bab0b\", \"observed_at_ms\": 1790677543612, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T06:13:20Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:924f79fa18494fd69c53865c7c8bab0b",
        "work_item_id": "wi:5c395fad257044489865d3bf1e5fcc76",
        "role": "decision",
        "created_at": "2026-09-29T10:25:43Z"
      }
    ]
  }
]
```
