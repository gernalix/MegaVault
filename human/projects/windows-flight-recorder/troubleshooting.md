# Windows Flight Recorder Troubleshooting

issue=Task Scheduler Access denied
check=Run systemlog doctor; status=inaccessible means current shell cannot inspect admin-created tasks; run doctor from elevated PowerShell.
workaround=Startup folder fallback launches logger/watchdog at user logon; fix_task_scheduler_admin.ps1 keeps fallback by default.

issue=systemlog watch appears idle
check=Run systemlog watch --debug --since-id 0 --limit 20; inspect db/table/last_id/current_max_id/rows_found/query.
workaround=Use systemlog probe logger/database/usb/session to verify live pipeline.

issue=No Security/session events
check=Run elevated; verify Security Event Log read permission.

issue=No temperature/SMART data
cause=Windows/firmware/driver may not expose sensors without vendor tools.
