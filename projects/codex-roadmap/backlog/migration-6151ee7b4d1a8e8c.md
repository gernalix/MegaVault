# Post-cutover C3 CI is still running legacy tests that require retired artifacts and schemas. Fresh evidence from PR #9997: CI/Roadmap integrity fail because tests expect /home/runner/work/codex-roadmap/codex-roadmap/roadmap.md and spiegazio

<!-- migration-6151ee7b4d1a8e8c -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:1c8ef738372aec85ae0e14f16a555e91`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:1c8ef738372aec85ae0e14f16a555e91

Post-cutover C3 CI is still running legacy tests that require retired artifacts and schemas. Fresh evidence from PR #9997: CI/Roadmap integrity fail because tests expect /home/runner/work/codex-roadmap/codex-roadmap/roadmap.md and spiegazioni.md, expect manual_order_overrides to exist, and expect old manual-order fields in the summary schema. These artifacts/features were intentionally retired by M2. This causes unrelated new C3 changes to fail CI despite targeted post-cutover tests passing. Update/retire the legacy tests and repository-consistency expectations so CI validates the current C3 architecture rather than removed projections/Workflowy ordering, without reintroducing retired components.

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
      "issue_id": "issue:1c8ef738372aec85ae0e14f16a555e91",
      "description": "Post-cutover C3 CI is still running legacy tests that require retired artifacts and schemas. Fresh evidence from PR #9997: CI/Roadmap integrity fail because tests expect /home/runner/work/codex-roadmap/codex-roadmap/roadmap.md and spiegazioni.md, expect manual_order_overrides to exist, and expect old manual-order fields in the summary schema. These artifacts/features were intentionally retired by M2. This causes unrelated new C3 changes to fail CI despite targeted post-cutover tests passing. Update/retire the legacy tests and repository-consistency expectations so CI validates the current C3 architecture rather than removed projections/Workflowy ordering, without reintroducing retired components.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790936354086,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-02T10:19:14Z"
    },
    "issue_work_item_links": []
  }
]
```
