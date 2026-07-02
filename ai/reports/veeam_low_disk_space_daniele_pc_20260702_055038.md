# Veeam low disk space diagnostic - Job daniele_pc

Generated: 2026-07-02 05.50.38 +02:00
Host: Windows 11 ThinkPad, `daniele_pc`
Scope: no backup files deleted, no formatting, no retention change, no job target change, no manual Backup Now started by Codex.

## Executive summary

Root cause probable: the warning was produced when Veeam used or evaluated `D:\VeeamBackup` on the Seagate Expansion USB drive, which had very little free space relative to its size. The intended target, Samsung T7, reappeared as `F:` after reconnect and had ample free space. After reconnect, Veeam resynchronized the rotated-drive repository to `F:\VeeamBackup\` and the latest automatic run completed successfully without a low-space warning.

Important distinction: C: being only about 154 GB used is not contradictory. The warning text refers to free space on the backup target, not the protected source volume.

## Current and observed volumes

Before T7 reconnect, Windows saw only the internal NVMe and Seagate USB. After reconnect, the T7 appeared as:

| Drive | Label | Device | Filesystem | Size | Free |
|---|---|---|---|---:|---:|
| C: | Windows | KXG8AZNV1T02 LA KIOXIA NVMe | NTFS | 1021.62 GB | 867.58 GB |
| D: | Seagate Expansion Drive | Seagate Expansion USB | NTFS | 3833.27 GB | 80.75 GB |
| E: | blank label | partition on Seagate USB | NTFS | 167.38 GB | 125.05 GB |
| F: | T7 Backup | Samsung PSSD T7 Shield USB | NTFS | 1000.19 GB | 903.57 GB before latest run |

After the automatic verification run completed, Windows no longer showed the T7 as mounted. This is expected because Veeam is configured to automatically disconnect/eject the target disk after backup completion. Veeam's DB recorded the T7 repository with about 888.49 GB free after the run.

## Veeam job configuration found

Sources used: `C:\ProgramData\Veeam\EndpointData\VeeamBackup.db` opened read-only, plus logs under `C:\ProgramData\Veeam\Endpoint\Job_daniele_pc\`.

| Field | Value |
|---|---|
| Job ID | `127388b7-49b5-45af-a71b-06c6cce0fdeb` |
| Job name in DB | `Job daniele_pc` |
| Repository ID | `4fda11a9-a3b6-498b-aedd-d74b57d05513` |
| Repository name | `Local folder` |
| Repository path | `F:\VeeamBackup\` |
| Rotated drive mode | enabled (`on_rotated_drive=1`) |
| Current rotated drive after reconnect | `T7 Backup (F:)`, Samsung PSSD T7 Shield |
| Other known rotated drive | `D:\`, Seagate Expansion SCSI Disk Device, not current |
| Backup source mode | `BackupMode=0`, `BackupAllUsbDrives=False`, explicit `Drives` empty |
| Source observed in logs | Disk 0 internal NVMe, including EFI/C:/WinRE; not D/E/F as source |
| Retention | days, `RetainDaysToKeep=30` |
| Compression | level `5` |
| Encryption | disabled (`StorageEncryptionEnabled=False`) |
| Active full | disabled (`EnableFullBackup=False`) |
| Synthetic full/transform | disabled (`TransformFullToSyntethic=False`) |
| Compact full | disabled (`EnableCompactFull=False`) |
| Health check/recheck | enabled monthly schedule (`EnableRecheck=True`) |

The official CLI export was attempted but failed without elevation/service permission:

```text
Veeam.Agent.Configurator.exe -export /f:<temp xml>
ExitCode: 1
Failed to send the request to Veeam Backup Service.
StatusCode=PermissionDenied / HTTP 403
```

Therefore the configuration above was reconstructed from DB + logs, without writing Veeam config.

## Backup chains and target usage

`F:\VeeamBackup\Job daniele_pc` on T7 before the latest automatic incremental contained:

| File | Type | Size |
|---|---:|---:|
| `Job daniele_pc2026-06-27T101818.vbk` | full | 85.36 GB |
| `Job daniele_pc2026-06-27T111734.vib` | incremental | 3.83 GB |
| `Job daniele_pc2026-06-29T143908.vib` | incremental | 7.24 GB |
| `Job daniele_pc.vbm` | metadata | about 0.11 MB |

Total T7 chain before latest run: about 96.43 GB. Latest automatic incremental on `F:` at `2026-07-02 05:45` added about 15.08 GB and completed successfully, so post-run chain is approximately 111.51 GB.

`D:\VeeamBackup` on Seagate contains two full backup sets and associated metadata:

| Folder/file | Size |
|---|---:|
| `D:\VeeamBackup\Job daniele_pc.adhoc.2026-07-01T222309\Job daniele_pc.adhoc.2026-07-01T222310.vbk` | 77.47 GB |
| `D:\VeeamBackup\Job daniele_pc\Job daniele_pc2026-07-02T003017.vbk` | 77.37 GB |
| two `.vbm` metadata files | negligible |

Total Veeam backup files on D: measured: about 154.84 GB. These may be valid recovery points / standalone fulls and were not deleted.

## Relevant log and DB evidence

Exact warning records from `Backup.Model.BackupJobSessionsView`:

```text
2026-07-01 22:23:04 - result=Warning
Backup location [D:\VeeamBackup] is getting low on free disk space (141,8 GB free of 3,5 TB)

