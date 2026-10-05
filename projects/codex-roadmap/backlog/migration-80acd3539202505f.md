# C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with

<!-- migration-80acd3539202505f -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:65bd233b608648a78c699bc721881bc0`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with

C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with spaces. load_item() would raise missing_or_invalid_model_reasoning for valid canonical items, including the active C3 pilot. Validation should not reinterpret canonical model labels; accept the stored exact model/reasoning values and quote them safely when generating the Symphony Codex config.

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
      "work_item_id": "wi:65bd233b608648a78c699bc721881bc0",
      "parent_id": null,
      "kind": "task",
      "title": "C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with",
      "objective": "C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with spaces. load_item() would raise missing_or_invalid_model_reasoning for valid canonical items, including the active C3 pilot. Validation should not reinterpret canonical model labels; accept the stored exact model/reasoning values and quote them safely when generating the Symphony Codex config.",
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
        "work_item_id": "wi:65bd233b608648a78c699bc721881bc0",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2360,
        "work_item_id": "wi:65bd233b608648a78c699bc721881bc0",
        "evidence_kind": "issue_inbox",
        "label": "issue:cd8d0c6936204265987158cd04e31218",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C3 Symphony bridge in active prompt 731707 currently validates execution-spec model/reasoning with SAFE_VALUE=[A-Za-z0-9][A-Za-z0-9._-]*, but canonical coding specs use values such as `GPT-6 Sol` and `GPT-5.6 Terra` with spaces. load_item() would raise missing_or_invalid_model_reasoning for valid canonical items, including the active C3 pilot. Validation should not reinterpret canonical model labels; accept the stored exact model/reasoning values and quote them safely when generating the Symphony Codex config.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:cd8d0c6936204265987158cd04e31218\", \"observed_at_ms\": 1790763945138, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T13:05:38Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:cd8d0c6936204265987158cd04e31218",
        "work_item_id": "wi:65bd233b608648a78c699bc721881bc0",
        "role": "decision",
        "created_at": "2026-09-30T10:25:45Z"
      }
    ]
  }
]
```
