# C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires

<!-- migration-9fc7ce7bfd162118 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:180ee1c55f104a2a93a05c0a7654c49e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires

C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires_at into the body while c2_worker reuses the stable c2-bind-<run> transport key. This is the same fenced replay identity bug already fixed for schedule/acknowledge. Authority-scope the bind_executor transport Issue key while preserving the canonical run/thread binding identity and idempotency; add regression coverage. Current C3 run f91ce3f175324137aba3c11128b9317b is directly affected.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:180ee1c55f104a2a93a05c0a7654c49e",
      "parent_id": null,
      "kind": "task",
      "title": "C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires",
      "objective": "C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires_at into the body while c2_worker reuses the stable c2-bind-<run> transport key. This is the same fenced replay identity bug already fixed for schedule/acknowledge. Authority-scope the bind_executor transport Issue key while preserving the canonical run/thread binding identity and idempotency; add regression coverage. Current C3 run f91ce3f175324137aba3c11128b9317b is directly affected.",
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
      "created_at": "2026-09-30T13:05:38Z",
      "updated_at": "2026-09-30T13:05:38Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:180ee1c55f104a2a93a05c0a7654c49e",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2361,
        "work_item_id": "wi:180ee1c55f104a2a93a05c0a7654c49e",
        "evidence_kind": "issue_inbox",
        "label": "issue:ce28f5bf42524b16ad3caf679aea297d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 Codex worker repeatedly crashes during thread binding with submit_mutation.MutationSubmitError request_key_conflict:c2-bind-<run>. bind_executor is supervisor-fenced, so _writer_submit injects a changing lease_expires_at into the body while c2_worker reuses the stable c2-bind-<run> transport key. This is the same fenced replay identity bug already fixed for schedule/acknowledge. Authority-scope the bind_executor transport Issue key while preserving the canonical run/thread binding identity and idempotency; add regression coverage. Current C3 run f91ce3f175324137aba3c11128b9317b is directly affected.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:ce28f5bf42524b16ad3caf679aea297d\", \"observed_at_ms\": 1790764057106, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T13:05:38Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:ce28f5bf42524b16ad3caf679aea297d",
        "work_item_id": "wi:180ee1c55f104a2a93a05c0a7654c49e",
        "role": "decision",
        "created_at": "2026-09-30T10:27:37Z"
      }
    ]
  }
]
```
