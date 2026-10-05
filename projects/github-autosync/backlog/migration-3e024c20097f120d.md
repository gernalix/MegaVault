# Make repo_single_writer discover eligible PRs consistently

<!-- migration-3e024c20097f120d -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 92.

Provenance: `wi:9e30e4d3e93c4881831529b1ab7cf726`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Make repo_single_writer discover eligible PRs consistently

Prompt 205775 Phase C codex-usage-monitor worker queued roadmap_finish but opened PR #9 with title "Make Phase C source databases Datasette friendly" instead of canonical [single-writer] prefix; repo_single_writer.process discovers only prefixed PRs, leaving a green queued integration undiscovered.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "92",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "92"
      ]
    },
    "source": {
      "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
      "parent_id": null,
      "kind": "task",
      "title": "Make repo_single_writer discover eligible PRs consistently",
      "objective": "Prompt 205775 Phase C codex-usage-monitor worker queued roadmap_finish but opened PR #9 with title \"Make Phase C source databases Datasette friendly\" instead of canonical [single-writer] prefix; repo_single_writer.process discovers only prefixed PRs, leaving a green queued integration undiscovered.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 9000,
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
      "created_at": "2026-09-27T21:04:00Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1001,
        "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
        "evidence_kind": "issue_inbox",
        "label": "issue:707a9aa432a34519be4c32032c4aab85",
        "uri": "codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"code_location\": null, \"description\": \"Prompt 205775 Phase C codex-usage-monitor worker queued roadmap_finish but opened PR #9 with title \\\"Make Phase C source databases Datasette friendly\\\" instead of canonical [single-writer] prefix; repo_single_writer.process discovers only prefixed PRs, leaving a green queued integration undiscovered.\", \"executor\": null, \"executor_ref\": \"01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"issue_id\": \"issue:707a9aa432a34519be4c32032c4aab85\", \"observed_at_ms\": 1790536573747, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:04:00Z"
      },
      {
        "evidence_id": 1891,
        "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:707a9aa432a34519be4c32032c4aab85",
        "work_item_id": "wi:9e30e4d3e93c4881831529b1ab7cf726",
        "role": "decision",
        "created_at": "2026-09-27T19:16:13Z"
      }
    ]
  }
]
```
