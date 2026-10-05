# Repository consistency still requires PROMPT_ID inside every materialized prompt body, while roadmap_db rejects executio

<!-- migration-9bb3f7e3763e3b9a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:148f9388b72f456480cb0155a51c5665`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Repository consistency still requires PROMPT_ID inside every materialized prompt body, while roadmap_db rejects executio

Riconciliare la regola CI che richiede PROMPT_ID nel corpo dei prompt con la validazione canonica che rifiuta metadati esecuzione nel prompt_text; aggiornare contratto e test affinché i prompt registrati siano validi.

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
      "work_item_id": "wi:148f9388b72f456480cb0155a51c5665",
      "parent_id": null,
      "kind": "task",
      "title": "Repository consistency still requires PROMPT_ID inside every materialized prompt body, while roadmap_db rejects executio",
      "objective": "Riconciliare la regola CI che richiede PROMPT_ID nel corpo dei prompt con la validazione canonica che rifiuta metadati esecuzione nel prompt_text; aggiornare contratto e test affinché i prompt registrati siano validi.",
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
        "work_item_id": "wi:148f9388b72f456480cb0155a51c5665",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2129,
        "work_item_id": "wi:148f9388b72f456480cb0155a51c5665",
        "evidence_kind": "issue_inbox",
        "label": "issue:123a2c220c3842a5a85cee6e1370bf69",
        "uri": "codex://threads/01a0ee5c-f61d-7e32-b4a5-4d864d009725",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ee5c-f61d-7e32-b4a5-4d864d009725\", \"code_location\": null, \"description\": \"Repository consistency still requires PROMPT_ID inside every materialized prompt body, while roadmap_db rejects execution metadata in prompt_text. A newly registered prompt therefore passes the writer but makes CI fail test_pending_prompt_metadata_is_canonical.\", \"executor\": null, \"executor_ref\": \"01a0ee5c-f61d-7e32-b4a5-4d864d009725\", \"issue_id\": \"issue:123a2c220c3842a5a85cee6e1370bf69\", \"observed_at_ms\": 1790706693285, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:08:36Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:123a2c220c3842a5a85cee6e1370bf69",
        "work_item_id": "wi:148f9388b72f456480cb0155a51c5665",
        "role": "decision",
        "created_at": "2026-09-29T18:31:33Z"
      }
    ]
  }
]
```
