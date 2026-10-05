# RDC supervisor: correggere l’invio del prompt dal composer corrente

<!-- migration-b5f2db6abdb18e09 -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:faf3525f8b624553bd6c9921fa8efd5f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### RDC supervisor: correggere l’invio del prompt dal composer corrente

ChatGPT RDC supervisor: send_message() is also stale against the current ChatGPT composer. After correctly stopping a stuck generation and filling "continua" into the live ProseMirror [contenteditable=true][role=textbox], the supervisor failed to submit it because its composer/send selectors do not match the current UI; the text remained in the composer until a direct Enter keypress was used. Update _composer()/send_message() selectors and add a live E2E assertion that a nudge actually creates a new user turn, not merely fills the composer.

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
      "work_item_id": "wi:faf3525f8b624553bd6c9921fa8efd5f",
      "parent_id": null,
      "kind": "task",
      "title": "RDC supervisor: correggere l’invio del prompt dal composer corrente",
      "objective": "ChatGPT RDC supervisor: send_message() is also stale against the current ChatGPT composer. After correctly stopping a stuck generation and filling \"continua\" into the live ProseMirror [contenteditable=true][role=textbox], the supervisor failed to submit it because its composer/send selectors do not match the current UI; the text remained in the composer until a direct Enter keypress was used. Update _composer()/send_message() selectors and add a live E2E assertion that a nudge actually creates a new user turn, not merely fills the composer.",
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
        "work_item_id": "wi:faf3525f8b624553bd6c9921fa8efd5f",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1023,
        "work_item_id": "wi:faf3525f8b624553bd6c9921fa8efd5f",
        "evidence_kind": "issue_inbox",
        "label": "issue:b27be300fde6490ca3cca5736cdb5cab",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"ChatGPT RDC supervisor: send_message() is also stale against the current ChatGPT composer. After correctly stopping a stuck generation and filling \\\"continua\\\" into the live ProseMirror [contenteditable=true][role=textbox], the supervisor failed to submit it because its composer/send selectors do not match the current UI; the text remained in the composer until a direct Enter keypress was used. Update _composer()/send_message() selectors and add a live E2E assertion that a nudge actually creates a new user turn, not merely fills the composer.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b27be300fde6490ca3cca5736cdb5cab\", \"observed_at_ms\": 1790518805671, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:05:32Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:b27be300fde6490ca3cca5736cdb5cab",
        "work_item_id": "wi:faf3525f8b624553bd6c9921fa8efd5f",
        "role": "decision",
        "created_at": "2026-09-27T14:20:05Z"
      }
    ]
  }
]
```
