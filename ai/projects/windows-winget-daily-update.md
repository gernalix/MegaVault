META:
name=Windows Winget Daily Update
slug=windows-winget-daily-update
path=C:\Users\seste\Documents\windows\maintenance
script=C:\Users\seste\Documents\windows\maintenance\winget_daily_update.ps1
task=Winget Daily Update
verified_at=2026-06-27T11:20:00+02:00
protocol=MEGAVAULT_PROTOCOL.md:v3
metadata=UNKNOWN_NOT_PRESENT

PURPOSE:
purpose=Daily Windows package source refresh and upgrade automation via winget
primary_output=timestamped_logs
operator=seste
scope=local_windows_maintenance

STACK:
os=Windows
shell=PowerShell 7 if available; Windows PowerShell fallback
pwsh_detected=7.6.3
package_manager=winget.exe
scheduler=Windows Task Scheduler
task_engine=C:\Program Files\WindowsApps\Microsoft.PowerShell_7.6.3.0_x64__8wekyb3d8bbwe\pwsh.exe

MAP:
entry=C:\Users\seste\Documents\windows\maintenance\winget_daily_update.ps1
ui=Task Scheduler MMC,PowerShell cmdlets
core=winget_daily_update.ps1
db=none
tests=PowerShell parse check via [scriptblock]::Create
scripts=winget_daily_update.ps1
avoid=deleting task/logs unless operator requests; editing unrelated MegaVault dirty files

ARCH:
component=Task Scheduler daily trigger -> pwsh.exe -> winget_daily_update.ps1
component=script creates logs dir beside itself
component=script resolves winget.exe from PATH or LOCALAPPDATA WindowsApps
component=Invoke-LoggedCommand wraps Start-Process with stdout/stderr redirection and timeout
boundary=Task registration controls schedule/runlevel/wake behavior
boundary=Script controls winget commands/logging/continuation semantics

FLOW:
flow=daily_03:00_when_available -> pwsh -NoProfile -ExecutionPolicy Bypass -File script
flow=script_start -> create logs dir -> open timestamped log
flow=winget source update -> log stdout/stderr -> continue on nonzero/timeout
flow=winget upgrade -> log stdout/stderr -> continue on nonzero/timeout
flow=winget upgrade --all --accept-package-agreements --accept-source-agreements -> log stdout/stderr -> continue on nonzero/timeout
flow=summary -> latest.log copy

INV:
arch=one script owns maintenance behavior
scheduler=StartWhenAvailable=True
scheduler=WakeToRun=False
scheduler=MultipleInstances=IgnoreNew
scheduler=ExecutionTimeLimit=PT2H
security=RunLevel=Limited currently; RunLevel=Highest denied from non-admin session on 2026-06-27
data=logs stored beside script in maintenance\logs
data=latest.log mirrors most recent run
backup=no backup/state DB; generated logs are operational evidence only
migration=no schema
version=script path stable unless task action updated
perf=per-command timeout=45m; task timeout=2h
ux=manual start via Start-ScheduledTask -TaskName 'Winget Daily Update'

BUILD:
cmd=none
env=Windows with winget.exe and PowerShell
requirements=winget.exe available to interactive user
create_task_cmd=Register-ScheduledTask -TaskName 'Winget Daily Update' -Action $Action -Trigger $Trigger -Settings $Settings -Principal $Principal -Description 'Daily winget source update and package upgrades. Logs are written next to the script.'
elevated_variant=rerun registration from admin PowerShell with New-ScheduledTaskPrincipal -RunLevel Highest

TEST:
parse=[scriptblock]::Create((Get-Content -LiteralPath script -Raw))
task_check=Get-ScheduledTask -TaskName 'Winget Daily Update'
manual_run=Start-ScheduledTask -TaskName 'Winget Daily Update'
log_read=Get-Content 'C:\Users\seste\Documents\windows\maintenance\logs\latest.log' -Tail 200
not_run_during_creation=manual task execution intentionally not performed to avoid unsolicited upgrades

DATA:
DB=none
Schema=none
Backup=none
Restore=none
Import=none
Export=none
Migration=none
Retention=UNKNOWN
Paths=C:\Users\seste\Documents\windows\maintenance\winget_daily_update.ps1; C:\Users\seste\Documents\windows\maintenance\logs

DNB:
dnb=do not set WakeToRun=True
dnb=do not stop entire script on single winget package failure
dnb=preserve stdout/stderr timestamped logs
dnb=preserve accept-package/source-agreement flags for upgrade --all
dnb=do not register duplicate task name
dnb=do not remove existing unrelated scheduled tasks

BUG:
issue=RunLevel Highest registration failed from current session
cause=Access is denied
workaround=run task registration from elevated PowerShell

RISK:
risk=winget upgrades may require admin rights for some packages; current task RunLevel=Limited
risk=winget may hang on installer prompts; timeout mitigates each command
risk=Task Scheduler interactive logon type runs only when user context is available
risk=latest.log overwritten each successful script completion

ROAD:
now=task registered daily at 03:00 with StartWhenAvailable and no wake
next=optionally re-register elevated from admin PowerShell
later=consider log retention cleanup once preferred retention period is known

LINK:
meta=UNKNOWN_NOT_PRESENT
human=../../human/projects/windows-winget-daily-update/overview.md
legacy=UNKNOWN
repo=../../../windows/maintenance
script=../../../windows/maintenance/winget_daily_update.ps1
logs=../../../windows/maintenance/logs

OPEN:
open=metadata file absent for this maintenance script
open=log retention policy unknown
open=whether user wants elevated task re-registration from admin shell
