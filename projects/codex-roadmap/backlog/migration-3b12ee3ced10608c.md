# PROMPT_ID authority duplication/drift: MegaVault prompt_id_registry and codex-roadmap/roadmap.sqlite both store prompt lifecycle/identity. Current read-only comparison found 339 overlapping IDs, 153 C3-only IDs (many historical reservations

<!-- migration-3b12ee3ced10608c -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:99b052e168314081b6f0bff5ca1c0414`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:99b052e168314081b6f0bff5ca1c0414

PROMPT_ID authority duplication/drift: MegaVault prompt_id_registry and codex-roadmap/roadmap.sqlite both store prompt lifecycle/identity. Current read-only comparison found 339 overlapping IDs, 153 C3-only IDs (many historical reservations) and 8 MegaVault-only IDs including recent materialized/used prompts such as 200487, 774390, 660629, 992303 and 669941. Maintaining two registries plus allocate/materialize bridge adds reconciliation cost and permits stale identity views. Define one canonical owner for PROMPT_ID allocation/lifecycle and make the other a projection/read-through view, with a migration that preserves historical IDs and uniqueness.

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
      "issue_id": "issue:99b052e168314081b6f0bff5ca1c0414",
      "description": "PROMPT_ID authority duplication/drift: MegaVault prompt_id_registry and codex-roadmap/roadmap.sqlite both store prompt lifecycle/identity. Current read-only comparison found 339 overlapping IDs, 153 C3-only IDs (many historical reservations) and 8 MegaVault-only IDs including recent materialized/used prompts such as 200487, 774390, 660629, 992303 and 669941. Maintaining two registries plus allocate/materialize bridge adds reconciliation cost and permits stale identity views. Define one canonical owner for PROMPT_ID allocation/lifecycle and make the other a projection/read-through view, with a migration that preserves historical IDs and uniqueness.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": "chatgpt",
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": "wi:c5bdf708a71d40c5a9902838ab8d8021",
      "origin_run_id": null,
      "observed_at_ms": 1790873663567,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T16:54:23Z"
    },
    "issue_work_item_links": []
  }
]
```
