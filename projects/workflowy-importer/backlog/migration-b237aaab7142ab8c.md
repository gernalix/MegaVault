# Investigate Fedora Service · user:workflowy-roadmap-sync.service recurring DOWN incident

<!-- migration-b237aaab7142ab8c -->

Migrated project backlog. Project: **workflowy-importer**; project_id: 96.

This entry is passive backlog, not authorization to execute. C3 is retired. Original instructions below are historical requirements; C3 intake/router/worker/writer, PROMPT_ID allocation, automatic scheduling, Workflowy control and global orchestration requirements are superseded by the retirement request of 2026-10-05. Preserve independent functional requirements; do not restart C3 or allocate execution state until a human starts this task.

Reconciliation: Merged duplicate/complementary observations and subtasks; every original requirement retained. Conflicting historical instructions are preserved explicitly below; none is silently dropped. Source status, blockers, acceptance, priorities, timestamps and dependencies remain attached.

Related projects: 96.

Provenance: `wi:e8b30d54c8db4af2b6b9b61b94b5845d`, `wi:08e57056aea44263a73e37c675c9b194`, `issue:e22726e3b2d09cb1f0ab09356b9a49d8`, `issue:5fd4c0f8e97a6a58827ecee9c9b5d3ad`, `issue:5ffc3e63789c0ffb6cd645beec21cc51`, `issue:c7b8390236186de90fbae8d76b194388`, `issue:c892f930a0238fe54d97385548cbfa51`, `issue:76a031934639e1461065bb9808f424aa`, `issue:40dfebb49c16b9cfafc5f1b4ec14df02`, `issue:6939f32b0c547d498ada61e2b7c0c822`, `issue:9594567d14963810f5f016112a9602e1`, `issue:b7f70b1c84ea922a2e6da12d0890bb1f`, `issue:c4ab6433504a298719fea5531eb46ebb`, `issue:836c1fcc2a578e570dc60d9605dfc291`, `issue:090548031b73a59df448f93b8ee31bea`, `issue:98d13c26c0cf10723692fbb9d7aca9f2`.

[Complete immutable C3 archive](https://github.com/gernalix/codex-roadmap/tree/eb165d45cdcdcc613ab4a37f45f4c9199178f494/archive/retirement-2026-10-05).

### Investigate recurring workflowy-roadmap-sync DOWN alerts

Determine why monitor 63 reports missing heartbeat for workflowy-roadmap-sync.service, distinguish intended skip from failure using live evidence, and apply only a scoped correction if warranted.

status: pending

### Uptime Kuma monitor transitioned to DOWN.

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-09-30 11:30:23.337 (row 695367)
Failure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s

status: pending

### issue:e22726e3b2d09cb1f0ab09356b9a49d8

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 08:34:48.179 (row 736235)
Failure context: No heartbeat in the time window

state: pending

### issue:5fd4c0f8e97a6a58827ecee9c9b5d3ad

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 09:27:28.975 (row 737961)
Failure context: No heartbeat in the time window

state: pending

### issue:5ffc3e63789c0ffb6cd645beec21cc51

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 09:54:30.100 (row 738834)
Failure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s

state: pending

### issue:c7b8390236186de90fbae8d76b194388

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 10:04:53.174 (row 739145)
Failure context: No heartbeat in the time window

state: pending

### issue:c892f930a0238fe54d97385548cbfa51

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 10:14:22.867 (row 739479)
Failure context: No heartbeat in the time window

state: pending

### issue:76a031934639e1461065bb9808f424aa

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 10:36:27.088 (row 740193)
Failure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=missings threshold=300s

state: pending

### issue:40dfebb49c16b9cfafc5f1b4ec14df02

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 10:44:22.769 (row 740437)
Failure context: No heartbeat in the time window

state: pending

### issue:6939f32b0c547d498ada61e2b7c0c822

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 11:38:27.071 (row 742183)
Failure context: No heartbeat in the time window

state: pending

### issue:9594567d14963810f5f016112a9602e1

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:04:22.532 (row 743043)
Failure context: No heartbeat in the time window

state: pending

### issue:b7f70b1c84ea922a2e6da12d0890bb1f

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:11:49.525 (row 743240)
Failure context: user:workflowy-roadmap-sync.service: inactive/dead; job freshness stale age=339.395s threshold=300s

state: pending

### issue:c4ab6433504a298719fea5531eb46ebb

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:16:29.885 (row 743396)
Failure context: No heartbeat in the time window

state: pending

### issue:836c1fcc2a578e570dc60d9605dfc291

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:22:23.063 (row 743576)
Failure context: No heartbeat in the time window

state: pending

### issue:090548031b73a59df448f93b8ee31bea

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:32:22.159 (row 743899)
Failure context: No heartbeat in the time window

state: pending

### issue:98d13c26c0cf10723692fbb9d7aca9f2

Uptime Kuma monitor transitioned to DOWN.
Monitor: Fedora Service · user:workflowy-roadmap-sync.service (id 63)
Heartbeat: 2026-10-01 12:57:24.775 (row 744713)
Failure context: No heartbeat in the time window

state: pending

Full original records and context: [project source attachment](https://github.com/gernalix/MegaVault/blob/task/c3-retirement-20261005/projects/workflowy-importer/backlog/sources/migration-b237aaab7142ab8c.json).
