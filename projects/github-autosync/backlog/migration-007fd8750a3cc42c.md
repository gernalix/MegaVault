# Separate worker completion from supervisor-owned integration

<!-- migration-007fd8750a3cc42c -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 92.

Provenance: `wi:4d32aecaaa1f40a2b882cd1b283098c0`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Separate worker completion from supervisor-owned integration

Codex CLI workers can report false integration blockers because their sandbox may make ~/.local/state canonical locks read-only and block DNS/GitHub even when the supervising ChatGPT/RDC session has working host access. Separate worker-local implementation/test completion from supervisor-owned canonical integration so verified work is not misclassified as blocked solely by worker sandbox/network limitations.

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
      "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
      "parent_id": null,
      "kind": "task",
      "title": "Separate worker completion from supervisor-owned integration",
      "objective": "Codex CLI workers can report false integration blockers because their sandbox may make ~/.local/state canonical locks read-only and block DNS/GitHub even when the supervising ChatGPT/RDC session has working host access. Separate worker-local implementation/test completion from supervisor-owned canonical integration so verified work is not misclassified as blocked solely by worker sandbox/network limitations.",
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
      "created_at": "2026-09-27T21:03:11Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 981,
        "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
        "evidence_kind": "issue_inbox",
        "label": "issue:b97dc56296844979b6e06fec962224a8",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Codex CLI workers can report false integration blockers because their sandbox may make ~/.local/state canonical locks read-only and block DNS/GitHub even when the supervising ChatGPT/RDC session has working host access. Separate worker-local implementation/test completion from supervisor-owned canonical integration so verified work is not misclassified as blocked solely by worker sandbox/network limitations.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:b97dc56296844979b6e06fec962224a8\", \"observed_at_ms\": 1790531286062, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:03:11Z"
      },
      {
        "evidence_id": 1889,
        "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
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
        "issue_id": "issue:b97dc56296844979b6e06fec962224a8",
        "work_item_id": "wi:4d32aecaaa1f40a2b882cd1b283098c0",
        "role": "decision",
        "created_at": "2026-09-27T17:48:06Z"
      }
    ]
  }
]
```
