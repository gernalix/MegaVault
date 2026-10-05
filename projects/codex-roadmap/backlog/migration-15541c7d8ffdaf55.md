# C3 audit_events è quasi interamente rumore: ~295.081 eventi terminal_reconcile_skipped su ~296k totali. Evitare di persistere i no-op/skipped ad ogni ciclo o coalescerli/metricizzarli fuori dallo storico canonico, mantenendo solo eventi azi

<!-- migration-15541c7d8ffdaf55 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:11a03c388d1e429e9b26e60a2fd0cf9d`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:11a03c388d1e429e9b26e60a2fd0cf9d

C3 audit_events è quasi interamente rumore: ~295.081 eventi terminal_reconcile_skipped su ~296k totali. Evitare di persistere i no-op/skipped ad ogni ciclo o coalescerli/metricizzarli fuori dallo storico canonico, mantenendo solo eventi azionabili o cambi di stato.

state: pending

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
      "issue_id": "issue:11a03c388d1e429e9b26e60a2fd0cf9d",
      "description": "C3 audit_events è quasi interamente rumore: ~295.081 eventi terminal_reconcile_skipped su ~296k totali. Evitare di persistere i no-op/skipped ad ogni ciclo o coalescerli/metricizzarli fuori dallo storico canonico, mantenendo solo eventi azionabili o cambi di stato.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790873176543,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T16:46:16Z"
    },
    "issue_work_item_links": []
  }
]
```
