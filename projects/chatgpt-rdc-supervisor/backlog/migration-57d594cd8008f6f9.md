# RDC supervisor: impedire invii duplicati tra percorso manuale e automatico

<!-- migration-57d594cd8008f6f9 -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:94bef287ab7a4dc7960a084a9ab6a72f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### RDC supervisor: impedire invii duplicati tra percorso manuale e automatico

c2-roadmap-live-watch.py contains duplicated/manual-steer handling paths or is easy to patch into duplication: two MANUAL_STEER blocks can coexist, risking duplicate sends or inconsistent Stop→Send behavior. Consolidate manual steer into one canonical function/path and add a regression test that one queued steer produces exactly one user message.

status: waiting

current_action: WAITING_ON_EVIDENCE

next_action: Identify the real installed duplicate-send path and authoritative owner first, then retarget/reconcile before any RDC code worker.

blocker: The item names the wrong/unknown repository path; no current installed duplicate-send owner/path has been identified.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "canonical repository identity",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:94bef287ab7a4dc7960a084a9ab6a72f",
      "parent_id": null,
      "kind": "task",
      "title": "RDC supervisor: impedire invii duplicati tra percorso manuale e automatico",
      "objective": "c2-roadmap-live-watch.py contains duplicated/manual-steer handling paths or is easy to patch into duplication: two MANUAL_STEER blocks can coexist, risking duplicate sends or inconsistent Stop→Send behavior. Consolidate manual steer into one canonical function/path and add a regression test that one queued steer produces exactly one user message.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "WAITING_ON_EVIDENCE",
      "next_action": "Identify the real installed duplicate-send path and authoritative owner first, then retarget/reconcile before any RDC code worker.",
      "blocker": "The item names the wrong/unknown repository path; no current installed duplicate-send owner/path has been identified.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:06:31Z",
      "updated_at": "2026-09-28T22:47:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:94bef287ab7a4dc7960a084a9ab6a72f",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1032,
        "work_item_id": "wi:94bef287ab7a4dc7960a084a9ab6a72f",
        "evidence_kind": "issue_inbox",
        "label": "issue:e28e4f60098a45d9899cab1418bfa7d3",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"c2-roadmap-live-watch.py\", \"description\": \"c2-roadmap-live-watch.py contains duplicated/manual-steer handling paths or is easy to patch into duplication: two MANUAL_STEER blocks can coexist, risking duplicate sends or inconsistent Stop→Send behavior. Consolidate manual steer into one canonical function/path and add a regression test that one queued steer produces exactly one user message.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:e28e4f60098a45d9899cab1418bfa7d3\", \"observed_at_ms\": 1790530875087, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:06:31Z"
      },
      {
        "evidence_id": 1656,
        "work_item_id": "wi:94bef287ab7a4dc7960a084a9ab6a72f",
        "evidence_kind": "classification",
        "label": "RDC whole-batch reconciliation explicitly requires correct owner/path before code.",
        "uri": null,
        "value_json": "\"RDC whole-batch reconciliation explicitly requires correct owner/path before code.\"",
        "created_at": "2026-09-28T22:47:20Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:e28e4f60098a45d9899cab1418bfa7d3",
        "work_item_id": "wi:94bef287ab7a4dc7960a084a9ab6a72f",
        "role": "decision",
        "created_at": "2026-09-27T17:41:15Z"
      }
    ]
  }
]
```
