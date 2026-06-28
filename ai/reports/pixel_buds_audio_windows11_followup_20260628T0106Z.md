# Pixel Buds Pro 2 Windows 11 audio routing follow-up

META:
created_utc=2026-06-28T01:06:00Z
host=DANIELE_PC
user=seste
protocol=MEGAVAULT_PROTOCOL.md VERSION=3
previous_report=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_20260628T005406Z.md
followup_report=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_followup_20260628T0106Z.md
branch=codex/pixel-buds-windows-audio

PURPOSE:
bug=Pixel Buds Pro 2 Bluetooth connected but audio remains on ThinkPad speakers.
goal=remove stale pairing+phantom endpoints; force clean re-pair before default routing.

PREVIOUS_ATTEMPT_FAILED:
reason=Set-PixelBudsAudio.ps1 could only set default endpoint after a valid render endpoint existed.
evidence=script exited 2 because Headphones Pixel Buds endpoint was CM_PROB_PHANTOM/state=8.
action=PixelBudsAudioRouteAtLogon and PixelBudsAudioRouteOnPnp disabled; tasks were noisy/useless while endpoint phantom.

DIAG_CURRENT:
admin_initial=False
admin_repair=True via UAC elevated PowerShell
bt_device_before=D's Pixel Buds Pro 2 BTHENUM+BTHLE OK; many BTHLE services OK
audio_before=APX speaker/microphone OK; MMDEVAPI Headphones/Headset Pixel Buds phantom
services_before=ApxSvc stopped; AudioSrv/AudioEndpointBuilder/bthserv/BTAGService/BthAvctpSvc/DeviceAssociationService running
windows_update_optional=No Qualcomm/AMD/Realtek/Bluetooth/audio optional driver offered; only Lenovo Fn/function keys driver 10.17.2606.1
event_bthusb=paired/unpaired events for remote 10:d9:a2:4f:07:df
event_issue=DeviceSetupManager had prior APX/MMDEVAPI removal failures 0xE000020B before this follow-up

BACKUP:
restore_point=created by elevated script
registry_backup=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T010049Z\registry
run_log=C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T010049Z
exports=HKLM MMDevices Audio; HKCU Audio PolicyConfig; HKLM BTHPORT Parameters Devices

COMMANDS_EXECUTED:
cmd=Disable-ScheduledTask PixelBudsAudioRouteAtLogon
cmd=Disable-ScheduledTask PixelBudsAudioRouteOnPnp
cmd=Get-PnpDevice filtered Pixel/Buds/APX/MMDEVAPI
cmd=Get-Service bthserv,AudioSrv,AudioEndpointBuilder,DeviceAssociationService,BTAGService,BthAvctpSvc,ApxSvc,BluetoothUserService_*
cmd=Get-CimInstance Win32_PnPSignedDriver Bluetooth/audio
cmd=Microsoft.Update.Session search IsInstalled=0 Type=Driver
cmd=Get-WinEvent System,Kernel-PnP,DeviceSetupManager,Audio,Bluetooth logs
cmd=Start-Process powershell -Verb RunAs -File Repair-PixelBudsAudioElevated.ps1
cmd=pnputil /remove-device <Pixel Buds/APX/MMDEVAPI/BTHLE/BTHENUM instance> /force
cmd=BluetoothAPIs.dll BluetoothRemoveDevice(10D9A24F07DF)

CHANGES_APPLIED:
task=PixelBudsAudioRouteAtLogon disabled
task=PixelBudsAudioRouteOnPnp disabled
script_created=C:\Users\seste\Documents\windows\maintenance\Repair-PixelBudsAudioElevated.ps1
device_removal=28 Pixel Buds related PnP instances removed successfully via pnputil elevated
removed_instances=BTHENUM root, BTHLE root, BTHLE GATT services, BTHENUM app/control services, HID, APX speaker/microphone, SWD APX unit, MMDEVAPI Headphones/Headset
services=BTAGService,BthAvctpSvc,bthserv,AudioSrv,AudioEndpointBuilder,DeviceAssociationService stopped/restarted elevated
scan=pnputil /scan-devices exit 0
pairing=BluetoothRemoveDevice returned 0; BTHUSB event ID 10 confirmed link key removed
driver_update=no driver update/reinstall performed; not indicated by Windows Update diagnostics

