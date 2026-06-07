# MEGAVAULT_PROTOCOL.md

VERSION=4

PURPOSE=Global documentation constitution. Defines how MegaVault is structured, written, validated, maintained and consumed by Codex.

GOAL=Maximize Codex decision quality, project understanding, safety, maintainability and recovery speed.

PRIMARY_OUTPUT=Operational knowledge.

NOT=Documentation for humans.

---

# CORE PRINCIPLES

P1=AI Vault authoritative.
P2=Human Vault derived.
P3=Legacy docs historical.
P4=1 AI doc/project.
P5=Max useful information density.
P6=No duplicated truths.
P7=No invented knowledge.
P8=Documentation debt is technical debt.
P9=Code reality > documentation assumptions.
P10=Codex should become productive after reading metadata+AI doc.

---

# SOURCE PRIORITY

1=project.metadata.json
2=AI doc
3=Repository code
4=Human docs
5=Legacy docs

Conflict resolution:

metadata > ai_doc > code > human > legacy

---

# CODEX ENTRY WORKFLOW

Mandatory order:

1. Read dev/project.metadata.json
2. Read ai_doc
3. Read task-relevant files
4. Read legacy only if needed

Forbidden:

* repository-wide exploration before ai_doc
* using Human docs as operational source
* using legacy as primary source

---

# AI DOC OBJECTIVE

Question:

"What does Codex need to know to modify this project safely and efficiently?"

Only information answering that question belongs inside AI docs.

---

# AI DOC FORMAT

One file only.

Required sections:

META
PURPOSE
STACK
MAP
ARCH
FLOW
INV
BUILD
TEST
DATA
DNB
BUG
RISK
ROAD
LINK
OPEN

Optional:

DECISIONS
RELEASE
PERF
SECURITY
INTEGRATIONS

Missing required section = documentation bug.

---

# AI DOC STYLE

Allowed:

* key=value
* lists
* checklists
* abbreviations
* identifiers
* commands
* paths

Avoid:

* prose
* introductions
* tutorials
* marketing text
* filler
* repeated information

BAD:

"The application uses Room to store user data."

GOOD:

DB=Room

BETTER:

DB=Room
Schema=v10
Backup=multitimer.db
Import=validate_before_swap

---

# INFORMATION DENSITY RULE

Every line must answer at least one question:

* what?
* where?
* how?
* why?
* risk?
* invariant?
* command?
* dependency?

If none:

DELETE LINE.

---

# TOKEN OPTIMIZATION RULE

Goal is NOT:

min_tokens

Goal IS:

max_useful_information_per_token

BAD:

DB=Room

BETTER:

DB=Room
Schema=v10
Backup=multitimer.db
Import=validate_before_swap
Retention=snapshot_history,audit_events

Compression must never remove operational knowledge.

---

# ANTI-INVENTORY RULE

Repository inventories are low value.

BAD:

src/
test/
build/
assets/

GOOD:

entry=MainActivity.kt
import=ImportManager.kt
timeline=TimelineViewModel.kt

Only document files/directories operationally relevant.

---

# CODE-FIRST ENRICHMENT RULE

When documentation is weak:

1. metadata
2. ai_doc
3. human docs
4. legacy docs
5. README
6. build files
7. scripts
8. tests
9. source code

Code is authoritative.

Documentation must be updated from code reality.

Never assume docs are correct.

---

# ENRICHMENT PRIORITY

Extract knowledge in this order:

1. entrypoints
2. architecture
3. data flow
4. storage
5. backup
6. import/export
7. migrations
8. integrations
9. tests
10. scripts
11. release process
12. invariants
13. risks
14. roadmap

---

# MAP RULES

Must contain:

entry=
ui=
core=
db=
tests=
scripts=
avoid=

Avoid listing entire repository.

List only development-critical locations.

---

# ARCH RULES

ARCH explains:

* components
* responsibilities
* boundaries

FLOW explains:

* data flow
* event flow
* critical workflows

ARCH ≠ folder tree.

---

# INVARIANT RULES

INV is highest-value section.

Types:

arch=
data=
ux=
backup=
migration=
version=
i18n=
security=
perf=

Examples:

