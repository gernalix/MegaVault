# Provide reliable Grindr Android chat selection on Pixel

<!-- migration-1c742bc13e1d12bc -->

Migrated project backlog. Project: **grindr-export**; project_id: 106.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 106.

Provenance: `wi:2588d81073d74251acee6c0848d6ee22`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Provide reliable Grindr Android chat selection on Pixel

Resolve the observed inability to select an Inbox chat reliably through ADB: UIAutomator exposes only the Home container and tabs while chat rows are absent from the accessibility tree; direct ChatActivityV2 launch and run-as are unavailable. Establish a supported selection path, with a manual fallback if needed.

Acceptance:

- A reliable, supported way to select a target Inbox chat on Pixel is documented or implemented, or a concrete external blocker and safe manual fallback are recorded.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "106",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "106"
      ]
    },
    "source": {
      "work_item_id": "wi:2588d81073d74251acee6c0848d6ee22",
      "parent_id": null,
      "kind": "task",
      "title": "Provide reliable Grindr Android chat selection on Pixel",
      "objective": "Resolve the observed inability to select an Inbox chat reliably through ADB: UIAutomator exposes only the Home container and tabs while chat rows are absent from the accessibility tree; direct ChatActivityV2 launch and run-as are unavailable. Establish a supported selection path, with a manual fallback if needed.",
      "acceptance_json": "[\"A reliable, supported way to select a target Inbox chat on Pixel is documented or implemented, or a concrete external blocker and safe manual fallback are recorded.\"]",
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
      "created_at": "2026-09-30T16:26:58Z",
      "updated_at": "2026-09-30T16:26:58Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2440,
        "work_item_id": "wi:2588d81073d74251acee6c0848d6ee22",
        "evidence_kind": "issue_inbox",
        "label": "issue:ada761dfe10242fdaea782537ac798c0",
        "uri": "codex://threads/01a0f296-d084-7f52-b5ac-330501c88689",
        "value_json": "{\"chat_url\": \"codex://threads/01a0f296-d084-7f52-b5ac-330501c88689\", \"code_location\": null, \"description\": \"Grindr Android sul Pixel: UIAutomator espone soltanto il contenitore Home e i cinque tab; screenshot mostra Inbox popolata ma righe e testi non sono presenti nel tree. Questo blocca la selezione affidabile della chat via ADB. ChatActivityV2 non esportata impedisce avvio diretto; accesso run-as non disponibile perché app non debuggable. Necessario mantenere una modalità di selezione manuale oppure acquisizione UI supportata con semantica Compose.\", \"executor\": null, \"executor_ref\": \"01a0f296-d084-7f52-b5ac-330501c88689\", \"issue_id\": \"issue:ada761dfe10242fdaea782537ac798c0\", \"observed_at_ms\": 1790779818083, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:26:58Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:ada761dfe10242fdaea782537ac798c0",
        "work_item_id": "wi:2588d81073d74251acee6c0848d6ee22",
        "role": "decision",
        "created_at": "2026-09-30T16:26:58Z"
      }
    ]
  }
]
```
