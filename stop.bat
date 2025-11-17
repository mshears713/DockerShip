@echo off
REM ============================================================================
REM Harbor Docker Learning - Windows Batch Stop Script
REM ============================================================================
REM
REM This script stops the Harbor Docker Learning application
REM Run: stop.bat
REM
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo   [33m🛑 Stopping Harbor Docker Learning...[0m
echo.

REM Check if Docker is running
docker version >nul 2>&1
if errorlevel 1 (
    echo   [33m⚠️  Docker is not running[0m
    echo   [90mThe application is likely already stopped.[0m
    echo.
    pause
    exit /b 0
)

REM Ask user what they want to do
echo   [36mHow do you want to stop the application?[0m
echo.
echo   [97m1) Stop (containers remain, can be quickly restarted)[0m
echo   [97m2) Stop and remove (clean shutdown, keeps data)[0m
echo   [97m3) Stop and remove everything (including data - fresh start)[0m
echo   [97m4) Cancel[0m
echo.

set /p CHOICE="  Enter choice (1-4): "

if "!CHOICE!"=="1" goto :stop
if "!CHOICE!"=="2" goto :down
if "!CHOICE!"=="3" goto :down_volumes
if "!CHOICE!"=="4" goto :cancel

echo   [31m❌ Invalid choice[0m
echo.
pause
exit /b 1

:stop
echo.
echo   [33m⏸️  Stopping containers...[0m
docker-compose stop

if not errorlevel 1 (
    echo   [32m✅ Application stopped[0m
    echo   [90mTo restart: docker-compose start[0m
) else (
    echo   [31m❌ Failed to stop containers[0m
)
echo.
pause
exit /b 0

:down
echo.
echo   [33m🛑 Stopping and removing containers...[0m
docker-compose down

if not errorlevel 1 (
    echo   [32m✅ Application stopped and removed[0m
    echo   [90mYour data is preserved in Docker volumes[0m
    echo   [90mTo restart: docker-compose up -d[0m
) else (
    echo   [31m❌ Failed to stop and remove containers[0m
)
echo.
pause
exit /b 0

:down_volumes
echo.
echo   [31m⚠️  This will delete ALL application data![0m
set /p CONFIRM="  Are you sure? (yes/no): "

if not "!CONFIRM!"=="yes" (
    echo   [33m❌ Cancelled[0m
    echo.
    pause
    exit /b 0
)

echo.
echo   [33m🗑️  Stopping and removing everything...[0m
docker-compose down -v

if not errorlevel 1 (
    echo   [32m✅ Application and data completely removed[0m
    echo   [90mTo start fresh: docker-compose up -d --build[0m
) else (
    echo   [31m❌ Failed to remove everything[0m
)
echo.
pause
exit /b 0

:cancel
echo.
echo   [33m❌ Cancelled[0m
echo.
pause
exit /b 0
