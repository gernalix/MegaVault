[CmdletBinding()]
param(
    [string]$Serial,
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [int]$TimeoutSec = 240,
    [switch]$SkipUnlockAttempt,
    [switch]$NoExit
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$QaDir = Join-Path $ReportRoot "qa\device_ready_$Timestamp"
New-Item -ItemType Directory -Path $QaDir -Force | Out-Null
$SummaryPath = Join-Path $QaDir "device_ready_summary.txt"

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

function Invoke-Adb {
    param([string[]]$Args)
    if ($Serial) { & $Adb -s $Serial @Args } else { & $Adb @Args }
}

function Get-DeviceRows {
    $lines = & $Adb devices -l
    $lines | Where-Object { $_ -match "^\S+\s+\S+" -and $_ -notmatch "^List" } | ForEach-Object {
        $parts = $_ -split "\s+"
        [pscustomobject]@{ Serial = $parts[0]; State = $parts[1]; Raw = $_ }
    }
}

if (-not $Serial) {
    $deadline = (Get-Date).AddSeconds($TimeoutSec)
    do {
        $rows = Get-DeviceRows
        $candidate = $rows | Where-Object State -eq "device" | Select-Object -First 1
        if ($candidate) {
            $Serial = $candidate.Serial
            break
        }
        Start-Sleep -Seconds 2
    } while ((Get-Date) -lt $deadline)
}

if (-not $Serial) {
    "FAIL no online adb device found within $TimeoutSec sec" | Tee-Object -FilePath $SummaryPath
    & $Adb devices -l | Tee-Object -FilePath (Join-Path $QaDir "adb_devices.txt")
    $global:WaitAndroidDeviceReadyExitCode = 1
    if ($NoExit) { return }
    exit 1
}

& $Adb -s $Serial wait-for-device
$deadline = (Get-Date).AddSeconds($TimeoutSec)
$bootCompleted = ""
do {
    $bootCompleted = (& $Adb -s $Serial shell getprop sys.boot_completed 2>$null | Out-String).Trim()
    if ($bootCompleted -eq "1") { break }
    Start-Sleep -Seconds 2
} while ((Get-Date) -lt $deadline)

$state = (& $Adb -s $Serial get-state 2>$null | Out-String).Trim()
$props = [ordered]@{
    serial         = $Serial
    state          = $state
    boot_completed = $bootCompleted
    model          = ((& $Adb -s $Serial shell getprop ro.product.model 2>$null) -join "").Trim()
    sdk            = ((& $Adb -s $Serial shell getprop ro.build.version.sdk 2>$null) -join "").Trim()
    release        = ((& $Adb -s $Serial shell getprop ro.build.version.release 2>$null) -join "").Trim()
}

$windowBefore = (& $Adb -s $Serial shell dumpsys window 2>$null | Out-String)
$keyguardPattern = "mDreamingLockscreen=true|mShowingLockscreen=true|isStatusBarKeyguard=true|mInputRestricted=true|isKeyguardShowing=true"
$keyguardBefore = $windowBefore -match $keyguardPattern

if (-not $SkipUnlockAttempt) {
    & $Adb -s $Serial shell input keyevent KEYCODE_WAKEUP | Out-Null
    & $Adb -s $Serial shell wm dismiss-keyguard | Out-Null
    & $Adb -s $Serial shell cmd statusbar collapse | Out-Null
    Start-Sleep -Milliseconds 700
    & $Adb -s $Serial shell input swipe 500 1800 500 300 250 | Out-Null
    Start-Sleep -Seconds 1
}

$uiPath = Join-Path $QaDir "ui.xml"
& $Adb -s $Serial exec-out uiautomator dump /dev/tty > $uiPath
$uiText = Get-Content -LiteralPath $uiPath -Raw -ErrorAction SilentlyContinue
$windowAfter = (& $Adb -s $Serial shell dumpsys window 2>$null | Out-String)
$keyguardAfter = $windowAfter -match $keyguardPattern
$pinRequired = $uiText -match "(?i)(enter pin|pin|password|pattern|unlock for all features|use fingerprint)"

$screenshotPath = Join-Path $QaDir "screen.png"
$adbForCmd = $Adb.Replace('"', '""')
$serialForCmd = $Serial.Replace('"', '""')
$screenForCmd = $screenshotPath.Replace('"', '""')
cmd /c "`"$adbForCmd`" -s `"$serialForCmd`" exec-out screencap -p > `"$screenForCmd`""

& $Adb -s $Serial logcat -d -t 400 > (Join-Path $QaDir "logcat_tail.txt")
& $Adb devices -l > (Join-Path $QaDir "adb_devices.txt")

$status = "PASS"
$message = "Device ready"
if ($bootCompleted -ne "1") {
    $status = "FAIL"
    $message = "Boot did not complete within timeout"
} elseif ($keyguardAfter -and $pinRequired) {
    $status = "WARN"
    $message = "manual unlock required"
} elseif ($keyguardAfter) {
    $status = "WARN"
    $message = "Keyguard may still be visible"
}

$summary = @(
    "status=$status",
    "message=$message",
    "serial=$Serial",
    "state=$state",
    "boot_completed=$bootCompleted",
    "keyguard_before=$keyguardBefore",
    "keyguard_after=$keyguardAfter",
    "pin_required=$pinRequired",
    "qa_dir=$QaDir",
    "model=$($props.model)",
    "sdk=$($props.sdk)",
    "release=$($props.release)"
)
$summary | Tee-Object -FilePath $SummaryPath

if ($Serial -match "adb-.*_adb-tls-connect\._tcp" -and (($props.model -match "Pixel 8a") -or ($props.model -match "Pixel_8a"))) {
    "policy_note=physical Pixel detected; do not use this serial for tests unless policy explicitly changes" | Add-Content -LiteralPath $SummaryPath -Encoding UTF8
}

$code = if ($status -eq "FAIL") { 1 } elseif ($status -eq "WARN") { 2 } else { 0 }
$global:WaitAndroidDeviceReadyExitCode = $code
if ($NoExit) { return }
exit $code
