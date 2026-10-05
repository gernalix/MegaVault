# Reduce C2 single-writer GitHub roundtrip latency

<!-- migration-d35be66ad932656a -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:43a64f7bc5704840a0f82cd2ad9172e9`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Reduce C2 single-writer GitHub roundtrip latency

C2 single-writer mutations routed through GitHub Issues/Actions create material control-plane latency and repeated status checking during the roadmap executor: executor starts, PASS receipts, supervisor claims and order mutations are frequently queued before canonical readback, leaving workers idle or forcing follow-up checks. The current main CLI thread contains many queued mutation markers and multiple waits on Issues/Actions. Consider a lower-latency local fenced writer path with GitHub as audit/replication, or an event-driven acknowledgement channel that removes polling without weakening single-writer guarantees.

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
      "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
      "parent_id": null,
      "kind": "task",
      "title": "Reduce C2 single-writer GitHub roundtrip latency",
      "objective": "C2 single-writer mutations routed through GitHub Issues/Actions create material control-plane latency and repeated status checking during the roadmap executor: executor starts, PASS receipts, supervisor claims and order mutations are frequently queued before canonical readback, leaving workers idle or forcing follow-up checks. The current main CLI thread contains many queued mutation markers and multiple waits on Issues/Actions. Consider a lower-latency local fenced writer path with GitHub as audit/replication, or an event-driven acknowledgement channel that removes polling without weakening single-writer guarantees.",
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
      "created_at": "2026-09-27T21:11:32Z",
      "updated_at": "2026-09-29T22:21:33Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "tag": "source:issue-inbox"
      },
      {
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "tag": "priority:p0"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1050,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:34db6222e06844ffaac20c9c2919ec57",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"mutation-transport\", \"description\": \"C2 single-writer mutations routed through GitHub Issues/Actions create material control-plane latency and repeated status checking during the roadmap executor: executor starts, PASS receipts, supervisor claims and order mutations are frequently queued before canonical readback, leaving workers idle or forcing follow-up checks. The current main CLI thread contains many queued mutation markers and multiple waits on Issues/Actions. Consider a lower-latency local fenced writer path with GitHub as audit/replication, or an event-driven acknowledgement channel that removes polling without weakening single-writer guarantees.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:34db6222e06844ffaac20c9c2919ec57\", \"observed_at_ms\": 1790540693480, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"codex-roadmap\"}",
        "created_at": "2026-09-27T21:11:32Z"
      },
      {
        "evidence_id": 1060,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:38f9a33136b84ec4ba54417eb38ad19d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Single writer via GitHub Issues/Actions è il collo di bottiglia dominante del workflow C2: executor-start, PASS receipt, supervisor claim e mutation restano spesso queued e costringono worker ed executor ad attendere readback o fare controlli successivi. Mantenere fencing/single-writer ma ridurre il round-trip GitHub nel percorso critico.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:38f9a33136b84ec4ba54417eb38ad19d\", \"observed_at_ms\": 1790541647821, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:13:22Z"
      },
      {
        "evidence_id": 1064,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:1d909cf6c7b0426eacb878b9b3e5ccb5",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Dopo i fix recenti Workflowy non sembra più il principale collo di bottiglia: reorder Inbox/Roadmap, refresh persistence, churn e Reset to AI order hanno evidenza E2E positiva. Prima di sostituire Workflowy, completare #2330 e concentrare lo snellimento su mutation/lifecycle path, scheduler/dispatch, lease recovery e Git guard.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:1d909cf6c7b0426eacb878b9b3e5ccb5\", \"observed_at_ms\": 1790541649723, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:13:23Z"
      },
      {
        "evidence_id": 1894,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "classification",
        "label": "User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/cod",
        "uri": null,
        "value_json": "\"User explicitly requested P0 for the C2 batch on 2026-09-30; this item is currently runnable and belongs to gernalix/codex-roadmap.\"",
        "created_at": "2026-09-29T22:21:33Z"
      },
      {
        "evidence_id": 2144,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:008a6cd87eec4278aead7d1f9496ba87",
        "uri": "codex-thread:01a0ee88-bb5a-75b0-a1b1-956ec41ed053",
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Il single-writer può ritardare patch runtime C2 urgenti già testate: PR #6090 (cap globale scheduler, recovery fail-closed su agentMessage.questions, test backfill reale) resta queued mentre il Master Goal attende il deploy. Valutare una fast-lane sicura/priorità per fix del control plane senza bypassare le garanzie del writer.\", \"executor\": null, \"executor_ref\": \"codex-thread:01a0ee88-bb5a-75b0-a1b1-956ec41ed053\", \"issue_id\": \"issue:008a6cd87eec4278aead7d1f9496ba87\", \"observed_at_ms\": 1790709219154, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"gernalix/codex-roadmap\"}",
        "created_at": "2026-09-30T10:16:35Z"
      },
      {
        "evidence_id": 2312,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:4c7a3279311041abaf24e7cfbe0b1281",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Major roadmap writer latency bottleneck: .github/workflows/apply-roadmap-mutations.yml uses actions/checkout@v4 with fetch-depth: 0. Live runs spend ~1-2+ minutes in checkout and logs show hundreds of remote branches/history being fetched, while actual mutation application takes fractions of a second. The workflow only resets/fetches/pushes main and does not use git log/merge-base/rev-list in its apply path. Evaluate switching to a shallow single-ref checkout (e.g. fetch-depth 2) and bounded main fetch, with targeted writer tests, to preserve single-writer semantics while removing hosted checkout cold-start overhead.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4c7a3279311041abaf24e7cfbe0b1281\", \"observed_at_ms\": 1790762815278, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:24:32Z"
      },
      {
        "evidence_id": 2496,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:771c391e41454f28bd82ae33a0206e23",
        "uri": "https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1",
        "value_json": "{\"chat_url\": \"https://chatgpt.com/g/g-p-6ab69fbdbaf88191a39a75ff5c9e3d70-c2/c/6abcd235-20f0-83eb-861e-d8a0e79d25c1\", \"code_location\": null, \"description\": \"C2 runtime idempotency collision observed in the acceleration chat: request_key_conflict blocked progress until manually resolved, and the conflict was later identified as a duplicate mutation. The writer/runtime should distinguish exact idempotent replay from semantic collision, auto-accept byte-equivalent replays, and return the conflicting canonical request for true mismatches so dispatch does not require manual receipt hunting.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:771c391e41454f28bd82ae33a0206e23\", \"observed_at_ms\": 1790784889163, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "evidence_id": 2507,
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "evidence_kind": "issue_inbox",
        "label": "issue:c83505e0659f449caa754e60f063b79b",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"C3 fenced mutations can expire in the GitHub single-writer queue before application: Issues #7648-#7650 were generated with current supervisor token 241 but later rejected by the writer as stale_or_expired_supervisor after queue/checkout latency. This can make runtime recovery and Inbox triage repeatedly fail despite valid submission-time authority. Preserve fencing while making queued authorized mutations robust to writer latency (for example via atomic renewal/revalidation at apply time or sufficient lease semantics), without weakening stale-writer rejection.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c83505e0659f449caa754e60f063b79b\", \"observed_at_ms\": 1790792371969, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:38f9a33136b84ec4ba54417eb38ad19d",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-09-27T20:40:47Z"
      },
      {
        "issue_id": "issue:1d909cf6c7b0426eacb878b9b3e5ccb5",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-09-27T20:40:49Z"
      },
      {
        "issue_id": "issue:008a6cd87eec4278aead7d1f9496ba87",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-09-29T19:13:39Z"
      },
      {
        "issue_id": "issue:4c7a3279311041abaf24e7cfbe0b1281",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-09-30T10:06:55Z"
      },
      {
        "issue_id": "issue:34db6222e06844ffaac20c9c2919ec57",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-09-27T20:24:53Z"
      },
      {
        "issue_id": "issue:38f9a33136b84ec4ba54417eb38ad19d",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-09-27T20:40:47Z"
      },
      {
        "issue_id": "issue:1d909cf6c7b0426eacb878b9b3e5ccb5",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-09-27T20:40:49Z"
      },
      {
        "issue_id": "issue:008a6cd87eec4278aead7d1f9496ba87",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-09-29T19:13:39Z"
      },
      {
        "issue_id": "issue:4c7a3279311041abaf24e7cfbe0b1281",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-09-30T10:06:55Z"
      },
      {
        "issue_id": "issue:771c391e41454f28bd82ae33a0206e23",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:771c391e41454f28bd82ae33a0206e23",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:c83505e0659f449caa754e60f063b79b",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "decision",
        "created_at": "2026-10-01T12:32:14Z"
      },
      {
        "issue_id": "issue:c83505e0659f449caa754e60f063b79b",
        "work_item_id": "wi:43a64f7bc5704840a0f82cd2ad9172e9",
        "role": "matched",
        "created_at": "2026-10-01T12:32:14Z"
      }
    ]
  }
]
```
