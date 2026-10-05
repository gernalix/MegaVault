# RDC supervisor watcher: evitare falso positivo di processo già attivo da pgrep

<!-- migration-808320ed1859e02a -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:7dd7e7121347484ab59f9a274598c5a1`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### RDC supervisor watcher: evitare falso positivo di processo già attivo da pgrep

Supervisor watcher bootstrap bug: process-presence check used pgrep -f on the watcher command line and matched the shell/pgrep invocation itself, falsely reporting ALREADY_RUNNING while no watcher process existed and no logs were being produced. Use a robust PID file/systemd unit or exact process identity check and verify liveness after launch.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "canonical repository identity",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:7dd7e7121347484ab59f9a274598c5a1",
      "parent_id": null,
      "kind": "task",
      "title": "RDC supervisor watcher: evitare falso positivo di processo già attivo da pgrep",
      "objective": "Supervisor watcher bootstrap bug: process-presence check used pgrep -f on the watcher command line and matched the shell/pgrep invocation itself, falsely reporting ALREADY_RUNNING while no watcher process existed and no logs were being produced. Use a robust PID file/systemd unit or exact process identity check and verify liveness after launch.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:05:32Z",
      "updated_at": "2026-09-27T21:05:32Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:7dd7e7121347484ab59f9a274598c5a1",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1025,
        "work_item_id": "wi:7dd7e7121347484ab59f9a274598c5a1",
        "evidence_kind": "issue_inbox",
        "label": "issue:0c2107aad4f6432e9183866c0a4dbfaf",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Supervisor watcher bootstrap bug: process-presence check used pgrep -f on the watcher command line and matched the shell/pgrep invocation itself, falsely reporting ALREADY_RUNNING while no watcher process existed and no logs were being produced. Use a robust PID file/systemd unit or exact process identity check and verify liveness after launch.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0c2107aad4f6432e9183866c0a4dbfaf\", \"observed_at_ms\": 1790520106373, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:05:32Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:0c2107aad4f6432e9183866c0a4dbfaf",
        "work_item_id": "wi:7dd7e7121347484ab59f9a274598c5a1",
        "role": "decision",
        "created_at": "2026-09-27T14:41:46Z"
      }
    ]
  }
]
```
