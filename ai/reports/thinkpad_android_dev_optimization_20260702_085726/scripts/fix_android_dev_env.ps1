[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$AndroidSdk = (Join-Path $env:LOCALAPPDATA "Android\Sdk"),
    [string]$JavaHome,
    [string[]]$SdkPackages = @(
        "platform-tools",
        "emulator",
        "cmdline-tools;latest",
        "platforms;android-35",
        "platforms;android-36",
        "build-tools;36.0.0"
    ),
    [switch]$AcceptSdkLicenses,
    [switch]$SkipSdkInstall,
    [switch]$InstallGlobalGradle,
    [switch]$AddDefenderExclusions,
    [switch]$SetPowerAC
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogPath = Join-Path $LogDir "fix_android_dev_env_$Timestamp.txt"
$BackupPath = Join-Path $LogDir "env_backup_$Timestamp.json"

function Write-Log {
    param([string]$Message)
    $Message
}

function Normalize-PathEntry {
    param([string]$Entry)
    if ([string]::IsNullOrWhiteSpace($Entry)) { return "" }
    [Environment]::ExpandEnvironmentVariables($Entry).TrimEnd("\").ToLowerInvariant()
}

function Add-UserPathEntry {
    param([string]$Entry)
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $items = @()
    if ($userPath) { $items = $userPath -split ";" | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } }
    $wanted = Normalize-PathEntry $Entry
    $exists = $false
    foreach ($item in $items) {
        if ((Normalize-PathEntry $item) -eq $wanted) {
            $exists = $true
            break
        }
    }
    if (-not $exists) {
        $items += $Entry
        [Environment]::SetEnvironmentVariable("Path", ($items -join ";"), "User")
        Write-Log "ADDED User PATH: $Entry"
    } else {
        Write-Log "OK User PATH already has: $Entry"
    }
}

function Resolve-JavaHome {
    param([string]$Requested)
    if ($Requested -and (Test-Path -LiteralPath (Join-Path $Requested "bin\javac.exe"))) {
        return $Requested
    }
    $candidates = @(
        "$env:ProgramFiles\Android\Android Studio\jbr",
        "$env:LOCALAPPDATA\Programs\Android Studio\jbr"
    )
    $candidates += Get-ChildItem -Path "$env:ProgramFiles\Eclipse Adoptium", "$env:ProgramFiles\Java" -Directory -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match "21" } |
        ForEach-Object { $_.FullName }
    foreach ($candidate in $candidates) {
        if ($candidate -and (Test-Path -LiteralPath (Join-Path $candidate "bin\javac.exe"))) {
            return $candidate
        }
    }
    return $null
}

function Find-SdkManager {
    param([string]$Sdk)
    $candidate = Join-Path $Sdk "cmdline-tools\latest\bin\sdkmanager.bat"
    if (Test-Path -LiteralPath $candidate) { return $candidate }
    $cmd = Get-Command sdkmanager -ErrorAction SilentlyContinue
    if ($cmd) { return $cmd.Source }
    return $null
}

function Test-SdkPackageInstalled {
    param(
        [string]$Package,
        [string]$Sdk,
        [string]$InstalledRaw
    )
    switch -Regex ($Package) {
        "^cmdline-tools;latest$" { return (Test-Path -LiteralPath (Join-Path $Sdk "cmdline-tools\latest\bin\sdkmanager.bat")) }
        "^platform-tools$" { return (Test-Path -LiteralPath (Join-Path $Sdk "platform-tools\adb.exe")) }
        "^emulator$" { return (Test-Path -LiteralPath (Join-Path $Sdk "emulator\emulator.exe")) }
        "^platforms;android-(.+)$" { return (Test-Path -LiteralPath (Join-Path $Sdk "platforms\android-$($Matches[1])")) }
        "^build-tools;(.+)$" { return (Test-Path -LiteralPath (Join-Path $Sdk "build-tools\$($Matches[1])")) }
        default { return ($InstalledRaw -match [regex]::Escape($Package)) }
    }
}

