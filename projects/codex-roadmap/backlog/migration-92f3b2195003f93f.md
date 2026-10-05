# Codex human-only live terminal

<!-- migration-92f3b2195003f93f -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:4c5d8a8f173042c2ba39be81cc66ccab`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Codex human-only live terminal

Create a read-only live terminal view of the active Codex session that shows only user-facing assistant text and suppresses tool/diff/status noise, using relative age labels such as “3 min fa” or “2 h 5 min fa” instead of absolute timestamps.

Acceptance:

- Live view follows the intended Codex session deterministically; shows only human-facing assistant messages; relative age labels update correctly; no duplicate execution/session is created; documented command exists.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

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
      "work_item_id": "wi:4c5d8a8f173042c2ba39be81cc66ccab",
      "parent_id": null,
      "kind": "task",
      "title": "Codex human-only live terminal",
      "objective": "Create a read-only live terminal view of the active Codex session that shows only user-facing assistant text and suppresses tool/diff/status noise, using relative age labels such as “3 min fa” or “2 h 5 min fa” instead of absolute timestamps.",
      "acceptance_json": "[\"Live view follows the intended Codex session deterministically; shows only human-facing assistant messages; relative age labels update correctly; no duplicate execution/session is created; documented command exists.\"]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 85,
      "current_action": "Parked during roadmap semantic reconciliation.",
      "next_action": "Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.",
      "blocker": "Deferred pending Symphony migration/replacement decision.",
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "/home/daniele/projects/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T22:30:04Z",
      "updated_at": "2026-09-28T06:45:01Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1442,
        "work_item_id": "wi:4c5d8a8f173042c2ba39be81cc66ccab",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:01Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
