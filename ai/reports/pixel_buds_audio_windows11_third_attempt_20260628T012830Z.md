# Pixel Buds Pro 2 Windows 11 audio routing third attempt

META:
created_utc=2026-06-28T01:28:30Z
updated_utc=2026-06-28T01:34:19Z
host=DANIELE_PC
user=seste
pc=ThinkPad P14s Gen 5 AMD
os=Windows 11 Pro build 26200
protocol=MEGAVAULT_PROTOCOL.md VERSION=3
branch=codex/pixel-buds-windows-audio
report_path=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_third_attempt_20260628T012830Z.md
log_dir=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T012830Z
previous_report_1=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_20260628T005406Z.md
previous_report_2=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_followup_20260628T0106Z.md

TITLE:
bug=Pixel Buds Pro 2 pair/connect on Windows 11, but playback remains on ThinkPad speakers.
attempt=3
result=BLOCKED_NOT_FIXED

CONTEXT:
pairing_clean_already_done=True, per user after second attempt.
known_previous_failure=First attempt installed routing script/tasks, but endpoint stayed phantom/unplugged; routing script exited 2.
known_previous_repair=Second attempt disabled routing tasks, removed stale pairing/device stack elevated, required physical pairing; after clean pairing issue persisted.
rule=Do not create more scripts/tasks unless a live active Buds render endpoint exists.

PRIVILEGES:
requirement=Verify actual Codex command runner privilege before destructive operations.
whoami=seste\daniele
windows_principal_admin=False
net_session_command=net session
net_session_exit_code=2
net_session_output=System error 5 has occurred. Access is denied.
current_process=pwsh.exe PID 21532 path C:\Program Files\WindowsApps\Microsoft.PowerShell_7.6.3.0_x64__8wekyb3d8bbwe\pwsh.exe start 2026-06-28 03:28:29 local
parent_runtime=Codex Desktop MSIX app; app resources codex.exe observed under C:\Program Files\WindowsApps\OpenAI.Codex_26.623.5546.0_x64__2p2nqsd0c76g0\app\resources\codex.exe
interpretation=Codex command runner not elevated.
safety_decision=Stopped before destructive device removal, driver reinstall, service reconfiguration, or pairing reset.

HOST_PROFILE:
computer=DANIELE_PC
bt_adapter=Qualcomm FastConnect 6900 Bluetooth Adapter
bt_adapter_hwid=USB\VID_10AB&PID_9309&REV_0001
bt_driver_provider=Qualcomm Atheros Communications
bt_driver_version=2.0.0.1326
bt_driver_date=2025-11-18
bt_driver_inf=oem125.inf
audio_internal=Realtek High Definition Audio
audio_internal_driver=6.0.9847.1, Realtek Semiconductor Corp., 2025-10-06, oem103.inf
audio_bt_stack=AMD Bluetooth Audio/LE Render/LE Capture driver 6.0.3.38, 2025-12-11, oem73.inf
amd_audio_device=AMD Audio Device driver 6.0.3.61, 2025-12-11, oem72.inf
apx_driver=Microsoft apxunit.inf 10.0.26100.8737, 2026-06-18

SYMPTOMS_OBSERVED:
observed=Bluetooth/PnP shows D's Pixel Buds Pro 2 present/OK.
observed=CoreAudio render endpoint for Buds exists only as Headphones state=8/unplugged.
observed=AudioEndpoint PnP entries for Headphones and Headset Pixel Buds are Status=Unknown Problem=CM_PROB_PHANTOM.
observed=Default Console and Multimedia remain Speakers.
observed=Default Communications remains 2 - SyncMaster.
observed=Windows audio cannot be routed to Buds because the render endpoint is not active.

