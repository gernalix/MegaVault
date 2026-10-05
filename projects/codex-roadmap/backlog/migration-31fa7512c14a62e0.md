# Coalesce recurrent Kuma heartbeat alerts in C2 Inbox

<!-- migration-31fa7512c14a62e0 -->

Migrated project backlog. Project: **codex-roadmap**; project_id: 51.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Independent request retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 51.

Provenance: `wi:c04fddf34c024cc49a9dc94974212e9e`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Coalesce recurrent Kuma heartbeat alerts in C2 Inbox

For repeated short no-heartbeat DOWN events on the same Kuma monitor/current incident, preserve every transition as evidence but avoid creating repeated pending Inbox rows and duplicate regression successors. Detect a genuine new incident after recovery, verify monitoring fidelity, and test bounded coalescing with monitor IDs 42/63/65/73 without hiding persistent outages.

status: waiting

current_action: Parked during roadmap semantic reconciliation.

next_action: Reassess after Symphony acquisition/migration scope is decided; resume only if the capability remains necessary outside Symphony.

blocker: Deferred pending Symphony migration/replacement decision.

Full original records and context: [project source attachment](https://github.com/gernalix/MegaVault/blob/task/c3-retirement-20261005/projects/codex-roadmap/backlog/sources/migration-31fa7512c14a62e0.json).
