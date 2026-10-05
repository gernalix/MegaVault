# Aggiungere la riconciliazione di progetto prima dei batch C2

<!-- migration-d6c513e16dc7b8a8 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:b4973cff2a6449bfa8e93af99d71ed7a`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Aggiungere la riconciliazione di progetto prima dei batch C2

Before dispatching a prioritized batch for one repository, reconcile current user requests, Inbox findings and canonical work-item specifications. Apply latest-user-intent-wins, mark stale or duplicate items superseded, identify dependencies and file overlaps, and consolidate compatible build/test cycles. Keep unrelated repositories parallel. The cited PersonalHub contradictions are motivating evidence; this task owns the C2 roadmap dispatch gate, not PersonalHub implementation.

status: blocked

current_action: BLOCKED

next_action: When Symphony scope is decided or a concrete current control-plane integrity failure occurs, freshly reconcile all seven batch-00 items and decide the smallest deterministic identity/readiness automation; otherwise keep using the pushed whole-batch checkpoint.

blocker: Separate C2-only deterministic semantic-compaction automation conflicts with the required AI semantic judgment and may be replaced by Symphony; no present duplicate-prevention or integrity defect requires another C2 code lane.

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
      "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
      "parent_id": null,
      "kind": "task",
      "title": "Aggiungere la riconciliazione di progetto prima dei batch C2",
      "objective": "Before dispatching a prioritized batch for one repository, reconcile current user requests, Inbox findings and canonical work-item specifications. Apply latest-user-intent-wins, mark stale or duplicate items superseded, identify dependencies and file overlaps, and consolidate compatible build/test cycles. Keep unrelated repositories parallel. The cited PersonalHub contradictions are motivating evidence; this task owns the C2 roadmap dispatch gate, not PersonalHub implementation.",
      "acceptance_json": "[]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "BLOCKED",
      "next_action": "When Symphony scope is decided or a concrete current control-plane integrity failure occurs, freshly reconcile all seven batch-00 items and decide the smallest deterministic identity/readiness automation; otherwise keep using the pushed whole-batch checkpoint.",
      "blocker": "Separate C2-only deterministic semantic-compaction automation conflicts with the required AI semantic judgment and may be replaced by Symphony; no present duplicate-prevention or integrity defect requires another C2 code lane.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-28T00:51:30Z",
      "updated_at": "2026-09-28T06:41:59Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "tag": "priority:p2"
      },
      {
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:948b530657cb46c78a5e403826e2b7f4",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T06:44:12Z",
        "actor": "c2-root-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "wi:e0eed3bec9584f3a82f28c77b7a00e38",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T06:44:12Z",
        "actor": "c2-root-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:5ab7dc7a6bf07aabc2a5",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:46:56Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:87ec725cf06e0cc7baca",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:88e2221ae2d33f610713",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:76ddc66ecd08ec2293c8",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:27dcb919a9e66ad2d3f0",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:d257e2780924892d9910",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:e685443f4fb7023f4e8c",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:7d878ed8bcc02e621b6f",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:4b619576fe52c78445ba",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:559ea5622b4f97cef5a0",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:7d61e8468fac8b307a62",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:997e9ab1a0748109a2cc",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:45513b096c545fc3e78d",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:087805c7fd0056031b85",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:4ea18b6d9c56ed8adb63",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:56a7bdf9a5a5ca6e262c",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:8e8e94ee08904dcfd342",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:3212129bc8e8dce87f68",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:d8e13b38be7ed8f9e1e9",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:8d8ce18fa8c47d1ad721",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:3bccf071755721ed153c",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:b5cf99bcc96cf8ed1319",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:bf4ec7e1b332d95a7f00",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:48baa9fa46efd11cef2a",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:892a3bf9a32133fef74d",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:d4ecc67dc0f97dd38e7d",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:06Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:89469e41b023f86eb4aa",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:18a44d989857a75fd450",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:14f698729113df1566d8",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:2b2909ff2958df515a4c",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:3493812dbfb15ba5079c",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:3c1e3041ace1d9459ff5",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:ca85ec32e60d1eb8a1a1",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:a35709005a09b3b892f8",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:269fd0d176ce10cbc976",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:3701cf2fffb9850c256e",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:f4d4d4c1788a00a7e81f",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:24381b8dca9c8d787d0a",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:5ebc51207dabaeb96be9",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:d79d44ce1fc99bea6b13",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:af191398dabc8e389060",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:110c40096c8641f25b19",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:2ec4595cf61c613d6646",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:63077c4cdea14df6395f",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:5abe58c430bc4e58e182",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:19472414ba33f00e78ea",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:e54edc40652bb1cace8e",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:2c1d09849c6c9628e151",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:55f55ab5697a0dcc9533",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:b911f987b9d93f197c67",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:46c738169cfda462b42e",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:f4c698ff366d3dae4407",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:a9b7929e2d14df79302b",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:2068d3c50552345474dc",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:4054f4f049d80c2fbbf5",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:075282a1de3792c91e83",
        "to_work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:49:07Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:b4973cff2a6449bfa8e93af99d71ed7a:f3fa2ef2b3b6b20bea31eb857228248b",
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": null,
        "completed_json": "[\"Reconciled all executable semantic batches against canonical C2 and MegaVault identity; saved and pushed checkpoint 56cdbcbc.\", \"Proved 118 active non-Inbox roadmap rows map to valid MegaVault projects and saved batches; zero runnable roadmap rows have execution specs.\", \"Preserved existing repository lanes and recorded exact conditional recovery for every BLOCKED item.\"]",
        "remaining_json": "[\"Deterministic C2 automation of semantic compaction is deferred pending the Symphony migration decision; the native checkpoint/manual pre-batch gate remains authoritative.\", \"On a concrete external/user transition, re-reconcile the affected entire batch and resume its existing lane.\"]",
        "evidence_json": "[\"operations/task-state/ROADMAP-BATCH-RECONCILIATION-20260928.md at pushed commit 56cdbcbc\", \"Remote C2 main 7cc58729 and MegaVault master 5c26b3d8 read-only snapshots; zero runnable_with_spec, one unrelated Inbox active run.\"]",
        "blocker": "Separate C2-only deterministic semantic-compaction automation conflicts with the required AI semantic judgment and may be replaced by Symphony; no present duplicate-prevention or integrity defect requires another C2 code lane.",
        "next_action": "When Symphony scope is decided or a concrete current control-plane integrity failure occurs, freshly reconcile all seven batch-00 items and decide the smallest deterministic identity/readiness automation; otherwise keep using the pushed whole-batch checkpoint.",
        "strict_contract": 1,
        "payload_sha256": "f3fa2ef2b3b6b20bea31eb857228248bb480afeea428c675131ff7180531b5ae",
        "captured_at": 1790627251.0110936
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 1348,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "issue_inbox",
        "label": "issue:4213b5a51c0b4a83ade6e97537cf8cf2",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"La roadmap C2 esegue i task dello stesso progetto/repo in ordine troppo letterale senza una riconciliazione semantica di progetto prima del dispatch. Nel blocco PersonalHub questo ha prodotto lavoro contraddittorio e ripetuto: task History chiuso perché confliggeva col contratto precedente nonostante l'intento utente più recente; gate/fix Datasette5 eseguiti poco prima della richiesta di rimuovere Datasette Lite; task i18n MissingTranslation ancora attivo mentre la direttiva più recente è English-only; più worker/PR sullo stesso repo causano merge queue e cicli CI/build duplicati. Aggiungere un project-level reconciliation/compaction gate prima di eseguire un batch prioritario sullo stesso repo: aggregare task/inbox/spec recenti, applicare latest-user-intent-wins, marcare stale/duplicate/superseded, costruire dependency/file-overlap plan e consolidare integrazione/test finali.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4213b5a51c0b4a83ade6e97537cf8cf2\", \"observed_at_ms\": 1790555237136, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-28T00:51:30Z"
      },
      {
        "evidence_id": 1431,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "classification",
        "label": "Roadmap batch reconciliation found 231 of 275 active work items lacked usable C2 project metadata.",
        "uri": null,
        "value_json": "\"Roadmap batch reconciliation found 231 of 275 active work items lacked usable C2 project metadata.\"",
        "created_at": "2026-09-28T06:41:59Z"
      },
      {
        "evidence_id": 1432,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "classification",
        "label": "MegaVault-backed inference resolved all 231 before batching; without this step repository-only grouping would have miscl",
        "uri": null,
        "value_json": "\"MegaVault-backed inference resolved all 231 before batching; without this step repository-only grouping would have misclassified a majority of the active backlog.\"",
        "created_at": "2026-09-28T06:41:59Z"
      },
      {
        "evidence_id": 1433,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "classification",
        "label": "The reconciled plan reduced 275 active items into 20 semantic batches and identified 92 stale/duplicate plus 59 Symphony",
        "uri": null,
        "value_json": "\"The reconciled plan reduced 275 active items into 20 semantic batches and identified 92 stale/duplicate plus 59 Symphony-deferred items.\"",
        "created_at": "2026-09-28T06:41:59Z"
      },
      {
        "evidence_id": 1650,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "executor_result",
        "label": "operations/task-state/ROADMAP-BATCH-RECONCILIATION-20260928.md at pushed commit 56cdbcbc",
        "uri": null,
        "value_json": "\"operations/task-state/ROADMAP-BATCH-RECONCILIATION-20260928.md at pushed commit 56cdbcbc\"",
        "created_at": "2026-09-28T20:27:31Z"
      },
      {
        "evidence_id": 1651,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "executor_result",
        "label": "Remote C2 main 7cc58729 and MegaVault master 5c26b3d8 read-only snapshots; zero runnable_with_spec, one unrelated Inbox ",
        "uri": null,
        "value_json": "\"Remote C2 main 7cc58729 and MegaVault master 5c26b3d8 read-only snapshots; zero runnable_with_spec, one unrelated Inbox active run.\"",
        "created_at": "2026-09-28T20:27:31Z"
      },
      {
        "evidence_id": 2454,
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "evidence_kind": "issue_inbox",
        "label": "issue:1ad5ccfe30434102a3277be43fe520f6",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"Candidate C2 cleanup command from the acceleration chat: after tested PRs/security gate completed, obsolete Symphony follow-ups and historical failed run 731707 still required manual reconciliation even though canonical evidence proved the work superseded/fulfilled. Add a deterministic `reconcile-superseded` style operation that, given merged commit/test evidence and parent linkage, previews and atomically closes/relinks stale failed or pending descendants without re-executing them.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:1ad5ccfe30434102a3277be43fe520f6\", \"observed_at_ms\": 1790784889637, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:4213b5a51c0b4a83ade6e97537cf8cf2",
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "role": "decision",
        "created_at": "2026-09-28T00:27:17Z"
      },
      {
        "issue_id": "issue:1ad5ccfe30434102a3277be43fe520f6",
        "work_item_id": "wi:b4973cff2a6449bfa8e93af99d71ed7a",
        "role": "decision",
        "created_at": "2026-09-30T16:45:28Z"
      }
    ]
  }
]
```
