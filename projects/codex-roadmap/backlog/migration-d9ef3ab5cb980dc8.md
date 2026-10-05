# Clarify triage run and worker projection mismatch

<!-- migration-d9ef3ab5cb980dc8 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:9398702bbb024ab2bc63ee2b261490f5`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Clarify triage run and worker projection mismatch

Identify the run and workers projection referenced by this watcher capture; determine whether an active triage run with worker_ref and unexpired lease but an empty worker list is a real lifecycle inconsistency or expected projection behavior. Preserve the capture as evidence; do not infer a fix before the missing context is known.

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
      "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
      "parent_id": null,
      "kind": "task",
      "title": "Clarify triage run and worker projection mismatch",
      "objective": "Identify the run and workers projection referenced by this watcher capture; determine whether an active triage run with worker_ref and unexpired lease but an empty worker list is a real lifecycle inconsistency or expected projection behavior. Preserve the capture as evidence; do not infer a fix before the missing context is known.",
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
      "created_at": "2026-09-29T22:33:28Z",
      "updated_at": "2026-09-29T22:33:28Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1901,
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "evidence_kind": "issue_inbox",
        "label": "issue:03ce78b53e5af80b0a463ee29dfa3661",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": null, \"description\": \"Run attivo senza worker corrispondente\\n\\nObserved by the C2 semantic watcher. Category: fragility.\\nEvidence already available: Il run canonico di triage è running, ha worker_ref e lease non scaduta; workers è però vuoto.\\nMaterial impact: La classificazione dello stato del Goal resta ambigua e può causare una valutazione errata dell’avanzamento.\\nCapture only: do not infer priority, research, deduplicate, triage, or dispatch from this observation.\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:03ce78b53e5af80b0a463ee29dfa3661\", \"observed_at_ms\": 1790653155449, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-29T22:33:28Z"
      },
      {
        "evidence_id": 1938,
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "evidence_kind": "issue_inbox",
        "label": "issue:286206c8a07b6b438d9677c8d9c06b7d",
        "uri": "codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e719-60ff-7b91-82db-1d7c55787c67\", \"code_location\": null, \"description\": \"Run attivo senza telemetria del worker corrispondente\\n\\nObserved by the C2 semantic watcher. Category: fragility.\\nEvidence already available: Il run canonico `Triage C2 issue inbox` è `running`, ha `worker_ref` e lease non scaduta; `workers` è vuoto.\\nMaterial impact: La telemetria non consente di distinguere un executor vivo da un run orfano, rendendo incerta la classificazione del progresso e il recupero sicuro.\\nCapture only: do not infer priority, research, deduplicate, triage, or dispatch from this observation.\", \"executor\": null, \"executor_ref\": \"01a0e719-60ff-7b91-82db-1d7c55787c67\", \"issue_id\": \"issue:286206c8a07b6b438d9677c8d9c06b7d\", \"observed_at_ms\": 1790658517823, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T00:10:53Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:286206c8a07b6b438d9677c8d9c06b7d",
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "role": "matched",
        "created_at": "2026-09-29T05:08:37Z"
      },
      {
        "issue_id": "issue:03ce78b53e5af80b0a463ee29dfa3661",
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "role": "decision",
        "created_at": "2026-09-29T03:39:15Z"
      },
      {
        "issue_id": "issue:286206c8a07b6b438d9677c8d9c06b7d",
        "work_item_id": "wi:9398702bbb024ab2bc63ee2b261490f5",
        "role": "decision",
        "created_at": "2026-09-29T05:08:37Z"
      }
    ]
  }
]
```
