# Fix c2-runtime supervisor renewal starvation

<!-- migration-00cc6cc31057eced -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:786751b25b874e6e9fca02e037c5d02c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Fix c2-runtime supervisor renewal starvation

Correct c2-runtime.advance() renewal threshold relative to the 180-second supervisor TTL so an otherwise valid canonical authority can proceed to acknowledge and launch rather than returning after every renew_supervisor request. Preserve fencing and use the reported 2026-09-29 12:35–12:36 repeated renewal cycles and stalled triage run as evidence.

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
      "work_item_id": "wi:786751b25b874e6e9fca02e037c5d02c",
      "parent_id": null,
      "kind": "task",
      "title": "Fix c2-runtime supervisor renewal starvation",
      "objective": "Correct c2-runtime.advance() renewal threshold relative to the 180-second supervisor TTL so an otherwise valid canonical authority can proceed to acknowledge and launch rather than returning after every renew_supervisor request. Preserve fencing and use the reported 2026-09-29 12:35–12:36 repeated renewal cycles and stalled triage run as evidence.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
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
      "created_at": "2026-09-30T07:10:05Z",
      "updated_at": "2026-09-30T07:10:05Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:786751b25b874e6e9fca02e037c5d02c",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2041,
        "work_item_id": "wi:786751b25b874e6e9fca02e037c5d02c",
        "evidence_kind": "issue_inbox",
        "label": "issue:8a849a3288134b8892aef6a763344390",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2-runtime supervisor renewal starvation: advance() renews whenever canonical lease_expires_at <= now+300, but supervisor TTL is 180s. Therefore the renewal condition is effectively always true; advance() returns immediately after queuing renew_supervisor and never reaches acknowledge/launch. Evidence: repeated runtime cycles at 12:35-12:36 reported only renew_supervisor while the triage run stayed running with no worker and Inbox rose to 292. Fix renewal threshold relative to TTL and allow dispatch while same canonical authority is still safely valid.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:8a849a3288134b8892aef6a763344390\", \"observed_at_ms\": 1790678252980, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T07:10:05Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:8a849a3288134b8892aef6a763344390",
        "work_item_id": "wi:786751b25b874e6e9fca02e037c5d02c",
        "role": "decision",
        "created_at": "2026-09-29T10:37:32Z"
      }
    ]
  }
]
```
