# Prompt 739482 - XFCE window tiling repair

created_at=2026-06-10T14:26:33+02:00
host=daniele-Surface-Pro
scope=user XFCE/X11 window-manager settings
backup=/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_739482_xfce_window_tiling_backup_20260610T142633+0200.txt

## Environment

XDG_CURRENT_DESKTOP=XFCE
DESKTOP_SESSION=xfce
XDG_SESSION_TYPE=x11
GDMSESSION=xfce
DISPLAY=:0.0
window_manager=xfwm4
xfwm4_version=4.18.0
xfce4_session_version=4.18.3
os=Linux Mint 22.3 Zena

## Cause

cause_shortcuts=normal arrow tiling shortcuts were not mapped: only `<Super>KP_Left` and `<Super>KP_Right` existed for `tile_left_key` and `tile_right_key`.
cause_workspace_confusion=edge workspace wrapping was not enabled: `/general/wrap_workspaces=false` and `/general/wrap_windows=false`; workspace switching remains bound to `<Primary><Alt>Left/Right`.
cause_drag=edge tiling itself was already enabled: `/general/tile_on_move=true`, `/general/snap_to_border=true`, `/general/use_compositing=true`.
note_super=standalone `Super_L` is bound to `xfce4-popup-whiskermenu`; synthetic `xdotool` tests for plain Super combos were unreliable, while WM shortcuts such as `Alt+F10` were received.

## Settings Changed

changed=/xfwm4/custom/<Super>Left -> tile_left_key
changed=/xfwm4/custom/<Super>Right -> tile_right_key
changed=/xfwm4/custom/<Primary><Super>Left -> tile_left_key
changed=/xfwm4/custom/<Primary><Super>Right -> tile_right_key
confirmed=/general/tile_on_move=true
left_existing=/xfwm4/custom/<Super>KP_Left -> tile_left_key
right_existing=/xfwm4/custom/<Super>KP_Right -> tile_right_key
unchanged=/commands/custom/Super_L -> xfce4-popup-whiskermenu
unchanged=/xfwm4/custom/<Primary><Alt>Left -> left_workspace_key
unchanged=/xfwm4/custom/<Primary><Alt>Right -> right_workspace_key

## Commands Applied

```bash
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Super>Left' --create -t string -s tile_left_key
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Super>Right' --create -t string -s tile_right_key
xfconf-query -c xfwm4 -p /general/tile_on_move -s true
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Primary><Super>Left' --create -t string -s tile_left_key
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Primary><Super>Right' --create -t string -s tile_right_key
```

## Verification

readback_shortcuts=confirmed mappings for `<Super>Left`, `<Super>Right`, `<Primary><Super>Left`, `<Primary><Super>Right`, `<Super>KP_Left`, `<Super>KP_Right`.
readback_xfwm4=tile_on_move=true, snap_to_border=true, use_compositing=true, wrap_windows=false, wrap_workspaces=false.
test_windows=opened two `xfce4-terminal` windows titled `CodexTileLeft` and `CodexTileRight`.
keyboard_test=`Ctrl+Super+Left/Right` produced left/right tiled geometry once during live test: left `x=24 y=116 w=1330 h=1668`, right `x=1392 y=116 w=1330 h=1668`, screen `2736x1824`.
test_limitation=plain `Super+Left/Right` and synthetic drag via `xdotool` were not reliable enough as automated proof in this session; final manual test should use physical keys and titlebar drag.

## Final Use

preferred_shortcuts=try `Super+Left` and `Super+Right` first.
verified_fallback_shortcuts=`Ctrl+Super+Left` and `Ctrl+Super+Right`.
drag_expected=drag a non-maximized or restored window by titlebar to the left/right screen edge; `xfwm4` should tile because `tile_on_move=true`.

## Rollback

```bash
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Super>Left' -r
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Super>Right' -r
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Primary><Super>Left' -r
xfconf-query -c xfce4-keyboard-shortcuts -p '/xfwm4/custom/<Primary><Super>Right' -r
```
