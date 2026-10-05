# Resume bulk Inbox triage safely after GitHub API rate limits

<!-- migration-37d7d5d9167c47b1 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:be3cd0afad414f6297bc52155eceb0b1`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Resume bulk Inbox triage safely after GitHub API rate limits

C2 Inbox full-drain triage hit GitHub API rate-limit HTTP 403 while submitting the 18th fenced disposition in a burst; submit_mutation.py failed during _matching_issues before creating the Issue. gh api rate_limit showed the core bucket reset moments later and the same request succeeded. Bulk Inbox processing needs bounded rate-limit-aware submission/resume without duplicate mutations.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

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
      "work_item_id": "wi:be3cd0afad414f6297bc52155eceb0b1",
      "parent_id": null,
      "kind": "task",
      "title": "Resume bulk Inbox triage safely after GitHub API rate limits",
      "objective": "C2 Inbox full-drain triage hit GitHub API rate-limit HTTP 403 while submitting the 18th fenced disposition in a burst; submit_mutation.py failed during _matching_issues before creating the Issue. gh api rate_limit showed the core bucket reset moments later and the same request succeeded. Bulk Inbox processing needs bounded rate-limit-aware submission/resume without duplicate mutations.",
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
      "created_at": "2026-09-27T21:07:19Z",
      "updated_at": "2026-09-28T06:45:05Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:be3cd0afad414f6297bc52155eceb0b1",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1042,
        "work_item_id": "wi:be3cd0afad414f6297bc52155eceb0b1",
        "evidence_kind": "issue_inbox",
        "label": "issue:c8b72a5a290d4e72af4039d778779e27",
        "uri": "codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6",
        "value_json": "{\"chat_url\": \"codex://threads/01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"code_location\": null, \"description\": \"C2 Inbox full-drain triage hit GitHub API rate-limit HTTP 403 while submitting the 18th fenced disposition in a burst; submit_mutation.py failed during _matching_issues before creating the Issue. gh api rate_limit showed the core bucket reset moments later and the same request succeeded. Bulk Inbox processing needs bounded rate-limit-aware submission/resume without duplicate mutations.\", \"executor\": null, \"executor_ref\": \"01a0e425-7cbe-7270-b9b4-6d074a91c1b6\", \"issue_id\": \"issue:c8b72a5a290d4e72af4039d778779e27\", \"observed_at_ms\": 1790543095168, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:07:19Z"
      },
      {
        "evidence_id": 1459,
        "work_item_id": "wi:be3cd0afad414f6297bc52155eceb0b1",
        "evidence_kind": "classification",
        "label": "User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to",
        "uri": null,
        "value_json": "\"User explicitly directed that C2 will soon be largely replaced by Symphony; this C2-only enhancement is non-essential to current roadmap execution and should not compete for slots before the migration decision.\"",
        "created_at": "2026-09-28T06:45:05Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:c8b72a5a290d4e72af4039d778779e27",
        "work_item_id": "wi:be3cd0afad414f6297bc52155eceb0b1",
        "role": "decision",
        "created_at": "2026-09-27T21:04:55Z"
      }
    ]
  }
]
```
