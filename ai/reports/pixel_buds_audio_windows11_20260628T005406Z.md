# Pixel Buds Pro 2 Windows 11 audio routing bug

META:
created_utc=2026-06-28T00:54:06Z
host=DANIELE_PC
user=seste
pc=ThinkPad P14s Gen 5 AMD
os=Windows 11 Pro build 26200
shell=powershell_non_admin
protocol=MEGAVAULT_PROTOCOL.md VERSION=3
report_path=C:\Users\seste\Documents\MegaVault\ai\reports\pixel_buds_audio_windows11_20260628T005406Z.md

PURPOSE:
bug=Pixel Buds Pro 2 connected via Bluetooth but playback remains on ThinkPad speakers.
goal=root_cause+persistent_reversible_fix+regression_test.

HOST_PROFILE:
computer=DANIELE_PC
os=Microsoft Windows 11 Pro
build=26200
admin=False
bt_adapter=Qualcomm FastConnect 6900 Bluetooth Adapter driver 2.0.0.1326
audio_internal=Realtek High Definition Audio driver 6.0.9847.1
audio_bt=AMD Bluetooth Audio/LE Render/LE Capture driver 6.0.3.38
apx_driver=Microsoft apxunit.inf 10.0.26100.8737 observed in Kernel-PnP

SYMPTOMS:
observed=Windows/PnP shows D's Pixel Buds Pro 2 Bluetooth devices OK.
observed=Playback default remained Speakers for console+multimedia.
observed=Communications default remained 2 - SyncMaster.
observed=Pixel Buds render endpoint exists only as Headphones state=8/unplugged.
observed=Pixel Buds AudioEndpoint PnP status=Unknown problem=CM_PROB_PHANTOM.

