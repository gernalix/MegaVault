# Route C2 browser workers through the RDC channel bridge

<!-- migration-e5008aa9802b4885 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:0f43364c82a14bfd9aac43c0de9221a9`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Route C2 browser workers through the RDC channel bridge

Route C2 ChatGPT/RDC browser workers through the deployed channel bridge instead of the normal Chrome endpoint, and prevent regression to endpoint=chrome.

Acceptance:

- The C2 ChatGPT/RDC worker path explicitly uses the deployed channel bridge or an equivalent non-normal-profile endpoint.
- Focused regression coverage proves this worker path cannot silently fall back to endpoint=chrome.

status: blocked

current_action: Fail-closed terminal reconciliation after missing workspace readback.

next_action: Recover the tracker workspace or re-run the task through the canonical Symphony workspace path, then verify Git integration before PASS.

blocker: Symphony tracker terminal result cannot be imported because its required workspace is missing.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "canonical MegaVault project_id",
      "related_projects": [
        "51"
      ]
    },
    "source": {
      "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
      "parent_id": null,
      "kind": "task",
      "title": "Route C2 browser workers through the RDC channel bridge",
      "objective": "Route C2 ChatGPT/RDC browser workers through the deployed channel bridge instead of the normal Chrome endpoint, and prevent regression to endpoint=chrome.",
      "acceptance_json": "[\"The C2 ChatGPT/RDC worker path explicitly uses the deployed channel bridge or an equivalent non-normal-profile endpoint.\", \"Focused regression coverage proves this worker path cannot silently fall back to endpoint=chrome.\"]",
      "status": "blocked",
      "executor_policy": "codex",
      "sort_order": null,
      "current_action": "Fail-closed terminal reconciliation after missing workspace readback.",
      "next_action": "Recover the tracker workspace or re-run the task through the canonical Symphony workspace path, then verify Git integration before PASS.",
      "blocker": "Symphony tracker terminal result cannot be imported because its required workspace is missing.",
      "project_id": "51",
      "project_name": "codex-roadmap",
      "repo": "gernalix/codex-roadmap",
      "prompt_id": "471635",
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T00:02:52Z",
      "updated_at": "2026-10-02T11:03:35Z"
    },
    "prompt_metadata": [
      {
        "prompt_id": "471635",
        "slug": "route-c2-browser-workers-through-the-rdc-channel-471635",
        "chat_guidance": null,
        "prompt_type": "Prompt",
        "model": "gpt-5.6-sol",
        "reasoning": "medium",
        "megavault_mode": null,
        "campaign_id": null,
        "explanation": "",
        "current_path": "prompts/route-c2-browser-workers-through-the-rdc-channel-471635.md",
        "materialization_sha256": "f6a4181c6dd20a7d9ded093b9a204481803ca892fbe7de3f34cf6cde69e3d04b",
        "created_at": "2026-10-02T10:56:23Z",
        "updated_at": "2026-10-02T10:56:23Z"
      }
    ],
    "prompt_materializations": [
      {
        "prompt_id": "471635",
        "body": "PROMPT_ID=471635\n\n# Route C2 browser workers through the RDC channel bridge\n\n## Objective\nRoute C2 ChatGPT/RDC browser workers through the deployed channel bridge instead of the normal Chrome endpoint, and prevent regression to endpoint=chrome.\n\n## Acceptance criteria\n- The C2 ChatGPT/RDC worker path explicitly uses the deployed channel bridge or an equivalent non-normal-profile endpoint.\n- Focused regression coverage proves this worker path cannot silently fall back to endpoint=chrome.\n\n## Current action\nRequeued after correcting a false running projection; no executor is currently active.\n\n## Next action\nPrepare the smallest isolated code change and focused regression test for channel-bridge routing.\n",
        "sha256": "f6a4181c6dd20a7d9ded093b9a204481803ca892fbe7de3f34cf6cde69e3d04b",
        "created_at": "2026-10-02T10:56:23Z",
        "actor": "c2-intake"
      }
    ],
    "analyses": [],
    "executions": [],
    "status_history": [
      {
        "history_id": 1135,
        "prompt_id": "471635",
        "old_status": null,
        "new_status": "pending",
        "changed_at": "2026-10-02T10:56:23Z",
        "actor": "c2-intake",
        "note": "work item materialized for Codex"
      },
      {
        "history_id": 1136,
        "prompt_id": "471635",
        "old_status": "pending",
        "new_status": "running",
        "changed_at": "2026-10-02T10:56:52Z",
        "actor": "c2-scheduler",
        "note": null
      },
      {
        "history_id": 1137,
        "prompt_id": "471635",
        "old_status": "running",
        "new_status": "blocked",
        "changed_at": "2026-10-02T11:03:35Z",
        "actor": "c2-executor-result",
        "note": "executor_result:run:f47984400157448fadcb5142184414aa"
      }
    ],
    "work_item_tags": [
      {
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "tag": "browser"
      },
      {
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "tag": "bug"
      },
      {
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "tag": "c2"
      },
      {
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "tag": "rdc"
      },
      {
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "tag": "source:state-correction"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "run:f47984400157448fadcb5142184414aa",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "run_id": "f47984400157448fadcb5142184414aa",
        "prompt_id": "471635",
        "outcome": "BLOCKED",
        "summary": "Fail-closed terminal reconciliation after missing workspace readback.",
        "completed_json": "[\"Tracker Symphony #3 returned a terminal PASS report with commit 37bb1e7d.\"]",
        "remaining_json": "[\"Recover the missing Symphony workspace or reproduce the verified commit through the canonical Git integration path before accepting PASS.\"]",
        "evidence_json": "[\"Tracker issue https://github.com/gernalix/c3-symphony/issues/3 is CLOSED with C3_RESULT PASS and commit 37bb1e7d.\", \"Canonical worker readback failed symphony_workspace_import_missing; no workspace or importable commit was present at the required C3 workspace path.\"]",
        "blocker": "Symphony tracker terminal result cannot be imported because its required workspace is missing.",
        "next_action": "Recover the tracker workspace or re-run the task through the canonical Symphony workspace path, then verify Git integration before PASS.",
        "strict_contract": 1,
        "payload_sha256": "b4a704a4354430da20f6367f1e782ba6975a71343b2fa5c78c053baa098141bb",
        "captured_at": 1790939015.1021478
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 2054,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "issue_inbox",
        "label": "issue:33fe62b104584d5288c13a2e6ee3e42b",
        "uri": "codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"code_location\": null, \"description\": \"La branch task/wi-5681590a-normal-chrome usa un symlink al profilo Chrome predefinito con --remote-debugging-port=9333, ma il Chrome normale attuale (PID 159272) non espone alcun listener CDP né DevToolsActivePort; browser-health resta unhealthy. Chrome 136+ ignora il debug remoto della directory dati predefinita anche se il path è alias.\", \"executor\": null, \"executor_ref\": \"01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"issue_id\": \"issue:33fe62b104584d5288c13a2e6ee3e42b\", \"observed_at_ms\": 1790688408487, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T08:05:26Z"
      },
      {
        "evidence_id": 2056,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "issue_inbox",
        "label": "issue:375467c68d304275be577eeabff06563",
        "uri": "codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"code_location\": null, \"description\": \"Chrome normale con profilo predefinito non offre CDP tramite --remote-debugging-port (riprodotto su Chrome 153); l'accesso UI a chrome://extensions/ richiesto per installare un bridge persistente è stato rifiutato dalla browser security policy del tool, che vieta workaround. Senza installazione/autorizzazione esterna di un bridge supportato non è possibile verificare il controllo reale delle tab da chatgpt-rdc-supervisor.\", \"executor\": null, \"executor_ref\": \"01a0ed4c-bb88-7e23-acff-b332f3b366d3\", \"issue_id\": \"issue:375467c68d304275be577eeabff06563\", \"observed_at_ms\": 1790688967452, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T08:12:52Z"
      },
      {
        "evidence_id": 2094,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "issue_inbox",
        "label": "issue:54e54f1337744ae484bf00cee8221276",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C2 browser recovery stale endpoint: tools/c2_browser_recovery.py still hardcodes http://127.0.0.1:9333 for /json/version and /json/list, but the normal-Chrome channel architecture uses Chrome DevToolsActivePort on a dynamic port plus chatgpt-rdc-channel-bridge on another local endpoint. This makes recovery/browser-health assumptions stale and risks either permanent false-unhealthy state or pressure to reintroduce managed-Chrome/CDP-port workarounds. Recovery must consume the approved bridge/current-session abstraction, never launch or signal Chrome.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:54e54f1337744ae484bf00cee8221276\", \"observed_at_ms\": 1790698648445, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T09:59:56Z"
      },
      {
        "evidence_id": 2127,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "issue_inbox",
        "label": "issue:e91efb6d00894509914ada177e7d269e",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Correggere subito il bug C2 per cui c2_chatgpt_executor.py crea ChatGPTBrowser() col default endpoint=chrome invece di usare channel-bridge, causando il popup Chrome “Allow remote debugging?” ogni pochi minuti e timeout Playwright. La correzione deve usare il channel bridge anche per i worker C2 e includere una regression test che impedisca di colpire il profilo Chrome normale.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:e91efb6d00894509914ada177e7d269e\", \"observed_at_ms\": 1790706457076, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:08:36Z"
      },
      {
        "evidence_id": 2587,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "executor_result",
        "label": "Tracker issue https://github.com/gernalix/c3-symphony/issues/3 is CLOSED with C3_RESULT PASS and commit 37bb1e7d.",
        "uri": null,
        "value_json": "\"Tracker issue https://github.com/gernalix/c3-symphony/issues/3 is CLOSED with C3_RESULT PASS and commit 37bb1e7d.\"",
        "created_at": "2026-10-02T11:03:35Z"
      },
      {
        "evidence_id": 2588,
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "evidence_kind": "executor_result",
        "label": "Canonical worker readback failed symphony_workspace_import_missing; no workspace or importable commit was present at the",
        "uri": null,
        "value_json": "\"Canonical worker readback failed symphony_workspace_import_missing; no workspace or importable commit was present at the required C3 workspace path.\"",
        "created_at": "2026-10-02T11:03:35Z"
      }
    ],
    "work_item_runs": [
      {
        "run_id": "f47984400157448fadcb5142184414aa",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "event_key": "c2-schedule-1925405e4ff8034e31f092e528e00d2d",
        "attempt": 1,
        "executor": "symphony",
        "state": "failed",
        "lease_until": 1790938732.9855173,
        "worker_ref": "c3-run:f47984400157448fadcb5142184414aa",
        "checkpoint_commit": null,
        "metadata_json": "{\"activity\": \"coding\", \"command_json\": null, \"executor\": \"symphony\", \"goal_mode\": 0, \"max_attempts\": 3, \"model\": \"gpt-5.6-sol\", \"model_id\": \"gpt-5.6-sol\", \"project_url\": null, \"prompt_id\": \"471635\", \"reasoning\": \"medium\", \"reasoning_effort\": \"medium\", \"repo\": \"gernalix/codex-roadmap\", \"resources_json\": \"[]\", \"symphony_route\": {\"mode\": \"production\", \"source_repos\": [\"gernalix/codex-roadmap\"], \"tracker_repo\": \"gernalix/c3-symphony\"}, \"work_item_id\": \"wi:0f43364c82a14bfd9aac43c0de9221a9\", \"worktree\": \"/home/daniele/.local/share/codex-github-autosync/worktrees/gernalix_codex-roadmap/471635\"}",
        "created_at": 1790938612.9682434
      }
    ],
    "issue_work_item_links": [
      {
        "issue_id": "issue:33fe62b104584d5288c13a2e6ee3e42b",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "matched",
        "created_at": "2026-09-29T13:26:48Z"
      },
      {
        "issue_id": "issue:375467c68d304275be577eeabff06563",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "matched",
        "created_at": "2026-09-29T13:36:07Z"
      },
      {
        "issue_id": "issue:54e54f1337744ae484bf00cee8221276",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "matched",
        "created_at": "2026-09-29T16:17:28Z"
      },
      {
        "issue_id": "issue:e91efb6d00894509914ada177e7d269e",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "matched",
        "created_at": "2026-09-29T18:27:37Z"
      },
      {
        "issue_id": "issue:33fe62b104584d5288c13a2e6ee3e42b",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "decision",
        "created_at": "2026-09-29T13:26:48Z"
      },
      {
        "issue_id": "issue:375467c68d304275be577eeabff06563",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "decision",
        "created_at": "2026-09-29T13:36:07Z"
      },
      {
        "issue_id": "issue:54e54f1337744ae484bf00cee8221276",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "decision",
        "created_at": "2026-09-29T16:17:28Z"
      },
      {
        "issue_id": "issue:e91efb6d00894509914ada177e7d269e",
        "work_item_id": "wi:0f43364c82a14bfd9aac43c0de9221a9",
        "role": "decision",
        "created_at": "2026-09-29T18:27:37Z"
      }
    ]
  }
]
```
