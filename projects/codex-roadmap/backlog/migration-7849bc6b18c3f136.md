# c2_executor_result.py --payload help says JSON object but CLI reads a file path

<!-- migration-7849bc6b18c3f136 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:afc8ff1a5230497fb5debd7808585f9b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### c2_executor_result.py --payload help says JSON object but CLI reads a file path

La guida del comando indica un JSON diretto, ma il programma tenta di leggerlo come percorso di file. Chi conclude un lavoro seguendo la guida può ricevere un errore: va reso coerente il contratto del comando.

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
      "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
      "parent_id": null,
      "kind": "task",
      "title": "c2_executor_result.py --payload help says JSON object but CLI reads a file path",
      "objective": "La guida del comando indica un JSON diretto, ma il programma tenta di leggerlo come percorso di file. Chi conclude un lavoro seguendo la guida può ricevere un errore: va reso coerente il contratto del comando.",
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
      "created_at": "2026-09-30T04:54:29Z",
      "updated_at": "2026-09-30T04:54:29Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "tag": "priority:p1"
      },
      {
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2011,
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "evidence_kind": "issue_inbox",
        "label": "issue:be770205a21b47d8aa956b693e537fc4",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2_executor_result.py CLI contract mismatch: --help says --payload is a JSON object, but main() calls args.payload.read_text(), so passing the documented inline JSON raises FileNotFoundError. Impact: normal executor completion can fail despite following the advertised CLI. Evidence observed while closing work item wi:ee525059023d407ab0fdca10fb3b6c12.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:be770205a21b47d8aa956b693e537fc4\", \"observed_at_ms\": 1790675106544, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"https://github.com/gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T04:54:29Z"
      },
      {
        "evidence_id": 2047,
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "evidence_kind": "issue_inbox",
        "label": "issue:081b6b0679cb4928959b9237dbac9ed6",
        "uri": "chatgpt-web",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"c2_executor_result.py --help descrive --payload come JSON object, ma l'implementazione interpreta l'argomento come percorso Path e fallisce con OSError [Errno 36] se si passa JSON inline; allineare help/CLI oppure accettare entrambi.\", \"executor\": \"chatgpt\", \"executor_ref\": \"chatgpt-web\", \"issue_id\": \"issue:081b6b0679cb4928959b9237dbac9ed6\", \"observed_at_ms\": 1790682478964, \"origin_run_id\": null, \"origin_work_item_id\": \"wi:c2b1264824d748d0b828e02468ae1089\", \"repo\": null}",
        "created_at": "2026-09-30T07:29:15Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:081b6b0679cb4928959b9237dbac9ed6",
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "role": "matched",
        "created_at": "2026-09-29T11:47:58Z"
      },
      {
        "issue_id": "issue:be770205a21b47d8aa956b693e537fc4",
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "role": "decision",
        "created_at": "2026-09-29T09:45:06Z"
      },
      {
        "issue_id": "issue:081b6b0679cb4928959b9237dbac9ed6",
        "work_item_id": "wi:afc8ff1a5230497fb5debd7808585f9b",
        "role": "decision",
        "created_at": "2026-09-29T11:47:58Z"
      }
    ]
  }
]
```
