# roadmap_result.py hardcodes /home/daniele/projects/codex-roadmap for its protected refresh. If that preserved checkout i

<!-- migration-e316b02eb7a2bec7 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:826f5d0f2c4642fbb868053069d95ccc`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### roadmap_result.py hardcodes /home/daniele/projects/codex-roadmap for its protected refresh. If that preserved checkout i

Correggere il refresh protetto in roadmap_result.py affinché usi un checkout main verificato invece di dipendere da un checkout canonico che può trovarsi su un branch task; mantenere i controlli di integrità e fallire in modo esplicito se non esiste una copia sicura.

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
      "work_item_id": "wi:826f5d0f2c4642fbb868053069d95ccc",
      "parent_id": null,
      "kind": "task",
      "title": "roadmap_result.py hardcodes /home/daniele/projects/codex-roadmap for its protected refresh. If that preserved checkout i",
      "objective": "Correggere il refresh protetto in roadmap_result.py affinché usi un checkout main verificato invece di dipendere da un checkout canonico che può trovarsi su un branch task; mantenere i controlli di integrità e fallire in modo esplicito se non esiste una copia sicura.",
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
      "created_at": "2026-09-30T10:08:36Z",
      "updated_at": "2026-09-30T10:08:36Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:826f5d0f2c4642fbb868053069d95ccc",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2132,
        "work_item_id": "wi:826f5d0f2c4642fbb868053069d95ccc",
        "evidence_kind": "issue_inbox",
        "label": "issue:a87604ba1361405c971b7441d8f53253",
        "uri": "codex://threads/01a0ee5c-f61d-7e32-b4a5-4d864d009725",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ee5c-f61d-7e32-b4a5-4d864d009725\", \"code_location\": null, \"description\": \"roadmap_result.py hardcodes /home/daniele/projects/codex-roadmap for its protected refresh. If that preserved checkout is on a task branch, terminalization fails current_run_refresh_failed even when invoked from a clean verified main checkout.\", \"executor\": null, \"executor_ref\": \"01a0ee5c-f61d-7e32-b4a5-4d864d009725\", \"issue_id\": \"issue:a87604ba1361405c971b7441d8f53253\", \"observed_at_ms\": 1790706949108, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:08:36Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:a87604ba1361405c971b7441d8f53253",
        "work_item_id": "wi:826f5d0f2c4642fbb868053069d95ccc",
        "role": "decision",
        "created_at": "2026-09-29T18:35:49Z"
      }
    ]
  }
]
```
