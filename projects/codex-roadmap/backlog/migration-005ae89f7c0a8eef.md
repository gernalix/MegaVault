# Operational task state — checkpoint notifications via ntfy

<!-- migration-005ae89f7c0a8eef -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 15, 51.

Provenance: `task:CHATGPT-20260924-NTFY-CHECKPOINTS`, `state:gate:d9a7f05f5f4c41fffdf5`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Operational task state — checkpoint notifications via ntfy

status: waiting

current_action: Phase 2 is implemented except credential-store population/activation. Kuma watchdog is live and healthy; the remaining implementation/validation lane is blocked on credential-store writes.

next_action: Credential-store population is the sole blocker. On Fedora, source the protected `~/.config/codex/secrets/ntfy-checkpoints.env`, pipe `NTFY_PASSWORD` into GitHub secret `NTFY_CHECKPOINT_PUBLISHER_PASSWORD`, and pipe `NTFY_SUBSCRIBER_PASSWORD` into Secret Service attributes `service=ntfy-checkpoints`, `username=checkpoint-subscriber` without printing either value. Then resume here: enable the Fedora subscriber and perform the real checkpoint end-to-end test.

blocker: Protected publisher/subscriber credentials must be populated before subscriber activation and one real checkpoint test.

### Resolve blocker: Credential-store writes are currently blocked by the Remote Desktop tool safety layer: attempts to pipe the existing passwords into GitHub Actions secrets or GNOME Secret Service are rejected before execution. Do not expose, regenerate or commit them. Other implementation/monitoring work can continue.

status: blocked

next_action: Obtain an approved credential-store write path without exposing secrets, then verify publisher/subscriber.

