# Semplificare la console operativa C2

<!-- migration-5fb2d76effeeac6a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:99008c0293d643908124d64ce79d7a77`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Semplificare la console operativa C2

Rivedere l’interfaccia C2 Control/Codex vista umana/Codex CLI e renderla una console coerente per stato operativo, Inbox, blocchi, writer, lease, executor, progresso e Next action. Ridurre contenuti duplicati, usare timestamp relativi e delta recenti, e mostrare alert solo per eventi che richiedono intervento umano.

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
      "work_item_id": "wi:99008c0293d643908124d64ce79d7a77",
      "parent_id": null,
      "kind": "task",
      "title": "Semplificare la console operativa C2",
      "objective": "Rivedere l’interfaccia C2 Control/Codex vista umana/Codex CLI e renderla una console coerente per stato operativo, Inbox, blocchi, writer, lease, executor, progresso e Next action. Ridurre contenuti duplicati, usare timestamp relativi e delta recenti, e mostrare alert solo per eventi che richiedono intervento umano.",
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
      "created_at": "2026-09-30T10:16:35Z",
      "updated_at": "2026-09-30T10:16:35Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:99008c0293d643908124d64ce79d7a77",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2148,
        "work_item_id": "wi:99008c0293d643908124d64ce79d7a77",
        "evidence_kind": "issue_inbox",
        "label": "issue:03afae4b0e434843b433c87d5d02584a",
        "uri": "chatgpt-desktop",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Rivedere e semplificare l’intero sistema C2 Control / Codex vista umana / Codex CLI mostrato nella UI corrente. Verificare che sia ancora attuale rispetto all’architettura C2 e renderlo una console generale unica o coerente per l’intera C2: economica, snella, concisa ma comprensibile, informativa e non ridondante. Eliminare duplicazioni (es. testo Codex grezzo + Companion Live che ripete lo stesso stato), privilegiare stato operativo/actionable (salute Master Goal, Inbox/WAITING/BLOCKED/batch, writer fence/lease/executor, progresso e Next action), timestamp relativi e delta recenti; mantenere accesso al dettaglio solo on demand. Aggiungere un sistema di alert ad alta salienza per soli eventi che richiedono attenzione/intervento umano, con motivo e azione richiesta, evitando rumore. Deve facilitare al massimo gestione e diagnosi della C2 senza dover interpretare log tecnici. Lo screenshot 2026-09-29 mostra inoltre Master Goal bloccato da ~2h47m a Inbox step 1 con 263 pending, writer fence detenuto da altro supervisor e triage run con lease scaduta/no executor binding: verificare che la UI distingua chiaramente blocco operativo da alert umano e che il sistema di recovery/supervisione renda la situazione actionable. Destinare l’esecuzione a ChatGPT Desktop.\", \"executor\": null, \"executor_ref\": \"chatgpt-desktop\", \"issue_id\": \"issue:03afae4b0e434843b433c87d5d02584a\", \"observed_at_ms\": 1790709992572, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-30T10:16:35Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:03afae4b0e434843b433c87d5d02584a",
        "work_item_id": "wi:99008c0293d643908124d64ce79d7a77",
        "role": "decision",
        "created_at": "2026-09-29T19:26:32Z"
      }
    ]
  }
]
```
