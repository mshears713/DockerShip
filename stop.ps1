#!/usr/bin/env pwsh
# ============================================================================
# Harbor Docker Learning - PowerShell Stop Script
# ============================================================================
#
# This script stops the Harbor Docker Learning application
# Run: .\stop.ps1
#
# ============================================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "  🛑 Stopping Harbor Docker Learning..." -ForegroundColor Yellow
Write-Host ""

# Check if Docker is running
try {
    $null = docker version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ⚠️  Docker is not running" -ForegroundColor Yellow
        Write-Host "  The application is likely already stopped." -ForegroundColor Gray
        Write-Host ""
        exit 0
    }
} catch {
    Write-Host "  ⚠️  Docker is not running" -ForegroundColor Yellow
    Write-Host "  The application is likely already stopped." -ForegroundColor Gray
    Write-Host ""
    exit 0
}

# Ask user what they want to do
Write-Host "  How do you want to stop the application?" -ForegroundColor Cyan
Write-Host ""
Write-Host "  1) Stop (containers remain, can be quickly restarted)" -ForegroundColor White
Write-Host "  2) Stop and remove (clean shutdown, keeps data)" -ForegroundColor White
Write-Host "  3) Stop and remove everything (including data - fresh start)" -ForegroundColor White
Write-Host "  4) Cancel" -ForegroundColor White
Write-Host ""

$choice = Read-Host "  Enter choice (1-4)"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "  ⏸️  Stopping containers..." -ForegroundColor Yellow
        docker-compose stop

        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✅ Application stopped" -ForegroundColor Green
            Write-Host "  To restart: docker-compose start" -ForegroundColor Gray
        } else {
            Write-Host "  ❌ Failed to stop containers" -ForegroundColor Red
        }
    }

    "2" {
        Write-Host ""
        Write-Host "  🛑 Stopping and removing containers..." -ForegroundColor Yellow
        docker-compose down

        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✅ Application stopped and removed" -ForegroundColor Green
            Write-Host "  Your data is preserved in Docker volumes" -ForegroundColor Gray
            Write-Host "  To restart: docker-compose up -d" -ForegroundColor Gray
        } else {
            Write-Host "  ❌ Failed to stop and remove containers" -ForegroundColor Red
        }
    }

    "3" {
        Write-Host ""
        Write-Host "  ⚠️  This will delete ALL application data!" -ForegroundColor Red
        $confirm = Read-Host "  Are you sure? (yes/no)"

        if ($confirm -eq "yes") {
            Write-Host ""
            Write-Host "  🗑️  Stopping and removing everything..." -ForegroundColor Yellow
            docker-compose down -v

            if ($LASTEXITCODE -eq 0) {
                Write-Host "  ✅ Application and data completely removed" -ForegroundColor Green
                Write-Host "  To start fresh: docker-compose up -d --build" -ForegroundColor Gray
            } else {
                Write-Host "  ❌ Failed to remove everything" -ForegroundColor Red
            }
        } else {
            Write-Host "  ❌ Cancelled" -ForegroundColor Yellow
        }
    }

    "4" {
        Write-Host ""
        Write-Host "  ❌ Cancelled" -ForegroundColor Yellow
    }

    default {
        Write-Host ""
        Write-Host "  ❌ Invalid choice" -ForegroundColor Red
    }
}

Write-Host ""
