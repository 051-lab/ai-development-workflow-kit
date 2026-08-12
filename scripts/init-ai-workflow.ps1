[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$RepositoryPath = ".",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$repo = (Resolve-Path -LiteralPath $RepositoryPath).Path
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$kitRoot = Split-Path -Parent $scriptDir
$sourceDir = Join-Path $kitRoot "templates\docs\ai"
$targetDir = Join-Path $repo "docs\ai"

if (-not (Test-Path -LiteralPath $sourceDir -PathType Container)) {
    throw "Template directory not found: $sourceDir"
}

New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
$files = @("PROJECT.md", "STATE.md", "DECISIONS.md", "REFERENCES.md", "INBOX.md")

foreach ($name in $files) {
    $src = Join-Path $sourceDir $name
    $dst = Join-Path $targetDir $name

    if ((Test-Path -LiteralPath $dst) -and -not $Force) {
        Write-Host "preserve  $dst"
        continue
    }

    Copy-Item -LiteralPath $src -Destination $dst -Force
    Write-Host "write     $dst"
}

Write-Host "ready     $targetDir"