data=Tags shared(Session,Event)
ux=Timeline derives START/STOP
backup=validate_before_swap
version=monotonic_only

Missing invariant = documentation bug.

---

# DNB RULES

DNB = DO_NOT_BREAK

Contains:

* fragile systems
* regression-prone flows
* historical landmines

Examples:

DNB:

* import_restore_flow
* backup_compat_v9_v10
* shared_tag_model

Missing DNB = documentation bug.

---

# BUG RULES

BUG contains:

* active bugs
* known regressions
* historical failures

Format:

BUG:
issue=
cause=
workaround=

Unknown cause allowed.

Invented cause forbidden.

---

# UNKNOWN RULE

Never fabricate.

Allowed:

UNKNOWN
TODO
OPEN QUESTION

Forbidden:

educated guesses presented as facts.

---

# ROAD RULES

ROAD:

now=
next=
later=

Only actionable work.

No dreams.
No vague aspirations.

---

# OPEN RULES

OPEN contains:

* unresolved conflicts
* missing information
* stale docs
* architecture uncertainty

---

# DATA RULES

Must include when applicable:

DB=
Schema=
Backup=
Restore=
Import=
Export=
Migration=
Retention=
Paths=

Missing storage rules = documentation bug.

---

# BUILD RULES

BUILD:

cmd=
env=
requirements=

TEST:

unit=
integration=
smoke=
device=

Unknown allowed.

Invented commands forbidden.

---

# DOCUMENTATION DEBT

Documentation bug examples:

* missing invariant
* missing DNB
* missing roadmap
* missing storage rule
* missing test command
* broken link
* stale commit reference
* stale architecture description

Treat as real bugs.

---

# HUMAN DOC RULES

Purpose=human understanding.

AI docs optimize execution.

Human docs optimize comprehension.

Required:

overview
features
roadmap
changelog
troubleshooting

Human docs may explain.

AI docs must compress.

---

# BIDIRECTIONAL LINKS

AI doc must link:

metadata
human docs
legacy docs
repo

Human overview must link:

AI doc
metadata
legacy docs
repo

Broken link = documentation bug.

---

# UPDATE RULES

Update AI doc when:

* architecture changes
* DB changes
* build changes
* tests change
* import/export changes
* backup changes
* versioning changes
* release process changes

Update Human docs when:

* UX changes
* features change
* workflow changes
* changelog changes
* roadmap changes

---

# MEGAVAULT SIZE RULE

MegaVault stores lightweight operational documentation only.

Forbidden in MegaVault:

* huge files
* raw dumps
* massive logs
* complete snapshots
* archives
* databases
* reports hundreds of MB large

Every single file in MegaVault must stay at most a few MB.

If analysis generates large output:

1. Store the large artifact outside MegaVault.
2. Add only a compact MegaVault summary.
3. Summary must include external path, date, purpose and operational notes.

Before every MegaVault commit or push:

1. List staged files with sizes.
2. Block the commit if any staged file exceeds a few MB.
3. Do not use Git LFS for MegaVault unless the user explicitly changes this protocol.

---


# MEGAVAULT GIT SYNC RULE

If any file under MegaVault/ai or MegaVault/human is modified:

1. Run git status in the MegaVault repository.
2. Commit the MegaVault changes with a clear descriptive message.
3. Run git push for the MegaVault repository.
4. Include the MegaVault commit hash in the final report.

If git push cannot be completed because of network, credentials, conflicts, remote rejection or any other error:

* do not report success silently
* preserve local changes
* report the exact failure
* report whether commit succeeded locally
* report the manual command needed to finish the sync

MegaVault documentation changes are incomplete until committed and pushed, unless the user explicitly requested local-only changes.

---

# VALIDATION CHECKLIST

Every project must have:

metadata
ai_doc
human docs
working links

Every AI doc must contain:

META
PURPOSE
STACK
MAP
ARCH
FLOW
INV
BUILD
TEST
DATA
DNB
BUG
RISK
ROAD
LINK
OPEN

Missing section = failure.

---

# SUCCESS CRITERION

A fresh Codex session should understand:

* purpose
* architecture
* storage
* invariants
* risks
* build
* test
* roadmap

after reading:

