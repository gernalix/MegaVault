[CmdletBinding()]
param(
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$AsJson
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$CsvPath = Join-Path $LogDir "android_device_matrix_$Timestamp.csv"
$JsonPath = Join-Path $LogDir "android_device_matrix_$Timestamp.json"

function Find-Adb {
    $cmd = Get-Command adb -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    if ($env:ANDROID_HOME) {
        $candidate = Join-Path $env:ANDROID_HOME "platform-tools\adb.exe"
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    throw "adb not found. Check ANDROID_HOME and PATH."
}

$Adb = Find-Adb
$rows = @()
$lines = & $Adb devices -l
foreach ($line in $lines) {
    if ($line -notmatch "^(\S+)\s+(\S+)(.*)$" -or $line -match "^List") { continue }
    $serial = $Matches[1]
    $state = $Matches[2]
    $details = $Matches[3]
    $row = [ordered]@{
        Serial        = $serial
        State         = $state
        Details       = $details.Trim()
        Model         = ""
        Manufacturer  = ""
        Android       = ""
        Sdk           = ""
        BootCompleted = ""
        Battery       = ""
        Keyguard      = ""
        TransportId   = ""
    }
    if ($details -match "transport_id:(\S+)") { $row.TransportId = $Matches[1] }
    if ($state -eq "device") {
        $row.Model = ((& $Adb -s $serial shell getprop ro.product.model 2>$null) -join "").Trim()
        $row.Manufacturer = ((& $Adb -s $serial shell getprop ro.product.manufacturer 2>$null) -join "").Trim()
        $row.Android = ((& $Adb -s $serial shell getprop ro.build.version.release 2>$null) -join "").Trim()
        $row.Sdk = ((& $Adb -s $serial shell getprop ro.build.version.sdk 2>$null) -join "").Trim()
        $row.BootCompleted = ((& $Adb -s $serial shell getprop sys.boot_completed 2>$null) -join "").Trim()
        $battery = (& $Adb -s $serial shell dumpsys battery 2>$null | Select-String "level|status" | ForEach-Object { $_.Line.Trim() }) -join "; "
        $row.Battery = $battery
        $window = (& $Adb -s $serial shell dumpsys window 2>$null | Out-String)
        $row.Keyguard = if ($window -match "mDreamingLockscreen=true|mShowingLockscreen=true|isStatusBarKeyguard=true|mInputRestricted=true|isKeyguardShowing=true") { "maybe_locked" } else { "not_detected" }
    }
    $rows += [pscustomobject]$row
}

$rows | Export-Csv -LiteralPath $CsvPath -NoTypeInformation -Encoding UTF8
$rows | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $JsonPath -Encoding UTF8

if ($AsJson) {
    $rows | ConvertTo-Json -Depth 4
} else {
    $rows | Format-Table -AutoSize
    "CSV=$CsvPath"
    "JSON=$JsonPath"
}
