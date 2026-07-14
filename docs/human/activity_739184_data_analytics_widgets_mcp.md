# Activity 739184 - Data Analytics MCP startup fix

Date: 2026-07-14
Status: PASS CON WARNING

## Root cause

`dataAnalyticsWidgets` is not configured through `codex mcp add` or `~/.codex/config.toml`. It is bundled by the installed Data Analytics plugin:

`/home/daniele/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599/.mcp.json`

Effective MCP command:

```text
cwd=/home/daniele/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599
command=node
args=./mcp/server.cjs --stdio
transport=stdio
```

The server crashed before answering MCP `initialize` because `mcp/server.cjs` loads `assets/datascience.png` at module startup and that file was missing from the plugin cache. Node exited with `ENOENT`, so Codex reported `connection closed: initialize response`.

## Fix

Generated the missing plugin asset from the existing SVG:

`assets/datascience.svg` -> `assets/datascience.png`

No server was disabled. No model, YOLO mode, timeout, retry, or global Codex setting was changed. No package was reinstalled or updated.

## Backups

Plugin backup:

`/home/daniele/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599/backups/activity_739184_20260714T140237+0200`

MegaVault registry backup:

`/home/daniele/MegaVault/backups/activity_739184_20260714T140520+0200`

## Test summary

- Fedora version: Fedora Linux 44 Workstation, kernel `7.1.3-200.fc44.x86_64`.
- Codex CLI: `/usr/local/bin/codex`, `codex-cli 0.144.4`.
- Manual pre-fix server run from plugin root: FAIL, `ENOENT assets/datascience.png`.
- Manual post-fix server start: PASS, no stdout/stderr noise and no immediate crash.
- Manual JSON-RPC handshake: PASS, `data-analytics-widgets`, protocol `2024-11-05`, 5 tools, 3 resources.
- `codex mcp list`: PASS/coherent, no user-configured MCP servers; this server is plugin-provided.
- `codex doctor`: PASS, `17 ok`, `0 warn`, `0 fail`.
- Real `codex --yolo` startup: PASS, two separate TTY launches from `/home` had no `MCP startup incomplete` and no `connection closed: initialize response`.

## Remaining warning

This is a local plugin-cache repair. If a future plugin refresh or reinstall restores the same incomplete upstream package, the missing PNG could reappear. The current installed cache is fixed and verified.

MegaVault was already dirty before this work with unrelated deletions and a `.gitignore` modification; those were not touched.
