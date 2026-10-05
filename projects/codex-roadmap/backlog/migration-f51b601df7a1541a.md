# C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s t

<!-- migration-f51b601df7a1541a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:d1e672b5b2be4467a3b5e3e805655d61`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s t

C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s tests -p "test_c2_*.py" -q` aborts because an imported CLI path invokes argparse (`python3 -m unittest clear ... --source-modified-at`), after many ResourceWarnings for unclosed sqlite connections. This forces hand-maintained targeted test lists and increases validation latency/risk. Fix test discovery/import side effects when convenient; do not block the C3 migration on it.

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
      "work_item_id": "wi:d1e672b5b2be4467a3b5e3e805655d61",
      "parent_id": null,
      "kind": "task",
      "title": "C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s t",
      "objective": "C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s tests -p \"test_c2_*.py\" -q` aborts because an imported CLI path invokes argparse (`python3 -m unittest clear ... --source-modified-at`), after many ResourceWarnings for unclosed sqlite connections. This forces hand-maintained targeted test lists and increases validation latency/risk. Fix test discovery/import side effects when convenient; do not block the C3 migration on it.",
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
        "work_item_id": "wi:d1e672b5b2be4467a3b5e3e805655d61",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2295,
        "work_item_id": "wi:d1e672b5b2be4467a3b5e3e805655d61",
        "evidence_kind": "issue_inbox",
        "label": "issue:9c5255d82e2349e39f3362a71922c603",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 broad unittest discovery is not a reliable validation gate: `PYTHONPATH=tools:tests python3 -m unittest discover -s tests -p \\\"test_c2_*.py\\\" -q` aborts because an imported CLI path invokes argparse (`python3 -m unittest clear ... --source-modified-at`), after many ResourceWarnings for unclosed sqlite connections. This forces hand-maintained targeted test lists and increases validation latency/risk. Fix test discovery/import side effects when convenient; do not block the C3 migration on it.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:9c5255d82e2349e39f3362a71922c603\", \"observed_at_ms\": 1790760993288, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:9c5255d82e2349e39f3362a71922c603",
        "work_item_id": "wi:d1e672b5b2be4467a3b5e3e805655d61",
        "role": "decision",
        "created_at": "2026-09-30T09:36:33Z"
      }
    ]
  }
]
```
