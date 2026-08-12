[CmdletBinding()]
param(
    [Parameter(Position = 0, Mandatory = $true)]
    [string]$RepositoryPath,
    [Parameter(Position = 1)]
    [string]$SessionName,
    [string]$Distribution
)

$ErrorActionPreference = "Stop"

$wsl = Get-Command wsl.exe -ErrorAction SilentlyContinue
if (-not $wsl) {
    throw "wsl.exe is required but was not found on PATH."
}

try {
    $repo = (Resolve-Path -LiteralPath $RepositoryPath -ErrorAction Stop).Path
} catch {
    throw "Repository path does not exist: $RepositoryPath"
}
if (-not (Test-Path -LiteralPath $repo -PathType Container)) {
    throw "Repository path is not a directory: $repo"
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$bashLauncher = Join-Path $scriptDir "start-ai-project.sh"
if (-not (Test-Path -LiteralPath $bashLauncher -PathType Leaf)) {
    throw "WSL launcher not found: $bashLauncher"
}

function Convert-ToWslPath([string]$WindowsPath) {
    $conversionArgs = @()
    if ($Distribution) {
        $conversionArgs += @("--distribution", $Distribution)
    }
    $conversionArgs += @("wslpath", "-a", $WindowsPath)
    $converted = & $wsl.Source @conversionArgs 2>&1
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0 -or -not $converted) {
        throw "Could not convert path to WSL form: $WindowsPath"
    }
    return ($converted | Select-Object -Last 1).ToString().Trim()
}

$wslRepo = Convert-ToWslPath $repo
$wslLauncher = Convert-ToWslPath ((Resolve-Path -LiteralPath $bashLauncher).Path)

$launcherArgs = @($wslLauncher, $wslRepo)
if ($PSBoundParameters.ContainsKey("SessionName")) {
    $launcherArgs += $SessionName
}

$wslArgs = @()
if ($Distribution) {
    $wslArgs += @("--distribution", $Distribution)
}
$wslArgs += @("bash") + $launcherArgs
& $wsl.Source @wslArgs
exit $LASTEXITCODE
