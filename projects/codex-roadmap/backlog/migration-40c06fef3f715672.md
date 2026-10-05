# Validare la sintassi dei launcher Codex prima dell'avvio

<!-- migration-40c06fef3f715672 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:2e8c2a75a54f4fa9a54e33c87133fbe3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Validare la sintassi dei launcher Codex prima dell'avvio

Codex CLI automation wrapper accepted --search only as a global option before exec; placing --search after codex exec caused immediate exit code 2 and killed the tmux job before work began. Harden long-running launcher/wrapper generation to validate option placement against the installed Codex CLI or use codex --search exec consistently.

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
      "work_item_id": "wi:2e8c2a75a54f4fa9a54e33c87133fbe3",
      "parent_id": null,
      "kind": "task",
      "title": "Validare la sintassi dei launcher Codex prima dell'avvio",
      "objective": "Codex CLI automation wrapper accepted --search only as a global option before exec; placing --search after codex exec caused immediate exit code 2 and killed the tmux job before work began. Harden long-running launcher/wrapper generation to validate option placement against the installed Codex CLI or use codex --search exec consistently.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "/home/daniele/projects/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-10-01T12:32:14Z",
      "updated_at": "2026-10-01T12:32:14Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:2e8c2a75a54f4fa9a54e33c87133fbe3",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2513,
        "work_item_id": "wi:2e8c2a75a54f4fa9a54e33c87133fbe3",
        "evidence_kind": "issue_inbox",
        "label": "issue:61d9ea60b51d4c36b37f3e96cac2234a",
        "uri": "c3-webapp-night-run",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Codex CLI automation wrapper accepted --search only as a global option before exec; placing --search after codex exec caused immediate exit code 2 and killed the tmux job before work began. Harden long-running launcher/wrapper generation to validate option placement against the installed Codex CLI or use codex --search exec consistently.\", \"executor\": null, \"executor_ref\": \"c3-webapp-night-run\", \"issue_id\": \"issue:61d9ea60b51d4c36b37f3e96cac2234a\", \"observed_at_ms\": 1790793400153, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/codex-roadmap\"}",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:61d9ea60b51d4c36b37f3e96cac2234a",
        "work_item_id": "wi:2e8c2a75a54f4fa9a54e33c87133fbe3",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ]
  }
]
```
