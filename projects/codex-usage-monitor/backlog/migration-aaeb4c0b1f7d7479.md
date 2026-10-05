# Quantify Symphony pilot Codex token and quota cost

<!-- migration-aaeb4c0b1f7d7479 -->

Migrated project backlog. Project: **codex-usage-monitor**; project_id: 8.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 8.

Provenance: `wi:a588bda1aa184789a0bfa8c78e951e86`, `issue:7e44b55cf4a948208c2a2659e643c40d`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Quantify Symphony pilot Codex token and quota cost

Measure the reported pilot input/output and cached-token usage against actual Codex quota or billing, and assess whether workflow/context trimming reduces cost before high-volume roadmap migration.

status: pending

### issue:7e44b55cf4a948208c2a2659e643c40d

C3 Symphony can consume Codex quota invisibly while neither Codex Desktop nor CLI is open: on 2026-10-03 GH-4 / PersonalHub PROMPT_ID 281063 auto-started GPT-5.6 Sol medium and consumed 2,180,580 tokens in ~4 minutes; the Symphony backend reported 31,164,019 total tokens over ~79 minutes. Add a fail-safe execution/quota gate so background Codex work cannot start or continue unexpectedly, expose clearly when a token-consuming executor is active, and make autonomous background execution explicitly controllable without disabling the rest of C3.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "8",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "8"
      ]
    },
    "source": {
      "work_item_id": "wi:a588bda1aa184789a0bfa8c78e951e86",
      "parent_id": null,
      "kind": "task",
      "title": "Quantify Symphony pilot Codex token and quota cost",
      "objective": "Measure the reported pilot input/output and cached-token usage against actual Codex quota or billing, and assess whether workflow/context trimming reduces cost before high-volume roadmap migration.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "/home/daniele/projects/symphony",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-29T11:13:57Z",
      "updated_at": "2026-09-29T11:13:57Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:a588bda1aa184789a0bfa8c78e951e86",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1691,
        "work_item_id": "wi:a588bda1aa184789a0bfa8c78e951e86",
        "evidence_kind": "issue_inbox",
        "label": "issue:cdc3a26fa40341a08e154b0e20442ad2",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Symphony pilot token-cost finding: a trivial two-file canary completed correctly in one turn using gpt-5.6-terra medium, but Symphony/Codex reported 142,852 cumulative input tokens and 1,178 output tokens across 6 response records; 112,384 input tokens were cached. Before migrating high-volume roadmap execution, quantify how this maps to Codex quota/cost and whether workflow/context trimming materially reduces it.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:cdc3a26fa40341a08e154b0e20442ad2\", \"observed_at_ms\": 1790583046391, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/symphony\"}",
        "created_at": "2026-09-29T11:13:57Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:cdc3a26fa40341a08e154b0e20442ad2",
        "work_item_id": "wi:a588bda1aa184789a0bfa8c78e951e86",
        "role": "decision",
        "created_at": "2026-09-28T08:10:46Z"
      }
    ]
  },
  {
    "routing": {
      "project": "8",
      "reason": "complementary evidence for same explicitly identified objective",
      "related_projects": [
        "8"
      ]
    },
    "source": {
      "issue_id": "issue:7e44b55cf4a948208c2a2659e643c40d",
      "description": "C3 Symphony can consume Codex quota invisibly while neither Codex Desktop nor CLI is open: on 2026-10-03 GH-4 / PersonalHub PROMPT_ID 281063 auto-started GPT-5.6 Sol medium and consumed 2,180,580 tokens in ~4 minutes; the Symphony backend reported 31,164,019 total tokens over ~79 minutes. Add a fail-safe execution/quota gate so background Codex work cannot start or continue unexpectedly, expose clearly when a token-consuming executor is active, and make autonomous background execution explicitly controllable without disabling the rest of C3.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790989548668,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-03T01:05:48Z"
    },
    "issue_work_item_links": []
  }
]
```