function Invoke-LoggedNative {
    param(
        [string]$Label,
        [string]$FilePath,
        [string[]]$Arguments = @()
    )
    Write-Log "RUN ${Label}: $FilePath $($Arguments -join ' ')"
    try {
        & $FilePath @Arguments 2>&1 | ForEach-Object { $_ }
        Write-Log "EXIT ${Label}: $LASTEXITCODE"
    } catch {
        Write-Log "ERROR ${Label}: $($_.Exception.Message)"
    }
}

function Add-DefenderExclusionSafe {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        Write-Log "SKIP Defender exclusion missing path: $Path"
        return
    }
    try {
        Add-MpPreference -ExclusionPath $Path -ErrorAction Stop
        Write-Log "ADDED Defender exclusion: $Path"
    } catch {
        Write-Log "WARN Defender exclusion not applied for $Path : $($_.Exception.Message)"
    }
}

& {
    Write-Log "ReportRoot=$ReportRoot"
    Write-Log "Timestamp=$(Get-Date -Format o)"

    $backup = [ordered]@{
        Timestamp            = (Get-Date -Format o)
        User_ANDROID_HOME    = [Environment]::GetEnvironmentVariable("ANDROID_HOME", "User")
        User_ANDROID_SDK_ROOT = [Environment]::GetEnvironmentVariable("ANDROID_SDK_ROOT", "User")
        User_JAVA_HOME       = [Environment]::GetEnvironmentVariable("JAVA_HOME", "User")
        User_Path            = [Environment]::GetEnvironmentVariable("Path", "User")
        Machine_Path         = [Environment]::GetEnvironmentVariable("Path", "Machine")
    }
    $backup | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $BackupPath -Encoding UTF8
    Write-Log "BACKUP env saved: $BackupPath"

    $resolvedJavaHome = Resolve-JavaHome -Requested $JavaHome
    if (-not $resolvedJavaHome) {
        Write-Log "WARN no valid JDK found. Install Android Studio bundled JDK or JDK 21."
    }

    if (Test-Path -LiteralPath $AndroidSdk) {
        [Environment]::SetEnvironmentVariable("ANDROID_HOME", $AndroidSdk, "User")
        [Environment]::SetEnvironmentVariable("ANDROID_SDK_ROOT", $AndroidSdk, "User")
        $env:ANDROID_HOME = $AndroidSdk
        $env:ANDROID_SDK_ROOT = $AndroidSdk
        Write-Log "SET User ANDROID_HOME=$AndroidSdk"
        Write-Log "SET User ANDROID_SDK_ROOT=$AndroidSdk"
    } else {
        Write-Log "WARN Android SDK path missing: $AndroidSdk"
    }

    if ($resolvedJavaHome) {
        [Environment]::SetEnvironmentVariable("JAVA_HOME", $resolvedJavaHome, "User")
        $env:JAVA_HOME = $resolvedJavaHome
        Write-Log "SET User JAVA_HOME=$resolvedJavaHome"
    }

    Add-UserPathEntry "%ANDROID_HOME%\platform-tools"
    Add-UserPathEntry "%ANDROID_HOME%\emulator"
    Add-UserPathEntry "%ANDROID_HOME%\cmdline-tools\latest\bin"
    if ($resolvedJavaHome) { Add-UserPathEntry "%JAVA_HOME%\bin" }

    if ($InstallGlobalGradle) {
        $gradle = Get-Command gradle -ErrorAction SilentlyContinue
        if ($gradle) {
            Write-Log "OK global Gradle already present: $($gradle.Source)"
        } else {
            Invoke-LoggedNative "winget install Gradle" "winget" @("install", "--id", "Gradle.Gradle", "--exact", "--accept-source-agreements", "--accept-package-agreements")
        }
    } else {
        Write-Log "SKIP global Gradle install. Gradle wrapper remains preferred."
    }

    if (-not $SkipSdkInstall) {
        $sdkManager = Find-SdkManager -Sdk $AndroidSdk
        if ($sdkManager) {
            if ($AcceptSdkLicenses) {
                Write-Log "Accepting Android SDK licenses if prompted."
                try {
                    $yes = 1..80 | ForEach-Object { "y" }
                    $yes | & $sdkManager --licenses 2>&1 | ForEach-Object { $_ }
                    Write-Log "EXIT sdkmanager --licenses: $LASTEXITCODE"
                } catch {
                    Write-Log "WARN sdkmanager --licenses failed: $($_.Exception.Message)"
                }
            }
            $installedRaw = & $sdkManager --list_installed 2>&1 | Out-String -Width 240
            $installedRaw | Set-Content -LiteralPath (Join-Path $LogDir "sdkmanager_list_installed_before_$Timestamp.txt") -Encoding UTF8
            foreach ($pkg in $SdkPackages) {
                if (Test-SdkPackageInstalled -Package $pkg -Sdk $AndroidSdk -InstalledRaw $installedRaw) {
                    Write-Log "OK SDK package installed: $pkg"
                } else {
                    Invoke-LoggedNative "sdkmanager install $pkg" $sdkManager @($pkg)
                }
            }
        } else {
            Write-Log "WARN sdkmanager missing. Install Android SDK Command-line Tools from Android Studio SDK Manager."
        }
    } else {
        Write-Log "SKIP SDK install/update by parameter."
    }

    if ($SetPowerAC) {
        Write-Log "Applying AC-only power tuning: no sleep/hibernate on AC, processor max 100 on AC. DC/battery settings unchanged."
        Invoke-LoggedNative "powercfg AC sleep off" "powercfg" @("/SETACVALUEINDEX", "SCHEME_CURRENT", "SUB_SLEEP", "STANDBYIDLE", "0")
        Invoke-LoggedNative "powercfg AC hibernate off" "powercfg" @("/SETACVALUEINDEX", "SCHEME_CURRENT", "SUB_SLEEP", "HIBERNATEIDLE", "0")
        Invoke-LoggedNative "powercfg AC processor max 100" "powercfg" @("/SETACVALUEINDEX", "SCHEME_CURRENT", "SUB_PROCESSOR", "PROCTHROTTLEMAX", "100")
        Invoke-LoggedNative "powercfg activate current" "powercfg" @("/SETACTIVE", "SCHEME_CURRENT")
    } else {
        Write-Log "SKIP power plan changes."
    }

    if ($AddDefenderExclusions) {
        Write-Log "SECURITY NOTE: Defender exclusions reduce scanning on local development caches/repos only. Do not add Downloads/Desktop broadly."
        $exclusions = New-Object System.Collections.Generic.List[string]
        $exclusions.Add((Join-Path $env:USERPROFILE ".gradle"))
        $exclusions.Add((Join-Path $env:USERPROFILE ".android"))
        $exclusions.Add($AndroidSdk)
        $docs = Join-Path $env:USERPROFILE "Documents"
        $devRoot = Join-Path $docs "android studio"
        if (Test-Path -LiteralPath $devRoot) { $exclusions.Add($devRoot) }
        Get-ChildItem -Path $docs -Recurse -Filter gradlew.bat -ErrorAction SilentlyContinue |
            ForEach-Object { Split-Path -Parent $_.FullName } |
            Sort-Object -Unique |
            ForEach-Object {
                if ($_ -like "$docs*") { $exclusions.Add($_) }
            }
        $exclusions | Sort-Object -Unique | ForEach-Object { Add-DefenderExclusionSafe -Path $_ }
    } else {
        Write-Log "SKIP Defender exclusions. Re-run with -AddDefenderExclusions from an elevated shell to apply."
    }

    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $env:Path = (($machinePath, $userPath) -join ";")
    Write-Log "Session PATH refreshed from Machine + User."

    Write-Log "Final command discovery:"
    "adb", "emulator", "sdkmanager", "java", "javac", "gradle", "git", "pwsh", "python", "winget" |
        ForEach-Object {
            $cmd = Get-Command $_ -ErrorAction SilentlyContinue
            if ($cmd) { "{0}: {1}" -f $_, $cmd.Source } else { "{0}: MISSING" -f $_ }
        }
} | Tee-Object -FilePath $LogPath

"Wrote $LogPath"
