# MegaVault contiene ancora le view quota_overview e quota_diagnostics, ma la tabella sorgente quota_snapshots non esiste nel DB corrente. Sono residui stale/broken e vanno rimossi o riallineati all'owner canonico codex-usage-monitor, evitand

<!-- migration-539082d115cc77cf -->

Migrated project backlog. Project: **megavault**; project_id: 23.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 23.

Provenance: `issue:36f8601f38c64ee2a7aaf56d8d6efe87`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:36f8601f38c64ee2a7aaf56d8d6efe87

MegaVault contiene ancora le view quota_overview e quota_diagnostics, ma la tabella sorgente quota_snapshots non esiste nel DB corrente. Sono residui stale/broken e vanno rimossi o riallineati all'owner canonico codex-usage-monitor, evitando una seconda superficie quota in MegaVault.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "23",
      "reason": "canonical repository identity",
      "related_projects": [
        "23"
      ]
    },
    "source": {
      "issue_id": "issue:36f8601f38c64ee2a7aaf56d8d6efe87",
      "description": "MegaVault contiene ancora le view quota_overview e quota_diagnostics, ma la tabella sorgente quota_snapshots non esiste nel DB corrente. Sono residui stale/broken e vanno rimossi o riallineati all'owner canonico codex-usage-monitor, evitando una seconda superficie quota in MegaVault.",
      "repo": "gernalix/MegaVault",
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790873334978,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T16:48:54Z"
    },
    "issue_work_item_links": []
  }
]
```
