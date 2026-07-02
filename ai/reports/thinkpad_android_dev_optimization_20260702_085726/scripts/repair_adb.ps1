[CmdletBinding()]
param(
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$WirelessHost,
    [int]$WirelessPort = 5555,
    [switch]$ReconnectUsb
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogPath = Join-Path $LogDir "repair_adb_$Timestamp.txt"

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

& {
    "Timestamp=$(Get-Date -Format o)"
    "adb=$Adb"
    & $Adb version
    "Before:"
    & $Adb devices -l
    "Killing adb server..."
    & $Adb kill-server
    Start-Sleep -Seconds 1
    "Starting adb server..."
    & $Adb start-server
    "mDNS services after start-server:"
    & $Adb mdns services
    if ($ReconnectUsb) {
        "adb reconnect offline/device:"
        & $Adb reconnect
    }
    if ($WirelessHost) {
        "Connecting wireless adb: ${WirelessHost}:$WirelessPort"
        & $Adb connect "${WirelessHost}:$WirelessPort"
    }
    "Waiting briefly for USB/wireless devices to reappear..."
    $devices = @()
    foreach ($i in 1..8) {
        $devices = & $Adb devices -l
        if ($devices -match "\sdevice\s") { break }
        Start-Sleep -Seconds 2
    }
    "After:"
    $devices
    "mDNS services final:"
    & $Adb mdns services
    if ($devices -match "unauthorized") {
        "WARN unauthorized device: unlock phone, accept RSA fingerprint, then re-run."
    }
    if ($devices -match "offline") {
        "WARN offline device: try cable reconnect, adb reconnect, or disable/re-enable wireless debugging."
    }
    if ($devices -notmatch "\sdevice\s") {
        "WARN no ready device. For wireless debugging, pair/connect from Developer options or pass -WirelessHost."
    }
} | Tee-Object -FilePath $LogPath

"Wrote $LogPath"