SNAPSHOT_AUDIO_ENDPOINTS:
active_playback=Speakers (Realtek(R) Audio) OK; 2 - SyncMaster (AMD High Definition Audio Device) OK.
buds_playback=Headphones (2- D's Pixel Buds Pro 2) SWD\MMDEVAPI\{0.0.0.00000000}.{29D565D0-6EDF-47D6-ABB2-93AB893BC12D} Status=Unknown Problem=CM_PROB_PHANTOM state=8/unplugged.
buds_capture=Headset (D's Pixel Buds Pro 2) SWD\MMDEVAPI\{0.0.1.00000000}.{A9029857-F21A-4F7C-8BE8-B39F07F58160} Status=Unknown Problem=CM_PROB_PHANTOM.
default_console=Speakers {7352e93d-b994-4494-a4d7-66e08cbf6545}
default_multimedia=Speakers {7352e93d-b994-4494-a4d7-66e08cbf6545}
default_communications=2 - SyncMaster {98a82e04-2e8a-492a-9c1f-d756e5bf609f}

SNAPSHOT_PNP:
buds_bluetooth=D's Pixel Buds Pro 2 status=OK problem=CM_PROB_NONE.
buds_media=D's Pixel Buds Pro 2 status=OK problem=CM_PROB_NONE.
buds_audioendpoint=Headphones/Headset Pixel Buds status=Unknown problem=CM_PROB_PHANTOM.
reappeared_nodes=BTHLE/BTHENUM/APX Pixel Buds nodes exist after clean pairing; MMDEVAPI endpoints are still phantom.
meaning=Bluetooth/control plane and APX/media driver plane are present; Windows endpoint plane is not usable for playback.

SERVICES:
ApxSvc=Stopped Manual.
AudioEndpointBuilder=Running Automatic.
AudioSrv=Running Automatic.
bthserv=Running Manual.
DeviceAssociationService=Running Manual.
BTAGService=Running Manual.
BthAvctpSvc=Running Manual.
BluetoothUserService_11f663=Stopped Manual.
action=Read-only service status only; no restart attempted because runner is not elevated and destructive repair phase was blocked.

TASKS:
PixelBudsAudioRouteAtLogon=Disabled.
PixelBudsAudioRouteOnPnp=Disabled.
assessment=Correct to keep disabled while endpoint is phantom; enabling them would repeat a known exit-2 workaround failure.
changes_this_attempt=None.

EVENT_VIEWER:
range=last 24h filtered for BTHUSB, Bluetooth-User, Kernel-PnP, AudioEndpointBuilder, DeviceSetupManager, Windows Bluetooth logs.
raw_log=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T012830Z\events-last24h-filtered.txt
finding=No evidence that default-device selection is the primary failure; endpoint/PnP remains the blocking layer.

WINDOWS_UPDATE_LENOVO:
windows_update_driver_search=Only Lenovo System Driver Update 10.17.2606.1 for Fn/function keys offered; no Qualcomm/AMD/Realtek/Bluetooth/audio optional driver offered.
lenovo_vantage_installed=True.
lenovo_vantage_service=LenovoVantageService running.
lenovo_commercial_vantage=E046963F.LenovoSettingsforEnterprise_20.2603.19.0_x64__k1h2ywk1493x8.
lenovo_available_updates=Lenovo Intelligent Thermal Solution Driver 2.2.111.0 and AMD ACPBUS Driver 6.0.3.119 only.
lenovo_bt_catalog=Qualcomm Bluetooth Driver - 11 version 2.0.0.1326 present in Lenovo catalog/cache with status 3; installed adapter driver is already 2.0.0.1326.
lenovo_audio_catalog=Realtek Audio Driver version 6.0.9847.1 present in Lenovo catalog/cache with status 3; installed Realtek driver is already 6.0.9847.1.
interpretation=No direct Bluetooth/audio update was found locally via Windows Update or Lenovo Vantage cache. AMD ACPBUS is available and may be relevant to AMD audio bus stability, but installing it requires elevation/restore point and was not attempted.

DIAGNOSIS_CATEGORY:
primary=D_Phantom_unplugged
note=The user request also used an earlier A-G wording where phantom/unplugged was category C; this report uses the later explicit Phase-3 category list where D=Phantom/unplugged.
proof_command=C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 -StatusOnly
proof_output=RenderEndpoint name='Headphones' state=8 id='{0.0.0.00000000}.{29D565D0-6EDF-47D6-ABB2-93AB893BC12D}'; Headphones/Headset Pixel Buds PnP Problem=CM_PROB_PHANTOM.
not_A=No active stereo Buds render endpoint exists.
not_B=No active/default Buds endpoint exists.
not_C=Not only hands-free; both Headphones and Headset endpoints are phantom.
not_E=An endpoint exists, but it is phantom/unplugged rather than absent.
not_F=No evidence that mixer/per-app routing is the primary blocker because the endpoint itself is not active.
not_G_primary=Runtime privilege is a repair blocker, but the machine-state diagnosis is still endpoint phantom/unplugged.

ROOT_CAUSE_UPDATED:
most_likely=Windows creates/retains Pixel Buds Bluetooth/APX device nodes after pairing, but the MMDEVAPI audio endpoint activation fails, leaving the playback endpoint phantom/unplugged.
evidence=Bluetooth device and MEDIA nodes OK; APX driver present; AudioEndpoint Headphones/Headset Pixel Buds CM_PROB_PHANTOM; render endpoint state=8; defaults remain speakers/monitor.
probable_layer=Windows Bluetooth audio endpoint/APX/MMDEVAPI activation path, not simple output selection.
secondary_possibilities=AMD ACPBUS/audio bus update pending; Bluetooth LE Audio/APX service state; Buds firmware/cross-device issue; Lenovo/Windows driver runtime bug.
unknown=Whether AMD ACPBUS 6.0.3.119 fixes endpoint materialization; not tested because elevated restore-point-protected install was blocked.

COMMANDS_EXECUTED:
cmd=Get-Content C:\Users\seste\.codex\attachments\0efd19f2-1b3c-4b14-b377-109170b36f16\pasted-text.txt
cmd=Get-Content C:\Users\seste\Documents\MegaVault\ai\MEGAVAULT_PROTOCOL.md
cmd=Get-Content previous reports under C:\Users\seste\Documents\MegaVault\ai\reports
cmd=whoami
cmd=whoami /groups
cmd=whoami /priv
cmd=net session
cmd=Get-Process -Id $PID | Select Name,Id,Path,StartTime
cmd=WindowsPrincipal.IsInRole(Administrator)
cmd=Get-CimInstance Win32_Process filtered Codex/OpenAI and current process parentage
cmd=Get-ScheduledTask PixelBudsAudioRouteAtLogon,PixelBudsAudioRouteOnPnp
cmd=Get-Service ApxSvc,AudioEndpointBuilder,AudioSrv,bthserv,DeviceAssociationService,BTAGService,BthAvctpSvc,BluetoothUserService_*
cmd=Get-PnpDevice present/non-present filtered Pixel/Buds/Google/Bluetooth/BTH/BTHENUM/Audio/MMDEVAPI/APX
cmd=pnputil /enum-devices /connected and /disconnected
cmd=Get-CimInstance Win32_PnPSignedDriver filtered Bluetooth/audio/Qualcomm/AMD/Realtek/APX
cmd=Microsoft.Update.Session search for uninstalled drivers and all visible updates
cmd=registry read of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render/Capture
cmd=C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 -StatusOnly
cmd=Get-WinEvent filtered last 24h for BTHUSB/Bluetooth/User/Kernel-PnP/AudioEndpointBuilder/DeviceSetupManager
cmd=Read Lenovo Vantage app/package/service/install paths
cmd=Parse Lenovo SystemUpdateAddin session JSON/XML for available and Bluetooth/audio-relevant packages
cmd=git -C C:\Users\seste\Documents\MegaVault status --short --branch

FAILED_COMMANDS:
failure=net session
exit_code=2
message=System error 5 has occurred. Access is denied.
interpretation=Actual Codex command runner is not elevated; destructive repair commands must not run from this process.
failure=Select-String -Recurse during an initial Lenovo Vantage broad search
exit_code=1
message=A parameter cannot be found that matches parameter name 'Recurse'.
interpretation=PowerShell usage error only; no system modification. Corrected by using Get-ChildItem -Recurse -File | Select-String.
failure=Get-Content C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T012830Z\lenovo-systemupdate-search.txt
exit_code=1
message=Cannot find path because the file does not exist.
interpretation=Non-destructive log lookup mismatch; corrected data exists in lenovo-systemupdate-search-corrected.txt and lenovo-systemupdate-summary.txt.

CHANGES_APPLIED:
system_changes=None.
device_removal=None this attempt.
driver_changes=None.
service_changes=None.
script_or_task_created=None.
task_state_changed=None this attempt; previous tasks remain disabled.
logs_written=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T012830Z
report_written=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_third_attempt_20260628T012830Z.md

TESTS:
status_script=exit 0 StatusOnly; confirms Buds endpoint state=8/unplugged and defaults still Speakers/SyncMaster.
audio_test_real=NOT_RUN_NOT_MEANINGFUL from Codex because no active Buds render endpoint exists; Windows would still use Speakers.
disconnect_reconnect_test=NOT_RUN; destructive/repair phase blocked by non-elevated runner and user physical interaction required.
default_output_test=FAILED current state; Console/Multimedia remain Speakers.
speaker_not_used_test=FAILED/NOT_VERIFIABLE; no active Buds endpoint to carry sound.
final_success_criteria_met=False.

ROLLBACK:
this_attempt=No destructive system changes to roll back.
tasks_if_needed=Enable-ScheduledTask PixelBudsAudioRouteAtLogon; Enable-ScheduledTask PixelBudsAudioRouteOnPnp, but only after Buds audio works live.
previous_repair_restore=Use restore point from 2026-06-28T010049Z second attempt if prior elevated removal caused broader regression.
logs=Delete C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T012830Z if no longer needed.
report=Git revert this report commit if documentation must be removed.

TODO:
manual_required=Run repair phase from a genuinely elevated PowerShell/Codex-capable process or explicitly approve an elevated helper flow; create restore point first.
next_repair=For category D, remove only Buds-corrupted PnP/BTHENUM/APX/MMDEVAPI instances, restart audio/Bluetooth services, rescan PnP, then pair physically from case.
driver_escalation=Install Lenovo-offered AMD ACPBUS Driver 6.0.3.119 only with restore point/elevation if endpoint remains phantom after elevated device-stack cleanup; reboot if required.
manual_pairing=Buds in case, lid open, hold rear button until LED pulses, pair from Windows Bluetooth add-device UI.
manual_firmware=Verify Pixel Buds firmware from Pixel phone if Windows still creates phantom endpoints after Lenovo/elevated repair.
cross_test=Test Pixel Buds on phone/other PC and another Bluetooth headset on ThinkPad to distinguish Buds firmware issue vs ThinkPad/Windows Bluetooth endpoint stack.
post_success=Only after stereo endpoint is active, set Buds as default Console/Multimedia/Communications and consider re-enabling a lightweight routing task.

OUTCOME:
fixed=False.
blocked=True.
blocker=Codex command runner not elevated; destructive endpoint cleanup/driver repair intentionally not attempted.
effective_root_cause=Pixel Buds endpoint remains MMDEVAPI phantom/unplugged after clean pairing.
next_concrete_action=Use an elevated repair session with restore point to clean Buds/APX/MMDEVAPI instances again after the persisted post-pairing phantom state, then install Lenovo AMD ACPBUS update if endpoint activation still fails.
