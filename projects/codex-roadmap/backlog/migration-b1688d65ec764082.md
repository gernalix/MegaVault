# Diagnose malformed SQLite image in C2 triage snapshot receipt read

<!-- migration-b1688d65ec764082 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:d7d08413702e40478ef902f441ff96dc`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Diagnose malformed SQLite image in C2 triage snapshot receipt read

The reported sqlite3.DatabaseError arose while waiting for a human-copy writer receipt; the source says rows 1-7 applied and row 8 copy submitted. No exact active work item covers snapshot integrity in this receipt path; preserve the event for scoped diagnosis. No verified priority or dependency change.

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
      "work_item_id": "wi:d7d08413702e40478ef902f441ff96dc",
      "parent_id": null,
      "kind": "task",
      "title": "Diagnose malformed SQLite image in C2 triage snapshot receipt read",
      "objective": "The reported sqlite3.DatabaseError arose while waiting for a human-copy writer receipt; the source says rows 1-7 applied and row 8 copy submitted. No exact active work item covers snapshot integrity in this receipt path; preserve the event for scoped diagnosis. No verified priority or dependency change.",
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
      "created_at": "2026-09-30T09:25:36Z",
      "updated_at": "2026-09-30T09:25:36Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:d7d08413702e40478ef902f441ff96dc",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2070,
        "work_item_id": "wi:d7d08413702e40478ef902f441ff96dc",
        "evidence_kind": "issue_inbox",
        "label": "issue:73895a8fa06643babb210e0ff4b40021",
        "uri": "codex://threads/01a0ed8f-c306-7a81-b4f9-e58a4192711b",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ed8f-c306-7a81-b4f9-e58a4192711b\", \"code_location\": null, \"description\": \"C2 Inbox triage batch snapshot read failed with sqlite3.DatabaseError: database disk image is malformed while waiting for row 8 human-copy writer receipt; rows 1-7 were writer-applied, row 8 copy mutation was submitted. Inspect snapshot integrity/sync before resuming.\", \"executor\": null, \"executor_ref\": \"01a0ed8f-c306-7a81-b4f9-e58a4192711b\", \"issue_id\": \"issue:73895a8fa06643babb210e0ff4b40021\", \"observed_at_ms\": 1790693398504, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T09:25:36Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:73895a8fa06643babb210e0ff4b40021",
        "work_item_id": "wi:d7d08413702e40478ef902f441ff96dc",
        "role": "decision",
        "created_at": "2026-09-29T14:49:58Z"
      }
    ]
  }
]
```