DIAG:
playback_devices_active=2 - SyncMaster; Speakers (Realtek(R) Audio)
playback_devices_buds=Headphones (2- D's Pixel Buds Pro 2) phantom/unplugged
capture_devices_buds=Headset (D's Pixel Buds Pro 2) phantom
default_console=Speakers {7352e93d-b994-4494-a4d7-66e08cbf6545}
default_multimedia=Speakers {7352e93d-b994-4494-a4d7-66e08cbf6545}
default_communications=2 - SyncMaster {98a82e04-2e8a-492a-9c1f-d756e5bf609f}
services=bthserv,AudioSrv,AudioEndpointBuilder,DeviceAssociationService running
extra_services=BTAGService,BthAvctpSvc,BluetoothUserService running
apxsvc=Stopped; start blocked from non-admin shell
eventlog_7d_bluetooth_audio=no critical Bluetooth/audio errors matching Pixel Buds
eventlog_device_setup=2026-06-28T00:38Z APX/AudioEndpoint devices configured+started; removal failures 0xE000020B observed during prior device removal cycle
app_volume_policy=no PolicyConfig entries found referencing known endpoint GUIDs/Pixel/Buds/Speakers
app_volume_events=RealtekAudioControl volume changed to 0 on 2026-06-25 and 2026-06-22; not routing-relevant

ROOT_CAUSE:
most_likely=Bluetooth pairing/control plane is connected, but Windows audio endpoint plane is not active.
evidence=BT BTHENUM+BTHLE devices OK; APX MEDIA speaker/mic OK; MMDEVAPI audio endpoints phantom; render endpoint state=8/unplugged.
impact=CoreAudio cannot route default playback to Pixel Buds while endpoint is unplugged/phantom.
not_primary=default-device misselection alone; app-volume mixer lock; hands-free conflict.
uncertain=why endpoint remains unplugged: Buds not fully audio-connected/in-case, stale APX/MMDEVAPI state after failed removal, or Windows LE Audio/APX service/driver issue requiring elevated repair.

COMMANDS_EXECUTED:
cmd=Get-Content C:\Users\seste\Documents\MegaVault\ai\MEGAVAULT_PROTOCOL.md
cmd=Get-PnpDevice -Class AudioEndpoint/Bluetooth and Pixel/Buds filters
cmd=Get-Service bthserv,AudioSrv,AudioEndpointBuilder,DeviceAssociationService,BTAGService,BthAvctpSvc,ApxSvc,BluetoothUserService_*
cmd=Get-CimInstance Win32_PnPSignedDriver filtered Bluetooth/audio
cmd=Get-WinEvent System/Application/Bluetooth/Audio/Kernel-PnP/DeviceSetupManager last 7-30d
cmd=reg.exe export HKCU\...\Audio\PolicyConfig and HKLM\...\MMDevices\Audio
cmd=powershell -File C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1 -StatusOnly
cmd=powershell -File C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1
cmd=Register-ScheduledTask PixelBudsAudioRouteAtLogon
cmd=schtasks /Create PixelBudsAudioRouteOnPnp /SC ONEVENT /EC Microsoft-Windows-Kernel-PnP/Configuration /MO EventID=410

BACKUP:
registry_backup=C:\Users\seste\Documents\windows\backups\pixel-buds-audio-20260628T004945Z
exported=HKCU Audio PolicyConfig; HKLM MMDevices Audio; host profile
missing=HKCU Sound Mapper key absent; export failed harmlessly
restore_point=not_created; session non-admin and no destructive driver/device operation performed

CHANGES_APPLIED:
script_created=C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1
script_behavior=detect Pixel Buds PnP+MMDEVAPI endpoints; set default console/multimedia/communications only if active stereo/headphones endpoint exists; log every action; exit non-zero on failure
task_created=PixelBudsAudioRouteAtLogon
task_created=PixelBudsAudioRouteOnPnp
service_change_attempted=ApxSvc start and BTAGService/BthAvctpSvc restart attempted; blocked by non-admin access; no service state changed
handsfree_disabled=no; not justified because hands-free endpoint also phantom and disabling could remove mic without fixing missing stereo endpoint
device_removed=no; destructive/unpair action not performed without elevated snapshot/restore point and physical reconnection confirmation
driver_changed=no; no driver reinstall/update performed

TEST:
script_status=exit 0 StatusOnly; Buds Headphones endpoint state=8; defaults Speakers/SyncMaster
script_route=exit 2; no active stereo/headphones Pixel Buds render endpoint found; no silent failure
default_output_after=Console/Multimedia still Speakers because Buds endpoint unavailable
speakers_not_default_when_buds_connected=FAILED in current state; Buds Bluetooth connected but audio endpoint not active
audio_playback_test=not meaningful/currently would play through Speakers
disconnect_reconnect=not performed by script; no safe non-admin API available; manual Buds case/ear reconnect required for next validation
regression_hook=scheduled tasks will rerun routing at login and on Kernel-PnP device-start events

ROLLBACK:
remove_tasks=schtasks /Delete /TN PixelBudsAudioRouteAtLogon /F; schtasks /Delete /TN PixelBudsAudioRouteOnPnp /F
remove_script=delete C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1
remove_logs=delete %LOCALAPPDATA%\PixelBudsAudio\pixel-buds-audio.log
restore_registry=reg import files under C:\Users\seste\Documents\windows\backups\pixel-buds-audio-20260628T004945Z if needed
risk=script only changes CoreAudio default endpoint when Buds endpoint is active; no driver/device deletion

TODO:
manual=Take Pixel Buds out of case/in ears, ensure they are selected as connected for audio, then run C:\Users\seste\Documents\windows\maintenance\Set-PixelBudsAudio.ps1
manual=If endpoint remains state=8, open elevated PowerShell and restart AudioSrv, AudioEndpointBuilder, bthserv, BTAGService, BthAvctpSvc, BluetoothUserService_*, then rerun script
manual=If still phantom, create restore point, then remove/re-pair Pixel Buds from Windows Bluetooth settings; verify APX/MMDEVAPI endpoint becomes state=1
manual=If repair still fails, check Lenovo Vantage/Windows Update optional drivers for Qualcomm Bluetooth + AMD Bluetooth Audio/LE Audio + Realtek Audio Control failure
manual=Only consider disabling Hands-free Telephony if stereo endpoint becomes active but routing flips to headset mode

OUTCOME:
status=PARTIAL_FIX_DEPLOYED
fixed=Persistent non-destructive routing automation installed and tested for explicit failure/logging.
not_fixed=Current live audio cannot be moved to Pixel Buds because Windows reports no active Buds playback endpoint.
next_success_criterion=After physical/elevated reconnect, script sets Console+Multimedia+Communications default to Headphones Pixel Buds and playback no longer uses Speakers.
