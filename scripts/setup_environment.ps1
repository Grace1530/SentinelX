Write-Host "SentinelX environment setup" -ForegroundColor Cyan

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Error "Python is not installed or not available in PATH."
    exit 1
}

if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Error "Node.js is not installed or not available in PATH."
    exit 1
}

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

Write-Host "Virtual environment ready." -ForegroundColor Green

Write-Host ""
Write-Host "Activate with:" -ForegroundColor Yellow
Write-Host ".\.venv\Scripts\Activate.ps1"

Write-Host ""
Write-Host "Then install backend dependencies:" -ForegroundColor Yellow
Write-Host "pip install -r backend\requirements.txt"

Write-Host ""
Write-Host "Then install frontend dependencies:" -ForegroundColor Yellow
Write-Host "cd frontend"
Write-Host "npm install"