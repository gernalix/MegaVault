# Aggiungere a PersonalHub un modulo Notifications che sostituisca Notisave: catturare le notifiche accessibili via Android NotificationListenerService (titolo, testo, app/package, timestamp, notification key e principali extras; eventi POSTE

<!-- migration-1f4ce835bad83560 -->

Migrated project backlog. Project: **personalhub**; project_id: 49.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 49.

Provenance: `issue:6ab711a9cb384219a8916b07402d8360`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:6ab711a9cb384219a8916b07402d8360

Aggiungere a PersonalHub un modulo Notifications che sostituisca Notisave: catturare le notifiche accessibili via Android NotificationListenerService (titolo, testo, app/package, timestamp, notification key e principali extras; eventi POSTED/UPDATED/REMOVED), salvarle append-only in un database SQLite dedicato e non versionato da Git, e offrire almeno timeline, ricerca full-text e filtri per app/data. Integrare il modulo direttamente in PersonalHub invece di creare un'app separata; evitare polling/foreground service per mantenere il consumo batteria minimo. Prevedere export/backup separato dal Git. Scope iniziale MVP, estensibile in seguito a statistiche e correlazioni con altri moduli PH.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "49",
      "reason": "explicit PersonalHub subject",
      "related_projects": [
        "49"
      ]
    },
    "source": {
      "issue_id": "issue:6ab711a9cb384219a8916b07402d8360",
      "description": "Aggiungere a PersonalHub un modulo Notifications che sostituisca Notisave: catturare le notifiche accessibili via Android NotificationListenerService (titolo, testo, app/package, timestamp, notification key e principali extras; eventi POSTED/UPDATED/REMOVED), salvarle append-only in un database SQLite dedicato e non versionato da Git, e offrire almeno timeline, ricerca full-text e filtri per app/data. Integrare il modulo direttamente in PersonalHub invece di creare un'app separata; evitare polling/foreground service per mantenere il consumo batteria minimo. Prevedere export/backup separato dal Git. Scope iniziale MVP, estensibile in seguito a statistiche e correlazioni con altri moduli PH.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790880827335,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T18:53:47Z"
    },
    "issue_work_item_links": []
  }
]
```
