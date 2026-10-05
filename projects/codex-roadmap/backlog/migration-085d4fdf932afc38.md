# C3 auto-preparation repository casing bug found by the first real PersonalHub batch: c3_auto_prepare.repo_slug lowercases the canonical MegaVault GitHub slug and rewrites work_items.repo from gernalix/PersonalHub to gernalix/personalhub. Th

<!-- migration-085d4fdf932afc38 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:e57a0f1bda9646cc86d5b1dd43a0269f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:e57a0f1bda9646cc86d5b1dd43a0269f

C3 auto-preparation repository casing bug found by the first real PersonalHub batch: c3_auto_prepare.repo_slug lowercases the canonical MegaVault GitHub slug and rewrites work_items.repo from gernalix/PersonalHub to gernalix/personalhub. The production Symphony bridge intentionally verifies the exact remote identity and rejects the prepared worktree with production_worktree_identity_mismatch. Preserve canonical remote_url casing while using a case-insensitive normalized key only for matching; add regression coverage.

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
      "issue_id": "issue:e57a0f1bda9646cc86d5b1dd43a0269f",
      "description": "C3 auto-preparation repository casing bug found by the first real PersonalHub batch: c3_auto_prepare.repo_slug lowercases the canonical MegaVault GitHub slug and rewrites work_items.repo from gernalix/PersonalHub to gernalix/personalhub. The production Symphony bridge intentionally verifies the exact remote identity and rejects the prepared worktree with production_worktree_identity_mismatch. Preserve canonical remote_url casing while using a case-insensitive normalized key only for matching; add regression coverage.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": "symphony",
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": "wi:8740f8fd8e744642b01a3abc7055172e",
      "origin_run_id": "73fc69fd43e94fce94b87dc85b1f0ff8",
      "observed_at_ms": 1790983887189,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-02T23:31:27Z"
    },
    "issue_work_item_links": []
  }
]
```
