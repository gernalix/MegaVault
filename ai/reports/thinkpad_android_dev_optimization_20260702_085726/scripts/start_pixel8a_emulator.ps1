[CmdletBinding()]
param(
    [string]$AvdName = "Pixel_8a",
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [int]$TimeoutSec = 360,
    [switch]$NoWait,
    [switch]$VisibleWindow,
    [switch]$NoExit
)

$ErrorActionPreference = "Stop"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$StdOut = Join-Path $LogDir "emulator_${AvdName}_stdout_$Timestamp.log"
$StdErr = Join-Path $LogDir "emulator_${AvdName}_stderr_$Timestamp.log"

function Find-Emulator {
    $cmd = Get-Command emulator -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    if ($env:ANDROID_HOME) {
        $candidate = Join-Path $env:ANDROID_HOME "emulator\emulator.exe"
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    throw "emulator not found. Check ANDROID_HOME and PATH."
}

$emulator = Find-Emulator
$avds = & $emulator -list-avds
if ($avds -notcontains $AvdName) {
    throw "AVD '$AvdName' not found. Available AVDs: $($avds -join ', ')"
}

$existing = (& adb devices | Select-String "^emulator-\d+\s+device").Line
if ($existing) {
    Write-Output "An emulator is already online: $existing"
    if (-not $NoWait) {
        $existingSerial = ($existing -split "\s+")[0]
        $global:StartPixel8aEmulatorSerial = $existingSerial
        & (Join-Path $PSScriptRoot "wait_android_device_ready.ps1") -Serial $existingSerial -TimeoutSec $TimeoutSec -ReportRoot $ReportRoot -NoExit
        $global:StartPixel8aEmulatorExitCode = $global:WaitAndroidDeviceReadyExitCode
        if ($NoExit) { return }
        exit $global:StartPixel8aEmulatorExitCode
    }
    return
}

$args = @(
    "-avd", $AvdName,
    "-no-snapshot-load",
    "-no-snapshot-save",
    "-no-boot-anim",
    "-gpu", "swiftshader_indirect"
)
if (-not $VisibleWindow) { $args += "-no-window" }

$startParams = @{
    FilePath               = $emulator
    ArgumentList           = $args
    RedirectStandardOutput = $StdOut
    RedirectStandardError  = $StdErr
    PassThru               = $true
}
if (-not $VisibleWindow) { $startParams.WindowStyle = "Hidden" }

$process = Start-Process @startParams
$global:StartPixel8aEmulatorProcessId = $process.Id
Write-Output "Started emulator '$AvdName' PID=$($process.Id)"
Write-Output "stdout=$StdOut"
Write-Output "stderr=$StdErr"

if (-not $NoWait) {
    $deadline = (Get-Date).AddSeconds([Math]::Min($TimeoutSec, 90))
    $emulatorSerial = $null
    do {
        $line = (& adb devices | Select-String "^emulator-\d+\s+").Line | Select-Object -First 1
        if ($line) {
            $emulatorSerial = ($line -split "\s+")[0]
            break
        }
        Start-Sleep -Seconds 2
    } while ((Get-Date) -lt $deadline)

    if (-not $emulatorSerial) {
        throw "Started emulator process PID=$($process.Id), but no emulator-* adb serial appeared within 90 seconds. See $StdErr"
    }

    Write-Output "Detected emulator serial: $emulatorSerial"
    $global:StartPixel8aEmulatorSerial = $emulatorSerial
    & (Join-Path $PSScriptRoot "wait_android_device_ready.ps1") -Serial $emulatorSerial -TimeoutSec $TimeoutSec -ReportRoot $ReportRoot -NoExit
    $global:StartPixel8aEmulatorExitCode = $global:WaitAndroidDeviceReadyExitCode
    if ($NoExit) { return }
    exit $global:StartPixel8aEmulatorExitCode
}
