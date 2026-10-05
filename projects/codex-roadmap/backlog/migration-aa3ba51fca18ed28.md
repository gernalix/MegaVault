# Add C2 fast local lane

<!-- migration-aa3ba51fca18ed28 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:933b7758bde84f93adf665280b3a8baa`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Add C2 fast local lane

Add an explicit user-authorized urgent local bypass with atomic C2 reconciliation.

Acceptance:

- Fast lane is explicit
- Reconciles through existing repository-submit path
- Records final repo/branch/commit/diff summary/tests/remaining blockers
- Does not fabricate intermediate lifecycle steps
- C2 resumes canonical authority after reconciliation

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
      "work_item_id": "wi:933b7758bde84f93adf665280b3a8baa",
      "parent_id": null,
      "kind": "task",
      "title": "Add C2 fast local lane",
      "objective": "Add an explicit user-authorized urgent local bypass with atomic C2 reconciliation.",
      "acceptance_json": "[\"Fast lane is explicit\", \"Reconciles through existing repository-submit path\", \"Records final repo/branch/commit/diff summary/tests/remaining blockers\", \"Does not fabricate intermediate lifecycle steps\", \"C2 resumes canonical authority after reconciliation\"]",
      "status": "waiting",
      "executor_policy": "chatgpt",
      "sort_order": null,
      "current_action": "Parked during roadmap semantic reconciliation.",
      "next_action": "Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.",
      "blocker": "Deferred pending Symphony migration/replacement decision.",
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "https://github.com/gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-28T03:17:30Z",
      "updated_at": "2026-09-28T06:45:01Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:933b7758bde84f93adf665280b3a8baa:002ffbf56ced0fa7b60b4318afbc4dbe",
        "work_item_id": "wi:933b7758bde84f93adf665280b3a8baa",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": "Stale RUNNING reconciled before fresh dispatch",
        "completed_json": "[]",
        "remaining_json": "[\"Add C2 fast local lane\"]",
        "evidence_json": "[\"No active claimed/running/recovering work_item_run exists; stale RUNNING lifecycle row is being requeued with a fresh run identity.\"]",
        "blocker": "stale running state without active run",
        "next_action": "Requeue through scheduler with a fresh run identity",
        "strict_contract": 0,
        "payload_sha256": "002ffbf56ced0fa7b60b4318afbc4dbec49a889cf5648a68ba21df0cc9e68456",
        "captured_at": 1790574370.771896
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 1387,
        "work_item_id": "wi:933b7758bde84f93adf665280b3a8baa",
        "evidence_kind": "executor_result",
        "label": "No active claimed/running/recovering work_item_run exists; stale RUNNING lifecycle row is being requeued with a fresh ru",
        "uri": null,
        "value_json": "\"No active claimed/running/recovering work_item_run exists; stale RUNNING lifecycle row is being requeued with a fresh run identity.\"",
        "created_at": "2026-09-28T05:46:10Z"
      },
      {
        "evidence_id": 1388,
        "work_item_id": "wi:933b7758bde84f93adf665280b3a8baa",
        "evidence_kind": "classification",
        "label": "No active claimed/running/recovering work_item_run exists; stale RUNNING lifecycle row is being requeued with a fresh ru",
        "uri": null,
        "value_json": "\"No active claimed/running/recovering work_item_run exists; stale RUNNING lifecycle row is being requeued with a fresh run identity.\"",
        "created_at": "2026-09-28T05:46:10Z"
      },
      {
        "evidence_id": 1440,
        "work_item_id": "wi:933b7758bde84f93adf665280b3a8baa",
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
