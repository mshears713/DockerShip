@echo off
REM ============================================================================
REM Harbor Docker Learning - Windows Batch Quick Start Script
REM ============================================================================
REM
REM This script makes it easy to start Harbor Docker Learning on Windows
REM Just double-click this file or run: start.bat
REM
REM ============================================================================

setlocal enabledelayedexpansion

REM Display banner
echo.
echo   [36m🚢 Harbor Docker Learning - Quick Start[0m
echo   [36m=========================================[0m
echo.

REM Check if Docker is running
echo   [33mChecking Docker status...[0m
docker version >nul 2>&1
if errorlevel 1 (
    echo   [31m❌ Docker is not running![0m
    echo.
    echo   [33mPlease start Docker Desktop and try again.[0m
    echo   [90mOn Windows, look for the whale icon in your system tray.[0m
    echo.
    echo   [33mDon't have Docker Desktop?[0m
    echo   [90mDownload from: https://www.docker.com/products/docker-desktop/[0m
    echo.
    pause
    exit /b 1
)

echo   [32m✅ Docker is running[0m

REM Check if docker-compose.yml exists
if not exist "docker-compose.yml" (
    echo   [31m❌ docker-compose.yml not found![0m
    echo   [33mPlease run this script from the project directory.[0m
    echo.
    pause
    exit /b 1
)

echo   [32m✅ Found docker-compose.yml[0m
echo.

REM Check for existing container
echo   [33mChecking for existing containers...[0m
docker ps -a --filter "name=harbor-docker-learning" --format "{{.Names}}" >nul 2>&1
if not errorlevel 1 (
    echo   [36mFound existing container[0m
    echo   [33mStarting container...[0m
    docker-compose start

    if not errorlevel 1 (
        goto :success
    ) else (
        echo   [33m⚠️  Failed to start existing container[0m
        echo   [33m🏗️  Rebuilding...[0m
    )
)

REM Build and start
echo   [33m🏗️  Building and starting application...[0m
echo   [90mThis may take a few minutes on first run...[0m
echo.

docker-compose up -d --build

if errorlevel 1 (
    echo   [31m❌ Failed to start application![0m
    echo   [33mCheck the error messages above for details.[0m
    echo.
    pause
    exit /b 1
)

:success
echo.
echo   [33m⏳ Waiting for application to be ready...[0m

REM Wait for application (simple wait since we can't easily check health in batch)
timeout /t 5 /nobreak >nul

echo.
echo   [32m✅ Harbor Docker Learning is running![0m
echo.
echo   [36m🌐 URL: [0mhttp://localhost:8501
echo.
echo   [33m📋 Useful commands:[0m
echo   [90m  docker-compose logs -f       # View live logs[0m
echo   [90m  docker-compose stop          # Stop application[0m
echo   [90m  docker-compose down          # Stop and remove containers[0m
echo   [90m  docker-compose restart       # Restart application[0m
echo.

REM Ask to open browser
set /p OPEN_BROWSER="  Open in browser now? (y/n): "
if /i "!OPEN_BROWSER!"=="y" (
    echo   [36m🌐 Opening browser...[0m
    start http://localhost:8501
)

echo.
echo   [36m🎉 Happy learning! 🚢[0m
echo.
pause
