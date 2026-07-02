[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$ProjectPath,
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$Apply,
    [switch]$CleanProjectBuildDirs,
    [switch]$CleanGlobalBuildCaches,
    [switch]$StopGradleDaemons
)

$ErrorActionPreference = "Stop"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogPath = Join-Path $LogDir "clean_gradle_android_caches_safe_$Timestamp.txt"

function Get-FullPathSafe {
    param([string]$Path)
    [IO.Path]::GetFullPath($Path)
}

function Test-UnderRoot {
    param([string]$Path, [string]$Root)
    $full = (Get-FullPathSafe $Path).TrimEnd("\")
    $rootFull = (Get-FullPathSafe $Root).TrimEnd("\")
    return $full.StartsWith($rootFull, [StringComparison]::OrdinalIgnoreCase)
}

function Remove-TargetSafe {
    param([string]$Path, [string]$AllowedRoot)
    if (-not (Test-Path -LiteralPath $Path)) { return }
    if (-not (Test-UnderRoot -Path $Path -Root $AllowedRoot)) {
        "SKIP outside allowed root: $Path"
        return
    }
    $item = Get-Item -LiteralPath $Path -Force
    $size = 0
    if ($item.PSIsContainer) {
        $size = (Get-ChildItem -LiteralPath $Path -Recurse -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
    } else {
        $size = $item.Length
    }
    if ($Apply) {
        Remove-Item -LiteralPath $Path -Recurse -Force
        "REMOVED $Path bytes=$size"
    } else {
        "DRYRUN would remove $Path bytes=$size"
    }
}

& {
    "Timestamp=$(Get-Date -Format o)"
    "Apply=$Apply"
    if ($StopGradleDaemons) {
        $gradlew = if ($ProjectPath) { Join-Path ([IO.Path]::GetFullPath($ProjectPath)) "gradlew.bat" } else { $null }
        if ($gradlew -and (Test-Path -LiteralPath $gradlew)) {
            "Stopping Gradle daemons via wrapper."
            Push-Location ([IO.Path]::GetFullPath($ProjectPath))
            & $gradlew --stop
            Pop-Location
        } elseif (Get-Command gradle -ErrorAction SilentlyContinue) {
            "Stopping Gradle daemons via global gradle."
            gradle --stop
        } else {
            "No gradle command found for daemon stop."
        }
    }

    if ($CleanProjectBuildDirs) {
        if (-not $ProjectPath) { throw "-ProjectPath is required with -CleanProjectBuildDirs" }
        $projectFull = [IO.Path]::GetFullPath($ProjectPath)
        if (-not (Test-Path -LiteralPath $projectFull)) { throw "ProjectPath not found: $projectFull" }
        "Project cleanup root=$projectFull"
        $targets = New-Object System.Collections.Generic.List[string]
        $targets.Add((Join-Path $projectFull ".gradle"))
        Get-ChildItem -LiteralPath $projectFull -Directory -Recurse -Force -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -eq "build" -and (Test-UnderRoot -Path $_.FullName -Root $projectFull) } |
            ForEach-Object { $targets.Add($_.FullName) }
        $targets | Sort-Object -Unique | ForEach-Object { Remove-TargetSafe -Path $_ -AllowedRoot $projectFull }
    }

    if ($CleanGlobalBuildCaches) {
        $home = [IO.Path]::GetFullPath($env:USERPROFILE)
        $gradleHome = Join-Path $home ".gradle"
        $androidHome = Join-Path $home ".android"
        "Global cache cleanup allowed root=$home"
        $targets = @(
            (Join-Path $gradleHome "caches\build-cache-*"),
            (Join-Path $gradleHome "caches\journal-*"),
            (Join-Path $gradleHome "daemon"),
            (Join-Path $androidHome "build-cache")
        )
        foreach ($pattern in $targets) {
            Get-ChildItem -Path $pattern -Force -ErrorAction SilentlyContinue | ForEach-Object {
                Remove-TargetSafe -Path $_.FullName -AllowedRoot $home
            }
        }
    }

    if (-not $Apply) {
        "No files removed. Re-run with -Apply after reviewing dry-run output."
    }
} | Tee-Object -FilePath $LogPath

"Wrote $LogPath"
