# Windows Flight Recorder Troubleshooting

issue=Task Scheduler Access denied
check=Run systemlog doctor; inspect AUDIT_REPORT.md; run fix_task_scheduler_admin.ps1 from elevated PowerShell.
workaround=Startup folder fallback launches logger/watchdog at user logon.

issue=No Security/session events
check=Run elevated; verify Security Event Log read permission.

issue=No temperature/SMART data
cause=Windows/firmware/driver may not expose sensors without vendor tools.
