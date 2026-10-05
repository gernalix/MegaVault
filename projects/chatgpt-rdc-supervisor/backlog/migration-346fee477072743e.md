# Reduce empty RDC worker-output polling

<!-- migration-346fee477072743e -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:58349358cc5f4aa19ebcba3ff3a3152c`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Reduce empty RDC worker-output polling

Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: repeated RDC read_process_output polling of multiple Codex processes with timeout_ms=8000/10000 produced empty 'No output in requested range' responses and consumed material wall-clock time. Example around 14:58:12-14:58:30 CEST: two polls returned no new output after ~18 seconds. Optimize worker monitoring to avoid long blocking empty polls, preferably event-driven/adaptive/backoff/batched.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "105"
      ]
    },
    "source": {
      "work_item_id": "wi:58349358cc5f4aa19ebcba3ff3a3152c",
      "parent_id": null,
      "kind": "task",
      "title": "Reduce empty RDC worker-output polling",
      "objective": "Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: repeated RDC read_process_output polling of multiple Codex processes with timeout_ms=8000/10000 produced empty 'No output in requested range' responses and consumed material wall-clock time. Example around 14:58:12-14:58:30 CEST: two polls returned no new output after ~18 seconds. Optimize worker monitoring to avoid long blocking empty polls, preferably event-driven/adaptive/backoff/batched.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "Parked during roadmap semantic reconciliation.",
      "next_action": "Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.",
      "blocker": "Deferred pending Symphony migration/replacement decision.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/codex-roadmap",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 0,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:05:29Z",
      "updated_at": "2026-09-28T06:45:04Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:58349358cc5f4aa19ebcba3ff3a3152c",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1010,
        "work_item_id": "wi:58349358cc5f4aa19ebcba3ff3a3152c",
        "evidence_kind": "issue_inbox",
        "label": "issue:4b9bdd7c196542139e1ed29fa0973653",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Retrospective bottleneck from ChatGPT conversation 6ab8f2d7-ad14-83eb-b53b-c386288d3e46: repeated RDC read_process_output polling of multiple Codex processes with timeout_ms=8000/10000 produced empty 'No output in requested range' responses and consumed material wall-clock time. Example around 14:58:12-14:58:30 CEST: two polls returned no new output after ~18 seconds. Optimize worker monitoring to avoid long blocking empty polls, preferably event-driven/adaptive/backoff/batched.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4b9bdd7c196542139e1ed29fa0973653\", \"observed_at_ms\": 1790516612393, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:05:29Z"
      },
      {
        "evidence_id": 1455,
        "work_item_id": "wi:58349358cc5f4aa19ebcba3ff3a3152c",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:04Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:4b9bdd7c196542139e1ed29fa0973653",
        "work_item_id": "wi:58349358cc5f4aa19ebcba3ff3a3152c",
        "role": "decision",
        "created_at": "2026-09-27T13:43:32Z"
      }
    ]
  }
]
```
