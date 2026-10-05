# Investigate canonical refresh Git fetch failure

<!-- migration-61aa37a461a16748 -->

Migrated project backlog. Project: **github-autosync**; project_id: 92.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 92.

Provenance: `wi:96202bfd9bc746638e8e835dd5cc718c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate canonical refresh Git fetch failure

Investigate the reported canonical-refresh failure where git fetch --depth=1 origin main exited 128; use live evidence to identify cause and restore reliable telemetry freshness without dispatching from triage.

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
      "work_item_id": "wi:96202bfd9bc746638e8e835dd5cc718c",
      "parent_id": null,
      "kind": "task",
      "title": "Investigate canonical refresh Git fetch failure",
      "objective": "Investigate the reported canonical-refresh failure where git fetch --depth=1 origin main exited 128; use live evidence to identify cause and restore reliable telemetry freshness without dispatching from triage.",
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
      "created_at": "2026-09-29T23:29:10Z",
      "updated_at": "2026-09-29T23:29:10Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:96202bfd9bc746638e8e835dd5cc718c",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1922,
        "work_item_id": "wi:96202bfd9bc746638e8e835dd5cc718c",
        "evidence_kind": "issue_inbox",
        "label": "issue:1adeff4f2087d2cf9c225d7a2c33beab",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": null, \"description\": \"Il refresh canonico fallisce durante il fetch Git\\n\\nObserved by the C2 semantic watcher. Category: fragility.\\nEvidence already available: Il log riporta `canonical-refresh failed` con `git fetch --depth=1 origin main` terminato con codice 128.\\nMaterial impact: Può lasciare la telemetria obsoleta e impedire una classificazione affidabile dello stato del Goal.\\nCapture only: do not infer priority, research, deduplicate, triage, or dispatch from this observation.\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:1adeff4f2087d2cf9c225d7a2c33beab\", \"observed_at_ms\": 1790656396575, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T23:29:10Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:1adeff4f2087d2cf9c225d7a2c33beab",
        "work_item_id": "wi:96202bfd9bc746638e8e835dd5cc718c",
        "role": "decision",
        "created_at": "2026-09-29T04:33:16Z"
      }
    ]
  }
]
```
