# sqlite-to-obsidian

Status: cross-project architecture handoff for the Fedora-side Obsidian projector.

## Goal

Create one reusable Fedora service that consumes registered Git/SQLite-derived sources and maintains one shared Obsidian vault with stable, explicit cross-project links.

The service must not become a second datastore. Source repositories/databases remain authoritative; generated Markdown is disposable and rebuildable.

## First source: PersonalHub

Canonical input:

```text
gernalix/PersonalHub-data
```

Do not read `gernalix/PersonalHub` source commits as user data and do not require direct access to the Android `personalhub.db`.

Consume:

```text
state/manifest.json
state/schema.json
state/tables/<table>/<shard>.jsonl
history/YYYY/MM/DD/*.jsonl       # optional historical views
objects/sha256/...                # referenced BLOBs when useful
changes/<timestamp>-g<generation>.json
```

Current PersonalHub semantic modules are People, Timer, Places, Substances, WordPulse and Soldi.

The renderer should ignore technical/runtime material unless it has direct human value. In particular, do not create one note per queue/ack/cache/history-internal row.

## Architecture

```text
source adapters
    ↓
normalized entities + explicit relations
    ↓
global identity registry
    ↓
Markdown/Properties/wikilink renderer
    ↓
ownership manifest + atomic vault publish
```

Suggested repository layout:

```text
sqlite-to-obsidian/
├── src/sqlite_to_obsidian/
│   ├── cli.py
│   ├── config.py
│   ├── identity.py
│   ├── manifest.py
│   ├── renderer.py
│   ├── runner.py
│   └── sources/
│       └── personalhub.py
├── systemd/
│   ├── sqlite-to-obsidian.service
│   └── sqlite-to-obsidian.timer
├── tests/
├── docs/
└── pyproject.toml
```

## Identity

Each generated object has a globally namespaced identity:

```text
<source>/<module>/<kind>/<canonical-id>
```

Example:

```text
personalhub/people/contact/17
personalhub/places/place/42
personalhub/soldi/transaction/981
```

A display label may change without changing identity or path ownership.

Cross-project links require an explicit registered mapping or relation. Name/label equality is insufficient.

## Incremental state

Persist at least:

- source repository/ref;
- last successfully consumed commit;
- source generation/schema version where available;
- adapter version;
- renderer/projection version;
- generated-path ownership manifest;
- content hash per generated note where useful.

A run succeeds only after the resulting vault and ownership state are internally consistent. Do not advance the consumed revision before publication succeeds.

`changes/` may narrow work, but correctness must survive missing historical change files by rebuilding from the current state manifest.

## Vault rules

Generated notes must include ownership metadata:

```yaml
---
generated_by: sqlite-to-obsidian
source: personalhub
source_revision: "<git-sha>"
projection_version: 1
canonical_id: "..."
---
```

Only owned files may be replaced or deleted. Manual/unowned notes are immutable from the projector's perspective.

Keep generated content under source namespaces, for example:

```text
Generated/
  PersonalHub/
    People/
    Places/
    Timer/
    Soldi/
    Substances/
    WordPulse/
```

Manual notes may live elsewhere in the same vault.

## PersonalHub projection policy

Prioritize:

- People contacts and meaningful fields/events;
- Places records and meaningful visits/check-ins;
- Timer sessions, quick events and other user-facing activity records;
- Soldi accounts, transactions, recurrences and explicit relations;
- Substances, prescriptions, intake events and useful stock history;
- WordPulse sessions/summaries and useful aggregates;
- shared Hub contexts/tags/relations when useful for navigation.

Avoid direct note generation for sync queues, sync-known rows, generation counters, integrity caches, raw snapshot plumbing and equivalent implementation detail.

## Runtime

Default Fedora design: a periodic systemd timer, not an always-on polling daemon.

Each run:

1. acquire a single-process lock;
2. fetch/pull registered sources;
3. detect unchanged source revisions and exit success quickly;
4. compute the minimal affected semantic set;
5. render into a staging area;
6. validate ownership, paths and links;
7. atomically publish changed/deleted owned files;
8. persist the new state;
9. emit compact structured run status for monitoring.

Use the MegaVault systemd service standard. Uptime Kuma should monitor last-run success and freshness.

## Safety

- never write to source data repositories as part of normal projection;
- never import Markdown back into a source;
- never store source credentials/tokens in the vault or repository;
- never follow arbitrary paths from source data outside configured roots;
- sanitize Markdown/YAML and filenames;
- bound file counts and record sizes;
- preserve unrelated vault files;
- use synthetic fixtures in tests.

## Tests

Minimum:

- deterministic rendering;
- rename keeps stable identity/path;
- explicit relation creates correct wikilink;
- label collision does not create a false relation;
- incremental create/update/delete;
- unchanged revision produces no vault mutations;
- missing incremental history falls back safely;
- schema-version change invokes bounded rebuild;
- crash before state commit is recoverable;
- unrelated manual file survives rebuild;
- cross-project mapping resolution;
- PersonalHub technical tables are excluded from semantic note generation.

## Future sources

New adapters may consume other project SQLite databases, exports or Git-materialized state. They must normalize into the shared identity/relation model rather than embed source-specific logic in the renderer.
