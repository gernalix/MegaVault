# Distinguish intentional Workflowy ExecCondition skip from Kuma outage

<!-- migration-402424b72059a1fa -->

Migrated project backlog. Project: **fedora-system-monitor**; project_id: 15.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 15.

Provenance: `wi:a392bc6406104fd98a665f42716d88ff`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Distinguish intentional Workflowy ExecCondition skip from Kuma outage

Workflowy roadmap-sync monitoring can report a false DOWN/no-heartbeat while the systemd oneshot is intentionally skipped by ExecCondition during safe C2 supervisor recovery. In the current CLI run, workflowy-roadmap-sync.service returned Result=exec-condition while preflight deferred a pending claim, and the Uptime Kuma bridge later captured monitor 63 DOWN for missing heartbeat even though this was expected fail-safe behavior. Monitor semantics should distinguish intentional ExecCondition skip/retry from service failure so expected recovery does not create outage noise.

status: waiting

current_action: WAITING_ON_EVIDENCE

next_action: Wait for one fresh reproducible ExecCondition skip that Kuma incorrectly counts as DOWN, then diagnose that exact event.

blocker: No current reproducible Workflowy ExecCondition false-DOWN event exists after producer stabilization.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "15",
      "reason": "canonical repository identity",
      "related_projects": [
        "15"
      ]
    },
    "source": {
      "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
      "parent_id": null,
      "kind": "task",
      "title": "Distinguish intentional Workflowy ExecCondition skip from Kuma outage",
      "objective": "Workflowy roadmap-sync monitoring can report a false DOWN/no-heartbeat while the systemd oneshot is intentionally skipped by ExecCondition during safe C2 supervisor recovery. In the current CLI run, workflowy-roadmap-sync.service returned Result=exec-condition while preflight deferred a pending claim, and the Uptime Kuma bridge later captured monitor 63 DOWN for missing heartbeat even though this was expected fail-safe behavior. Monitor semantics should distinguish intentional ExecCondition skip/retry from service failure so expected recovery does not create outage noise.",
      "acceptance_json": "[]",
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": 5000,
      "current_action": "WAITING_ON_EVIDENCE",
      "next_action": "Wait for one fresh reproducible ExecCondition skip that Kuma incorrectly counts as DOWN, then diagnose that exact event.",
      "blocker": "No current reproducible Workflowy ExecCondition false-DOWN event exists after producer stabilization.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/fedora-system-monitor",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T21:11:32Z",
      "updated_at": "2026-09-28T22:47:20Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1051,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:52529b673f27448c825576fc1b4b8306",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": \"uptime-kuma-systemd-heartbeat\", \"description\": \"Workflowy roadmap-sync monitoring can report a false DOWN/no-heartbeat while the systemd oneshot is intentionally skipped by ExecCondition during safe C2 supervisor recovery. In the current CLI run, workflowy-roadmap-sync.service returned Result=exec-condition while preflight deferred a pending claim, and the Uptime Kuma bridge later captured monitor 63 DOWN for missing heartbeat even though this was expected fail-safe behavior. Monitor semantics should distinguish intentional ExecCondition skip/retry from service failure so expected recovery does not create outage noise.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:52529b673f27448c825576fc1b4b8306\", \"observed_at_ms\": 1790540826891, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"fedora-system-monitor\"}",
        "created_at": "2026-09-27T21:11:32Z"
      },
      {
        "evidence_id": 1063,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:4a754e714d784eee88dee5d52f2dce5d",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Il monitoraggio Uptime Kuma dei servizi oneshot può generare falsi DOWN quando workflowy-roadmap-sync.service viene intenzionalmente saltato da ExecCondition durante recovery sicura. Distinguere skip/retry previsto da vero service failure/no-heartbeat.\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4a754e714d784eee88dee5d52f2dce5d\", \"observed_at_ms\": 1790541648879, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-27T21:13:23Z"
      },
      {
        "evidence_id": 1653,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "classification",
        "label": "Latest whole-batch reconciliation requires fresh event evidence before any code lane.",
        "uri": null,
        "value_json": "\"Latest whole-batch reconciliation requires fresh event evidence before any code lane.\"",
        "created_at": "2026-09-28T22:47:20Z"
      },
      {
        "evidence_id": 2168,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:684bb2fa8510d420b69c764a5597e026",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-29 23:22:34.473 (row 671756)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:684bb2fa8510d420b69c764a5597e026\", \"observed_at_ms\": 1790724189714, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      },
      {
        "evidence_id": 2172,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:d9ddc383ab81c8905292f7564f0214b5",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-29 23:45:30.596 (row 672502)\\nFailure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:d9ddc383ab81c8905292f7564f0214b5\", \"observed_at_ms\": 1790725616272, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      },
      {
        "evidence_id": 2177,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:4424296d9dc402fb2308172217e194af",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-30 00:17:25.888 (row 673516)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:4424296d9dc402fb2308172217e194af\", \"observed_at_ms\": 1790727458535, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      },
      {
        "evidence_id": 2179,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:1304a6867069d971d6483d5f0038beb6",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-30 00:34:26.376 (row 674061)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:1304a6867069d971d6483d5f0038beb6\", \"observed_at_ms\": 1790728501365, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      },
      {
        "evidence_id": 2180,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:09a42b45bc8545a8e04df1c97a27e2a5",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-30 00:37:23.024 (row 674178)\\nFailure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:09a42b45bc8545a8e04df1c97a27e2a5\", \"observed_at_ms\": 1790728752977, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:25:45Z"
      },
      {
        "evidence_id": 2292,
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "evidence_kind": "issue_inbox",
        "label": "issue:c6773304123bb8b94764f44d6e0ca260",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)\\nHeartbeat: 2026-09-30 09:18:22.754 (row 691062)\\nFailure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:c6773304123bb8b94764f44d6e0ca260\", \"observed_at_ms\": 1790759968232, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:21:51Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:4a754e714d784eee88dee5d52f2dce5d",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-27T20:40:48Z"
      },
      {
        "issue_id": "issue:684bb2fa8510d420b69c764a5597e026",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-29T23:23:09Z"
      },
      {
        "issue_id": "issue:d9ddc383ab81c8905292f7564f0214b5",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-29T23:46:56Z"
      },
      {
        "issue_id": "issue:4424296d9dc402fb2308172217e194af",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-30T00:17:38Z"
      },
      {
        "issue_id": "issue:1304a6867069d971d6483d5f0038beb6",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-30T00:35:01Z"
      },
      {
        "issue_id": "issue:09a42b45bc8545a8e04df1c97a27e2a5",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-30T00:39:12Z"
      },
      {
        "issue_id": "issue:c6773304123bb8b94764f44d6e0ca260",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "matched",
        "created_at": "2026-09-30T09:19:28Z"
      },
      {
        "issue_id": "issue:52529b673f27448c825576fc1b4b8306",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-27T20:27:06Z"
      },
      {
        "issue_id": "issue:4a754e714d784eee88dee5d52f2dce5d",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-27T20:40:48Z"
      },
      {
        "issue_id": "issue:684bb2fa8510d420b69c764a5597e026",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-29T23:23:09Z"
      },
      {
        "issue_id": "issue:d9ddc383ab81c8905292f7564f0214b5",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-29T23:46:56Z"
      },
      {
        "issue_id": "issue:4424296d9dc402fb2308172217e194af",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-30T00:17:38Z"
      },
      {
        "issue_id": "issue:1304a6867069d971d6483d5f0038beb6",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-30T00:35:01Z"
      },
      {
        "issue_id": "issue:09a42b45bc8545a8e04df1c97a27e2a5",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-30T00:39:12Z"
      },
      {
        "issue_id": "issue:c6773304123bb8b94764f44d6e0ca260",
        "work_item_id": "wi:a392bc6406104fd98a665f42716d88ff",
        "role": "decision",
        "created_at": "2026-09-30T09:19:28Z"
      }
    ]
  }
]
```
