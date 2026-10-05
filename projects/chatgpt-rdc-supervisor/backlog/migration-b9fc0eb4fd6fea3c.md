# RDC supervisor: definire soglie di stall e recovery basate su evidenza dinamica

<!-- migration-b9fc0eb4fd6fea3c -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105.

Provenance: `wi:c613a965f8a340f7906e512168c6626e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### RDC supervisor: definire soglie di stall e recovery basate su evidenza dinamica

ChatGPT RDC supervisor: generation-stall recovery is too conservative for the observed failure mode. On the roadmap executor chat the DOM signature and body length remained unchanged for about 40 seconds while the Stop button stayed active, with no slow-thinking banner. The current thresholds only suspect at 40s, verify at 90s and hard-stall at 180s, so a common dead generation can waste 1.5-3 minutes before intervention. Add an adaptive fast path for stable-signature + active Stop generations, using a bounded confirmation sample before stop+continue, while avoiding false positives during legitimate long tool calls.

status: waiting

current_action: WAITING_ON_EVIDENCE

next_action: Resume after trustworthy DOM progress instrumentation and bounded browser acceptance provide evidence for threshold design.

blocker: Dynamic stall/recovery thresholds depend on trustworthy DOM progress signals and bounded browser acceptance evidence that is not currently available.

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
      "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
      "parent_id": null,
      "kind": "task",
      "title": "RDC supervisor: definire soglie di stall e recovery basate su evidenza dinamica",
      "objective": "ChatGPT RDC supervisor: generation-stall recovery is too conservative for the observed failure mode. On the roadmap executor chat the DOM signature and body length remained unchanged for about 40 seconds while the Stop button stayed active, with no slow-thinking banner. The current thresholds only suspect at 40s, verify at 90s and hard-stall at 180s, so a common dead generation can waste 1.5-3 minutes before intervention. Add an adaptive fast path for stable-signature + active Stop generations, using a bounded confirmation sample before stop+continue, while avoiding false positives during legitimate long tool calls.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 9000,
      "current_action": "WAITING_ON_EVIDENCE",
      "next_action": "Resume after trustworthy DOM progress instrumentation and bounded browser acceptance provide evidence for threshold design.",
      "blocker": "Dynamic stall/recovery thresholds depend on trustworthy DOM progress signals and bounded browser acceptance evidence that is not currently available.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:05:32Z",
      "updated_at": "2026-09-28T22:47:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1024,
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "evidence_kind": "issue_inbox",
        "label": "issue:0db540b5c21a4d86b9433af2df3b0f9d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"ChatGPT RDC supervisor: generation-stall recovery is too conservative for the observed failure mode. On the roadmap executor chat the DOM signature and body length remained unchanged for about 40 seconds while the Stop button stayed active, with no slow-thinking banner. The current thresholds only suspect at 40s, verify at 90s and hard-stall at 180s, so a common dead generation can waste 1.5-3 minutes before intervention. Add an adaptive fast path for stable-signature + active Stop generations, using a bounded confirmation sample before stop+continue, while avoiding false positives during legitimate long tool calls.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:0db540b5c21a4d86b9433af2df3b0f9d\", \"observed_at_ms\": 1790518974874, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:05:32Z"
      },
      {
        "evidence_id": 1035,
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "evidence_kind": "issue_inbox",
        "label": "issue:fe685c09e9674c2abbba49b51cfaa250",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Roadmap executor live watcher used a 45-second unchanged-generation threshold as an automatic stop+continue action. For ChatGPT Extra High reasoning this is too aggressive and can interrupt legitimate long reasoning. Treat ~40-45s as suspected stall triggering observation/AI audit, ~90s as verification, and only use automatic recovery after a substantially longer confirmed-stall threshold (e.g. ~180s) unless explicit UI error evidence warrants earlier action.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:fe685c09e9674c2abbba49b51cfaa250\", \"observed_at_ms\": 1790520566597, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:06:32Z"
      },
      {
        "evidence_id": 1657,
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "evidence_kind": "classification",
        "label": "RDC whole-batch reconciliation marks this item signal-dependent and non-dispatchable.",
        "uri": null,
        "value_json": "\"RDC whole-batch reconciliation marks this item signal-dependent and non-dispatchable.\"",
        "created_at": "2026-09-28T22:47:20Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:fe685c09e9674c2abbba49b51cfaa250",
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "role": "matched",
        "created_at": "2026-09-27T14:49:26Z"
      },
      {
        "issue_id": "issue:0db540b5c21a4d86b9433af2df3b0f9d",
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "role": "decision",
        "created_at": "2026-09-27T14:22:54Z"
      },
      {
        "issue_id": "issue:fe685c09e9674c2abbba49b51cfaa250",
        "work_item_id": "wi:c613a965f8a340f7906e512168c6626e",
        "role": "decision",
        "created_at": "2026-09-27T14:49:26Z"
      }
    ]
  }
]
```
