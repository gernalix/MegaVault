# Verify Grindr chat oldest-history boundary before acquisition verdict

<!-- migration-c45152eb74d509bd -->

Migrated project backlog. Project: **grindr-export**; project_id: 106.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 106.

Provenance: `wi:e7df91c724b8481c81fb0098df9f8815`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Verify Grindr chat oldest-history boundary before acquisition verdict

Resolve conflicting Grindr chat acquisition verdicts by verifying the true oldest available history boundary and defining reliable PASS/FAIL evidence when the textual start marker is absent. Preserve the 65-child capture and do not assume temporary scroll stability proves completion.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "106",
      "reason": "canonical repository identity",
      "related_projects": [
        "106"
      ]
    },
    "source": {
      "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
      "parent_id": null,
      "kind": "task",
      "title": "Verify Grindr chat oldest-history boundary before acquisition verdict",
      "objective": "Resolve conflicting Grindr chat acquisition verdicts by verifying the true oldest available history boundary and defining reliable PASS/FAIL evidence when the textual start marker is absent. Preserve the 65-child capture and do not assume temporary scroll stability proves completion.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/grindr-export",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-29T18:28:35Z",
      "updated_at": "2026-09-29T18:28:35Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1813,
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "evidence_kind": "issue_inbox",
        "label": "issue:8786884745a94dbaa75e9ea8ba791eb3",
        "uri": "codex://threads/01a0e994-3c96-7be3-b166-ce74f13b6e9f",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e994-3c96-7be3-b166-ce74f13b6e9f\", \"code_location\": null, \"description\": \"grindr_dom_archive.py marks a complete 65-child chat acquisition FAIL solely when Grindr omits the textual start marker, despite the oldest available boundary being reached and documented.\", \"executor\": null, \"executor_ref\": \"01a0e994-3c96-7be3-b166-ce74f13b6e9f\", \"issue_id\": \"issue:8786884745a94dbaa75e9ea8ba791eb3\", \"observed_at_ms\": 1790625677170, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T18:28:35Z"
      },
      {
        "evidence_id": 1814,
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "evidence_kind": "issue_inbox",
        "label": "issue:e95a18904b9a4f50b8be9561fe519266",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"grindr-export false-positive oldest-boundary detection: reverse-scroll stability at 26 Aug was treated as history start, but user confirms conversation begins much earlier. Boundary verification must not trust temporary DOM scroll stability alone; acquisition must trigger/await older-history loading and verify true start marker or stronger terminal evidence.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:e95a18904b9a4f50b8be9561fe519266\", \"observed_at_ms\": 1790626491650, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T18:31:33Z"
      },
      {
        "evidence_id": 1815,
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "evidence_kind": "issue_inbox",
        "label": "issue:d9f674e3d605488e8353a40553cfae36",
        "uri": "codex://threads/01a0e994-3c96-7be3-b166-ce74f13b6e9f",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e994-3c96-7be3-b166-ce74f13b6e9f\", \"code_location\": null, \"description\": \"Critical Grindr exporter false positive: reverse-scroll stability can occur before lazy loading resumes; it must never prove the oldest history boundary without a terminal UI marker.\", \"executor\": null, \"executor_ref\": \"01a0e994-3c96-7be3-b166-ce74f13b6e9f\", \"issue_id\": \"issue:d9f674e3d605488e8353a40553cfae36\", \"observed_at_ms\": 1790626549794, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T18:37:39Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:e95a18904b9a4f50b8be9561fe519266",
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "role": "matched",
        "created_at": "2026-09-28T20:14:51Z"
      },
      {
        "issue_id": "issue:d9f674e3d605488e8353a40553cfae36",
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "role": "matched",
        "created_at": "2026-09-28T20:15:49Z"
      },
      {
        "issue_id": "issue:8786884745a94dbaa75e9ea8ba791eb3",
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "role": "decision",
        "created_at": "2026-09-28T20:01:17Z"
      },
      {
        "issue_id": "issue:e95a18904b9a4f50b8be9561fe519266",
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "role": "decision",
        "created_at": "2026-09-28T20:14:51Z"
      },
      {
        "issue_id": "issue:d9f674e3d605488e8353a40553cfae36",
        "work_item_id": "wi:e7df91c724b8481c81fb0098df9f8815",
        "role": "decision",
        "created_at": "2026-09-28T20:15:49Z"
      }
    ]
  }
]
```
