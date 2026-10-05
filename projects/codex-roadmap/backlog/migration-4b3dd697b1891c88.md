# C3 post-cutover preparation/dispatch race observed live on 2026-10-02. `c3_auto_prepare.py --apply --limit 1` called the documented `c2_prepare_codex` path, whose contract says preparation leaves the item pending and never dispatches; howev

<!-- migration-4b3dd697b1891c88 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:86d78fb985073fea1f1dc4dde153924c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:86d78fb985073fea1f1dc4dde153924c

C3 post-cutover preparation/dispatch race observed live on 2026-10-02. `c3_auto_prepare.py --apply --limit 1` called the documented `c2_prepare_codex` path, whose contract says preparation leaves the item pending and never dispatches; however the event-driven runtime immediately scheduled the newly materialized spec before the caller could validate/read back the prepared artifact. The first candidate also had acceptance_json=[] and entered Symphony as run f77c639f283c4abd9f85838e1c2d29e9 before supervisor intervention. Make preparation and dispatch sequencing explicit/fenced: preparation must provide a stable validation/readback boundary, and runtime must not auto-dispatch a newly prepared item until that boundary/eligibility gate is satisfied. Preserve normal event-driven scheduling after the gate.

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
      "issue_id": "issue:86d78fb985073fea1f1dc4dde153924c",
      "description": "C3 post-cutover preparation/dispatch race observed live on 2026-10-02. `c3_auto_prepare.py --apply --limit 1` called the documented `c2_prepare_codex` path, whose contract says preparation leaves the item pending and never dispatches; however the event-driven runtime immediately scheduled the newly materialized spec before the caller could validate/read back the prepared artifact. The first candidate also had acceptance_json=[] and entered Symphony as run f77c639f283c4abd9f85838e1c2d29e9 before supervisor intervention. Make preparation and dispatch sequencing explicit/fenced: preparation must provide a stable validation/readback boundary, and runtime must not auto-dispatch a newly prepared item until that boundary/eligibility gate is satisfied. Preserve normal event-driven scheduling after the gate.",
      "repo": "gernalix/codex-roadmap",
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": "wi:38b70e5910464b40bbd52e080fb83abb",
      "origin_run_id": null,
      "observed_at_ms": 1790937133189,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-02T10:32:13Z"
    },
    "issue_work_item_links": []
  }
]
```
