# Fence concurrent RDC and Computer-Use UI control globally

<!-- migration-48c44005cfa7380c -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:5f77be769c0b4c209ff54d4a875c18df`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Fence concurrent RDC and Computer-Use UI control globally

RDC/Computer-Use global single-writer missing: during Grindr/Pixel work multiple ChatGPT/Codex origin_instance values were concurrently issuing Remote Desktop Commander calls to the same Fedora bridge, while chatgpt-rdc-supervisor and an old cua-repl were also alive. This can produce overlapping UI/device control and apparent zombie actions (including unexpected desktop UI changes). Need one global authority/lease across RDC + CUA + supervisors, stale-worker fencing, and a PANIC STOP that revokes all UI-control writers without disabling the desired foreground session.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
      "parent_id": null,
      "kind": "task",
      "title": "Fence concurrent RDC and Computer-Use UI control globally",
      "objective": "RDC/Computer-Use global single-writer missing: during Grindr/Pixel work multiple ChatGPT/Codex origin_instance values were concurrently issuing Remote Desktop Commander calls to the same Fedora bridge, while chatgpt-rdc-supervisor and an old cua-repl were also alive. This can produce overlapping UI/device control and apparent zombie actions (including unexpected desktop UI changes). Need one global authority/lease across RDC + CUA + supervisors, stale-worker fencing, and a PANIC STOP that revokes all UI-control writers without disabling the desired foreground session.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "human",
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
      "created_at": "2026-09-29T19:22:21Z",
      "updated_at": "2026-09-29T19:22:21Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "tag": "priority:p0"
      },
      {
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1836,
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "evidence_kind": "issue_inbox",
        "label": "issue:1ac044b4f1cd44d38d7cc81dbf12ecca",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"RDC/Computer-Use global single-writer missing: during Grindr/Pixel work multiple ChatGPT/Codex origin_instance values were concurrently issuing Remote Desktop Commander calls to the same Fedora bridge, while chatgpt-rdc-supervisor and an old cua-repl were also alive. This can produce overlapping UI/device control and apparent zombie actions (including unexpected desktop UI changes). Need one global authority/lease across RDC + CUA + supervisors, stale-worker fencing, and a PANIC STOP that revokes all UI-control writers without disabling the desired foreground session.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:1ac044b4f1cd44d38d7cc81dbf12ecca\", \"observed_at_ms\": 1790629993701, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T19:22:21Z"
      },
      {
        "evidence_id": 2053,
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "evidence_kind": "issue_inbox",
        "label": "issue:af43c75ee9cd4c31a0403856fe5b70ca",
        "uri": "codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"code_location\": null, \"description\": \"Due work item C2 running (wi:5681590af5ba4d4db571817a02d58886 e wi:9bed381f17084d99ad0ae4bd55ff523d) richiedono lo stesso collegamento RDC al Chrome normale nello stesso repository; rischio di lavoro e integrazione concorrenti.\", \"executor\": null, \"executor_ref\": \"01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"issue_id\": \"issue:af43c75ee9cd4c31a0403856fe5b70ca\", \"observed_at_ms\": 1790688328867, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T08:01:47Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:af43c75ee9cd4c31a0403856fe5b70ca",
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "role": "matched",
        "created_at": "2026-09-29T13:25:28Z"
      },
      {
        "issue_id": "issue:1ac044b4f1cd44d38d7cc81dbf12ecca",
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "role": "decision",
        "created_at": "2026-09-28T21:13:13Z"
      },
      {
        "issue_id": "issue:af43c75ee9cd4c31a0403856fe5b70ca",
        "work_item_id": "wi:5f77be769c0b4c209ff54d4a875c18df",
        "role": "decision",
        "created_at": "2026-09-29T13:25:28Z"
      }
    ]
  }
]
```
