# megavault-project-exporter Overview

`megavault-project-exporter` creates one shareable ZIP for a selected MegaVault-registered project plus the MegaVault documentation archive.

## What it does
- Regenerates the project menu from MegaVault indices on every run.
- Lets the operator type only a project number.
- Creates nested `git archive` ZIPs for the selected project and MegaVault.
- Reuses an existing bundle when the project HEAD and MegaVault HEAD are unchanged.
- Stores final bundles only in `/home/daniele/codex-workspace/megavault-project-exporter/bundles/`.

## Runtime paths
- Script: `/home/daniele/codex-workspace/megavault-project-exporter/exporter.sh`
- Global command: `megavault-exporter`
- Symlink: `/home/daniele/.local/bin/megavault-exporter`
- Bundles: `/home/daniele/codex-workspace/megavault-project-exporter/bundles/`
- State: `/home/daniele/codex-workspace/megavault-project-exporter/state/`
- Logs: `/home/daniele/codex-workspace/megavault-project-exporter/logs/`
- Config: `~/.config/megavault-project-exporter/config.env`

## Command check
- Executable bit: `test -x /home/daniele/codex-workspace/megavault-project-exporter/exporter.sh`
- Launcher target: `ls -l /home/daniele/.local/bin/megavault-exporter`
- PATH resolution: `command -v megavault-exporter`
- Menu smoke test: `megavault-exporter --list`

## Modes
- Mint desktop: create/reuse bundle and copy the file reference with `wl-copy`, `xclip`, or `xsel`; otherwise print the path.
- Oracle VM with Mint SSH: copy ZIP to `/home/daniele/Downloads/megavault-bundles/`, verify checksum, then run clipboard copy on Mint.
- Headless/no Mint access: print ready `scp`, `rsync`, and Mint clipboard commands.

## Links
- AI doc: AI doc (`../../../ai/projects/megavault-project-exporter.md`; status=UNKNOWN)
- Metadata: dev/project.metadata.json (`../../../../megavault-project-exporter/dev/project.metadata.json`; status=UNKNOWN)
- Repository: repo path (`../../../../megavault-project-exporter`; status=UNKNOWN)
