# C3 schedule/ack deadlock: writer schedule mutation #9783 created claimed run abddbd99029d41af9969572eb20bdce7 for wi:26eb789fcbd94f85954f0c8494b22050 but left work_items.status=pending. c2_runtime only processes claimed/running runs when pa

<!-- migration-48e827b6dee63670 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `issue:59ad4b6948aa4184bcdb286e8ba22ac3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### issue:59ad4b6948aa4184bcdb286e8ba22ac3

C3 schedule/ack deadlock: writer schedule mutation #9783 created claimed run abddbd99029d41af9969572eb20bdce7 for wi:26eb789fcbd94f85954f0c8494b22050 but left work_items.status=pending. c2_runtime only processes claimed/running runs when parent work item status=running, so it emits active=0 and never submits acknowledge/executor_started. The new triage batch cannot launch.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "explicit C3/C2 repository subject",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "issue_id": "issue:59ad4b6948aa4184bcdb286e8ba22ac3",
      "description": "C3 schedule/ack deadlock: writer schedule mutation #9783 created claimed run abddbd99029d41af9969572eb20bdce7 for wi:26eb789fcbd94f85954f0c8494b22050 but left work_items.status=pending. c2_runtime only processes claimed/running runs when parent work item status=running, so it emits active=0 and never submits acknowledge/executor_started. The new triage batch cannot launch.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": "01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "chat_url": "codex://threads/01a0f7fd-fd04-73f3-8ab3-437d30ed9ebc",
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790870327122,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:58:47Z"
    },
    "issue_work_item_links": []
  }
]
```
