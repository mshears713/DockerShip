#!/usr/bin/env pwsh
# ============================================================================
# Harbor Docker Learning - PowerShell Quick Start Script
# ============================================================================
#
# This script makes it easy to start Harbor Docker Learning on Windows
# Just double-click this file or run: .\start.ps1
#
# ============================================================================

# Set error action preference
$ErrorActionPreference = "Stop"

# Display banner
function Show-Banner {
    Write-Host ""
    Write-Host "  🚢 Harbor Docker Learning - Quick Start" -ForegroundColor Cyan
    Write-Host "  =========================================" -ForegroundColor Cyan
    Write-Host ""
}

# Check if Docker is running
function Test-DockerRunning {
    Write-Host "  🔍 Checking Docker status..." -ForegroundColor Yellow

    try {
        $null = docker version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "  ✅ Docker is running" -ForegroundColor Green
            return $true
        }
    } catch {
        # Docker command not found or failed
    }

    Write-Host "  ❌ Docker is not running!" -ForegroundColor Red
    Write-Host ""
    Write-Host "  Please start Docker Desktop and try again." -ForegroundColor Yellow
    Write-Host "  On Windows, look for the whale icon in your system tray." -ForegroundColor Gray
    Write-Host ""
    Write-Host "  Don't have Docker Desktop?" -ForegroundColor Yellow
    Write-Host "  Download from: https://www.docker.com/products/docker-desktop/" -ForegroundColor Gray
    Write-Host ""

    return $false
}

# Check if docker-compose.yml exists
function Test-DockerComposeFile {
    if (Test-Path "docker-compose.yml") {
        Write-Host "  ✅ Found docker-compose.yml" -ForegroundColor Green
        return $true
    }

    Write-Host "  ❌ docker-compose.yml not found!" -ForegroundColor Red
    Write-Host "  Please run this script from the project directory." -ForegroundColor Yellow
    Write-Host ""
    return $false
}

# Start the application
function Start-Application {
    Write-Host ""
    Write-Host "  📦 Checking for existing containers..." -ForegroundColor Yellow

    # Check if container already exists
    $existingContainer = docker ps -a --filter "name=harbor-docker-learning" --format "{{.Names}}" 2>$null

    if ($existingContainer) {
        Write-Host "  📦 Found existing container: $existingContainer" -ForegroundColor Cyan
        Write-Host "  ▶️  Starting container..." -ForegroundColor Yellow

        docker-compose start

        if ($LASTEXITCODE -eq 0) {
            return $true
        } else {
            Write-Host "  ⚠️  Failed to start existing container" -ForegroundColor Yellow
            Write-Host "  🏗️  Rebuilding..." -ForegroundColor Yellow
        }
    }

    # Build and start
    Write-Host "  🏗️  Building and starting application..." -ForegroundColor Yellow
    Write-Host "  This may take a few minutes on first run..." -ForegroundColor Gray
    Write-Host ""

    docker-compose up -d --build

    if ($LASTEXITCODE -eq 0) {
        return $true
    } else {
        Write-Host "  ❌ Failed to start application!" -ForegroundColor Red
        Write-Host "  Check the error messages above for details." -ForegroundColor Yellow
        return $false
    }
}

# Wait for application to be ready
function Wait-ForApplication {
    Write-Host ""
    Write-Host "  ⏳ Waiting for application to be ready..." -ForegroundColor Yellow

    $maxAttempts = 30
    $attempt = 0

    while ($attempt -lt $maxAttempts) {
        try {
            $response = Invoke-WebRequest -Uri "http://localhost:8501/_stcore/health" -TimeoutSec 1 -UseBasicParsing 2>$null
            if ($response.StatusCode -eq 200) {
                Write-Host "  ✅ Application is ready!" -ForegroundColor Green
                return $true
            }
        } catch {
            # Not ready yet
        }

        $attempt++
        Start-Sleep -Seconds 1
        Write-Host "." -NoNewline -ForegroundColor Gray
    }

    Write-Host ""
    Write-Host "  ⚠️  Application is taking longer than expected to start" -ForegroundColor Yellow
    Write-Host "  It may still be initializing. Check the logs with:" -ForegroundColor Gray
    Write-Host "  docker-compose logs -f" -ForegroundColor Cyan
    return $false
}

# Show success message
function Show-Success {
    Write-Host ""
    Write-Host "  ✅ Harbor Docker Learning is running!" -ForegroundColor Green
    Write-Host ""
    Write-Host "  🌐 URL: " -NoNewline -ForegroundColor Cyan
    Write-Host "http://localhost:8501" -ForegroundColor White
    Write-Host ""
    Write-Host "  📋 Useful commands:" -ForegroundColor Yellow
    Write-Host "    docker-compose logs -f       # View live logs" -ForegroundColor Gray
    Write-Host "    docker-compose stop          # Stop application" -ForegroundColor Gray
    Write-Host "    docker-compose down          # Stop and remove containers" -ForegroundColor Gray
    Write-Host "    docker-compose restart       # Restart application" -ForegroundColor Gray
    Write-Host ""
}

# Open browser
function Open-Browser {
    $openBrowser = Read-Host "  Open in browser now? (y/n)"

    if ($openBrowser -eq 'y' -or $openBrowser -eq 'Y' -or $openBrowser -eq '') {
        Write-Host "  🌐 Opening browser..." -ForegroundColor Cyan
        Start-Process "http://localhost:8501"
    }

    Write-Host ""
    Write-Host "  🎉 Happy learning! 🚢" -ForegroundColor Cyan
    Write-Host ""
}

# Main execution
function Main {
    # Show banner
    Show-Banner

    # Check Docker
    if (-not (Test-DockerRunning)) {
        exit 1
    }

    # Check docker-compose.yml
    if (-not (Test-DockerComposeFile)) {
        exit 1
    }

    # Start application
    if (-not (Start-Application)) {
        exit 1
    }

    # Wait for readiness
    $ready = Wait-ForApplication

    # Show success
    Show-Success

    # Open browser
    Open-Browser
}

# Run main function
Main
