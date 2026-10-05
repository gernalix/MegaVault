# Correct C2 status reporting for runnable versus dispatchable work

<!-- migration-8667cebb836681ca -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:c4623c29fc8a42009ad8a210feacf0a4`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Correct C2 status reporting for runnable versus dispatchable work

Fix C2 status/dashboard reporting that says zero activities are immediately runnable while canonical runnable work items exist. Distinguish canonical runnable/actionable work from scheduler-dispatchable work under overrides/resources/concurrency and from waiting/blocked work; add a regression check against canonical runnable predicates.

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
      "work_item_id": "wi:c4623c29fc8a42009ad8a210feacf0a4",
      "parent_id": null,
      "kind": "task",
      "title": "Correct C2 status reporting for runnable versus dispatchable work",
      "objective": "Fix C2 status/dashboard reporting that says zero activities are immediately runnable while canonical runnable work items exist. Distinguish canonical runnable/actionable work from scheduler-dispatchable work under overrides/resources/concurrency and from waiting/blocked work; add a regression check against canonical runnable predicates.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T12:10:08Z",
      "updated_at": "2026-09-30T12:10:08Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:c4623c29fc8a42009ad8a210feacf0a4",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2272,
        "work_item_id": "wi:c4623c29fc8a42009ad8a210feacf0a4",
        "evidence_kind": "issue_inbox",
        "label": "issue:a0883b110f3244aa964fceff719399aa",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"BUG C2 status/dashboard: false \\\"0 attività immediatamente eseguibili\\\".\\n\\nEvidence observed 2026-09-30 around 09:30 CEST:\\n- c2_roadmap_status.py --refresh reports: \\\"Restano 30 attività reali: 0 eseguibili ora, 30 condizionali/in attesa\\\".\\n- Direct canonical query via \\\"python3 tools/c2_intake.py --db roadmap.sqlite runnable\\\" returns many work items with status=pending, actionable=1 and no blocker, including e.g.:\\n  - Verify recurring Oracle Datasette API Kuma heartbeat alert\\n  - Route web executor C2 intake through the canonical writer\\n  - Reduce C2 single-writer GitHub roundtrip latency\\n  - Resolve PersonalHub HubContextLinks unresolved dialog references\\n  - several Symphony tasks\\n- roadmap.sqlite also currently contains 46 pending required items.\\n\\nLikely the status renderer is conflating scheduler-ready-under-current-drain/override with canonically runnable/actionable work. Fix semantics/UI so it distinguishes at least:\\n1. canonically runnable/actionable;\\n2. currently dispatchable by scheduler under overrides/resources/concurrency;\\n3. waiting/blocked/conditional.\\nDo not present scheduler dispatch suppression as \\\"0 eseguibili\\\" when runnable work exists. Add regression coverage comparing c2_roadmap_status output with c2_intake runnable / canonical scheduler predicates.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:a0883b110f3244aa964fceff719399aa\", \"observed_at_ms\": 1790753976327, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:a0883b110f3244aa964fceff719399aa",
        "work_item_id": "wi:c4623c29fc8a42009ad8a210feacf0a4",
        "role": "decision",
        "created_at": "2026-09-30T07:39:36Z"
      }
    ]
  }
]
```
