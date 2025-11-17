# 🪟 Harbor Docker Learning - Windows Setup Guide

Complete guide to running Harbor Docker Learning on your Windows laptop using Docker.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Running with Docker Compose](#running-with-docker-compose)
4. [Running with Docker CLI](#running-with-docker-cli)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)
7. [Advanced Configuration](#advanced-configuration)

---

## 🎯 Prerequisites

### Required Software

1. **Docker Desktop for Windows**
   - Download from: https://www.docker.com/products/docker-desktop/
   - Version: 4.0 or higher
   - Requires: Windows 10 64-bit or Windows 11

2. **WSL 2** (Windows Subsystem for Linux 2)
   - Recommended for best performance
   - Docker Desktop will prompt you to install it
   - Guide: https://docs.microsoft.com/en-us/windows/wsl/install

3. **Git for Windows** (optional, for cloning repository)
   - Download from: https://git-scm.com/download/win

### System Requirements

- **OS**: Windows 10 64-bit (Pro, Enterprise, or Education) Build 19041 or higher, or Windows 11
- **RAM**: Minimum 4 GB, recommended 8 GB or more
- **Disk**: At least 10 GB free space
- **CPU**: 64-bit processor with Second Level Address Translation (SLAT)
- **Virtualization**: Hardware virtualization must be enabled in BIOS

---

## 🚀 Installation Steps

### Step 1: Install Docker Desktop

1. **Download Docker Desktop**
   ```
   https://www.docker.com/products/docker-desktop/
   ```

2. **Run the installer**
   - Double-click `Docker Desktop Installer.exe`
   - Follow the installation wizard
   - Check "Use WSL 2 instead of Hyper-V" (recommended)

3. **Start Docker Desktop**
   - Docker Desktop may require a system restart
   - After restart, launch Docker Desktop from Start Menu
   - Wait for Docker to start (whale icon in system tray turns steady)

4. **Verify Installation**

   Open PowerShell or Command Prompt and run:
   ```powershell
   docker --version
   docker-compose --version
   ```

   You should see version information for both commands.

### Step 2: Get the Application

#### Option A: Clone from Git (Recommended)

```powershell
# Clone the repository
git clone https://github.com/yourusername/DockerShip.git

# Navigate into the directory
cd DockerShip
```

#### Option B: Download ZIP

1. Download the ZIP file from GitHub
2. Extract to a folder (e.g., `C:\Users\YourName\DockerShip`)
3. Open PowerShell and navigate to the folder:
   ```powershell
   cd C:\Users\YourName\DockerShip
   ```

---

## 🐳 Running with Docker Compose (Recommended)

Docker Compose is the easiest way to run the application on Windows.

### Quick Start

```powershell
# Start the application (first time will download and build)
docker-compose up
```

The application will be available at: **http://localhost:8501**

Press `Ctrl+C` to stop the application.

### Common Docker Compose Commands

```powershell
# Start in background (detached mode)
docker-compose up -d

# View logs
docker-compose logs

# Follow logs in real-time
docker-compose logs -f

# Stop the application
docker-compose down

# Stop and remove all data (fresh start)
docker-compose down -v

# Rebuild after code changes
docker-compose up --build

# Check status
docker-compose ps

# View resource usage
docker-compose stats
```

### Running on a Different Port

If port 8501 is already in use, edit `docker-compose.yml`:

```yaml
ports:
  - "8080:8501"  # Change 8080 to any available port
```

Then access at: http://localhost:8080

---

## 🛠️ Running with Docker CLI

If you prefer to use Docker commands directly:

### Build the Image

```powershell
docker build -t harbor-docker-learning .
```

### Run the Container

```powershell
# Run in foreground (logs visible)
docker run -p 8501:8501 harbor-docker-learning

# Run in background
docker run -d -p 8501:8501 --name harbor-app harbor-docker-learning

# Run with persistent data
docker run -d -p 8501:8501 -v harbor-data:/app/data --name harbor-app harbor-docker-learning
```

### Managing the Container

```powershell
# View running containers
docker ps

# View all containers (including stopped)
docker ps -a

# View logs
docker logs harbor-app

# Follow logs in real-time
docker logs -f harbor-app

# Stop the container
docker stop harbor-app

# Start the container
docker start harbor-app

# Restart the container
docker restart harbor-app

# Remove the container
docker rm harbor-app

# Remove the container and volume
docker rm -v harbor-app
```

### Accessing Container Shell

```powershell
# Open bash shell in running container
docker exec -it harbor-app /bin/bash

# Run a single command
docker exec harbor-app ls -la /app
```

---

## 🔧 Troubleshooting

### Issue: Docker Desktop won't start

**Symptoms**: Docker Desktop shows "Docker Engine starting..." forever

**Solutions**:
1. **Enable WSL 2**:
   - Open PowerShell as Administrator
   ```powershell
   wsl --install
   wsl --set-default-version 2
   ```
   - Restart your computer

2. **Enable Virtualization in BIOS**:
   - Restart computer and enter BIOS (usually F2, F10, or Delete during boot)
   - Look for "Virtualization Technology" or "Intel VT-x" or "AMD-V"
   - Enable it and save changes

3. **Reset Docker Desktop**:
   - Right-click Docker icon in system tray
   - Select "Troubleshoot"
   - Click "Reset to factory defaults"

### Issue: Port 8501 already in use

**Symptoms**: Error "Bind for 0.0.0.0:8501 failed: port is already allocated"

**Solutions**:
1. **Find what's using the port**:
   ```powershell
   netstat -ano | findstr :8501
   ```

2. **Use a different port**:
   ```powershell
   docker run -p 8080:8501 harbor-docker-learning
   ```
   Access at http://localhost:8080

3. **Stop the conflicting application** or use Docker Compose with modified ports

### Issue: Slow performance

**Symptoms**: Container runs slowly, high CPU usage

**Solutions**:
1. **Enable WSL 2 Backend**:
   - Docker Desktop → Settings → General
   - Check "Use the WSL 2 based engine"
   - Click "Apply & Restart"

2. **Increase Resources**:
   - Docker Desktop → Settings → Resources
   - Increase Memory to 4 GB or more
   - Increase CPUs to 2 or more
   - Click "Apply & Restart"

3. **Store files in WSL filesystem**:
   - Move project to WSL: `\\wsl$\Ubuntu\home\youruser\DockerShip`
   - Much faster than Windows filesystem

### Issue: Cannot connect to Docker daemon

**Symptoms**: "Cannot connect to the Docker daemon at unix:///var/run/docker.sock"

**Solutions**:
1. **Start Docker Desktop**:
   - Open Docker Desktop from Start Menu
   - Wait for whale icon to become steady

2. **Check Docker Service**:
   - Open Services (Win+R, type `services.msc`)
   - Find "Docker Desktop Service"
   - Ensure it's Running

### Issue: Firewall blocking Docker

**Symptoms**: Firewall prompts when starting Docker

**Solution**:
- Click "Allow access" when Windows Firewall prompts
- Or manually allow in Firewall settings:
  - Control Panel → Windows Defender Firewall → Allow an app
  - Find Docker Desktop and check Private and Public networks

### Issue: WSL 2 installation required

**Symptoms**: Docker Desktop asks to install WSL 2 update

**Solution**:
1. Download WSL2 Linux kernel update package:
   ```
   https://aka.ms/wsl2kernel
   ```
2. Run the installer
3. Restart Docker Desktop

### Issue: Build fails with network errors

**Symptoms**: "failed to fetch metadata" or "download failed"

**Solutions**:
1. **Check internet connection**
2. **Configure Docker DNS**:
   - Docker Desktop → Settings → Docker Engine
   - Add to JSON config:
   ```json
   {
     "dns": ["8.8.8.8", "8.8.4.4"]
   }
   ```
   - Click "Apply & Restart"

### Issue: Volume permissions errors

**Symptoms**: "Permission denied" when accessing files

**Solution**:
- In Docker Desktop → Settings → Resources → File Sharing
- Add your project directory to shared paths
- Click "Apply & Restart"

---

## ❓ FAQ

### Do I need to install Python?

**No!** Docker containers include everything needed. Python and all dependencies are inside the container.

### Can I modify the code while container is running?

**Yes**, but you need to use a bind mount:
```powershell
docker run -p 8501:8501 -v ${PWD}:/app harbor-docker-learning
```
Changes to code will be reflected immediately (Streamlit has auto-reload).

### Where is my data stored?

- **Named volumes**: `C:\ProgramData\docker\volumes\`
- **Bind mounts**: Your specified Windows directory
- **Inside container**: Data is lost when container is removed (unless using volumes)

### How do I update to the latest version?

```powershell
# Pull latest code
git pull

# Rebuild container
docker-compose up --build
```

### Can I run multiple instances?

**Yes**, but they need different ports:
```powershell
# First instance
docker run -d -p 8501:8501 --name harbor-1 harbor-docker-learning

# Second instance
docker run -d -p 8502:8501 --name harbor-2 harbor-docker-learning
```

### How much disk space does this use?

- **Base image**: ~200 MB
- **Application**: ~50 MB
- **Total**: ~250-300 MB

### How do I completely remove everything?

```powershell
# Stop and remove containers
docker-compose down -v

# Remove images
docker rmi harbor-docker-learning

# Remove unused data
docker system prune -a --volumes
```

---

## ⚙️ Advanced Configuration

### Using Environment Variables

Create a `.env` file in the project directory:

```env
# Application Settings
STREAMLIT_SERVER_PORT=8501
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Custom Settings
APP_ENV=production
DEBUG=false
```

Then use in `docker-compose.yml`:
```yaml
services:
  harbor-app:
    env_file:
      - .env
```

### Custom Volume Location

To store data in a specific Windows folder:

**Edit docker-compose.yml**:
```yaml
volumes:
  - C:\docker-data\harbor:/app/data
```

Or use PowerShell variable:
```yaml
volumes:
  - ${USERPROFILE}\docker-data\harbor:/app/data
```

### Resource Limits

Limit container resources in `docker-compose.yml`:

```yaml
deploy:
  resources:
    limits:
      cpus: '1.0'
      memory: 512M
    reservations:
      cpus: '0.5'
      memory: 256M
```

### Using Specific Python Version

Edit `Dockerfile`, line 19:
```dockerfile
FROM python:3.11-slim    # Change to 3.9, 3.10, 3.12, etc.
```

Then rebuild:
```powershell
docker-compose up --build
```

### Automated Backups

Create a backup script `backup.ps1`:

```powershell
# Backup Docker volume
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupDir = "C:\docker-backups"

# Create backup directory
New-Item -ItemType Directory -Force -Path $backupDir

# Export volume data
docker run --rm -v harbor-data:/data -v ${backupDir}:/backup `
  ubuntu tar czf /backup/harbor-backup-${timestamp}.tar.gz -C /data .

Write-Host "Backup created: harbor-backup-${timestamp}.tar.gz"
```

Run with:
```powershell
.\backup.ps1
```

### Auto-Start on Windows Boot

1. **Create startup shortcut**:
   - Open folder: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
   - Create shortcut to Docker Desktop

2. **Create startup script** (`start-harbor.bat`):
   ```batch
   @echo off
   cd C:\Users\YourName\DockerShip
   docker-compose up -d
   ```

3. **Add to Task Scheduler**:
   - Open Task Scheduler
   - Create Basic Task
   - Trigger: At startup
   - Action: Start a program → `start-harbor.bat`

---

## 🎓 Learning Resources

### Docker Commands Cheat Sheet

```powershell
# Images
docker images                     # List images
docker pull <image>              # Download image
docker rmi <image>               # Remove image
docker build -t <name> .         # Build image

# Containers
docker ps                        # List running containers
docker ps -a                     # List all containers
docker run <image>               # Create and start container
docker start <container>         # Start stopped container
docker stop <container>          # Stop running container
docker restart <container>       # Restart container
docker rm <container>            # Remove container
docker logs <container>          # View logs
docker exec -it <container> bash # Shell access

# System
docker system df                 # Show disk usage
docker system prune              # Remove unused data
docker stats                     # Show resource usage

# Docker Compose
docker-compose up                # Start services
docker-compose down              # Stop services
docker-compose ps                # List services
docker-compose logs              # View logs
docker-compose build             # Build images
docker-compose restart           # Restart services
```

### Useful Docker Desktop Features

1. **Dashboard**:
   - View all containers, images, volumes
   - Start/stop containers with GUI
   - Access logs and stats

2. **Volumes Tab**:
   - Browse volume contents
   - Delete unused volumes
   - Export/import data

3. **Dev Environments**:
   - Quick setup for development
   - Integrated with Git

4. **Extensions**:
   - Install helpful Docker extensions
   - Resource monitor, disk usage analyzer, etc.

### Official Documentation

- Docker Desktop: https://docs.docker.com/desktop/windows/
- Docker Compose: https://docs.docker.com/compose/
- Dockerfile Reference: https://docs.docker.com/engine/reference/builder/
- WSL 2: https://docs.microsoft.com/en-us/windows/wsl/

---

## 🎉 Quick Start Script

Save this as `start.ps1` in your project directory:

```powershell
#!/usr/bin/env pwsh

Write-Host "🚢 Harbor Docker Learning - Quick Start" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Docker is running
$dockerStatus = docker version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Docker is not running!" -ForegroundColor Red
    Write-Host "Please start Docker Desktop and try again." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Docker is running" -ForegroundColor Green

# Check if container exists
$existingContainer = docker ps -a --filter "name=harbor-docker-learning" --format "{{.Names}}"

if ($existingContainer) {
    Write-Host "📦 Found existing container" -ForegroundColor Yellow
    Write-Host "Starting..." -ForegroundColor Yellow
    docker-compose start
} else {
    Write-Host "🏗️  Building and starting application..." -ForegroundColor Yellow
    docker-compose up -d --build
}

Write-Host ""
Write-Host "✅ Application is running!" -ForegroundColor Green
Write-Host "🌐 Open your browser to: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Commands:" -ForegroundColor Yellow
Write-Host "  docker-compose logs -f    # View logs" -ForegroundColor Gray
Write-Host "  docker-compose stop       # Stop application" -ForegroundColor Gray
Write-Host "  docker-compose down       # Stop and remove" -ForegroundColor Gray
Write-Host ""

# Optional: Open browser automatically
$openBrowser = Read-Host "Open browser now? (y/n)"
if ($openBrowser -eq 'y') {
    Start-Process "http://localhost:8501"
}
```

Run with:
```powershell
.\start.ps1
```

---

## 🆘 Getting Help

If you encounter issues not covered here:

1. **Check Docker Desktop logs**:
   - Click whale icon → Troubleshoot → View logs

2. **Check application logs**:
   ```powershell
   docker-compose logs
   ```

3. **Search GitHub Issues**:
   - Project repository issues page

4. **Docker Community**:
   - Docker Forums: https://forums.docker.com/
   - Stack Overflow: Tag `docker` and `docker-compose`

5. **Windows-specific Docker issues**:
   - Docker Desktop for Windows GitHub: https://github.com/docker/for-win/issues

---

## ✅ Verification Checklist

Before reporting issues, verify:

- [ ] Docker Desktop is installed and running
- [ ] WSL 2 is enabled (check Docker Desktop settings)
- [ ] Virtualization is enabled in BIOS
- [ ] No errors in Docker Desktop logs
- [ ] Port 8501 is available (or using alternative port)
- [ ] Internet connection is working (for first build)
- [ ] Antivirus/firewall allows Docker
- [ ] Sufficient disk space (at least 10 GB free)
- [ ] You're in the correct directory (contains `docker-compose.yml`)

---

**🎉 That's it! You're ready to learn Docker on Windows!**

If everything is working, open http://localhost:8501 and start your container learning journey! 🚢
