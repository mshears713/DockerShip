# 🐳 Docker Build and Testing Guide

**Step 48: Testing Docker Container Build and Run Locally**

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Building the Docker Image](#building-the-docker-image)
3. [Testing the Container](#testing-the-container)
4. [Verification Checklist](#verification-checklist)
5. [Common Issues and Solutions](#common-issues-and-solutions)
6. [Performance Testing](#performance-testing)
7. [Clean Up](#clean-up)

---

## Prerequisites

### Required Software

```bash
# Check Docker installation
docker --version
# Expected: Docker version 20.10.0 or higher

# Check Docker Compose (optional)
docker-compose --version
# Expected: Docker Compose version 2.0.0 or higher
```

### System Requirements

- **RAM:** 2GB minimum, 4GB recommended
- **Disk Space:** 2GB free for image and containers
- **OS:** Linux, macOS, or Windows with WSL2
- **Docker:** Version 20.10+ recommended

---

## Building the Docker Image

### Step 1: Verify Build Context

```bash
# Navigate to project root
cd /path/to/DockerShip

# Verify required files exist
ls -la Dockerfile requirements.txt app.py

# Check what will be included in build (optional)
# This shows files NOT excluded by .dockerignore
find . -type f | grep -v '.git' | grep -v '__pycache__' | head -20
```

**Expected Output:**
```
-rw-r--r-- 1 user user  12345 Nov 17 app.py
-rw-r--r-- 1 user user   6789 Nov 17 Dockerfile
-rw-r--r-- 1 user user   2345 Nov 17 requirements.txt
drwxr-xr-x 2 user user   4096 Nov 17 data/
drwxr-xr-x 2 user user   4096 Nov 17 utils/
```

---

### Step 2: Build the Image

```bash
# Basic build command
docker build -t harbor-docker-learning .

# Build with no cache (fresh build)
docker build --no-cache -t harbor-docker-learning .

# Build with progress output
docker build --progress=plain -t harbor-docker-learning .
```

**Expected Output:**
```
[+] Building 120.5s (12/12) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 1.23kB
 => [internal] load .dockerignore
 => => transferring context: 234B
 => [internal] load metadata for docker.io/library/python:3.11-slim
 => [1/7] FROM docker.io/library/python:3.11-slim
 => [internal] load build context
 => => transferring context: 234.56kB
 => [2/7] WORKDIR /app
 => [3/7] RUN apt-get update && apt-get install -y...
 => [4/7] COPY requirements.txt .
 => [5/7] RUN pip install --no-cache-dir --upgrade pip
 => [6/7] RUN pip install --no-cache-dir -r requirements.txt
 => [7/7] COPY . .
 => exporting to image
 => => exporting layers
 => => writing image sha256:abc123...
 => => naming to docker.io/library/harbor-docker-learning

Successfully built abc123def456
Successfully tagged harbor-docker-learning:latest
```

**Build Time Expectations:**
- First build: 2-5 minutes (downloading base image + packages)
- Subsequent builds: 10-30 seconds (using cached layers)

---

### Step 3: Verify Image Creation

```bash
# List Docker images
docker images harbor-docker-learning

# Check image size and creation date
docker inspect harbor-docker-learning | grep -E '"Size"|"Created"'
```

**Expected Output:**
```
REPOSITORY              TAG       IMAGE ID       CREATED         SIZE
harbor-docker-learning  latest    abc123def456   2 minutes ago   487MB
```

**Image Size Expectations:**
- With python:3.11-slim: ~450-500MB
- With python:3.11-alpine: ~200-250MB
- Actual size depends on dependencies

---

## Testing the Container

### Test 1: Basic Container Start

```bash
# Run container in foreground
docker run -p 8501:8501 harbor-docker-learning

# Or run in detached mode (background)
docker run -d -p 8501:8501 --name harbor-test harbor-docker-learning
```

**Expected Output (Foreground):**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.17.0.2:8501
```

**Expected Output (Detached):**
```
abc123def456789... (container ID)
```

---

### Test 2: Verify Container is Running

```bash
# Check running containers
docker ps

# Check container logs
docker logs harbor-test

# Follow logs in real-time
docker logs -f harbor-test
```

**Expected docker ps Output:**
```
CONTAINER ID   IMAGE                  STATUS         PORTS                    NAMES
abc123def456   harbor-docker-learning Up 2 minutes   0.0.0.0:8501->8501/tcp   harbor-test
```

**Expected Log Output:**
```
Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.17.0.2:8501
```

---

### Test 3: Access the Application

```bash
# Open in browser (macOS)
open http://localhost:8501

# Open in browser (Linux)
xdg-open http://localhost:8501

# Test with curl
curl http://localhost:8501

# Check health endpoint
curl http://localhost:8501/_stcore/health
```

**Expected Curl Output:**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Harbor Docker Learning</title>
    ...
```

**Expected Health Check:**
```json
{"status": "ok"}
```

---

### Test 4: Interactive Testing

Once the app is accessible:

1. **Home Page Loads**
   - Welcome message visible
   - Harbor theme applied (nautical colors)
   - Sidebar navigation present

2. **Tutorial Navigation**
   - Click through different sections
   - Tutorials load correctly
   - Content displays properly

3. **CLI Simulation**
   - Try: `docker ps`
   - Try: `docker run nginx`
   - Verify command validation works
   - Check visual feedback appears

4. **Progress Tracking**
   - Complete a tutorial
   - Verify progress bar updates
   - Check if progress persists (reload page)

---

### Test 5: Container Health Check

```bash
# Check container health status
docker inspect harbor-test | grep -A 5 "Health"

# Wait for health check results (takes ~30 seconds)
sleep 35
docker inspect harbor-test | grep "Health"
```

**Expected Output:**
```json
"Health": {
    "Status": "healthy",
    "FailingStreak": 0,
    "Log": [
        {
            "Start": "2024-01-15T10:30:00Z",
            "End": "2024-01-15T10:30:01Z",
            "ExitCode": 0,
            "Output": ""
        }
    ]
}
```

---

### Test 6: Resource Usage

```bash
# Check container resource usage
docker stats harbor-test --no-stream

# Detailed resource information
docker inspect harbor-test | grep -E '"Memory"|"CPU"'
```

**Expected Stats:**
```
CONTAINER ID   NAME          CPU %     MEM USAGE / LIMIT     MEM %     NET I/O
abc123def456   harbor-test   1.5%      120MiB / 1.95GiB      6.0%      1.2kB / 856B
```

**Expected Resource Usage:**
- **Memory:** 100-200MB (idle)
- **CPU:** 0.5-2% (idle), spikes during interaction
- **Disk:** ~500MB (image size)

---

## Verification Checklist

Use this checklist to ensure the container is working correctly:

### Build Phase
- [ ] Dockerfile builds without errors
- [ ] Build completes in reasonable time (<5 min first time)
- [ ] Image size is reasonable (~450-500MB)
- [ ] No security warnings in build output

### Startup Phase
- [ ] Container starts successfully
- [ ] No error messages in logs
- [ ] Port 8501 is accessible
- [ ] Health check passes (wait 30s)

### Application Phase
- [ ] Home page loads in browser
- [ ] Harbor theme is applied correctly
- [ ] Sidebar navigation works
- [ ] Tutorials load and display
- [ ] CLI simulation accepts commands
- [ ] Command validation works
- [ ] Visual feedback displays
- [ ] Progress tracking functions

### Performance Phase
- [ ] App responds quickly (<2 seconds)
- [ ] Memory usage is reasonable (<300MB)
- [ ] CPU usage is low when idle (<5%)
- [ ] No memory leaks over time

### Persistence Phase
- [ ] Database exists and is populated
- [ ] Tutorials display correctly
- [ ] User progress saves
- [ ] Progress persists after page reload

---

## Common Issues and Solutions

### Issue 1: Build Fails - "No space left on device"

**Error:**
```
ERROR: failed to solve: write /tmp/...: no space left on device
```

**Solution:**
```bash
# Clean up Docker resources
docker system prune -a

# Remove unused images
docker image prune -a

# Check available disk space
df -h
```

---

### Issue 2: Port 8501 Already in Use

**Error:**
```
Error starting userland proxy: listen tcp4 0.0.0.0:8501: bind: address already in use
```

**Solution:**
```bash
# Find what's using the port
lsof -i :8501
# or
netstat -tulpn | grep 8501

# Use a different port
docker run -p 8502:8501 harbor-docker-learning

# Or stop the conflicting service
docker stop $(docker ps -q --filter "publish=8501")
```

---

### Issue 3: Container Starts but App Not Accessible

**Symptoms:** Container running, but http://localhost:8501 times out

**Troubleshooting:**
```bash
# Check if Streamlit is actually running
docker logs harbor-test

# Verify port mapping is correct
docker port harbor-test

# Check if app is listening on correct address
docker exec harbor-test netstat -tlnp | grep 8501
```

**Solution:**
- Verify STREAMLIT_SERVER_ADDRESS=0.0.0.0 in Dockerfile
- Check firewall settings
- Try accessing via container IP directly

---

### Issue 4: Database Not Initialized

**Symptoms:** App loads but shows no tutorials

**Solution:**
```bash
# Check if database exists
docker exec harbor-test ls -l /app/data/

# Manually initialize database
docker exec harbor-test python -c "from data.database import init_database; from data.seed_data import seed_database; init_database(); seed_database()"

# Restart container
docker restart harbor-test
```

---

### Issue 5: Permission Denied Errors

**Error:**
```
PermissionError: [Errno 13] Permission denied: '/app/data/tutorials.sqlite'
```

**Solution:**
```bash
# Check file permissions in container
docker exec harbor-test ls -la /app/data/

# Rebuild with proper ownership
# (Already handled in Dockerfile with chown command)
docker build --no-cache -t harbor-docker-learning .
```

---

### Issue 6: Health Check Failing

**Symptoms:** Container status shows "unhealthy"

**Troubleshooting:**
```bash
# Check health check logs
docker inspect harbor-test | jq '.[0].State.Health.Log'

# Test health endpoint manually
docker exec harbor-test curl http://localhost:8501/_stcore/health

# Check Streamlit is running
docker exec harbor-test ps aux | grep streamlit
```

---

## Performance Testing

### Load Testing

```bash
# Install Apache Bench (if needed)
apt-get install apache2-utils

# Perform basic load test
ab -n 100 -c 10 http://localhost:8501/

# Monitor during load test (in another terminal)
docker stats harbor-test
```

**Expected Results:**
- Requests per second: 10-50 (depends on hardware)
- No errors or timeouts
- Memory stays under 500MB
- CPU spikes but recovers

---

### Memory Leak Testing

```bash
# Monitor memory over time
watch -n 5 'docker stats harbor-test --no-stream'

# Interact with app extensively for 10 minutes
# Check if memory keeps growing or stabilizes

# Memory should stabilize around 150-300MB
```

---

### Startup Time Testing

```bash
# Test cold start time
time docker run -d -p 8501:8501 --name startup-test harbor-docker-learning

# Wait for healthy status
while [ "$(docker inspect -f '{{.State.Health.Status}}' startup-test)" != "healthy" ]; do
    echo "Waiting for healthy status..."
    sleep 5
done

echo "Container is healthy!"
```

**Expected Startup Time:**
- Container start: <2 seconds
- App ready: 5-10 seconds
- Health check passes: 30-35 seconds

---

## Clean Up

### Remove Test Container

```bash
# Stop container
docker stop harbor-test

# Remove container
docker rm harbor-test

# One-liner: stop and remove
docker rm -f harbor-test
```

---

### Remove Image

```bash
# Remove image
docker rmi harbor-docker-learning

# Force remove (even if containers exist)
docker rmi -f harbor-docker-learning
```

---

### Complete Cleanup

```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Remove everything (careful!)
docker system prune -a --volumes
```

---

## Test Automation Script

Save this as `test-docker.sh`:

```bash
#!/bin/bash
set -e

echo "🚢 Harbor Docker Learning - Automated Testing"
echo "=============================================="

# Build image
echo "📦 Building Docker image..."
docker build -t harbor-docker-learning .

# Start container
echo "🚀 Starting container..."
CONTAINER_ID=$(docker run -d -p 8501:8501 --name harbor-test harbor-docker-learning)
echo "Container ID: $CONTAINER_ID"

# Wait for startup
echo "⏳ Waiting for application to start..."
sleep 10

# Test health endpoint
echo "🏥 Testing health endpoint..."
HEALTH=$(curl -s http://localhost:8501/_stcore/health)
echo "Health check: $HEALTH"

# Test home page
echo "🏠 Testing home page..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8501)
echo "HTTP Status: $HTTP_CODE"

if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Tests failed! HTTP code: $HTTP_CODE"
    exit 1
fi

# Cleanup
echo "🧹 Cleaning up..."
docker stop harbor-test
docker rm harbor-test

echo "🎉 Testing complete!"
```

Run with:
```bash
chmod +x test-docker.sh
./test-docker.sh
```

---

## Success Criteria

The Docker build and deployment is considered successful if:

✅ **Build Phase:**
- Image builds without errors
- Build time is reasonable (<5 minutes)
- No security warnings
- Image size is acceptable (~450-500MB)

✅ **Runtime Phase:**
- Container starts successfully
- Application accessible on port 8501
- Health checks pass
- No error messages in logs

✅ **Functionality Phase:**
- All tutorials display correctly
- CLI simulation works
- Progress tracking functions
- Harbor theme renders properly

✅ **Performance Phase:**
- Memory usage stays under 300MB
- CPU usage is low when idle
- App responds quickly
- No memory leaks

✅ **Reliability Phase:**
- Container runs for extended period without issues
- Health checks continue passing
- No crashes or restarts needed

---

## Next Steps

After successful testing:

1. **Tag for Production:**
   ```bash
   docker tag harbor-docker-learning:latest harbor-docker-learning:v1.0.0
   ```

2. **Push to Registry** (optional):
   ```bash
   docker tag harbor-docker-learning yourusername/harbor-docker-learning:latest
   docker push yourusername/harbor-docker-learning:latest
   ```

3. **Deploy to Production:**
   - See DEPLOYMENT.md for deployment instructions
   - Configure monitoring and logging
   - Set up automated backups

---

**Testing Status: ✅ DOCUMENTED**

*This testing guide provides comprehensive procedures for validating the Docker container build and deployment.*

*Last Updated: Phase 5, Step 48*
