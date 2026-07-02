[CmdletBinding()]
param(
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$IncludeSdkAvailable
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogPath = Join-Path $LogDir "audit_android_dev_env_$Timestamp.txt"
$PathCsv = Join-Path $LogDir "path_analysis_$Timestamp.csv"

function Write-Section {
    param([string]$Name)
    "`n===== $Name ====="
}

function Invoke-Captured {
    param(
        [string]$Name,
        [scriptblock]$Script
    )
    Write-Section $Name
    try {
        & $Script 2>&1 | Out-String -Width 260
    } catch {
        "ERROR: $($_.Exception.Message)"
    }
}

function Get-CommandInfoRow {
    param([string]$Name)
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    [pscustomobject]@{
        Command = $Name
        Found   = [bool]$cmd
        Path    = if ($cmd) { ($cmd.Source -join "; ") } else { "" }
    }
}

function Get-PathAnalysis {
    $rows = New-Object System.Collections.Generic.List[object]
    foreach ($scope in @("User", "Machine")) {
        $pathValue = [Environment]::GetEnvironmentVariable("Path", $scope)
        if ([string]::IsNullOrWhiteSpace($pathValue)) { continue }
        foreach ($entry in ($pathValue -split ";")) {
            if ([string]::IsNullOrWhiteSpace($entry)) { continue }
            $expanded = [Environment]::ExpandEnvironmentVariables($entry)
            $rows.Add([pscustomobject]@{
                Scope        = $scope
                Entry        = $entry
                Expanded     = $expanded
                Exists       = Test-Path -LiteralPath $expanded
                DuplicateKey = $expanded.TrimEnd("\").ToLowerInvariant()
            })
        }
    }
    $rows
}

$AndroidSdk = if ($env:ANDROID_HOME) { $env:ANDROID_HOME } else { Join-Path $env:LOCALAPPDATA "Android\Sdk" }
$StudioCandidates = @(
    "$env:LOCALAPPDATA\Programs\Android Studio",
    "$env:ProgramFiles\Android\Android Studio",
    "${env:ProgramFiles(x86)}\Android\Android Studio"
) | Where-Object { $_ -and (Test-Path -LiteralPath $_) }

& {
    "ReportRoot=$ReportRoot"
    "Timestamp=$(Get-Date -Format o)"

    Invoke-Captured "Windows version / model" {
        Get-ComputerInfo -Property WindowsProductName, WindowsVersion, OsHardwareAbstractionLayer, OsArchitecture, OsBuildNumber, CsManufacturer, CsModel, CsTotalPhysicalMemory, HyperVisorPresent
    }

    Invoke-Captured "Power plan / sleep" {
        powercfg /GETACTIVESCHEME
        powercfg /a
        powercfg /query SCHEME_CURRENT SUB_SLEEP STANDBYIDLE
        powercfg /query SCHEME_CURRENT SUB_SLEEP HIBERNATEIDLE
    }

    Invoke-Captured "CPU / RAM / disk" {
        Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, VirtualizationFirmwareEnabled, SecondLevelAddressTranslationExtensions
        Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize, FreePhysicalMemory
        Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free, Root
        Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus, Size
        try {
            Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId, Temperature, Wear, ReadErrorsTotal, WriteErrorsTotal, PowerOnHours
        } catch {
            "Storage reliability counters unavailable: $($_.Exception.Message)"
        }
    }

    Invoke-Captured "Virtualization / Hyper-V / WSL" {
        Get-CimInstance Win32_OptionalFeature -Filter "Name='Microsoft-Hyper-V-All' OR Name='HypervisorPlatform' OR Name='VirtualMachinePlatform' OR Name='Microsoft-Windows-Subsystem-Linux'" |
            Select-Object Name, InstallState, Caption
        try {
            foreach ($feature in @("Microsoft-Hyper-V-All", "HypervisorPlatform", "VirtualMachinePlatform", "Microsoft-Windows-Subsystem-Linux")) {
                Get-WindowsOptionalFeature -Online -FeatureName $feature -ErrorAction Stop | Select-Object FeatureName, State
            }
        } catch {
            "Get-WindowsOptionalFeature requires elevation here: $($_.Exception.Message)"
        }
        systeminfo | Select-String -Pattern "Hyper-V|Virtualization|hypervisor|Requirements"
        wsl --status
        wsl --list --verbose
    }

    Invoke-Captured "Tool discovery" {
        "adb", "emulator", "sdkmanager", "java", "javac", "gradle", "git", "pwsh", "python", "winget" |
            ForEach-Object { Get-CommandInfoRow $_ } |
            Format-Table -AutoSize
    }

    Invoke-Captured "Java / JDK" {
        java -version
        javac -version
        "JAVA_HOME(process)=$env:JAVA_HOME"
        "JAVA_HOME(user)=$([Environment]::GetEnvironmentVariable("JAVA_HOME", "User"))"
        "JAVA_HOME(machine)=$([Environment]::GetEnvironmentVariable("JAVA_HOME", "Machine"))"
        if ($env:JAVA_HOME) { Get-ChildItem -LiteralPath $env:JAVA_HOME -ErrorAction SilentlyContinue | Select-Object Name, FullName, LastWriteTime }
    }

    Invoke-Captured "Android Studio" {
        $StudioCandidates
        foreach ($studio in $StudioCandidates) {
            Get-ChildItem -LiteralPath $studio -Recurse -Filter product-info.json -ErrorAction SilentlyContinue | ForEach-Object {
                "--- $($_.FullName)"
                Get-Content -LiteralPath $_.FullName -Raw
            }
            $jbr = Join-Path $studio "jbr"
            if (Test-Path -LiteralPath $jbr) {
                "Bundled JDK: $jbr"
                & (Join-Path $jbr "bin\java.exe") -version
            }
        }
    }

    Invoke-Captured "Android SDK structure" {
        "ANDROID_HOME(process)=$env:ANDROID_HOME"
        "ANDROID_SDK_ROOT(process)=$env:ANDROID_SDK_ROOT"
        "SDK candidate=$AndroidSdk"
        if (Test-Path -LiteralPath $AndroidSdk) {
            Get-ChildItem -LiteralPath $AndroidSdk | Select-Object Name, FullName, LastWriteTime
            foreach ($sub in @("platform-tools", "emulator", "cmdline-tools\latest\bin", "build-tools", "platforms", "system-images")) {
                $p = Join-Path $AndroidSdk $sub
                "--- $p"
                if (Test-Path -LiteralPath $p) {
                    Get-ChildItem -LiteralPath $p -ErrorAction SilentlyContinue | Select-Object Name, FullName, LastWriteTime
                } else {
                    "MISSING"
                }
            }
        } else {
            "SDK path missing"
        }
    }

    Invoke-Captured "Android command checks" {
        adb version
        adb devices -l
        emulator -version
        emulator -list-avds
        sdkmanager --version
        sdkmanager --list_installed
        if ($IncludeSdkAvailable) {
            sdkmanager --list
        }
    }

    Invoke-Captured "Gradle / wrappers / versions" {
        gradle --version
        "GRADLE_USER_HOME(process)=$env:GRADLE_USER_HOME"
        "GRADLE_USER_HOME(user)=$([Environment]::GetEnvironmentVariable("GRADLE_USER_HOME", "User"))"
        $globalGradle = Join-Path $env:USERPROFILE ".gradle"
        if (Test-Path -LiteralPath $globalGradle) {
            Get-ChildItem -LiteralPath $globalGradle -Force | Select-Object Name, FullName, LastWriteTime
        }
        Get-ChildItem -Path (Join-Path $env:USERPROFILE "Documents") -Recurse -Filter gradlew.bat -ErrorAction SilentlyContinue | Select-Object FullName
        if (Get-Command rg -ErrorAction SilentlyContinue) {
            Push-Location (Join-Path $env:USERPROFILE "Documents")
            rg -n --glob "build.gradle*" --glob "settings.gradle*" --glob "gradle.properties" --glob "libs.versions.toml" "(com\.android\.application|com\.android\.library|agp|androidGradlePlugin|kotlin|org\.jetbrains\.kotlin|com\.google\.devtools\.ksp|compileSdk|targetSdk|minSdk|distributionUrl|org\.gradle\.jvmargs|org\.gradle\.configuration-cache)" .
            Pop-Location
        }
    }

    Invoke-Captured "Git / PowerShell / Python / winget" {
        git --version
        $PSVersionTable
        python --version
        winget --version
        winget list --id Google.AndroidStudio --accept-source-agreements
        winget list --id Git.Git --accept-source-agreements
        winget list --id Microsoft.PowerShell --accept-source-agreements
        winget list --id Microsoft.OpenJDK.21 --accept-source-agreements
        winget list --id Gradle.Gradle --accept-source-agreements
    }

    Invoke-Captured "Defender exclusions" {
        try {
            Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
        } catch {
            "Defender exclusion read unavailable, likely needs administrator: $($_.Exception.Message)"
        }
    }

    Invoke-Captured "PATH analysis" {
        $pathRows = Get-PathAnalysis
        $pathRows | Sort-Object Scope, Entry | Format-Table -AutoSize
        "Duplicates:"
        $pathRows | Group-Object DuplicateKey | Where-Object Count -gt 1 | ForEach-Object { $_.Group | Select-Object Scope, Entry, Expanded, Exists } | Format-Table -AutoSize
        "Broken literal entries:"
        $pathRows | Where-Object { -not $_.Exists -and $_.Entry -notmatch "%" } | Select-Object Scope, Entry, Expanded | Format-Table -AutoSize
        $pathRows | Export-Csv -LiteralPath $PathCsv -NoTypeInformation -Encoding UTF8
        "CSV=$PathCsv"
    }
} | Tee-Object -FilePath $LogPath

"Wrote $LogPath"
