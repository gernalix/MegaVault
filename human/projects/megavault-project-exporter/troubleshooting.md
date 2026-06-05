# megavault-project-exporter Troubleshooting

## Clipboard tool unavailable
Run in headless mode and use the printed `scp` or `rsync` command. On Mint, install or expose one of `wl-copy`, `xclip`, or `xsel` if file-reference clipboard copy is required.

## Project appears in menu but export fails
The menu reflects MegaVault registration. Export still requires the registered path to exist locally and be a Git repository.

## Bundle is regenerated unexpectedly
Check the state file under `state/`. Dirty project or MegaVault worktrees intentionally invalidate reuse because uncommitted changes need an explicit warning.

## Remote VM mode fails
Verify `MINT_HOST` in `~/.config/megavault-project-exporter/config.env`, SSH reachability, remote destination permissions, and that the Mint desktop session exposes a clipboard command.
