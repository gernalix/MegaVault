# Diagnose RDC navigation and ChatGPT 429 recurrence

<!-- migration-93a9db48e2c2a9ed -->

Migrated project backlog. Project: **chatgpt-rdc-supervisor**; project_id: 105.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 105, 96.

Provenance: `wi:c1111977abd94541a6ad7f406ea21840`, `issue:4ba4583bccbf4a5ab8d694da5eaf6bcf`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Diagnose RDC navigation and ChatGPT 429 recurrence

Determine whether the RDC supervisor forced home navigation and project sweeps are sustaining ChatGPT conversation-list HTTP 429s, and resolve the repeated workflowy-chatgpt-live.timer ECONNREFUSED on 127.0.0.1:9333. Preserve the user Chrome profile and chats; verify recovery and prevention.

status: pending

### issue:4ba4583bccbf4a5ab8d694da5eaf6bcf

Aggiornare chatgpt-rdc-supervisor per evitare la discovery globale invasiva delle nuove chat: il daemon oggi apre/refresha ogni minuto una pagina ChatGPT history e periodicamente scansiona i progetti, agganciando automaticamente conversazioni appena create. Rendere questa discovery opt-in/esplicita; in modalità normale osservare solo chat/worker esplicitamente registrati. Conservare la discovery esplicita per comandi manuali e per rollover/recovery realmente necessari. Acceptance: aprire nuove chat ChatGPT non registrate non deve causare refresh, navigazione, attach o altre interferenze da parte del supervisor.

state: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "105",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "105",
        "96"
      ]
    },
    "source": {
      "work_item_id": "wi:c1111977abd94541a6ad7f406ea21840",
      "parent_id": null,
      "kind": "task",
      "title": "Diagnose RDC navigation and ChatGPT 429 recurrence",
      "objective": "Determine whether the RDC supervisor forced home navigation and project sweeps are sustaining ChatGPT conversation-list HTTP 429s, and resolve the repeated workflowy-chatgpt-live.timer ECONNREFUSED on 127.0.0.1:9333. Preserve the user Chrome profile and chats; verify recovery and prevention.",
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
        "work_item_id": "wi:c1111977abd94541a6ad7f406ea21840",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2269,
        "work_item_id": "wi:c1111977abd94541a6ad7f406ea21840",
        "evidence_kind": "issue_inbox",
        "label": "issue:dc4e9184bde441ef8ba7bb39a69bc56d",
        "uri": "codex://threads/01a0f120-1cb3-7411-a60e-076e5daf98d9",
        "value_json": "{\"chat_url\": \"codex://threads/01a0f120-1cb3-7411-a60e-076e5daf98d9\", \"code_location\": null, \"description\": \"Diagnosi Chrome ChatGPT: verificati HTTP 429 sulle liste conversazioni e recupero di chat irraggiungibile tramite singolo reload. Il supervisor RDC attivo forza navigazione home ogni 60 secondi e sweep progetti ogni 300 secondi; rischio di sostenere rate limiting. Inoltre workflowy-chatgpt-live.timer ogni 90s fallisce ripetutamente con ECONNREFUSED 127.0.0.1:9333. Richiesta utente: correggere e prevenire alla radice senza perdere chat o profilo.\", \"executor\": null, \"executor_ref\": \"01a0f120-1cb3-7411-a60e-076e5daf98d9\", \"issue_id\": \"issue:dc4e9184bde441ef8ba7bb39a69bc56d\", \"observed_at_ms\": 1790751998788, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T12:10:08Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:dc4e9184bde441ef8ba7bb39a69bc56d",
        "work_item_id": "wi:c1111977abd94541a6ad7f406ea21840",
        "role": "decision",
        "created_at": "2026-09-30T07:06:38Z"
      }
    ]
  },
  {
    "routing": {
      "project": "105",
      "reason": "complementary evidence for same explicitly identified objective",
      "related_projects": [
        "105",
        "96"
      ]
    },
    "source": {
      "issue_id": "issue:4ba4583bccbf4a5ab8d694da5eaf6bcf",
      "description": "Aggiornare chatgpt-rdc-supervisor per evitare la discovery globale invasiva delle nuove chat: il daemon oggi apre/refresha ogni minuto una pagina ChatGPT history e periodicamente scansiona i progetti, agganciando automaticamente conversazioni appena create. Rendere questa discovery opt-in/esplicita; in modalità normale osservare solo chat/worker esplicitamente registrati. Conservare la discovery esplicita per comandi manuali e per rollover/recovery realmente necessari. Acceptance: aprire nuove chat ChatGPT non registrate non deve causare refresh, navigazione, attach o altre interferenze da parte del supervisor.",
      "repo": "gernalix/chatgpt-rdc-supervisor",
      "code_location": null,
      "executor": null,
      "executor_ref": null,
      "chat_url": null,
      "origin_work_item_id": null,
      "origin_run_id": null,
      "observed_at_ms": 1790863632117,
      "state": "pending",
      "matched_work_item_id": null,
      "promoted_work_item_id": null,
      "disposition_reason": null,
      "triaged_by": null,
      "triaged_at_ms": null,
      "created_at": "2026-10-01T14:07:12Z"
    },
    "issue_work_item_links": []
  }
]
```
