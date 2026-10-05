# Phase D — motore unico Fedora → Oracle → Datasette

<!-- migration-66b1d38c10bd6aef -->

Migrated project backlog. Project: **datasette5**; project_id: 10.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 10.

Provenance: `wi:6a187c7e94be40daba8dce5678ba64f6`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Phase D — motore unico Fedora → Oracle → Datasette

Implementare un unico motore idempotente che ogni minuto sincronizzi soltanto i DB con sync_to_oracle=yes dalle sorgenti canoniche Fedora alle copie Oracle usando snapshot SQLite consistenti, change detection, trasferimento sicuro e replace atomico; integrare l'istanza Datasette esistente senza istanze parallele e preservare sicurezza/autenticazione.

Acceptance:

- Il motore legge il database_inventory canonico e sincronizza solo sync_to_oracle=yes.
- Snapshot SQLite sono consistenti (backup API/VACUUM INTO o equivalente) e non copiano ciecamente DB live/WAL.
- Change detection evita trasferimenti inutili; trasferimento e replace Oracle sono sicuri, atomici e idempotenti.
- Cadenza effettiva è ogni minuto e lo stato è monitorabile senza duplicare job o timer.
- L'istanza datasette.danielegalati.com esistente usa le copie sincronizzate; nessuna nuova VPN/istanza parallela è introdotta senza necessità.
- Autenticazione/privacy esistenti restano funzionanti.

status: blocked

current_action: Inventory-selected sync engine implemented and staged; guarded integration and real runtime acceptance await external Actions billing and an authenticated Datasette mount.

next_action: When Actions billing is restored, rerun exact PR #4 test and integrate through repo single writer; then install the timer from merged canonical code, stage the eight selected DBs, configure only reviewed authorized Datasette mounts, and verify one-minute runtime plus privacy before PASS.

blocker: GitHub Actions billing/spending-limit rejection prevents PR #4 required CI/integration; mounting new sensitive copies before a reviewed permission/profile gate would violate privacy.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "10",
      "reason": "canonical repository identity",
      "related_projects": [
        "10"
      ]
    },
    "source": {
      "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
      "parent_id": "wi:68cd5b09eae24fe59352bd0750a559c1",
      "kind": "phase",
      "title": "Phase D — motore unico Fedora → Oracle → Datasette",
      "objective": "Implementare un unico motore idempotente che ogni minuto sincronizzi soltanto i DB con sync_to_oracle=yes dalle sorgenti canoniche Fedora alle copie Oracle usando snapshot SQLite consistenti, change detection, trasferimento sicuro e replace atomico; integrare l'istanza Datasette esistente senza istanze parallele e preservare sicurezza/autenticazione.",
      "acceptance_json": "[\"Il motore legge il database_inventory canonico e sincronizza solo sync_to_oracle=yes.\", \"Snapshot SQLite sono consistenti (backup API/VACUUM INTO o equivalente) e non copiano ciecamente DB live/WAL.\", \"Change detection evita trasferimenti inutili; trasferimento e replace Oracle sono sicuri, atomici e idempotenti.\", \"Cadenza effettiva è ogni minuto e lo stato è monitorabile senza duplicare job o timer.\", \"L'istanza datasette.danielegalati.com esistente usa le copie sincronizzate; nessuna nuova VPN/istanza parallela è introdotta senza necessità.\", \"Autenticazione/privacy esistenti restano funzionanti.\"]",
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": -9960,
      "current_action": "Inventory-selected sync engine implemented and staged; guarded integration and real runtime acceptance await external Actions billing and an authenticated Datasette mount.",
      "next_action": "When Actions billing is restored, rerun exact PR #4 test and integrate through repo single writer; then install the timer from merged canonical code, stage the eight selected DBs, configure only reviewed authorized Datasette mounts, and verify one-minute runtime plus privacy before PASS.",
      "blocker": "GitHub Actions billing/spending-limit rejection prevents PR #4 required CI/integration; mounting new sensitive copies before a reviewed permission/profile gate would violate privacy.",
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/datasette5",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-27T10:13:13Z",
      "updated_at": "2026-09-27T10:13:13Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "tag": "priority:p0"
      },
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "tag": "priority:absolute"
      },
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "tag": "datasette"
      },
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "tag": "oracle"
      },
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "tag": "sqlite-sync"
      }
    ],
    "work_item_dependencies": [
      {
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "depends_on_work_item_id": "wi:c0d99c19998740e2b386bb2bf54ae106",
        "required": 1,
        "note": "c2-intake"
      },
      {
        "work_item_id": "wi:9116862e72024e89b0033b4c6eeb146c",
        "depends_on_work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "required": 1,
        "note": "c2-intake"
      }
    ],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [
      {
        "receipt_id": "work-item:wi:6a187c7e94be40daba8dce5678ba64f6:eca636499cfcb2ceeed52cdd96af7faa",
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "run_id": null,
        "prompt_id": null,
        "outcome": "BLOCKED",
        "summary": "Inventory-selected sync engine implemented and staged; guarded integration and real runtime acceptance await external Actions billing and an authenticated Datasette mount.",
        "completed_json": "[\"Inventory selection, WAL-consistent snapshot, change hint, remote checksum and atomic replace implemented on isolated branch 00e9888.\", \"One-minute user unit/timer and health receipt defined; focused synthetic tests 4/4 PASS.\", \"Synthetic SQLite snapshot transferred to Oracle, quick_check=ok, and QA copy removed.\"]",
        "remaining_json": "[\"Integrate Datasette5 PR #4 through the guarded repository writer after CI can start.\", \"Install/read back the one-minute Fedora timer and verify real selected snapshots without duplicate jobs.\", \"Mount only selected Oracle copies on the existing Datasette instance with reviewed view permissions and verify privacy/authentication.\"]",
        "evidence_json": "[\"PR #4 exact test check annotation: job not started because recent account payments failed or spending limit needs increase; runner name empty and steps absent.\", \"Oracle host reachable and existing datasette.service active; private profile currently serves broad db/*.db glob, so new copies remain in unserved private staging.\"]",
        "blocker": "GitHub Actions billing/spending-limit rejection prevents PR #4 required CI/integration; mounting new sensitive copies before a reviewed permission/profile gate would violate privacy.",
        "next_action": "When Actions billing is restored, rerun exact PR #4 test and integrate through repo single writer; then install the timer from merged canonical code, stage the eight selected DBs, configure only reviewed authorized Datasette mounts, and verify one-minute runtime plus privacy before PASS.",
        "strict_contract": 1,
        "payload_sha256": "eca636499cfcb2ceeed52cdd96af7faa5a60f54252ed3504f50782912dfa067d",
        "captured_at": 1790589921.8416603
      }
    ],
    "work_item_evidence": [
      {
        "evidence_id": 1618,
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "evidence_kind": "executor_result",
        "label": "PR #4 exact test check annotation: job not started because recent account payments failed or spending limit needs increa",
        "uri": null,
        "value_json": "\"PR #4 exact test check annotation: job not started because recent account payments failed or spending limit needs increase; runner name empty and steps absent.\"",
        "created_at": "2026-09-28T10:05:21Z"
      },
      {
        "evidence_id": 1619,
        "work_item_id": "wi:6a187c7e94be40daba8dce5678ba64f6",
        "evidence_kind": "executor_result",
        "label": "Oracle host reachable and existing datasette.service active; private profile currently serves broad db/*.db glob, so new",
        "uri": null,
        "value_json": "\"Oracle host reachable and existing datasette.service active; private profile currently serves broad db/*.db glob, so new copies remain in unserved private staging.\"",
        "created_at": "2026-09-28T10:05:21Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