STATE_AFTER:
pairing_removed=True
event=2026-06-28 03:02:09 local BTHUSB: remote adapter 10:d9:a2:4f:07:df no longer paired; link key removed
phantom_mmdevapi_old=removed: C8E7E8CF/A29879CB no longer appear in PnP AudioEndpoint
audioendpoint_after=only SyncMaster, Microphone Array, Speakers active in PnP AudioEndpoint
buds_after=BTHLE/APX nodes reappeared because Buds are nearby/advertising, but no Windows playback endpoint exists yet
registry_after=generic Headphones state=8 remains; not mapped to active Pixel Buds PnP endpoint; not usable as playback target
default_after=Speakers for console/multimedia; SyncMaster for communications

ROOT_CAUSE_UPDATED:
cause=stale/incomplete Bluetooth pairing and APX/MMDEVAPI endpoint state caused Windows to keep only phantom playback endpoints.
evidence=pnputil removal succeeded; BluetoothRemoveDevice confirmed link key removal; old Pixel Buds MMDEVAPI endpoints disappeared.
remaining=clean physical pairing not yet completed, so Windows has not created a valid active stereo playback endpoint.
not_caused_by=app mixer override; Windows Update missing Bluetooth/audio driver; simple default-device selection.

TEST:
task_state=Disabled/Disabled
remove_test=pnputil removal exit 0 for all target instances
unpair_test=BluetoothRemoveDeviceResult=0; BTHUSB link-key removed event observed
endpoint_test_after=no Pixel Buds MMDEVAPI phantom endpoints remain in PnP
pairing_test=BLOCKED_MANUAL: requires Buds in case pairing mode and Windows Bluetooth add-device flow
audio_test=NOT_RUN: no active Buds playback endpoint after unpair; test would still use Speakers
reconnect_test=NOT_RUN: waiting for clean pairing

ROLLBACK:
system_restore=Use restore point "Before Pixel Buds Pro 2 Bluetooth audio repair 20260628T010049Z" if device stack repair causes regression.
registry_restore=reg import backups under C:\Users\seste\Documents\windows\logs\pixel-buds-repair\20260628T010049Z\registry
tasks_reenable=Enable-ScheduledTask PixelBudsAudioRouteAtLogon; Enable-ScheduledTask PixelBudsAudioRouteOnPnp
scripts=Repair script and Set script are files only; delete if no longer wanted.

NEXT_REQUIRED:
manual=Put Pixel Buds Pro 2 in real pairing mode from case: buds in case, lid open, hold rear button until LED pulses.
manual=Pair from Windows Add device/Bluetooth wizard opened during session.
then=Run C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 -StatusOnly
success=PnP AudioEndpoint shows Headphones Pixel Buds OK and render endpoint state=1.
then=Run C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 to set console/multimedia/communications defaults.
then=Run Windows audio test; verify speakers not default; disconnect/reconnect and repeat.
if_pairing_only_apx_no_mmdevapi=try reboot, then pair again; if still no endpoint, use Lenovo Vantage/Lenovo support for Qualcomm Bluetooth + AMD Bluetooth LE Audio stack; verify Pixel Buds firmware on Pixel phone.

OUTCOME:
status=PARTIAL_REAL_REPAIR_BLOCKED_ON_MANUAL_PAIRING
fixed=stale pairing key removed; old phantom MMDEVAPI endpoints removed; previous failing tasks disabled.
not_yet_fixed=no active Pixel Buds playback endpoint until clean pairing is completed.