2026-07-02 00:30:00 - result=Warning
Backup location [D:\VeeamBackup\] is getting low on free disk space (75,2 GB free of 3,5 TB)
```

Latest run after T7 reconnect:

```text
2026-07-02 05:45:01 - result=Success
Target repository: F:\VeeamBackup\
Reason/warning: null
Backed up size: 15.08 GB
Read size: 38.34 GB
Total used source size: 154.83 GB
```

Log path transitions observed:

```text
2026-06-27: Target.CurrentLink ... @F:\VeeamBackup\Job daniele_pc\Job daniele_pc2026-06-27T101818.vbk
2026-07-01: Target.CurrentLink ... @D:\VeeamBackup\Job daniele_pc.adhoc.2026-07-01T222309\...
2026-07-02 00:30: Target.CurrentLink ... @D:\VeeamBackup\Job daniele_pc\Job daniele_pc2026-07-02T003017.vbk
2026-07-02 05:45 after reconnect: Target.CurrentLink ... @F:\VeeamBackup\Job daniele_pc\Job daniele_pc2026-07-02T054517.vib
```

Event Viewer/Application only showed VSS snapshot activity and Veeam service lifecycle entries; no separate low-space event was needed for root cause.

## Comparison and interpretation

| Item | Measurement | Interpretation |
|---|---:|---|
| C: used | about 154.04 GB current | Source is modest; warning is not about source C:. |
| Source used size in latest successful session | about 154.83 GB | Matches internal OS volumes, not USB drives. |
| T7 free before run | about 903.57 GB | Plenty of space for current chain and incrementals. |
| T7 chain before latest run | about 96.43 GB | Expected scale for about 154 GB used source. |
| T7 chain after latest run | about 111.51 GB | Still leaves large margin. |
| D: free | about 80.75 GB / 3833.27 GB | Very low percentage; Veeam warning is justified for D:. |
| D: Veeam backup files | about 154.84 GB | Old/duplicate fulls exist; not deleted. |
| Retention | 30 days | Not immediately wrong; retention alone is not the warning root cause. |
| Synthetic/compact | disabled | Extra transform/compact space is unlikely to be the trigger. |

## Diagnosis

Most likely root cause: Veeam's rotated-drive repository contains both the intended Samsung T7 and the Seagate D: as known repository volumes. When the T7 was unavailable, Veeam either used or evaluated the Seagate path `D:\VeeamBackup`; because D: had only 75.2 GB-class free space out of about 3.5 TiB, Veeam correctly raised the warning.

Not supported by evidence:

- T7 genuinely low on space: no, it had about 903.57 GB free before the latest run.
- C: too large: no, C/source used size is about 154 GB.
- Job includes Seagate/T7 as protected source: no, logs and disk filter show internal Disk 0/OS volumes, with `BackupAllUsbDrives=False`.
- Synthetic/merge/compact extra space: unlikely, these features are disabled for this job.
- Warning stale only: partly. The warning was real for D: on prior runs; latest run on T7 succeeded, so UI/tray should clear after refresh if it tracks latest session.

## Fix applied / not applied

Applied:

- No destructive changes.
- T7 was disconnected/reconnected by user; after reconnect Veeam detected `T7 Backup (F:)` as current rotated drive.
- Veeam automatically refreshed/synchronized metadata and ran an incremental on `F:\VeeamBackup\`; it completed successfully with no low-space warning.
- Veeam then automatically disconnected/ejected the T7 according to the enabled setting.

Not applied:

- Did not delete D: backup sets.
- Did not delete T7 chain files.
- Did not format disks.
- Did not change retention.
- Did not change job target.
- Did not manually start Backup Now.
- Did not edit Veeam SQLite DB or registry.
- Did not remove the Seagate from Veeam's rotated-drive list, because that is a configuration change and should be confirmed/handled through Veeam UI or supported CLI.

## Recommended next steps

1. In Veeam UI, review the local repository / rotated drive settings and remove/forget the Seagate D: from the rotated media set if the Seagate should never be a backup target.
2. Do not delete `D:\VeeamBackup` until you decide whether those two full backups are useful recovery points. If safe to remove later, prefer Veeam-aware cleanup/import state where possible, not ad hoc deletion.
3. Keep the T7 available before scheduled backup windows. The post-backup auto-disconnect is fine, but the disk must be reconnected before the next run.
4. Consider assigning a stable drive letter to the T7 if it ever appears with a different letter, but only after confirming no other workflows depend on `F:`.
5. If the tray still shows the old warning while the latest session is success, refresh/reopen the Veeam UI; if still stale, inspect `Backup.Model.BackupJobSessionsView` latest row and `C:\ProgramData\Veeam\Endpoint\Job_daniele_pc\Job.Job_daniele_pc.Backup.log` again.

## Commands executed

Representative commands used in read-only mode:

```powershell
Get-Service | Where-Object { $_.Name -like '*Veeam*' -or $_.DisplayName -like '*Veeam*' }
Get-Volume | Select DriveLetter,FileSystemLabel,FileSystem,DriveType,HealthStatus,SizeRemaining,Size
Get-Disk | Select Number,FriendlyName,SerialNumber,BusType,PartitionStyle,OperationalStatus,HealthStatus,Size
Get-Partition | Select DiskNumber,PartitionNumber,DriveLetter,Type,Size
Get-ChildItem 'C:\ProgramData\Veeam\Endpoint','C:\ProgramData\Veeam\Backup' -Recurse -File
Select-String -Path 'C:\ProgramData\Veeam\Endpoint\Job_daniele_pc\*' -Pattern 'low on free disk space|Target.CurrentLink|retention|compact|health|D:\\|F:\\'
Get-WinEvent -FilterHashtable @{LogName='Application'; StartTime=(Get-Date).AddDays(-14)}
Veeam.Agent.Configurator.exe -export /f:<temp xml>   # failed with PermissionDenied/403
python sqlite3 read-only queries against C:\ProgramData\Veeam\EndpointData\VeeamBackup.db
Get-ChildItem D:\VeeamBackup -Recurse -File
Get-ChildItem F:\VeeamBackup -Recurse -File
```
