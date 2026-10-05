# c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejec

<!-- migration-b0849e15bb461b37 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:fb9c5ee65c8d4ec4a39043028e2ff623`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejec

c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejected because the first 16 prompt lines mentioned app-server config syntax containing `model=...`, which matched prompt_text_contains_execution_metadata even though it was explanatory task content and execution metadata was supplied separately in structured fields. Refine the guard to detect actual prompt-header execution metadata directives rather than arbitrary explanatory/config examples, while still rejecting embedded execution metadata.

Acceptance:

- Explanatory model= or reasoning= examples in prompt content are accepted when execution metadata is supplied separately.
- Actual execution-metadata directives in the prompt header remain rejected.
- Focused positive and negative guard tests pass.

status: waiting

next_action: After the active C3 security gate releases its writer lane, reconcile whether pre-cutover C3 work still needs a new Codex prompt. If yes, implement the narrow false-positive fix and focused tests; otherwise close as obsolete under the verified Symphony cutover decision.

blocker: The current c2_intake.prepare_codex guard scans the first 16 prompt lines for any model= or reasoning= token, so the reported explanatory app-server example can still be rejected. This is a concrete C3 prompt-preparation risk, but the active C3 security gate already has a materialized prompt and owns the codex-roadmap writer lane.

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
      "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
      "parent_id": null,
      "kind": "task",
      "title": "c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejec",
      "objective": "c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejected because the first 16 prompt lines mentioned app-server config syntax containing `model=...`, which matched prompt_text_contains_execution_metadata even though it was explanatory task content and execution metadata was supplied separately in structured fields. Refine the guard to detect actual prompt-header execution metadata directives rather than arbitrary explanatory/config examples, while still rejecting embedded execution metadata.",
      "acceptance_json": "[\"Explanatory model= or reasoning= examples in prompt content are accepted when execution metadata is supplied separately.\", \"Actual execution-metadata directives in the prompt header remain rejected.\", \"Focused positive and negative guard tests pass.\"]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": "After the active C3 security gate releases its writer lane, reconcile whether pre-cutover C3 work still needs a new Codex prompt. If yes, implement the narrow false-positive fix and focused tests; otherwise close as obsolete under the verified Symphony cutover decision.",
      "blocker": "The current c2_intake.prepare_codex guard scans the first 16 prompt lines for any model= or reasoning= token, so the reported explanatory app-server example can still be rejected. This is a concrete C3 prompt-preparation risk, but the active C3 security gate already has a materialized prompt and owns the codex-roadmap writer lane.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T12:24:32Z",
      "updated_at": "2026-09-30T12:39:50Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2307,
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "evidence_kind": "issue_inbox",
        "label": "issue:58b389c4c11c4220944f3ace5f8120e3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2_prepare_codex prompt header guard caused avoidable duplicate C3 preparation failures: both #7173 and #7175 were rejected because the first 16 prompt lines mentioned app-server config syntax containing `model=...`, which matched prompt_text_contains_execution_metadata even though it was explanatory task content and execution metadata was supplied separately in structured fields. Refine the guard to detect actual prompt-header execution metadata directives rather than arbitrary explanatory/config examples, while still rejecting embedded execution metadata.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:58b389c4c11c4220944f3ace5f8120e3\", \"observed_at_ms\": 1790762396209, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:24:32Z"
      },
      {
        "evidence_id": 2340,
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "evidence_kind": "classification",
        "label": "MegaVault resolves gernalix/codex-roadmap to active project 51.",
        "uri": null,
        "value_json": "\"MegaVault resolves gernalix/codex-roadmap to active project 51.\"",
        "created_at": "2026-09-30T12:39:50Z"
      },
      {
        "evidence_id": 2341,
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "evidence_kind": "classification",
        "label": "Current tools/c2_intake.py still applies the broad first-16-lines regex and lacks a regression test for an explanatory a",
        "uri": null,
        "value_json": "\"Current tools/c2_intake.py still applies the broad first-16-lines regex and lacks a regression test for an explanatory app-server configuration example.\"",
        "created_at": "2026-09-30T12:39:50Z"
      },
      {
        "evidence_id": 2342,
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "evidence_kind": "classification",
        "label": "The reported rejected preparations were historical C3 preparation attempts; current P0 security work is already running ",
        "uri": null,
        "value_json": "\"The reported rejected preparations were historical C3 preparation attempts; current P0 security work is already running on the same repository.\"",
        "created_at": "2026-09-30T12:39:50Z"
      },
      {
        "evidence_id": 2343,
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "evidence_kind": "classification",
        "label": "No second codex-roadmap implementation lane was started; fresh batch review is required after the active C3 writer finis",
        "uri": null,
        "value_json": "\"No second codex-roadmap implementation lane was started; fresh batch review is required after the active C3 writer finishes.\"",
        "created_at": "2026-09-30T12:39:50Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:58b389c4c11c4220944f3ace5f8120e3",
        "work_item_id": "wi:fb9c5ee65c8d4ec4a39043028e2ff623",
        "role": "decision",
        "created_at": "2026-09-30T09:59:56Z"
      }
    ]
  }
]
```
