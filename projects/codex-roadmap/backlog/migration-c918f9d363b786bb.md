# C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn

<!-- migration-c918f9d363b786bb -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:b22f9c7f75eb4b48906b879a2fcbb73f`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn

C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn 01a0f1db-5e25-7563-86c7-fc4f2779e0aa is already interrupted and thread status is notLoaded. The temporary c3_recover_731707.py waits/terminalizes incorrectly across interrupted/notLoaded recovery turns, consuming a worker slot and preventing clean continuation. Recovery must be bounded, detect interrupted/notLoaded promptly, tear down its app-server, and resume the same canonical run/thread without spawning duplicate lifecycle state.


status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:b22f9c7f75eb4b48906b879a2fcbb73f",
      "parent_id": null,
      "kind": "task",
      "title": "C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn",
      "objective": "C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn 01a0f1db-5e25-7563-86c7-fc4f2779e0aa is already interrupted and thread status is notLoaded. The temporary c3_recover_731707.py waits/terminalizes incorrectly across interrupted/notLoaded recovery turns, consuming a worker slot and preventing clean continuation. Recovery must be bounded, detect interrupted/notLoaded promptly, tear down its app-server, and resume the same canonical run/thread without spawning duplicate lifecycle state.\n",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T13:05:38Z",
      "updated_at": "2026-09-30T13:05:38Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:b22f9c7f75eb4b48906b879a2fcbb73f",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2365,
        "work_item_id": "wi:b22f9c7f75eb4b48906b879a2fcbb73f",
        "evidence_kind": "issue_inbox",
        "label": "issue:db11d84d291043e1aea5b1d397839d61",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C3 recovery wrapper hang: run f91ce3f175324137aba3c11128b9317b keeps c2-run unit and a private Codex app-server alive for >8 minutes even though canonical thread 01a0f1c8-8dfd-7490-b294-bf45e740598a latest recovery turn 01a0f1db-5e25-7563-86c7-fc4f2779e0aa is already interrupted and thread status is notLoaded. The temporary c3_recover_731707.py waits/terminalizes incorrectly across interrupted/notLoaded recovery turns, consuming a worker slot and preventing clean continuation. Recovery must be bounded, detect interrupted/notLoaded promptly, tear down its app-server, and resume the same canonical run/thread without spawning duplicate lifecycle state.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:db11d84d291043e1aea5b1d397839d61\", \"observed_at_ms\": 1790764711069, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T13:05:38Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:db11d84d291043e1aea5b1d397839d61",
        "work_item_id": "wi:b22f9c7f75eb4b48906b879a2fcbb73f",
        "role": "decision",
        "created_at": "2026-09-30T10:38:31Z"
      }
    ]
  }
]
```
