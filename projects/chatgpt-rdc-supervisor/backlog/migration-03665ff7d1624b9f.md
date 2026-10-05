# RDC supervisor: aggiornare i selettori DOM per stato auth, composer e turni

<!-- migration-03665ff7d1624b9f -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:db9f575d8f3a40e08fb16dec95a2ad11`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### RDC supervisor: aggiornare i selettori DOM per stato auth, composer e turni

ChatGPT RDC supervisor: i selettori DOM sono obsoleti rispetto alla UI ChatGPT attuale. Sulla chat 6ab8f2d7-ad14-83eb-b53b-c386288d3e46 il DOM contiene messaggi e un contenteditable visibile, ma inspect() restituisce authenticated=False, composer=False, error_kind=dom-unknown, turn_count=0 e text_chars=0. I selettori correnti (#prompt-textarea / textarea[data-testid*=prompt] / [contenteditable=true][data-lexical-editor=true] e [data-testid^=conversation-turn]/article) non riconoscono il composer/turni attuali, producendo falsi stalli e recovery errati. Aggiornare il parser con selettori resilienti e test E2E sulla UI reale.

status: pending

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
      "work_item_id": "wi:db9f575d8f3a40e08fb16dec95a2ad11",
      "parent_id": null,
      "kind": "task",
      "title": "RDC supervisor: aggiornare i selettori DOM per stato auth, composer e turni",
      "objective": "ChatGPT RDC supervisor: i selettori DOM sono obsoleti rispetto alla UI ChatGPT attuale. Sulla chat 6ab8f2d7-ad14-83eb-b53b-c386288d3e46 il DOM contiene messaggi e un contenteditable visibile, ma inspect() restituisce authenticated=False, composer=False, error_kind=dom-unknown, turn_count=0 e text_chars=0. I selettori correnti (#prompt-textarea / textarea[data-testid*=prompt] / [contenteditable=true][data-lexical-editor=true] e [data-testid^=conversation-turn]/article) non riconoscono il composer/turni attuali, producendo falsi stalli e recovery errati. Aggiornare il parser con selettori resilienti e test E2E sulla UI reale.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:05:31Z",
      "updated_at": "2026-09-27T21:05:31Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:db9f575d8f3a40e08fb16dec95a2ad11",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1021,
        "work_item_id": "wi:db9f575d8f3a40e08fb16dec95a2ad11",
        "evidence_kind": "issue_inbox",
        "label": "issue:ce4e4516976240248b433755ae51dd54",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"ChatGPT RDC supervisor: i selettori DOM sono obsoleti rispetto alla UI ChatGPT attuale. Sulla chat 6ab8f2d7-ad14-83eb-b53b-c386288d3e46 il DOM contiene messaggi e un contenteditable visibile, ma inspect() restituisce authenticated=False, composer=False, error_kind=dom-unknown, turn_count=0 e text_chars=0. I selettori correnti (#prompt-textarea / textarea[data-testid*=prompt] / [contenteditable=true][data-lexical-editor=true] e [data-testid^=conversation-turn]/article) non riconoscono il composer/turni attuali, producendo falsi stalli e recovery errati. Aggiornare il parser con selettori resilienti e test E2E sulla UI reale.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:ce4e4516976240248b433755ae51dd54\", \"observed_at_ms\": 1790518531007, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:05:31Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:ce4e4516976240248b433755ae51dd54",
        "work_item_id": "wi:db9f575d8f3a40e08fb16dec95a2ad11",
        "role": "decision",
        "created_at": "2026-09-27T14:15:31Z"
      }
    ]
  }
]
```
