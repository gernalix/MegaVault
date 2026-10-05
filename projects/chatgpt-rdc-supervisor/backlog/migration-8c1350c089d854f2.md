# Bootstrap ChatGPT project discovery from a known chat or project link

<!-- migration-8c1350c089d854f2 -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:c55ef1a126774d138eb9bb3b1734e37b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Bootstrap ChatGPT project discovery from a known chat or project link

Make ChatGPT project-to-chat discovery recover when project enumeration by project ID returns no accessible resources but a known chat within the project is accessible. Bootstrap from a project ID/link or query alternate indexes, then resolve and enumerate the project without requiring the user to supply a chat ID.

Acceptance:

- A project ID or project link can bootstrap discovery when a chat in that project is individually accessible.
- The resolver can use a known chat or alternate indexes to recover the project-chat relationship without user-supplied chat ID.
- Discovery preserves access boundaries and reports unresolved projects without guessing.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "canonical repository identity",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
      "parent_id": null,
      "kind": "task",
      "title": "Bootstrap ChatGPT project discovery from a known chat or project link",
      "objective": "Make ChatGPT project-to-chat discovery recover when project enumeration by project ID returns no accessible resources but a known chat within the project is accessible. Bootstrap from a project ID/link or query alternate indexes, then resolve and enumerate the project without requiring the user to supply a chat ID.",
      "acceptance_json": "[\"A project ID or project link can bootstrap discovery when a chat in that project is individually accessible.\", \"The resolver can use a known chat or alternate indexes to recover the project-chat relationship without user-supplied chat ID.\", \"Discovery preserves access boundaries and reports unresolved projects without guessing.\"]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T14:22:22Z",
      "updated_at": "2026-09-30T14:22:22Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
        "tag": "chatgpt"
      },
      {
        "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
        "tag": "project-discovery"
      },
      {
        "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
        "tag": "resolver"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2407,
        "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
        "evidence_kind": "issue_inbox",
        "label": "issue:3351ee4c231a4c14a724e5c0e413e3de",
        "uri": "codex://threads/01a0f296-d084-7f52-b5ac-330501c88689",
        "value_json": "{\"chat_url\": \"codex://threads/01a0f296-d084-7f52-b5ac-330501c88689\", \"code_location\": null, \"description\": \"Nel thread Codex 01a0f296-d084-7f52-b5ac-330501c88689, la discovery iniziale del progetto ChatGPT Grindr tramite elenco progetti/chat ha dichiarato il progetto g-p-6ab8156e66f481919a6966d7cbd0bd59 non accessibile; appena l'utente ha fornito l'ID esatto di una singola chat, Codex è riuscito ad aprirla e poi a enumerare l'intero progetto. Bottleneck/fragilità: la discovery da project ID non trova risorse che diventano accessibili tramite una chat nota. Serve rendere il resolver progetto↔chat capace di bootstrap da project ID/link o di interrogare indici alternativi senza richiedere all'utente un chat ID.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:3351ee4c231a4c14a724e5c0e413e3de\", \"observed_at_ms\": 1790777711526, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T14:22:22Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:3351ee4c231a4c14a724e5c0e413e3de",
        "work_item_id": "wi:c55ef1a126774d138eb9bb3b1734e37b",
        "role": "decision",
        "created_at": "2026-09-30T14:22:22Z"
      }
    ]
  }
]
```
