META:
name=megavault-project-exporter
slug=megavault-project-exporter
path=/home/daniele/codex-workspace/megavault-project-exporter
remote=none
branch=master
verified_commit=c5cb161
verified_at=2026-06-05T13:25:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
prompt=#271684

PURPOSE:
purpose=Ultra-fast cached ZIP bundler for sharing any MegaVault-registered project plus MegaVault docs with ChatGPT.

STACK:
lang=Bash
tools=git archive,zip,sha256sum,ssh,scp,rsync,wl-copy,xclip,xsel
platform=Linux Mint desktop or Oracle VM/headless shell
config=~/.config/megavault-project-exporter/config.env
deps_required=git,zip,sha256sum
deps_optional=wl-copy,xclip,xsel,ssh,scp,rsync

MAP:
entry=exporter.sh
config=config/config.env.example; runtime config in ~/.config/megavault-project-exporter/config.env
state=state/<project_slug>.env
bundles=bundles/megavault_bundle_<project>_<projectHEADshort>_<vaultHEADshort>.zip
logs=logs/exporter-YYYYMMDD.log
metadata=dev/project.metadata.json
tests=manual CLI smoke commands; no framework
avoid=daemon,background service,Tailscale dependency,hardcoded project list,menu cache,ZIP outside bundles/

ARCH:
menu=reloads MegaVault indices every run; PROJECT_INVENTORY first, PROJECT_INDEX second, metadata scan fallback only if indices unusable
selection=number,exact slug,or exact/name case-insensitive CLI
archive=git archive selected project HEAD + git archive MegaVault HEAD; nested archives stored in final bundle
cache=state compares project HEAD, MegaVault HEAD, dirty markers, ZIP path, ZIP checksum
clipboard=local file-reference clipboard if tool exists; fallback prints path
vm=optional SSH push to configured Mint host; verifies remote file checksum before remote clipboard
headless=no transfer; prints scp,rsync,and Mint clipboard commands

FLOW:
run=ensure dirs/config -> reload menu -> select project -> read git HEADs -> cache check -> archive if needed -> transfer/clipboard mode
cache_hit=state HEADs+dirty markers match and ZIP exists with matching sha256 -> reuse immediately
cache_miss=archive project + MegaVault in temp dir -> zip final under bundles/ -> write state
local=copy file reference via wl-copy/xclip/xsel else print path
vm=scp to MINT_DEST_DIR -> remote sha256 verify -> remote clipboard verify
headless=print ready scp/rsync/local clipboard commands

INV:
menu=no hardcoded projects; no cached menu; live MegaVault indices are reread each start
bundle=final ZIPs only in /home/daniele/codex-workspace/megavault-project-exporter/bundles
git=archives use committed HEAD only; dirty worktrees are warned and dirty marker invalidates cache
cache=reuse only when project HEAD, MegaVault HEAD, dirty marker, path, ZIP existence, and checksum agree
resources=no daemon; no resident app; no mandatory Tailscale; temp files removed
transfer=do not claim remote success until file exists and sha256 matches
clipboard=do not claim verified clipboard unless paste/remote command confirms or fallback explicitly says no tool

BUILD:
cmd=chmod +x exporter.sh
env=Linux shell with git+zip+sha256sum
requirements=git repository for selected project and MegaVault

TEST:
syntax=bash -n exporter.sh
menu=./exporter.sh --list
headless=./exporter.sh --project megavault-project-exporter --headless --yes
cache=run same command twice; second must report BUNDLE_ACTION=reused
archive=unzip -l bundles/<zip> must show project archive and MegaVault archive
local=./exporter.sh --project megavault-project-exporter --local --yes; clipboard tool may fallback to text path
vm=./exporter.sh --project megavault-project-exporter --vm --yes after MINT_HOST config

DATA:
DB=none
State=/home/daniele/codex-workspace/megavault-project-exporter/state
Bundles=/home/daniele/codex-workspace/megavault-project-exporter/bundles
Logs=/home/daniele/codex-workspace/megavault-project-exporter/logs
Config=~/.config/megavault-project-exporter/config.env
CacheKey=project HEAD + MegaVault HEAD + dirty markers
Export=final bundle ZIP
Import=none
Migration=state env format append-only/simple key=value
Retention=manual cleanup; generated ZIPs ignored by repo

DNB:
* no hardcoded project list
* no menu cache
* no final ZIP outside bundles/
* no daemon/service/Tailscale requirement
* do not include .git directories
* do not silently ignore dirty project/MegaVault worktrees
* do not report remote transfer/clipboard success without verification

BUG:
issue=clipboard tools absent on headless shells
cause=wl-copy/xclip/xsel are desktop-session tools
workaround=headless mode prints scp/rsync/Mint clipboard commands
issue=2026-06-05 wl-copy installed on X11 Mint but no Wayland socket
cause=tool presence did not mean usable clipboard backend
fix=try wl-copy first, then fall through to xclip/xsel when wl-copy exits nonzero

RISK:
risk=git archive excludes uncommitted changes; warning is mandatory when dirty
risk=remote SSH clipboard may fail without desktop DISPLAY/WAYLAND session
risk=large bundles can be slow to transfer; guardrail asks confirmation above threshold
risk=PROJECT_INVENTORY may contain stale missing paths; script falls back only if official indices unusable

ROAD:
now=create v1 exporter, register docs, verify cache and modes
next=add automated fixture tests if repeated changes are expected
later=optional retention policy for old bundles/state

LINK:
meta=../../../megavault-project-exporter/dev/project.metadata.json
human=../../human/projects/megavault-project-exporter/overview.md
changelog=../../human/projects/megavault-project-exporter/changelog.md
features=../../human/projects/megavault-project-exporter/features.md
roadmap=../../human/projects/megavault-project-exporter/roadmap.md
troubleshooting=../../human/projects/megavault-project-exporter/troubleshooting.md
repo=../../../megavault-project-exporter
index=../PROJECT_INDEX.md
inventory=../PROJECT_INVENTORY.md

OPEN:
open=remote VM verification requires configured MINT_HOST and SSH desktop session
open=clipboard file-reference behavior varies by desktop environment
open=no automated unit test harness yet
