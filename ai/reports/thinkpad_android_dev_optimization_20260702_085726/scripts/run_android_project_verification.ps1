[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$Module = "app",
    [string]$UseEmulator,
    [switch]$RunLint,
    [switch]$RunUnitTests,
    [switch]$RunConnectedTests,
    [switch]$InstallAndLaunch,
    [string]$PackageName,
    [switch]$FixLocalProperties,
    [switch]$KillStartedEmulator,
    [ValidateSet("EmulatorOrTcl", "EmulatorOnly", "TclOnly", "All")]
    [string]$DevicePolicy = "EmulatorOrTcl"
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$VerificationStartTime = Get-Date
$ProjectFull = [IO.Path]::GetFullPath($ProjectPath)
if (-not (Test-Path -LiteralPath $ProjectFull)) { throw "ProjectPath not found: $ProjectFull" }

$ProjectName = Split-Path -Leaf $ProjectFull
$QaDir = Join-Path $ReportRoot ("qa\{0}_{1}" -f ($ProjectName -replace "[^A-Za-z0-9_.-]", "_"), $Timestamp)
New-Item -ItemType Directory -Path $QaDir -Force | Out-Null
$SummaryPath = Join-Path $QaDir "summary.txt"
$JsonSummaryPath = Join-Path $QaDir "summary.json"

$Results = New-Object System.Collections.Generic.List[object]
$StartedEmulator = $false
$TargetSerial = $null
$DevicePolicyBlocked = $false

function Add-Result {
    param(
        [string]$Step,
        [string]$Status,
        [string]$Log,
        [int]$ExitCode = 0,
        [double]$Seconds = 0,
        [string]$Note = ""
    )
    $Results.Add([pscustomobject]@{
        Step     = $Step
        Status   = $Status
        ExitCode = $ExitCode
        Seconds  = [math]::Round($Seconds, 2)
        Log      = $Log
        Note     = $Note
    })
}

function Invoke-Step {
    param(
        [string]$Name,
        [string]$FilePath,
        [string[]]$Arguments,
        [string]$WorkingDirectory = $ProjectFull,
        [int[]]$WarnExitCodes = @(),
        [switch]$AllowFailure
    )
    $safeName = $Name -replace "[^A-Za-z0-9_.-]", "_"
    $log = Join-Path $QaDir "$safeName.log"
    $sw = [Diagnostics.Stopwatch]::StartNew()
    Push-Location $WorkingDirectory
    try {
        & $FilePath @Arguments *> $log
        $exit = if ($null -ne $LASTEXITCODE) { $LASTEXITCODE } else { 0 }
    } catch {
        $_ | Out-File -LiteralPath $log -Append -Encoding UTF8
        $exit = 999
    } finally {
        Pop-Location
        $sw.Stop()
    }
    if ($exit -eq 0) {
        Add-Result $Name "PASS" $log $exit $sw.Elapsed.TotalSeconds
    } elseif ($WarnExitCodes -contains $exit -or $AllowFailure) {
        Add-Result $Name "WARN" $log $exit $sw.Elapsed.TotalSeconds
    } else {
        Add-Result $Name "FAIL" $log $exit $sw.Elapsed.TotalSeconds
    }
    return $exit
}

function Find-Adb {
    $cmd = Get-Command adb -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    if ($env:ANDROID_HOME) {
        $candidate = Join-Path $env:ANDROID_HOME "platform-tools\adb.exe"
        if (Test-Path -LiteralPath $candidate) { return $candidate }
    }
    return $null
}

function Get-AdbDeviceRows {
    param([string]$AdbPath)
    & $AdbPath devices -l | Where-Object { $_ -match "^\S+\s+\S+" -and $_ -notmatch "^List" } | ForEach-Object {
        $parts = $_ -split "\s+"
        [pscustomobject]@{
            Serial = $parts[0]
            State  = $parts[1]
            Raw    = $_
        }
    }
}

function Test-DeviceAllowed {
    param([pscustomobject]$Row)
    $isEmulator = $Row.Serial -match "^emulator-\d+$"
    $isTcl = $Row.Raw -match "model:6102H|device:Cruze_Lite_S|product:6102H"
    switch ($DevicePolicy) {
        "All" { return $true }
        "EmulatorOnly" { return $isEmulator }
        "TclOnly" { return $isTcl }
        default { return ($isEmulator -or $isTcl) }
    }
}

function Disconnect-DisallowedDevices {
    param([string]$AdbPath)
    if ($DevicePolicy -eq "All") { return }
    $rows = Get-AdbDeviceRows -AdbPath $AdbPath | Where-Object State -eq "device"
    foreach ($row in $rows) {
        if (Test-DeviceAllowed -Row $row) { continue }
        if ($row.Serial -match "^adb-.*_adb-tls-connect\._tcp$") {
            & $AdbPath disconnect $row.Serial *> (Join-Path $QaDir ("disconnect_{0}.log" -f ($row.Serial -replace "[^A-Za-z0-9_.-]", "_")))
            Add-Result "disconnect disallowed device" "WARN" "" 0 0 "Disconnected $($row.Serial) due to DevicePolicy=$DevicePolicy"
        } else {
            $script:DevicePolicyBlocked = $true
            Add-Result "disallowed device present" "FAIL" "" 1 0 "Connected device cannot be disconnected automatically and is forbidden by DevicePolicy=${DevicePolicy}: $($row.Raw)"
        }
    }
    Start-Sleep -Seconds 1
    $remaining = Get-AdbDeviceRows -AdbPath $AdbPath | Where-Object { $_.State -eq "device" -and -not (Test-DeviceAllowed -Row $_) }
    foreach ($row in $remaining) {
        $script:DevicePolicyBlocked = $true
        Add-Result "disallowed device still connected" "FAIL" "" 1 0 "Refusing connected tests while forbidden device is visible: $($row.Raw)"
    }
}

function Select-AllowedTargetSerial {
    param([string]$AdbPath)
    $rows = Get-AdbDeviceRows -AdbPath $AdbPath | Where-Object State -eq "device"
    $allowed = $rows | Where-Object { Test-DeviceAllowed -Row $_ }
    $emulator = $allowed | Where-Object { $_.Serial -match "^emulator-\d+$" } | Select-Object -First 1
    if ($emulator) { return $emulator.Serial }
    $tcl = $allowed | Where-Object { $_.Raw -match "model:6102H|device:Cruze_Lite_S|product:6102H" } | Select-Object -First 1
    if ($tcl) { return $tcl.Serial }
    return $null
}

function Stop-NewAndroidEmulatorProcesses {
    param([datetime]$StartedAt)
    $sdkEmulatorRoot = if ($env:ANDROID_HOME) { Join-Path $env:ANDROID_HOME "emulator" } else { "" }
    $cleanupLog = Join-Path $QaDir "kill_emulator_process_fallback.log"
    foreach ($attempt in 1..8) {
        $processes = Get-Process -ErrorAction SilentlyContinue |
            Where-Object {
                $_.ProcessName -match "^(emulator|qemu-system)" -and
                $_.StartTime -ge $StartedAt.AddSeconds(-5) -and
                ($sdkEmulatorRoot -eq "" -or -not $_.Path -or $_.Path.StartsWith($sdkEmulatorRoot, [StringComparison]::OrdinalIgnoreCase))
            }
        if (-not $processes) {
            "No emulator/qemu processes from this run remain after attempt $attempt." | Add-Content -LiteralPath $cleanupLog -Encoding UTF8
            return
        }
        foreach ($process in $processes) {
            try {
                Stop-Process -Id $process.Id -Force -ErrorAction Stop
                "Stopped emulator/qemu PID $($process.Id) $($process.ProcessName) on cleanup attempt $attempt." | Add-Content -LiteralPath $cleanupLog -Encoding UTF8
            } catch {
                "WARN failed to stop PID $($process.Id) on cleanup attempt ${attempt}: $($_.Exception.Message)" | Add-Content -LiteralPath $cleanupLog -Encoding UTF8
            }
        }
        Start-Sleep -Seconds 2
    }
    $remaining = Get-Process -ErrorAction SilentlyContinue |
        Where-Object {
            $_.ProcessName -match "^(emulator|qemu-system)" -and
            $_.StartTime -ge $StartedAt.AddSeconds(-5) -and
            ($sdkEmulatorRoot -eq "" -or -not $_.Path -or $_.Path.StartsWith($sdkEmulatorRoot, [StringComparison]::OrdinalIgnoreCase))
        }
    foreach ($process in $remaining) {
        Add-Result "emulator cleanup" "FAIL" $cleanupLog 1 0 "Emulator/qemu process still alive after cleanup: PID $($process.Id) $($process.ProcessName)"
    }
}

try {
    $gradlew = Join-Path $ProjectFull "gradlew.bat"
    if (-not (Test-Path -LiteralPath $gradlew)) {
        Add-Result "gradle wrapper" "FAIL" "" 1 0 "gradlew.bat missing; project should use Gradle wrapper"
    } else {
        Add-Result "gradle wrapper" "PASS" $gradlew 0 0
    }

    Invoke-Step "git status" "git" @("status", "--short", "--branch") -AllowFailure | Out-Null

    $localProperties = Join-Path $ProjectFull "local.properties"
    if (Test-Path -LiteralPath $localProperties) {
        $lp = Get-Content -LiteralPath $localProperties -Raw
        if ($lp -match "sdk\.dir\s*=") {
            Add-Result "local.properties sdk.dir" "PASS" $localProperties
        } else {
            Add-Result "local.properties sdk.dir" "WARN" $localProperties 0 0 "local.properties exists but sdk.dir is missing"
        }
    } elseif ($FixLocalProperties -and $env:ANDROID_HOME) {
        $escaped = $env:ANDROID_HOME.Replace("\", "\\")
        "sdk.dir=$escaped" | Set-Content -LiteralPath $localProperties -Encoding ASCII
        Add-Result "local.properties sdk.dir" "PASS" $localProperties 0 0 "created from ANDROID_HOME"
    } else {
        Add-Result "local.properties sdk.dir" "WARN" "" 0 0 "missing; pass -FixLocalProperties to create"
    }

    if (Test-Path -LiteralPath $gradlew) {
        Invoke-Step "gradlew version" $gradlew @("--version", "--console=plain") | Out-Null
        Invoke-Step "assembleDebug" $gradlew @(":${Module}:assembleDebug", "--console=plain", "--stacktrace") | Out-Null
        if ($RunUnitTests) {
            Invoke-Step "testDebugUnitTest" $gradlew @(":${Module}:testDebugUnitTest", "--console=plain", "--stacktrace") | Out-Null
        }
        if ($RunLint) {
            Invoke-Step "lintDebug" $gradlew @(":${Module}:lintDebug", "--console=plain", "--stacktrace") -AllowFailure | Out-Null
        }
    }

    if ($UseEmulator) {
        $beforeEmu = (& adb devices | Select-String "^emulator-\d+\s+device").Line
        if (-not $beforeEmu) { $StartedEmulator = $true }
        & (Join-Path $PSScriptRoot "start_pixel8a_emulator.ps1") -AvdName $UseEmulator -ReportRoot $ReportRoot -TimeoutSec 360 -NoExit *> (Join-Path $QaDir "start_emulator.log")
        $emuExit = $global:StartPixel8aEmulatorExitCode
        $TargetSerial = $global:StartPixel8aEmulatorSerial
        if ($emuExit -eq 0 -or $emuExit -eq 2) {
            Add-Result "emulator ready" "PASS" (Join-Path $QaDir "start_emulator.log") $emuExit
        } else {
            Add-Result "emulator ready" "FAIL" (Join-Path $QaDir "start_emulator.log") $emuExit
        }
    }

    $adb = Find-Adb
    if ($RunConnectedTests -or $InstallAndLaunch) {
        if (-not $adb) {
            Add-Result "adb discovery" "FAIL" "" 1 0 "adb missing"
        } else {
            Disconnect-DisallowedDevices -AdbPath $adb
            if ($DevicePolicyBlocked) {
                Add-Result "device ready" "FAIL" "" 1 0 "Blocked by forbidden connected device under DevicePolicy=$DevicePolicy"
            } elseif (-not $TargetSerial) { $TargetSerial = Select-AllowedTargetSerial -AdbPath $adb }
            if (-not $DevicePolicyBlocked -and -not $TargetSerial) {
                Add-Result "device ready" "FAIL" "" 1 0 "No allowed target device for DevicePolicy=$DevicePolicy"
            } elseif (-not $DevicePolicyBlocked) {
                & (Join-Path $PSScriptRoot "wait_android_device_ready.ps1") -Serial $TargetSerial -ReportRoot $ReportRoot -TimeoutSec 240 -NoExit *> (Join-Path $QaDir "device_ready.log")
            $readyExit = $global:WaitAndroidDeviceReadyExitCode
            if ($readyExit -eq 0) {
                Add-Result "device ready" "PASS" (Join-Path $QaDir "device_ready.log") $readyExit
            } elseif ($readyExit -eq 2) {
                Add-Result "device ready" "WARN" (Join-Path $QaDir "device_ready.log") $readyExit 0 "manual unlock may be required"
            } else {
                Add-Result "device ready" "FAIL" (Join-Path $QaDir "device_ready.log") $readyExit
            }
            }
        }
    }

    if ($RunConnectedTests -and (Test-Path -LiteralPath $gradlew)) {
        $ready = $Results | Where-Object Step -eq "device ready" | Select-Object -Last 1
        if ($ready -and $ready.Status -eq "WARN") {
            Add-Result "connectedDebugAndroidTest" "WARN" "" 2 0 "skipped because manual unlock may be required"
        } elseif ($ready -and $ready.Status -eq "FAIL") {
            Add-Result "connectedDebugAndroidTest" "FAIL" "" 1 0 "device not ready"
        } else {
            Invoke-Step "connectedDebugAndroidTest" $gradlew @(":${Module}:connectedDebugAndroidTest", "--console=plain", "--stacktrace") -AllowFailure | Out-Null
        }
    }

    if ($InstallAndLaunch -and (Test-Path -LiteralPath $gradlew)) {
        Invoke-Step "installDebug" $gradlew @(":${Module}:installDebug", "--console=plain", "--stacktrace") -AllowFailure | Out-Null
        if ($PackageName -and $adb) {
            $serial = if ($TargetSerial) { $TargetSerial } else { Select-AllowedTargetSerial -AdbPath $adb }
            if ($serial) {
                & $adb -s $serial logcat -c
                $activity = (& $adb -s $serial shell cmd package resolve-activity --brief $PackageName 2>$null | Select-Object -Last 1)
                if ($activity -match "/") {
                    & $adb -s $serial shell am start -n $activity *> (Join-Path $QaDir "launch.log")
                    Add-Result "launch activity" "PASS" (Join-Path $QaDir "launch.log")
                } else {
                    Add-Result "launch activity" "WARN" "" 0 0 "could not resolve activity for $PackageName"
                }
                & $adb -s $serial exec-out uiautomator dump /dev/tty > (Join-Path $QaDir "ui_after_launch.xml")
                cmd /c "`"$adb`" -s `"$serial`" exec-out screencap -p > `"$QaDir\screen_after_launch.png`""
                & $adb -s $serial logcat -d > (Join-Path $QaDir "logcat_after_launch.txt")
            }
        } else {
            Add-Result "launch activity" "WARN" "" 0 0 "pass -PackageName to launch"
        }
    }
} finally {
    if ($KillStartedEmulator -and $StartedEmulator) {
        $adb = Find-Adb
        if ($adb) {
            $emus = (& $adb devices | Select-String "^emulator-\d+\s+").Line | ForEach-Object { ($_ -split "\s+")[0] }
            foreach ($emu in $emus) {
                & $adb -s $emu emu kill *> (Join-Path $QaDir "kill_$emu.log")
            }
        }
        if ($global:StartPixel8aEmulatorProcessId) {
            Start-Sleep -Seconds 3
            $emuProcess = Get-Process -Id $global:StartPixel8aEmulatorProcessId -ErrorAction SilentlyContinue
            if ($emuProcess) {
                Stop-Process -Id $global:StartPixel8aEmulatorProcessId -Force
                "Stopped emulator PID $global:StartPixel8aEmulatorProcessId" | Set-Content -LiteralPath (Join-Path $QaDir "kill_emulator_pid.log") -Encoding UTF8
            }
        }
        Stop-NewAndroidEmulatorProcesses -StartedAt $VerificationStartTime
    }
}

$overall = if ($Results.Status -contains "FAIL") { "FAIL" } elseif ($Results.Status -contains "WARN") { "WARN" } else { "PASS" }
$Results | Format-Table -AutoSize | Tee-Object -FilePath $SummaryPath
"overall=$overall" | Tee-Object -FilePath $SummaryPath -Append
"qa_dir=$QaDir" | Tee-Object -FilePath $SummaryPath -Append
$Results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $JsonSummaryPath -Encoding UTF8
Write-Output "overall=$overall"
Write-Output "summary=$SummaryPath"
Write-Output "qa_dir=$QaDir"
if ($overall -eq "FAIL") { exit 1 }
if ($overall -eq "WARN") { exit 2 }
exit 0
