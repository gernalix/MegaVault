# c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_tex

<!-- migration-d7b4572a025ac5ca -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:9ab6a2da5c254ecdafc30c9ed883440b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_tex

c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_text_contains_execution_metadata was surfaced locally as start_claim_rejected:<issue>:not_planned. This obscures the real validation failure, caused a ~60s wasted round-trip and repeated prepare Issues, and encourages blind retries. Prevalidate the same prompt-header rule locally before submission and/or surface the writer rejection reason instead of labeling every rejected mutation as a start-claim failure.

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
      "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
      "parent_id": null,
      "kind": "task",
      "title": "c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_tex",
      "objective": "c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_text_contains_execution_metadata was surfaced locally as start_claim_rejected:<issue>:not_planned. This obscures the real validation failure, caused a ~60s wasted round-trip and repeated prepare Issues, and encourages blind retries. Prevalidate the same prompt-header rule locally before submission and/or surface the writer rejection reason instead of labeling every rejected mutation as a start-claim failure.",
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
      "created_at": "2026-09-30T12:21:51Z",
      "updated_at": "2026-09-30T12:21:51Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2299,
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "evidence_kind": "issue_inbox",
        "label": "issue:cfe0d6fb3b6f44e39e1ccee2a0d94e0d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2_prepare_codex diagnostic bug: a prepare_codex mutation rejected by the canonical writer with C2IntakeError prompt_text_contains_execution_metadata was surfaced locally as start_claim_rejected:<issue>:not_planned. This obscures the real validation failure, caused a ~60s wasted round-trip and repeated prepare Issues, and encourages blind retries. Prevalidate the same prompt-header rule locally before submission and/or surface the writer rejection reason instead of labeling every rejected mutation as a start-claim failure.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:cfe0d6fb3b6f44e39e1ccee2a0d94e0d\", \"observed_at_ms\": 1790762064145, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      },
      {
        "evidence_id": 2354,
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "evidence_kind": "issue_inbox",
        "label": "issue:99b008ea1765438bbea03a8b3827803f",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 prepare_codex avoidable remote-rejection loop: prompt preparation submits a GitHub mutation before locally validating the same prompt_text_contains_execution_metadata rule enforced by the writer. C3 pilot prepare Issues #7173/#7175 were both rejected only after writer round trips because the prompt contained execution-metadata syntax; concurrent preparers also duplicated prompt/configure submissions for the same work item. Add local preflight parity with writer validation and suppress concurrent prepare for a work item that already has a prepare request/prompt materialization in flight. Low priority if this path is removed by C3.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:99b008ea1765438bbea03a8b3827803f\", \"observed_at_ms\": 1790763519552, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:55:06Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:99b008ea1765438bbea03a8b3827803f",
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "role": "matched",
        "created_at": "2026-09-30T10:18:39Z"
      },
      {
        "issue_id": "issue:cfe0d6fb3b6f44e39e1ccee2a0d94e0d",
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "role": "decision",
        "created_at": "2026-09-30T09:54:24Z"
      },
      {
        "issue_id": "issue:99b008ea1765438bbea03a8b3827803f",
        "work_item_id": "wi:9ab6a2da5c254ecdafc30c9ed883440b",
        "role": "decision",
        "created_at": "2026-09-30T10:18:39Z"
      }
    ]
  }
]
```
