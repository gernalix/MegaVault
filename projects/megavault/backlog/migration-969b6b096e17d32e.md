# Registrare gitguardian-fixer dopo la riconciliazione canonica

<!-- migration-969b6b096e17d32e -->

Migrated project backlog. Project: **megavault**; project_id: 23.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 23.

Provenance: `wi:bead141503364bba82cec8d78760c81b`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Registrare gitguardian-fixer dopo la riconciliazione canonica

Registrare il repository privato gernalix/gitguardian-fixer in MegaVault solo dopo aver riconciliato in modo canonico le modifiche preesistenti a megavault.sqlite limitate a prompt_id_allocation_requests, prompt_id_events e prompt_id_registry. Preservare tali dati; non sovrascriverli.

status: pending

### Original source records and attached context

```json
[
  {
    "routing": {
      "project": "23",
      "reason": "canonical repository identity",
      "related_projects": [
        "23"
      ]
    },
    "source": {
      "work_item_id": "wi:bead141503364bba82cec8d78760c81b",
      "parent_id": null,
      "kind": "task",
      "title": "Registrare gitguardian-fixer dopo la riconciliazione canonica",
      "objective": "Registrare il repository privato gernalix/gitguardian-fixer in MegaVault solo dopo aver riconciliato in modo canonico le modifiche preesistenti a megavault.sqlite limitate a prompt_id_allocation_requests, prompt_id_events e prompt_id_registry. Preservare tali dati; non sovrascriverli.",
      "acceptance_json": "[]",
      "status": "pending",
      "executor_policy": "auto",
      "sort_order": null,
      "current_action": null,
      "next_action": null,
      "blocker": null,
      "project_id": null,
      "project_name": null,
      "repo": "gernalix/MegaVault",
      "prompt_id": null,
      "task_id": null,
      "required": 1,
      "actionable": 1,
      "source_kind": "c2-intake",
      "source_ref": "c2-intake",
      "created_at": "2026-09-30T10:16:35Z",
      "updated_at": "2026-09-30T10:16:35Z"
    },
    "work_item_tags": [
      {
        "work_item_id": "wi:bead141503364bba82cec8d78760c81b",
        "tag": "source:issue-inbox"
      }
    ],
    "work_item_dependencies": [],
    "work_item_relations": [],
    "work_item_checkpoints": [],
    "work_item_result_receipts": [],
    "work_item_evidence": [
      {
        "evidence_id": 2147,
        "work_item_id": "wi:bead141503364bba82cec8d78760c81b",
        "evidence_kind": "issue_inbox",
        "label": "issue:bdd1ead67606481aaa4490da479090d0",
        "uri": "codex://threads/01a0ee5e-8aeb-7712-a472-8cfa436d1ea5",
        "value_json": "{\"chat_url\": \"codex://threads/01a0ee5e-8aeb-7712-a472-8cfa436d1ea5\", \"code_location\": null, \"description\": \"MegaVault registration for new private repository gernalix/gitguardian-fixer is blocked because /home/daniele/MegaVault has pre-existing uncommitted megavault.sqlite changes limited to prompt_id_allocation_requests, prompt_id_events, and prompt_id_registry; megavault_update.py reports dirty_worktree. Preserve those changes and register the repository only after canonical reconciliation.\", \"executor\": null, \"executor_ref\": \"01a0ee5e-8aeb-7712-a472-8cfa436d1ea5\", \"issue_id\": \"issue:bdd1ead67606481aaa4490da479090d0\", \"observed_at_ms\": 1790709563318, \"origin_run_id\": null, \"origin_work_item_id\": null, \"repo\": null}",
        "created_at": "2026-09-30T10:16:35Z"
      }
    ],
    "work_item_runs": [],
    "issue_work_item_links": [
      {
        "issue_id": "issue:bdd1ead67606481aaa4490da479090d0",
        "work_item_id": "wi:bead141503364bba82cec8d78760c81b",
        "role": "decision",
        "created_at": "2026-09-29T19:19:23Z"
      }
    ]
  }
]
```