blocker: Credential-store writes remain denied; NTFY parent is waiting and last publisher attempt had empty password/401 with no later materialization.

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "51",
      "reason": "semantic correction of source routing; original identity preserved",
      "related_projects": [
        "51",
        "15"
      ]
    },
    "source": {
      "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
      "parent_id": null,
      "kind": "task",
      "title": "Operational task state — checkpoint notifications via ntfy",
      "objective": null,
      "acceptance_json": null,
      "status": "waiting",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": "Phase 2 is implemented except credential-store population/activation. Kuma watchdog is live and healthy; the remaining implementation/validation lane is blocked on credential-store writes.",
      "next_action": "Credential-store population is the sole blocker. On Fedora, source the protected `~/.config/codex/secrets/ntfy-checkpoints.env`, pipe `NTFY_PASSWORD` into GitHub secret `NTFY_CHECKPOINT_PUBLISHER_PASSWORD`, and pipe `NTFY_SUBSCRIBER_PASSWORD` into Secret Service attributes `service=ntfy-checkpoints`, `username=checkpoint-subscriber` without printing either value. Then resume here: enable the Fedora subscriber and perform the real checkpoint end-to-end test.",
      "blocker": "Protected publisher/subscriber credentials must be populated before subscriber activation and one real checkpoint test.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": "CHATGPT-20260924-NTFY-CHECKPOINTS",
      "required": 1,
      "actionable": 0,
      "source_kind": "task_state",
      "source_ref": "CHATGPT-20260924-NTFY-CHECKPOINTS.md",
      "created_at": "2026-09-25T15:54:51Z",
      "updated_at": "2026-09-26T17:12:41Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [
      {
        "from_work_item_id": "state:step:7324dbeaafed954e9cbb",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:4b3f828253631930505b",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:99e8f6692dec6e59e047",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:81a6301abdffe3daee16",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:c608fe0ef0c890c9cb1c",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:6991351d6dbd266e194e",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:ed5f2fed53a2355da052",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:phase:b8e9d9ddf7809999f44c",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      },
      {
        "from_work_item_id": "state:step:cc7feee4d22d859f1585",
        "to_work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "relation_type": "superseded_by",
        "created_at": "2026-09-28T09:51:16Z",
        "actor": "c2-descendant-audit",
        "note": "DUPLICATE_MERGE"
      }
    ],
    "work_item_checkpoints": [
      {
        "checkpoint_id": 8,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "source_file": "CHATGPT-20260924-NTFY-CHECKPOINTS.md",
        "source_commit": "52bea96d02f55fac91cea210cf2e370b5963cc4f",
        "source_sha256": "6782eb978ba43d4abe0d68c22b922985750bfb9aed2bc1f7f2d74443abf11d93",
        "objective": "Implement reliable notifications for persistent ChatGPT/Codex checkpoints: GitHub publishes only after accepting a task-state push; a self-hosted ntfy service on the Oracle VM delivers to Android and browser/Fedora; Git remains canonical persistence.",
        "current_step": "Phase 2 is implemented except credential-store population/activation. Kuma watchdog is live and healthy; the remaining implementation/validation lane is blocked on credential-store writes.",
        "next_action": null,
        "blocker": "pre-migration / retired: historical evidence only",
        "completed_json": "[\"Created this persistent task state and updated the persistent-state protocol to require a complete executable checklist/current step.\", \"Added reproducible Oracle deployment files to `gernalix/vm_oracle`: pinned ntfy v2.28.0 Docker Compose, private server config, bootstrap and Fedora deployment wrapper.\", \"Deployed ntfy, Nginx routing, Cloudflare DNS/ingress and Web Push keys; public health is PASS.\", \"Diagnosed and repaired the duplicate stale Cloudflare ingress that caused HTTP 502.\", \"Hardened the bootstrap so the two ntfy account passwords are passed via environment rather than argv and all duplicate ntfy ingress entries are normalized before adding the canonical route.\", \"Reran the corrected Oracle bootstrap and verified the protected publisher/subscriber users plus their write-only/read-only topic ACLs.\", \"Removed the legacy duplicate Nginx server block and hardened `vm_oracle/ntfy/bootstrap.sh` to remove it on future deploys; clean redeploy returned `NTFY_ORIGIN=PASS` and `NTFY_PUBLIC=PASS`.\", \"Added and pushed the GitHub Actions checkpoint publisher to `codex-roadmap/main` (commit `237bfdd`).\", \"Added and pushed Fedora subscriber code/service/installer plus client documentation to `vm_oracle/main` (head `a1d3df2`).\", \"Installed the tracked Fedora subscriber executable/unit locally for static verification; activation is intentionally deferred until its read-only credential is in Secret Service.\", \"Added the reproducible Kuma watchdog helper to `vm_oracle`, applied it to Oracle after a timestamped SQLite backup, and verified monitor 72 produced a real UP heartbeat.\"]",
        "remaining_json": "[\"Populate the GitHub Actions publisher secret and Fedora Secret Service subscriber credential when the tool can perform credential-store writes; enable/test Fedora subscriber; run one real checkpoint end-to-end; perform browser/Android one-time subscription where device UI is available; finalize docs/state.\"]",
        "evidence_json": "[\"codex-roadmap persistent-state protocol now requires an executable checklist/current step.\", \"Public ntfy health: HTTP 200 with `{\\\"healthy\\\":true}`.\", \"Oracle ntfy container: healthy, bound to `127.0.0.1:3003`; Nginx host route: HTTP 200.\", \"Cloudflare config now has a single ntfy hostname route to `127.0.0.1:8001`.\", \"`/opt/ntfy/credentials.env`: root:root mode 0600; values were not recorded.\", \"After corrected bootstrap rerun, `ntfy user list` shows `checkpoint-publisher` with write-only access and `checkpoint-subscriber` with read-only access to `chatgpt-checkpoints`; anonymous has no access.\", \"`vm_oracle` auth/ingress hardening commit: `19b4dc3`; legacy Nginx cleanup is on remote history.\", \"GitHub publisher workflow: `codex-roadmap/main` commits `237bfdd` and `4d1c582`; the latter adds an explicit fail-fast when the repository secret is absent.\", \"Fedora subscriber implementation/docs: `vm_oracle/main` head `a1d3df2`.\", \"Fedora static validation: `python3 -m py_compile` PASS; installer `bash -n` PASS; installed unit `systemd-analyze verify` PASS.\", \"Credential materialization wrapper rerun: `NTFY_ORIGIN=PASS`, `NTFY_DEPLOY=PASS`; local client env path exists mode 0600 (values not read into chat).\", \"GitHub Actions run `35998658771`: trigger/path/task-ID logic reached the publish step; `NTFY_PASSWORD` was empty and authenticated ntfy correctly rejected the request with 401, so no false persisted-checkpoint notification was emitted.\", \"Kuma watchdog code: `vm_oracle/main` commits `237dc69` and `e5b5591`; runtime DB backup `/opt/uptime-kuma/data/kuma.db.bak-ntfy-20260924T122042Z`; monitor 72 heartbeat `status=1`, `200 - OK`.\"]",
        "captured_at": "2026-09-25T15:54:51Z"
      }
    ],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 113,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Created this persistent task state and updated the persistent-state protocol to require a complete executable checklist/current step.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-b996bc3997c7efc0",
        "value_json": "{\"text\": \"Created this persistent task state and updated the persistent-state protocol to require a complete executable checklist/current step.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 114,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Added reproducible Oracle deployment files to `gernalix/vm_oracle`: pinned ntfy v2.28.0 Docker Compose, private server config, bootstrap and Fedora deployment wrapper.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-ebba0a48ecd65c64",
        "value_json": "{\"text\": \"Added reproducible Oracle deployment files to `gernalix/vm_oracle`: pinned ntfy v2.28.0 Docker Compose, private server config, bootstrap and Fedora deployment wrapper.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 115,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Deployed ntfy, Nginx routing, Cloudflare DNS/ingress and Web Push keys; public health is PASS.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-7b4681fc6dafafdb",
        "value_json": "{\"text\": \"Deployed ntfy, Nginx routing, Cloudflare DNS/ingress and Web Push keys; public health is PASS.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 116,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Diagnosed and repaired the duplicate stale Cloudflare ingress that caused HTTP 502.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-3e3f94b746906de3",
        "value_json": "{\"text\": \"Diagnosed and repaired the duplicate stale Cloudflare ingress that caused HTTP 502.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 117,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Hardened the bootstrap so the two ntfy account passwords are passed via environment rather than argv and all duplicate ntfy ingress entries are normalized before adding the canonical route.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-96f6469572a68d8f",
        "value_json": "{\"text\": \"Hardened the bootstrap so the two ntfy account passwords are passed via environment rather than argv and all duplicate ntfy ingress entries are normalized before adding the canonical route.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 118,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Reran the corrected Oracle bootstrap and verified the protected publisher/subscriber users plus their write-only/read-only topic ACLs.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-c935228dae835554",
        "value_json": "{\"text\": \"Reran the corrected Oracle bootstrap and verified the protected publisher/subscriber users plus their write-only/read-only topic ACLs.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 119,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Removed the legacy duplicate Nginx server block and hardened `vm_oracle/ntfy/bootstrap.sh` to remove it on future deploys; clean redeploy returned `NTFY_ORIGIN=PASS` and `NTFY_PUBLIC=PASS`.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-364394f5127bb23b",
        "value_json": "{\"text\": \"Removed the legacy duplicate Nginx server block and hardened `vm_oracle/ntfy/bootstrap.sh` to remove it on future deploys; clean redeploy returned `NTFY_ORIGIN=PASS` and `NTFY_PUBLIC=PASS`.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 120,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Added and pushed the GitHub Actions checkpoint publisher to `codex-roadmap/main` (commit `237bfdd`).",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-9e04296ba2a5fcef",
        "value_json": "{\"text\": \"Added and pushed the GitHub Actions checkpoint publisher to `codex-roadmap/main` (commit `237bfdd`).\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 121,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Added and pushed Fedora subscriber code/service/installer plus client documentation to `vm_oracle/main` (head `a1d3df2`).",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-b8352cde83dd7c7f",
        "value_json": "{\"text\": \"Added and pushed Fedora subscriber code/service/installer plus client documentation to `vm_oracle/main` (head `a1d3df2`).\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 122,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Installed the tracked Fedora subscriber executable/unit locally for static verification; activation is intentionally deferred until its read-only credential is in Secret Service.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-87e976966b4563e5",
        "value_json": "{\"text\": \"Installed the tracked Fedora subscriber executable/unit locally for static verification; activation is intentionally deferred until its read-only credential is in Secret Service.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 123,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "completed",
        "label": "Added the reproducible Kuma watchdog helper to `vm_oracle`, applied it to Oracle after a timestamped SQLite backup, and verified monitor 72 produced a real UP heartbeat.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#completed-c4dd85040f0382be",
        "value_json": "{\"text\": \"Added the reproducible Kuma watchdog helper to `vm_oracle`, applied it to Oracle after a timestamped SQLite backup, and verified monitor 72 produced a real UP heartbeat.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 124,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "codex-roadmap persistent-state protocol now requires an executable checklist/current step.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-6b8401f5afbe26d8",
        "value_json": "{\"text\": \"codex-roadmap persistent-state protocol now requires an executable checklist/current step.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 125,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Public ntfy health: HTTP 200 with `{\"healthy\":true}`.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-4383ecdf3f25a97a",
        "value_json": "{\"text\": \"Public ntfy health: HTTP 200 with `{\\\"healthy\\\":true}`.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 126,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Oracle ntfy container: healthy, bound to `127.0.0.1:3003`; Nginx host route: HTTP 200.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-df7ea34cf00a53cd",
        "value_json": "{\"text\": \"Oracle ntfy container: healthy, bound to `127.0.0.1:3003`; Nginx host route: HTTP 200.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 127,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Cloudflare config now has a single ntfy hostname route to `127.0.0.1:8001`.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-7eb8a7802fdf5b9a",
        "value_json": "{\"text\": \"Cloudflare config now has a single ntfy hostname route to `127.0.0.1:8001`.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 128,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "`/opt/ntfy/credentials.env`: root:root mode 0600; values were not recorded.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-8aa50e563cb8f93e",
        "value_json": "{\"text\": \"`/opt/ntfy/credentials.env`: root:root mode 0600; values were not recorded.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 129,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "After corrected bootstrap rerun, `ntfy user list` shows `checkpoint-publisher` with write-only access and `checkpoint-subscriber` with read-only access to `chatgpt-checkpoints`; anonymous has no access.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-168f433974caf07b",
        "value_json": "{\"text\": \"After corrected bootstrap rerun, `ntfy user list` shows `checkpoint-publisher` with write-only access and `checkpoint-subscriber` with read-only access to `chatgpt-checkpoints`; anonymous has no access.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 130,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "`vm_oracle` auth/ingress hardening commit: `19b4dc3`; legacy Nginx cleanup is on remote history.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-9413c285dbddeaa7",
        "value_json": "{\"text\": \"`vm_oracle` auth/ingress hardening commit: `19b4dc3`; legacy Nginx cleanup is on remote history.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 131,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "GitHub publisher workflow: `codex-roadmap/main` commits `237bfdd` and `4d1c582`; the latter adds an explicit fail-fast when the repository secret is absent.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-d36a6f6a3f7d1b5a",
        "value_json": "{\"text\": \"GitHub publisher workflow: `codex-roadmap/main` commits `237bfdd` and `4d1c582`; the latter adds an explicit fail-fast when the repository secret is absent.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 132,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Fedora subscriber implementation/docs: `vm_oracle/main` head `a1d3df2`.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-a135a7a477098b17",
        "value_json": "{\"text\": \"Fedora subscriber implementation/docs: `vm_oracle/main` head `a1d3df2`.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 133,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Fedora static validation: `python3 -m py_compile` PASS; installer `bash -n` PASS; installed unit `systemd-analyze verify` PASS.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-563454e09c42ad30",
        "value_json": "{\"text\": \"Fedora static validation: `python3 -m py_compile` PASS; installer `bash -n` PASS; installed unit `systemd-analyze verify` PASS.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 134,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Credential materialization wrapper rerun: `NTFY_ORIGIN=PASS`, `NTFY_DEPLOY=PASS`; local client env path exists mode 0600 (values not read into chat).",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-eff382c49a15163f",
        "value_json": "{\"text\": \"Credential materialization wrapper rerun: `NTFY_ORIGIN=PASS`, `NTFY_DEPLOY=PASS`; local client env path exists mode 0600 (values not read into chat).\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 135,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "GitHub Actions run `35998658771`: trigger/path/task-ID logic reached the publish step; `NTFY_PASSWORD` was empty and authenticated ntfy correctly rejected the request with 401, so no false persisted-checkpoint notification was emitted.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-9d7c2de2ab109caf",
        "value_json": "{\"text\": \"GitHub Actions run `35998658771`: trigger/path/task-ID logic reached the publish step; `NTFY_PASSWORD` was empty and authenticated ntfy correctly rejected the request with 401, so no false persisted-checkpoint notification was emitted.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 136,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "evidence",
        "label": "Kuma watchdog code: `vm_oracle/main` commits `237dc69` and `e5b5591`; runtime DB backup `/opt/uptime-kuma/data/kuma.db.bak-ntfy-20260924T122042Z`; monitor 72 heartbeat `status=1`, `200 - OK`.",
        "uri": "state://CHATGPT-20260924-NTFY-CHECKPOINTS.md#evidence-f855b7059c67f49a",
        "value_json": "{\"text\": \"Kuma watchdog code: `vm_oracle/main` commits `237dc69` and `e5b5591`; runtime DB backup `/opt/uptime-kuma/data/kuma.db.bak-ntfy-20260924T122042Z`; monitor 72 heartbeat `status=1`, `200 - OK`.\"}",
        "created_at": "2026-09-25T15:54:51Z"
      },
      {
        "evidence_id": 355,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "classification",
        "label": "vm_oracle main e5b559 and codex-roadmap main: ntfy publisher/subscriber code and workflow exist; Fedora subscriber inact",
        "uri": null,
        "value_json": "\"vm_oracle main e5b559 and codex-roadmap main: ntfy publisher/subscriber code and workflow exist; Fedora subscriber inactive and credential names absent on 2026-09-26.\"",
        "created_at": "2026-09-26T17:12:41Z"
      },
      {
        "evidence_id": 1668,
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "evidence_kind": "issue_inbox",
        "label": "issue:054bd04ccc03423896c7a2b374346c63",
        "uri": null,
        "value_json": "{\"chat_url\": null, \"code_location\": null, \"description\": \"The codex-roadmap workflow Notify task-state checkpoint failed on the merged Symphony evaluation checkpoint while CI and Roadmap integrity passed. This does not block the task result but indicates checkpoint notification delivery is not reliable for successful task-state integrations.\\n\", \"executor\": null, \"executor_ref\": null, \"issue_id\": \"issue:054bd04ccc03423896c7a2b374346c63\", \"observed_at_ms\": 1790578462550, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": \"/home/daniele/projects/codex-roadmap\"}",
        "created_at": "2026-09-29T00:55:49Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:054bd04ccc03423896c7a2b374346c63",
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "role": "matched",
        "created_at": "2026-09-28T06:54:22Z"
      },
      {
        "issue_id": "issue:054bd04ccc03423896c7a2b374346c63",
        "work_item_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
        "role": "decision",
        "created_at": "2026-09-28T06:54:22Z"
      }
    ],
    "source_document": {
      "path": "/home/daniele/projects/codex-roadmap/operations/task-state/CHATGPT-20260924-NTFY-CHECKPOINTS.md",
      "text": "# Operational task state — checkpoint notifications via ntfy\n\nTASK_ID: CHATGPT-20260924-NTFY-CHECKPOINTS\nUpdated: 2026-09-24 14:27 Europe/Copenhagen\n\n## Objective\nImplement reliable notifications for persistent ChatGPT/Codex checkpoints: GitHub publishes only after accepting a task-state push; a self-hosted ntfy service on the Oracle VM delivers to Android and browser/Fedora; Git remains canonical persistence.\n\n## Constraints\n- Do not expose secrets/tokens in Git.\n- A checkpoint notification must mean the checkpoint is already present on the remote.\n- Keep Uptime Kuma for availability/watchdog duties, not as the event bus.\n- Prefer direct changes to canonical repos; no intermediate PRs unless technically required.\n- Do not disturb unrelated dirty worktrees.\n- Persist this task with commit + push checkpoints.\n\n## Plan / checklist\n### Phase 1 — Discovery\n- [x] Inspect vm_oracle deployment conventions and Oracle access path.\n- [x] Inspect codex-roadmap checkpoint workflow/hooks and identify the narrowest integration point.\n- [x] Check existing notification/credential conventions on Fedora.\n\n### Phase 2 — Implementation\n- [x] Add reproducible ntfy server deployment/configuration to vm_oracle.\n- [x] Deploy/start ntfy on Oracle with persistent storage and authentication; protected publisher/subscriber users and ACLs verified.\n- [x] Remove the duplicate Nginx ntfy server block while preserving the verified public route.\n- [x] Add a GitHub Actions publisher triggered only by accepted pushes changing `operations/task-state/**`.\n- [ ] Store publisher credential in GitHub Actions secret; never commit it.\n- [ ] Store subscriber credential in Fedora Secret Service; never commit it.\n- [x] Add tracked Fedora desktop subscriber + user-service installer and install/verify the unit locally.\n- [ ] Enable/validate the Fedora subscriber after its Secret Service credential is present.\n- [x] Document the browser/PWA and Android one-time authenticated subscription path.\n- [x] Add/adjust Kuma watchdog for ntfy availability if the existing monitoring architecture supports it safely.\n\n### Phase 3 — Validation\n- [x] Prove remote ntfy health.\n- [ ] Prove one real checkpoint push produces one ntfy event.\n- [x] Verify no notification is emitted before/without a successful push.\n- [ ] Verify affected repos are clean and pushed.\n- [ ] Update protocol/docs and close this state file.\n\n## Current step\nPhase 2 is implemented except credential-store population/activation. Kuma watchdog is live and healthy; the remaining implementation/validation lane is blocked on credential-store writes.\n\n## Verified facts\n- Fedora is reachable through Remote Desktop Commander.\n- Local repos codex-roadmap and vm_oracle are clean at task start.\n- MegaVault has unrelated local modifications and must not be touched casually.\n- ntfy is not currently installed as a Fedora command or service.\n- Oracle VM already has Docker, cloudflared and a validated `/etc/cloudflared/config.yml`; the existing tunnel can safely add a dedicated `ntfy.danielegalati.com` ingress without opening a host firewall port.\n- Fedora already uses owner-only `~/.config/codex/secrets/` files; this is the established unattended-service credential convention.\n- ntfy server v2.28.0 is the current stable release and supports private ACLs plus persisted Web Push subscriptions.\n- First Oracle deployment reached a healthy loopback ntfy service, created the Cloudflare DNS route and exposed a healthy public endpoint from Fedora. The only failure was Oracle's resolver not seeing the just-created hostname within the bootstrap timeout; this was a validation-location bug, not an ntfy/edge failure.\n- Oracle VM has Docker/Compose, 14 GiB free disk, and Uptime Kuma already bound to loopback; the canonical Cloudflare tunnel can route another hostname.\n- Fedora already has `secret-tool`, `notify-send`, and authenticated `gh` access.\n- A GitHub `push` workflow scoped to `operations/task-state/**` is a stronger event boundary than a local Git hook: it covers checkpoints pushed by any chat/client and runs only after GitHub accepted the commit.\n- `.github/workflows/notify-task-state-checkpoint.yml` is now on `codex-roadmap/main`; it emits one authenticated event per accepted push containing the changed task IDs plus repository/commit identity.\n- Fedora subscriber code, user unit and installer are tracked on `vm_oracle/main`; Python/bash syntax checks pass and the installed user unit passes `systemd-analyze verify`.\n- The existing deploy wrapper copied `/opt/ntfy/client.env` to Fedora as `~/.config/codex/secrets/ntfy-checkpoints.env` mode 0600 without exposing values.\n- Remote tool safety blocks automated transfer of the stored passwords into both GitHub Actions secrets and GNOME Secret Service; no credential value was printed or committed.\n- Real GitHub Actions run `35998658771` started after checkpoint commit `c7ad0ea`, resolved the changed task ID/SHA correctly, and failed only because `NTFY_PASSWORD` was empty; ntfy returned HTTP 401. This proves the workflow boundary is post-push and unauthenticated publication is rejected.\n- Uptime Kuma monitor `id=72` (`ntfy checkpoint service`) now checks `https://ntfy.danielegalati.com/v1/health` every 60 seconds with two retries; the first recorded heartbeat is UP (`200 - OK`).\n- Oracle currently runs ntfy healthy on loopback `127.0.0.1:3003`; Nginx host routing is HTTP 200 and `https://ntfy.danielegalati.com/v1/health` returns `{\"healthy\":true}`.\n- A stale duplicate Cloudflare ingress for `ntfy.danielegalati.com` pointed at unused port 8084 and caused the initial public 502; it was removed and the bootstrap now normalizes all duplicate entries to one `127.0.0.1:8001` route.\n- `/opt/ntfy/credentials.env` remains root-owned mode 0600 with the generated publisher/subscriber passwords; the corrected bootstrap has now created both users in the ntfy auth DB.\n- The bootstrap fix for password injection plus duplicate-ingress normalization is on `vm_oracle/main` in substantive commit `19b4dc3`; remote head at this checkpoint is `dd60451`.\n- Corrected bootstrap rerun completed successfully: public/origin health PASS; `checkpoint-publisher` is write-only on `chatgpt-checkpoints`, `checkpoint-subscriber` is read-only, and anonymous access remains denied.\n- The duplicate legacy Nginx block at `/etc/nginx/conf.d/ntfy-checkpoints.conf` was removed; the canonical `sites-enabled` block is the only remaining server block and public health remains PASS.\n\n## Decisions\n- Use one central ntfy topic/event stream rather than one topic per PROMPT_ID.\n- Git remote success is the event boundary; notification is downstream of push.\n- Prefer Oracle VM as always-on ntfy server.\n- Publish checkpoint events from a GitHub Actions `push` workflow on `codex-roadmap`, not from a Fedora Git hook, so every accepted remote checkpoint from any chat/client is covered.\n- Keep a Fedora subscriber/desktop notification path as a local convenience; Chrome/Android use ntfy subscriptions directly.\n\n## Completed\n- Created this persistent task state and updated the persistent-state protocol to require a complete executable checklist/current step.\n- Added reproducible Oracle deployment files to `gernalix/vm_oracle`: pinned ntfy v2.28.0 Docker Compose, private server config, bootstrap and Fedora deployment wrapper.\n- Deployed ntfy, Nginx routing, Cloudflare DNS/ingress and Web Push keys; public health is PASS.\n- Diagnosed and repaired the duplicate stale Cloudflare ingress that caused HTTP 502.\n- Hardened the bootstrap so the two ntfy account passwords are passed via environment rather than argv and all duplicate ntfy ingress entries are normalized before adding the canonical route.\n- Reran the corrected Oracle bootstrap and verified the protected publisher/subscriber users plus their write-only/read-only topic ACLs.\n- Removed the legacy duplicate Nginx server block and hardened `vm_oracle/ntfy/bootstrap.sh` to remove it on future deploys; clean redeploy returned `NTFY_ORIGIN=PASS` and `NTFY_PUBLIC=PASS`.\n- Added and pushed the GitHub Actions checkpoint publisher to `codex-roadmap/main` (commit `237bfdd`).\n- Added and pushed Fedora subscriber code/service/installer plus client documentation to `vm_oracle/main` (head `a1d3df2`).\n- Installed the tracked Fedora subscriber executable/unit locally for static verification; activation is intentionally deferred until its read-only credential is in Secret Service.\n- Added the reproducible Kuma watchdog helper to `vm_oracle`, applied it to Oracle after a timestamped SQLite backup, and verified monitor 72 produced a real UP heartbeat.\n\n## Remaining\nPopulate the GitHub Actions publisher secret and Fedora Secret Service subscriber credential when the tool can perform credential-store writes; enable/test Fedora subscriber; run one real checkpoint end-to-end; perform browser/Android one-time subscription where device UI is available; finalize docs/state.\n\n## Blockers\nCredential-store writes are currently blocked by the Remote Desktop tool safety layer: attempts to pipe the existing passwords into GitHub Actions secrets or GNOME Secret Service are rejected before execution. Do not expose, regenerate or commit them. Other implementation/monitoring work can continue.\n\n## Evidence\n- codex-roadmap persistent-state protocol now requires an executable checklist/current step.\n- Public ntfy health: HTTP 200 with `{\"healthy\":true}`.\n- Oracle ntfy container: healthy, bound to `127.0.0.1:3003`; Nginx host route: HTTP 200.\n- Cloudflare config now has a single ntfy hostname route to `127.0.0.1:8001`.\n- `/opt/ntfy/credentials.env`: root:root mode 0600; values were not recorded.\n- After corrected bootstrap rerun, `ntfy user list` shows `checkpoint-publisher` with write-only access and `checkpoint-subscriber` with read-only access to `chatgpt-checkpoints`; anonymous has no access.\n- `vm_oracle` auth/ingress hardening commit: `19b4dc3`; legacy Nginx cleanup is on remote history.\n- GitHub publisher workflow: `codex-roadmap/main` commits `237bfdd` and `4d1c582`; the latter adds an explicit fail-fast when the repository secret is absent.\n- Fedora subscriber implementation/docs: `vm_oracle/main` head `a1d3df2`.\n- Fedora static validation: `python3 -m py_compile` PASS; installer `bash -n` PASS; installed unit `systemd-analyze verify` PASS.\n- Credential materialization wrapper rerun: `NTFY_ORIGIN=PASS`, `NTFY_DEPLOY=PASS`; local client env path exists mode 0600 (values not read into chat).\n- GitHub Actions run `35998658771`: trigger/path/task-ID logic reached the publish step; `NTFY_PASSWORD` was empty and authenticated ntfy correctly rejected the request with 401, so no false persisted-checkpoint notification was emitted.\n- Kuma watchdog code: `vm_oracle/main` commits `237dc69` and `e5b5591`; runtime DB backup `/opt/uptime-kuma/data/kuma.db.bak-ntfy-20260924T122042Z`; monitor 72 heartbeat `status=1`, `200 - OK`.\n\n## Acceptance criteria\n- A pushed task-state checkpoint triggers a concise ntfy notification containing task ID and commit identity.\n- Failed/unpushed checkpoints do not claim persistence.\n- ntfy survives Oracle VM/service restarts and stores state persistently.\n- Secrets are not committed.\n- Browser/Fedora and Android can subscribe to the same authenticated stream.\n- The implementation is documented, tested, committed and pushed.\n\n## Next action\nCredential-store population is the sole blocker. On Fedora, source the protected `~/.config/codex/secrets/ntfy-checkpoints.env`, pipe `NTFY_PASSWORD` into GitHub secret `NTFY_CHECKPOINT_PUBLISHER_PASSWORD`, and pipe `NTFY_SUBSCRIBER_PASSWORD` into Secret Service attributes `service=ntfy-checkpoints`, `username=checkpoint-subscriber` without printing either value. Then resume here: enable the Fedora subscriber and perform the real checkpoint end-to-end test."
    }
  },
  {
    "routing": {
      "project": "51",
      "reason": "blocker subtask inherits explicitly identified parent project",
      "related_projects": [
        "51",
        "15"
      ]
    },
    "source": {
      "work_item_id": "state:gate:d9a7f05f5f4c41fffdf5",
      "parent_id": "task:CHATGPT-20260924-NTFY-CHECKPOINTS",
      "kind": "gate",
      "title": "Resolve blocker: Credential-store writes are currently blocked by the Remote Desktop tool safety layer: attempts to pipe the existing passwords into GitHub Actions secrets or GNOME Secret Service are rejected before execution. Do not expose, regenerate or commit them. Other implementation/monitoring work can continue.",
      "objective": null,
      "acceptance_json": null,
      "status": "blocked",
      "executor_policy": "auto",
      "sort_order": 1612,
      "current_action": null,
      "next_action": "Obtain an approved credential-store write path without exposing secrets, then verify publisher/subscriber.",
      "blocker": "Credential-store writes remain denied; NTFY parent is waiting and last publisher attempt had empty password/401 with no later materialization.",
      "project_id": null,
      "project_name": null,
      "repo": null,
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "task_state",
      "source_ref": "CHATGPT-20260924-NTFY-CHECKPOINTS.md#blocker",
      "created_at": "2026-09-25T15:54:51Z",
      "updated_at": "2026-09-27T22:23:04.386804Z"
    },
    "work_item_tags": [],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 1192,
        "work_item_id": "state:gate:d9a7f05f5f4c41fffdf5",
        "evidence_kind": "blocked_reconcile",
        "label": "Credential-store writes remain denied; NTFY parent is waiting and last publisher attempt had empty password/401 with no ",
        "uri": null,
        "value_json": "\"Credential-store writes remain denied; NTFY parent is waiting and last publisher attempt had empty password/401 with no later materialization.\"",
        "created_at": "2026-09-27T22:23:04.386804Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": []
  }
]
```
