# Regression: Implementare c2_supervisor_resume deterministico e bounded

<!-- migration-373fea55380b5acc -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:1fa8bb3014d24dc8b4a900ec74b9f2bd`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Implementare c2_supervisor_resume deterministico e bounded

Investigate and resolve the reported recurrence where three supervisor-resume cycles leave runtime.env authority stale against the active canonical lease, preventing fenced planning/dispatch mutations. Preserve the active owner and do not bypass fencing or create duplicate executor runs.

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
      "work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Implementare c2_supervisor_resume deterministico e bounded",
      "objective": "Investigate and resolve the reported recurrence where three supervisor-resume cycles leave runtime.env authority stale against the active canonical lease, preventing fenced planning/dispatch mutations. Preserve the active owner and do not bypass fencing or create duplicate executor runs.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "human",
      "sort_order": -8900,
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
      "created_at": "2026-09-30T13:51:11Z",
      "updated_at": "2026-09-30T13:51:11Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
        "to_work_item_id": "wi:1cb2ddbb334c4172a00aa58746861c33",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T13:51:11Z",
        "actor": "c2-issue-triage",
        "note": "issue:6a14f490fc5b4e86a737b7349076f12a"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2399,
        "work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
        "evidence_kind": "issue_inbox",
        "label": "issue:6a14f490fc5b4e86a737b7349076f12a",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": \"tools/c2_supervisor_resume.py\", \"description\": \"Repeated C2 supervisor-resume claims leave the native Master Goal unable to submit fenced planning or dispatch mutations. Across three resumed cycles, ~/.config/c2-supervisor/runtime.env did not match the active lease; the lease stayed on recovery_pointer /home/daniele/.local/share/c2-supervisor/worktrees/c2-autodrain-20260927/operations/task-state/C2-AUTODRAIN-20260927.md with current_action=recovery:authority and current_step=stale_takeover, while the local fencing token advanced 210 to 211 to 212. Canonical c2-supervisor-resume claims for tokens 210 (#7429) and 212 (#7431) applied; a c2_control intake using this runtime's old token was rejected as stale_or_expired_supervisor before submission. Root cause is undetermined. Resolve an owner-bound handoff or stable recovery identity; do not bypass the active fence or duplicate executor runs.\\n\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:6a14f490fc5b4e86a737b7349076f12a\", \"observed_at_ms\": 1790775066263, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T13:51:11Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:6a14f490fc5b4e86a737b7349076f12a",
        "work_item_id": "wi:1fa8bb3014d24dc8b4a900ec74b9f2bd",
        "role": "decision",
        "created_at": "2026-09-30T13:31:06Z"
      }
    ]
  }
]
```
