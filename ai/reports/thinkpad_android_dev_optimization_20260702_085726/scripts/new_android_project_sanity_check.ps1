[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ProjectPath,
    [string]$ReportRoot = (Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = "Continue"
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$ProjectFull = [IO.Path]::GetFullPath($ProjectPath)
if (-not (Test-Path -LiteralPath $ProjectFull)) { throw "ProjectPath not found: $ProjectFull" }
$LogDir = Join-Path $ReportRoot "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogPath = Join-Path $LogDir "new_android_project_sanity_check_$Timestamp.txt"

function Add-Check {
    param([string]$Name, [string]$Status, [string]$Detail)
    [pscustomobject]@{ Check = $Name; Status = $Status; Detail = $Detail }
}

$checks = New-Object System.Collections.Generic.List[object]
$gradlew = Join-Path $ProjectFull "gradlew.bat"
$checks.Add((Add-Check "Gradle wrapper" ($(if (Test-Path $gradlew) { "PASS" } else { "FAIL" })) $gradlew))

$settings = Get-ChildItem -LiteralPath $ProjectFull -Filter "settings.gradle*" -ErrorAction SilentlyContinue | Select-Object -First 1
$checks.Add((Add-Check "settings.gradle" ($(if ($settings) { "PASS" } else { "WARN" })) ($(if ($settings) { $settings.FullName } else { "missing" }))))

$buildFiles = Get-ChildItem -LiteralPath $ProjectFull -Recurse -Include "build.gradle", "build.gradle.kts", "libs.versions.toml", "gradle.properties" -ErrorAction SilentlyContinue
$allText = ($buildFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue }) -join "`n"

$localProperties = Join-Path $ProjectFull "local.properties"
if (Test-Path -LiteralPath $localProperties) {
    $lp = Get-Content -LiteralPath $localProperties -Raw
    $checks.Add((Add-Check "local.properties sdk.dir" ($(if ($lp -match "sdk\.dir\s*=") { "PASS" } else { "WARN" })) $localProperties))
} else {
    $checks.Add((Add-Check "local.properties" "WARN" "missing; Android Studio or verification script can create sdk.dir"))
}

$sdkDir = if ($env:ANDROID_HOME) { $env:ANDROID_HOME } else { Join-Path $env:LOCALAPPDATA "Android\Sdk" }
$checks.Add((Add-Check "ANDROID_HOME" ($(if (Test-Path -LiteralPath $sdkDir) { "PASS" } else { "FAIL" })) $sdkDir))

if ($allText -match "compileSdk\s*(?:=|\{)?\s*(\d+)") {
    $compileSdk = $Matches[1]
    $platformPath = Join-Path $sdkDir "platforms\android-$compileSdk"
    $checks.Add((Add-Check "compileSdk installed" ($(if (Test-Path -LiteralPath $platformPath) { "PASS" } else { "FAIL" })) "compileSdk=$compileSdk path=$platformPath"))
} else {
    $checks.Add((Add-Check "compileSdk" "WARN" "not detected"))
}

foreach ($pair in @(
    @{ Name = "AGP"; Pattern = 'agp\s*=\s*"([^"]+)"|com\.android\.application.*version\s*"([^"]+)"' },
    @{ Name = "Kotlin"; Pattern = 'kotlin\s*=\s*"([^"]+)"|org\.jetbrains\.kotlin.*version\s*"([^"]+)"' },
    @{ Name = "KSP"; Pattern = 'ksp\s*=\s*"([^"]+)"|com\.google\.devtools\.ksp.*version\s*"([^"]+)"' }
)) {
    if ($allText -match $pair.Pattern) {
        $version = ($Matches.Values | Where-Object { $_ -and $_ -notmatch $pair.Pattern } | Select-Object -First 1)
        $checks.Add((Add-Check "$($pair.Name) version" "PASS" $version))
    } else {
        $checks.Add((Add-Check "$($pair.Name) version" "WARN" "not detected"))
    }
}

$gradleProps = Join-Path $ProjectFull "gradle.properties"
if (Test-Path -LiteralPath $gradleProps) {
    $gp = Get-Content -LiteralPath $gradleProps -Raw
    foreach ($opt in "org.gradle.daemon=true", "org.gradle.parallel=true", "org.gradle.caching=true") {
        $checks.Add((Add-Check $opt ($(if ($gp -match [regex]::Escape($opt)) { "PASS" } else { "WARN" })) $gradleProps))
    }
    if ($gp -match "org\.gradle\.configuration-cache=true") {
        $checks.Add((Add-Check "configuration cache" "PASS" "enabled; disable if plugins/tests break"))
    } else {
        $checks.Add((Add-Check "configuration cache" "WARN" "not enabled; only enable after a clean build confirms compatibility"))
    }
    if ($gp -match "org\.gradle\.jvmargs=.*-Xmx(\d+)([gmGM])") {
        $checks.Add((Add-Check "Gradle JVM memory" "PASS" $Matches[0]))
    } else {
        $checks.Add((Add-Check "Gradle JVM memory" "WARN" "consider -Xmx4g or -Xmx6g on this 32 GB machine"))
    }
} else {
    $checks.Add((Add-Check "gradle.properties" "WARN" "missing"))
}

if ($allText -match "room\.schemaLocation|exportSchema\s*=\s*true") {
    $checks.Add((Add-Check "Room schema export" "PASS" "schema export configured or referenced"))
} elseif ($allText -match "androidx\.room|room-runtime|room-compiler") {
    $checks.Add((Add-Check "Room schema export" "WARN" "Room detected; verify schemaLocation/exportSchema"))
}

if ($allText -match "androidx\.compose|composeBom|ui-test-junit4") {
    $checks.Add((Add-Check "Compose testing" "PASS" "Compose dependencies detected; watch for deprecated test imports during lint"))
}

$checks | Format-Table -AutoSize | Tee-Object -FilePath $LogPath
"Wrote $LogPath"
$overall = if ($checks.Status -contains "FAIL") { "FAIL" } elseif ($checks.Status -contains "WARN") { "WARN" } else { "PASS" }
"overall=$overall"
if ($overall -eq "FAIL") { exit 1 }
if ($overall -eq "WARN") { exit 2 }
exit 0
