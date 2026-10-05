# c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer c

<!-- migration-a4f1293a81747fcf -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:3b758b1f12c74de183199965f8689b02`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer c

c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer can create the same prompt worktree before git worktree add, causing `fatal: .../731707 already exists` instead of re-verifying/adopting the now-existing canonical task/731707 worktree. This occurred while preparing P0 C3 child wi:5eb06a... prompt 731707. Make worktree allocation idempotent under concurrent preparation by re-checking/verifying the target/branch after an add failure caused by concurrent creation.

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
      "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
      "parent_id": null,
      "kind": "task",
      "title": "c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer c",
      "objective": "c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer can create the same prompt worktree before git worktree add, causing `fatal: .../731707 already exists` instead of re-verifying/adopting the now-existing canonical task/731707 worktree. This occurred while preparing P0 C3 child wi:5eb06a... prompt 731707. Make worktree allocation idempotent under concurrent preparation by re-checking/verifying the target/branch after an add failure caused by concurrent creation.",
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
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2300,
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "evidence_kind": "issue_inbox",
        "label": "issue:b03d9a46f9a44a8d8b3f4eff77880af1",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2_prepare_codex.py has a TOCTOU race in _roadmap_worktree: after target.exists() returns false, a concurrent preparer can create the same prompt worktree before git worktree add, causing `fatal: .../731707 already exists` instead of re-verifying/adopting the now-existing canonical task/731707 worktree. This occurred while preparing P0 C3 child wi:5eb06a... prompt 731707. Make worktree allocation idempotent under concurrent preparation by re-checking/verifying the target/branch after an add failure caused by concurrent creation.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b03d9a46f9a44a8d8b3f4eff77880af1\", \"observed_at_ms\": 1790762289572, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      },
      {
        "evidence_id": 2497,
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "evidence_kind": "issue_inbox",
        "label": "issue:9284bb1a308d4f08999ab46d1ee8a2c6",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"C2 prompt preparation race observed in the acceleration chat: `prepared_prompt_body_conflict` occurred because another executor had already materialized the same gate with a different prompt body. Recovery correctly avoided creating a duplicate by reading/validating the canonical prompt, but the prepare path should make this automatic: canonical existing prompt ownership wins, equivalent retries become no-ops, and mismatched concurrent materializations return a structured conflict without forcing manual recovery.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:9284bb1a308d4f08999ab46d1ee8a2c6\", \"observed_at_ms\": 1790784889406, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:b03d9a46f9a44a8d8b3f4eff77880af1",
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "role": "decision",
        "created_at": "2026-09-30T09:58:09Z"
      },
      {
        "issue_id": "issue:9284bb1a308d4f08999ab46d1ee8a2c6",
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:9284bb1a308d4f08999ab46d1ee8a2c6",
        "work_item_id": "wi:3b758b1f12c74de183199965f8689b02",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ]
  }
]
```
