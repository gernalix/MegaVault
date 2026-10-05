# Restore Codex Desktop Linux access through the current Cloudflare challenge

<!-- migration-46ce29468b106f4d -->

Migrated project backlog. Project: **chrome-codex-switcher**; project_id: 99.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 99.

Provenance: `wi:880930830ac54dcdb3ccf8d062f8648b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Restore Codex Desktop Linux access through the current Cloudflare challenge

Codex Desktop Linux remains unusable after upgrading chatgpt from 26.917.71314-1 to 26.924.22138-1. Local app-server 0.158.0-alpha.2.1 initializes successfully and thread/read works, but renderer/network requests to chatgpt.com repeatedly hit Cloudflare managed challenge (Enable JavaScript and cookies to continue) and RequestError, reproducing the same failure seen earlier today. Desktop cannot be relied on as C2 supervisor until this is fixed; CLI/app-server remains functional.

status: waiting

current_action: WAITING_ON_EVIDENCE

next_action: Wait for a reproducible current managed Desktop challenge plus supported app/network diagnostics or a vendor/client state change, then reconcile.

blocker: No current reproducible Codex Desktop Cloudflare challenge is tied to a chrome-codex-switcher source defect.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "99",
      "reason": "canonical repository identity",
      "related_projects": [
        "99"
      ]
    },
    "source": {
      "work_item_id": "wi:880930830ac54dcdb3ccf8d062f8648b",
      "parent_id": null,
      "kind": "task",
      "title": "Restore Codex Desktop Linux access through the current Cloudflare challenge",
      "objective": "Codex Desktop Linux remains unusable after upgrading chatgpt from 26.917.71314-1 to 26.924.22138-1. Local app-server 0.158.0-alpha.2.1 initializes successfully and thread/read works, but renderer/network requests to chatgpt.com repeatedly hit Cloudflare managed challenge (Enable JavaScript and cookies to continue) and RequestError, reproducing the same failure seen earlier today. Desktop cannot be relied on as C2 supervisor until this is fixed; CLI/app-server remains functional.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "WAITING_ON_EVIDENCE",
      "next_action": "Wait for a reproducible current managed Desktop challenge plus supported app/network diagnostics or a vendor/client state change, then reconcile.",
      "blocker": "No current reproducible Codex Desktop Cloudflare challenge is tied to a chrome-codex-switcher source defect.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chrome-codex-switcher",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:04:54Z",
      "updated_at": "2026-09-28T22:47:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:880930830ac54dcdb3ccf8d062f8648b",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1007,
        "work_item_id": "wi:880930830ac54dcdb3ccf8d062f8648b",
        "evidence_kind": "issue_inbox",
        "label": "issue:0e436ac7de2e43959ddcb2b129491573",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"codex-desktop\", \"description\": \"Codex Desktop Linux remains unusable after upgrading chatgpt from 26.917.71314-1 to 26.924.22138-1. Local app-server 0.158.0-alpha.2.1 initializes successfully and thread/read works, but renderer/network requests to chatgpt.com repeatedly hit Cloudflare managed challenge (Enable JavaScript and cookies to continue) and RequestError, reproducing the same failure seen earlier today. Desktop cannot be relied on as C2 supervisor until this is fixed; CLI/app-server remains functional.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0e436ac7de2e43959ddcb2b129491573\", \"observed_at_ms\": 1790538341502, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:04:54Z"
      },
      {
        "evidence_id": 1658,
        "work_item_id": "wi:880930830ac54dcdb3ccf8d062f8648b",
        "evidence_kind": "classification",
        "label": "Batch-12 reconciliation classifies this as an external/version/session evidence wait with no source fix authority.",
        "uri": null,
        "value_json": "\"Batch-12 reconciliation classifies this as an external/version/session evidence wait with no source fix authority.\"",
        "created_at": "2026-09-28T22:47:20Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:0e436ac7de2e43959ddcb2b129491573",
        "work_item_id": "wi:880930830ac54dcdb3ccf8d062f8648b",
        "role": "decision",
        "created_at": "2026-09-27T19:45:41Z"
      }
    ]
  }
]
```
