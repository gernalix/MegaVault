# Regression: Regression: impedire il riavvio automatico del browser RDC da C2

<!-- migration-d2e3e31d1d9a9ff6 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:e3a021dde2134b8980cb33a4cc3243c3`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Regression: Regression: impedire il riavvio automatico del browser RDC da C2

C2/RDC browser isolation failure: chatgpt-rdc-supervisor normal-chrome-profile is a symlink to ~/.config/google-chrome. Chrome rejects CDP on the default profile, browser-health then fails every minute, while recovery/manual supervisor actions can launch/kill processes against the real Chrome profile. During the incident Chrome PID 923372 (normal browser, --restore-last-session) coredumped with SIGTRAP at 17:41:15 and multiple Chrome windows/ChatGPT conversations became unavailable. Supervisor must never mutate/kill/relaunch the user normal Chrome profile; use a physically separate profile and hard fencing.

status: pending

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
      "work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
      "parent_id": null,
      "kind": "task",
      "title": "Regression: Regression: impedire il riavvio automatico del browser RDC da C2",
      "objective": "C2/RDC browser isolation failure: chatgpt-rdc-supervisor normal-chrome-profile is a symlink to ~/.config/google-chrome. Chrome rejects CDP on the default profile, browser-health then fails every minute, while recovery/manual supervisor actions can launch/kill processes against the real Chrome profile. During the incident Chrome PID 923372 (normal browser, --restore-last-session) coredumped with SIGTRAP at 17:41:15 and multiple Chrome windows/ChatGPT conversations became unavailable. Supervisor must never mutate/kill/relaunch the user normal Chrome profile; use a physically separate profile and hard fencing.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 5000,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T09:59:56Z",
      "updated_at": "2026-09-30T09:59:56Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
        "tag": "regression"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
        "to_work_item_id": "wi:db4eb9c690ce4db88f75f0e8823409b0",
        "relation_type": "regression_of",
        "created_at": "2026-09-30T09:59:56Z",
        "actor": "c2-issue-triage",
        "note": "issue:80d776b455e0470eb008d6859aeb404c"
      }
    ],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2090,
        "work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
        "evidence_kind": "issue_inbox",
        "label": "issue:80d776b455e0470eb008d6859aeb404c",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2/RDC browser isolation failure: chatgpt-rdc-supervisor normal-chrome-profile is a symlink to ~/.config/google-chrome. Chrome rejects CDP on the default profile, browser-health then fails every minute, while recovery/manual supervisor actions can launch/kill processes against the real Chrome profile. During the incident Chrome PID 923372 (normal browser, --restore-last-session) coredumped with SIGTRAP at 17:41:15 and multiple Chrome windows/ChatGPT conversations became unavailable. Supervisor must never mutate/kill/relaunch the user normal Chrome profile; use a physically separate profile and hard fencing.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:80d776b455e0470eb008d6859aeb404c\", \"observed_at_ms\": 1790697596139, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T09:59:56Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:80d776b455e0470eb008d6859aeb404c",
        "work_item_id": "wi:e3a021dde2134b8980cb33a4cc3243c3",
        "role": "decision",
        "created_at": "2026-09-29T15:59:56Z"
      }
    ]
  }
]
```