1. project.metadata.json
2. ai/projects/<slug>.md

without repository-wide exploration.


---

# NEW PROJECT WORKFLOW

Mandatory order:

1. Create project.metadata.json
2. Create AI doc
3. Create Human overview
4. Create Human roadmap
5. Create Human changelog
6. Create Human troubleshooting
7. Create bidirectional links
8. Commit MegaVault
9. Push MegaVault

Feature work starts only after documentation baseline exists.

---

# UNDOCUMENTED EXISTING PROJECT WORKFLOW

Mandatory order:

1. Inspect repository
2. Identify entrypoints
3. Identify architecture
4. Identify storage
5. Identify build/test process
6. Create metadata
7. Create AI doc
8. Create Human docs
9. Mark unknowns as UNKNOWN
10. Commit MegaVault
11. Push MegaVault

Feature work starts only after documentation baseline exists.

---

# MEGAVAULT CLEAN STATE RULE

MegaVault must never be left in a dirty state between tasks.

Before starting any new task involving MegaVault:

1. Check git status.
2. Check local commits ahead of origin.
3. Check pending pushes.

If dirty state exists:

1. Resolve it first.
2. Push pending MegaVault commits.
3. Report any failure.
4. Do not continue normal project work until MegaVault state is clean.

Clean state definition:

git_status=clean
unpushed_commits=0
uncommitted_changes=0
branch_sync=origin

Dirty MegaVault state is a protocol violation.

---

# TASK COMPLETION RULE

A task touching MegaVault is not complete until:

1. Documentation updated.
2. Changes committed.
3. Changes pushed.
4. Push verified.
5. Commit hash reported.

Final report must include:

MEGAVAULT_STATUS=clean
MEGAVAULT_COMMIT=<hash>
MEGAVAULT_PUSH=success

---

# AI DOC LANGUAGE SPEC

FORMAT=ultracompressed
STYLE=operational
PROSE=forbidden
FILLER=forbidden
NARRATIVE=forbidden

Allowed:

key=value
lists
checklists
paths
commands
identifiers
abbreviations

Rule:

1 line = 1 operational fact

Example:

DB=Room
Schema=v12
Backup=validate_before_swap

Not:

"The application uses Room and stores user data locally."



---

# GIT BRANCH DOCUMENTATION RULE

Every project metadata and AI doc must document the operational Git branch.

Required:

GIT:
repo=<repository>
branch=<primary_operational_branch>

If multiple active branches exist:

branch_main=<branch>
branch_release=<branch>
branch_hotfix=<branch>

Codex must:

1. Read documented branch before work.
2. Verify current branch matches documentation.
3. Update documentation if workflow changes.
4. Report branch mismatches.

Missing operational branch documentation = documentation bug.

---

# PROJECT METADATA REQUIREMENT

project.metadata.json must include:

repo
branch
project_type
status
ai_doc
human_overview

Missing branch field = metadata bug.


---

# PROJECT DELETION RULE

Default action = archive.

Project deletion requests must be interpreted as archive unless the user explicitly requests permanent destruction.

ARCHIVE:

1. Remove active code/repository if requested.
2. Move AI docs to archive.
3. Move Human docs to archive.
4. Mark metadata:

STATUS=archived

5. Update MegaVault indexes.

PURGE:

Only when explicitly requested.

Before purge:

1. Report assets to be destroyed.
2. Require confirmation.

After confirmation:

1. Delete code.
2. Delete repository.
3. Delete AI docs.
4. Delete Human docs.
5. Remove index references.

Archive is preferred.
Purge is exceptional.

---

# ARCHIVE DISCOVERY RULE

MegaVault must maintain archive indexes.

Required files:

ai/archive/ARCHIVE_INDEX.md
human/archive/ARCHIVE_INDEX.md

Each archived project entry must include:

slug=
old_repo=
status=archived
archived_at=
reason=
keywords=
domain=
stack=
former_ai_doc=
former_human_docs=
reuse_notes=

Before creating a new project:

1. Read active project index.
2. Read archive index.
3. Search archive keywords/domain/stack.
4. Report possible reusable archived projects.
5. Reuse knowledge when relevant.

Missing archive index = documentation bug.
