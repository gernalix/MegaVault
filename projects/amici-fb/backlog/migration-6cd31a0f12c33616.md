# Investigate Fedora Service · amici-fb.service recurring DOWN incident

<!-- migration-6cd31a0f12c33616 -->

Migrated project backlog. Project: **amici-fb**; project_id: 1.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 1.

Provenance: `wi:edc894e1d7e94037a48581ce7d310d64`, `issue:4ddcf0a67d1a4242a16ef7dca92ae958`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate amici-fb.service (id 64) DOWN alert

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · amici-fb.service (id 64)
Heartbeat: 2026-09-30 06:26:22.179 (row 685509)
Failure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.

status: pending

### issue:4ddcf0a67d1a4242a16ef7dca92ae958

Servizio "amici fb": farlo ripartire subito e renderlo resiliente. Verificare perché ha smesso di avviarsi/eseguire, ripristinare il servizio senza perdere o duplicare lavoro, e rendere il meccanismo robusto a reboot, crash, kill/OOM, errori temporanei di rete e fallimenti del processo. Preferire un'unità systemd/user o altro supervisore canonico con avvio automatico, Restart/backoff appropriati, lock/idempotenza per evitare esecuzioni concorrenti o duplicate, logging utile e verifica finale end-to-end che il servizio sia attivo e continui a ripartire automaticamente dopo un arresto controllato. Correggere la causa strutturale, non solo avviare manualmente il processo una volta.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "1",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "1"
      ]
    },
    "source": {
      "work_item_id": "wi:edc894e1d7e94037a48581ce7d310d64",
      "parent_id": null,
      "kind": "task",
      "title": "Investigate amici-fb.service (id 64) DOWN alert",
      "objective": "Uptime Kuma monitor transitioned to DOWN.\nMonitor: Fedora Service · amici-fb.service (id 64)\nHeartbeat: 2026-09-30 06:26:22.179 (row 685509)\nFailure context: No heartbeat in the time window Identify whether this alert is transient or persistent, inspect the named monitor/service, and record an evidence-based cause and scoped resolution or blocker.",
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
      "created_at": "2026-09-30T12:10:08Z",
      "updated_at": "2026-09-30T12:10:08Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:edc894e1d7e94037a48581ce7d310d64",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2252,
        "work_item_id": "wi:edc894e1d7e94037a48581ce7d310d64",
        "evidence_kind": "issue_inbox",
        "label": "issue:bca178723570f2e35462d4f32622edfe",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"Uptime Kuma monitor transitioned to DOWN.\\nMonitor: Fedora Service · amici-fb.service (id 64)\\nHeartbeat: 2026-09-30 06:26:22.179 (row 685509)\\nFailure context: No heartbeat in the time window\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:bca178723570f2e35462d4f32622edfe\", \"observed_at_ms\": 1790749943612, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:bca178723570f2e35462d4f32622edfe",
        "work_item_id": "wi:edc894e1d7e94037a48581ce7d310d64",
        "role": "decision",
        "created_at": "2026-09-30T06:32:23Z"
      }
    ]
  },
  {
    "routing": {
      "project": "1",
      "reason": "complementary evidence for same explicitly identified objective",
      "related_projects": [
        "1"
      ]
    },
    "source": {
      "issue_id": "issue:4ddcf0a67d1a4242a16ef7dca92ae958",
      "description": "Servizio \"amici fb\": farlo ripartire subito e renderlo resiliente. Verificare perché ha smesso di avviarsi/eseguire, ripristinare il servizio senza perdere o duplicare lavoro, e rendere il meccanismo robusto a reboot, crash, kill/OOM, errori temporanei di rete e fallimenti del processo. Preferire un'unità systemd/user o altro supervisore canonico con avvio automatico, Restart/backoff appropriati, lock/idempotenza per evitare esecuzioni concorrenti o duplicate, logging utile e verifica finale end-to-end che il servizio sia attivo e continui a ripartire automaticamente dopo un arresto controllato. Correggere la causa strutturale, non solo avviare manualmente il processo una volta.",
      "repo": null,
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790870167231,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T15:56:07Z"
    },
    "issue_work_item_links": []
  }
]
```
