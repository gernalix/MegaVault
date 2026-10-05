# Phase E — UX Datasette standard e navigazione frictionless

<!-- migration-676af5eef66f4bf3 -->

Migrated project backlog. Project: **datasette5**; project_id: 10.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 10.

Provenance: `wi:9116862e72024e89b0033b4c6eeb146c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Phase E — UX Datasette standard e navigazione frictionless

Implementare sull'istanza Datasette esistente una UX generica/riutilizzabile per i DB esposti: date locali d/m/yy hh:mm mantenendo raw epoch, boolean visuali coerenti, URL/link cliccabili senza perdere raw quando utile, mappe quando esistono lat/lon, click-to-filter sui valori e filtro giornaliero sulle date, FK/backlink e label come via primaria di navigazione; nascondere dall'interfaccia ordinaria i DB obsoleti/non selezionati.

Acceptance:

- L'interfaccia ordinaria mostra solo i DB con datasette_expose=yes, salvo endpoint tecnici non navigabili strettamente necessari.
- Date sono human-readable in ora locale e mantengono la colonna raw epoch/ms per sorting/audit.
- Boolean 1/0 hanno rappresentazione visuale coerente senza perdere il raw quando serve.
- Link/URL sono cliccabili secondo uno schema canonico; non si fa affidamento su Markdown grezzo nei viewer generici.
- Mappe sono disponibili quando esistono location/lat-lon utili.
- Click su valore applica il filtro per quel valore; click su data filtra tutte le entry del giorno.
- FK/backlink e label semantiche consentono navigazione frictionless sui DB selezionati.
- Verifica runtime reale su datasette.danielegalati.com passa mantenendo privacy/autenticazione.

status: pending

current_action: Waiting on Phase D

next_action: Dopo Phase D, applicare la UX standard ai soli DB esposti e verificare il runtime reale.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "10",
      "reason": "canonical repository identity",
      "related_projects": [
        "10"
      ]
    },
    "source": {
      "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
      "parent_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
      "kind": "phase",
      "title": "Phase E — UX Datasette standard e navigazione frictionless",
      "objective": "Implementare sull'istanza Datasette esistente una UX generica/riutilizzabile per i DB esposti: date locali d/m/yy hh:mm mantenendo raw epoch, boolean visuali coerenti, URL/link cliccabili senza perdere raw quando utile, mappe quando esistono lat/lon, click-to-filter sui valori e filtro giornaliero sulle date, FK/backlink e label come via primaria di navigazione; nascondere dall'interfaccia ordinaria i DB obsoleti/non selezionati.",
      "acceptance_json": "[\"L'interfaccia ordinaria mostra solo i DB con datasette_expose=yes, salvo endpoint tecnici non navigabili strettamente necessari.\", \"Date sono human-readable in ora locale e mantengono la colonna raw epoch/ms per sorting/audit.\", \"Boolean 1/0 hanno rappresentazione visuale coerente senza perdere il raw quando serve.\", \"Link/URL sono cliccabili secondo uno schema canonico; non si fa affidamento su Markdown grezzo nei viewer generici.\", \"Mappe sono disponibili quando esistono location/lat-lon utili.\", \"Click su valore applica il filtro per quel valore; click su data filtra tutte le entry del giorno.\", \"FK/backlink e label semantiche consentono navigazione frictionless sui DB selezionati.\", \"Verifica runtime reale su datasette.danielegalati.com passa mantenendo privacy/autenticazione.\"]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": -9950,
      "current_action": "Waiting on Phase D",
      "next_action": "Dopo Phase D, applicare la UX standard ai soli DB esposti e verificare il runtime reale.",
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/datasette5",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T10:14:09Z",
      "updated_at": "2026-09-27T10:14:09Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "tag": "priority:p0"
      },
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "tag": "priority:absolute"
      },
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "tag": "datasette"
      },
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "tag": "ux"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "depends_on_work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "required": 1,
        "note": "c2-intake"
      },
      {
        "work_item_id": "wi:e20d87af9a6641c385b03b40aa72ab8a",
        "depends_on_work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "required": 1,
        "note": "c2-intake"
      },
      {
        "work_item_id": "wi:879ae0332e364440ad013f090a63714d",
        "depends_on_work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "required": 1,
        "note": "c2-intake"
      }
    ],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
