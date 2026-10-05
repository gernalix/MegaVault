# C3 Symphony ownership recovery gap found by the first real PersonalHub batch: release_unstarted_symphony_run can mark a run failed and remove C3 resource leases after the worker fails before external binding/tracker publication, but reserve

<!-- migration-5a9cb22e83c44cd3 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:3d44ce0d12dc42998a8d70e0f1ab3c43`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:3d44ce0d12dc42998a8d70e0f1ab3c43

C3 Symphony ownership recovery gap found by the first real PersonalHub batch: release_unstarted_symphony_run can mark a run failed and remove C3 resource leases after the worker fails before external binding/tracker publication, but reserve_ownership may already have persisted a durable reserved owner. The successor run is then rejected with symphony_ownership_conflict although the prior run has no tracker, binding, result, or worktree changes. Add a safe evidence-gated recovery/retirement path for reserved ownership from a failed unstarted run; do not weaken ownership protection for published or ambiguous runs.

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
      "issue_id": "issue:3d44ce0d12dc42998a8d70e0f1ab3c43",
      "description": "C3 Symphony ownership recovery gap found by the first real PersonalHub batch: release_unstarted_symphony_run can mark a run failed and remove C3 resource leases after the worker fails before external binding/tracker publication, but reserve_ownership may already have persisted a durable reserved owner. The successor run is then rejected with symphony_ownership_conflict although the prior run has no tracker, binding, result, or worktree changes. Add a safe evidence-gated recovery/retirement path for reserved ownership from a failed unstarted run; do not weaken ownership protection for published or ambiguous runs.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": "symphony",
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
      "origin_run_id": "04d159166ae24da0bc776b108ba871db",
      "observed_at_ms": 1790984208577,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-02T23:36:48Z"
    },
    "issue_work_item_links": []
  }
]
```
