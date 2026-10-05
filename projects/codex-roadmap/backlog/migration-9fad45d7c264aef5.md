# C3 roadmap snapshot efficiency/stability finding: c3-roadmap-snapshot.service repeatedly reports left-over git processes in its control group on subsequent starts, and several successful snapshot cycles consumed roughly 1–2.5 GB peak memory

<!-- migration-9fad45d7c264aef5 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:5aa64d45f2b14a028b9df61d89ca31f6`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:5aa64d45f2b14a028b9df61d89ca31f6

C3 roadmap snapshot efficiency/stability finding: c3-roadmap-snapshot.service repeatedly reports left-over git processes in its control group on subsequent starts, and several successful snapshot cycles consumed roughly 1–2.5 GB peak memory despite only refreshing the read-only roadmap snapshot. This is a material desktop/OOM risk and unnecessary resource cost. Investigate child-process cleanup and memory amplification in c2_snapshot_sync/c3-roadmap-snapshot execution; ensure each invocation reaps git children and keeps bounded memory while preserving canonical snapshot correctness.

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
      "issue_id": "issue:5aa64d45f2b14a028b9df61d89ca31f6",
      "description": "C3 roadmap snapshot efficiency/stability finding: c3-roadmap-snapshot.service repeatedly reports left-over git processes in its control group on subsequent starts, and several successful snapshot cycles consumed roughly 1–2.5 GB peak memory despite only refreshing the read-only roadmap snapshot. This is a material desktop/OOM risk and unnecessary resource cost. Investigate child-process cleanup and memory amplification in c2_snapshot_sync/c3-roadmap-snapshot execution; ensure each invocation reaps git children and keeps bounded memory while preserving canonical snapshot correctness.",
      "repo": "gernalix/codex-roadmap",
      "code_location": "systemd/c3-roadmap-snapshot.service",
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790856480958,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T12:08:00Z"
    },
    "issue_work_item_links": []
  }
]
```
