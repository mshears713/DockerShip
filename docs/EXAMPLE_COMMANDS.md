# 🐳 Harbor Docker Learning - Example Command Sessions

**Pre-written Docker CLI Sessions for Practice and Reference**

---

## 📋 Table of Contents

1. [Session 1: Getting Started with Containers](#session-1-getting-started-with-containers)
2. [Session 2: Managing Container Lifecycle](#session-2-managing-container-lifecycle)
3. [Session 3: Working with Images](#session-3-working-with-images)
4. [Session 4: Advanced Container Operations](#session-4-advanced-container-operations)
5. [Session 5: Real-World Scenarios](#session-5-real-world-scenarios)
6. [Session 6: Troubleshooting Common Issues](#session-6-troubleshooting-common-issues)
7. [Quick Reference Commands](#quick-reference-commands)

---

## Session 1: Getting Started with Containers

**Objective:** Learn the most basic Docker commands
**Duration:** 10 minutes
**Difficulty:** Beginner

### Commands to Try

```bash
# 1. Check if Docker is working (this is simulated in Harbor Docker Learning)
docker ps
```

**Expected Output:**
```
✅ Command executed successfully!

🌊 Checking the harbor for ships...

CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
(No containers are currently running)

🏗️ Harbor Metaphor: You're looking at an empty harbor - no ships sailing yet!
```

**Explanation:**
- `docker ps` shows running containers
- Empty result means no containers are active
- Like looking at a harbor with no ships

---

```bash
# 2. Run your first container
docker run nginx
```

**Expected Output:**
```
🎉 Success! Container created and started!

🚢 Launching a new ship from the Nginx blueprint...
⛵ Container is now sailing in the harbor!

Container Details:
- Image: nginx
- Status: Running
- Container ID: abc123def456

🏗️ Harbor Metaphor: You just built and launched a ship from the Nginx blueprint!
It's now actively sailing and ready to serve web pages.
```

**Explanation:**
- `docker run` creates AND starts a container
- nginx is a popular web server image
- Container runs in the foreground by default

---

```bash
# 3. List running containers again
docker ps
```

**Expected Output:**
```
✅ Viewing active ships in the harbor...

CONTAINER ID   IMAGE    COMMAND                 CREATED        STATUS        PORTS
abc123def456   nginx    "nginx -g 'daemon..."   1 minute ago   Up 1 minute   80/tcp

🏗️ Harbor Metaphor: You can see your Nginx ship sailing!
It's listening on port 80, ready to handle web traffic.
```

**Explanation:**
- Now you see your running container
- Shows container ID, image, status, and ports
- Think of it as a harbor manifest

---

```bash
# 4. View ALL containers (including stopped)
docker ps -a
```

**Expected Output:**
```
✅ Viewing ALL ships in the harbor (active and anchored)...

CONTAINER ID   IMAGE    COMMAND                 CREATED        STATUS            PORTS
abc123def456   nginx    "nginx -g 'daemon..."   2 minutes ago  Up 2 minutes      80/tcp
def789ghi012   nginx    "nginx -g 'daemon..."   5 minutes ago  Exited (0) 3 mins

🏗️ Harbor Metaphor: The -a flag shows BOTH sailing ships and anchored ones!
```

**Explanation:**
- `-a` flag = "all containers"
- Includes stopped (Exited) containers
- Stopped containers still exist, just not running

---

### Session 1 Summary

**Commands Learned:**
- ✅ `docker ps` - List running containers
- ✅ `docker ps -a` - List all containers
- ✅ `docker run <image>` - Create and start container

**Key Concepts:**
- Containers can be running or stopped
- `docker run` combines create + start
- Container IDs uniquely identify each container

---

## Session 2: Managing Container Lifecycle

**Objective:** Learn to control container states
**Duration:** 15 minutes
**Difficulty:** Beginner-Intermediate

### Commands to Try

```bash
# 1. Run a container in detached mode (background)
docker run -d nginx
```

**Expected Output:**
```
✅ Container started in detached mode!

🚢 Ship launched in the background...
Container ID: hij456klm789

🏗️ Harbor Metaphor: The -d flag means "detached" - the ship sails independently
without you watching it constantly. You can go do other things!
```

**Explanation:**
- `-d` = detached mode
- Container runs in background
- Returns immediately with container ID
- Like setting a ship on autopilot

---

```bash
# 2. Stop a running container
docker stop hij456klm789
```

**Expected Output:**
```
✅ Container stopped successfully!

⚓ Dropping anchor...
Container hij456klm789 has been stopped.

Status: Running → Stopped
The container still exists, just not active.

🏗️ Harbor Metaphor: You've anchored the ship. It's not sailing anymore,
but it's still in the harbor and can set sail again later!
```

**Explanation:**
- `docker stop` gracefully stops a container
- Container still exists (not deleted)
- Can be restarted later
- Like anchoring a ship

---

```bash
# 3. Verify the container is stopped
docker ps
docker ps -a
```

**Expected Output:**
```
# docker ps
(No running containers)

# docker ps -a
CONTAINER ID   IMAGE   STATUS              CREATED
hij456klm789   nginx   Exited (0) 10s ago  2 minutes ago

🏗️ Harbor Metaphor:
- docker ps = Show sailing ships only
- docker ps -a = Show ALL ships (sailing + anchored)
```

**Explanation:**
- Stopped container disappears from `docker ps`
- But appears in `docker ps -a`
- Status shows "Exited"

---

```bash
# 4. Restart the stopped container
docker start hij456klm789
```

**Expected Output:**
```
✅ Container restarted!

⛵ Lifting anchor... Ship is sailing again!
Container hij456klm789 is now running.

Status: Stopped → Running

🏗️ Harbor Metaphor: The ship sets sail again! Same ship, same cargo,
just resuming its journey from where it stopped.
```

**Explanation:**
- `docker start` restarts a stopped container
- Same container, same state
- Quick restart (no rebuild needed)

---

```bash
# 5. Restart command (stop + start in one)
docker restart hij456klm789
```

**Expected Output:**
```
✅ Container restarted!

🔄 Anchoring ship... then immediately setting sail again!

Container hij456klm789:
1. Stopped gracefully
2. Started again
All in one command!

🏗️ Harbor Metaphor: Quick maintenance - anchor briefly, then sail again.
```

**Explanation:**
- `docker restart` = stop + start
- Useful for applying configuration changes
- Like a quick service restart

---

```bash
# 6. Remove a stopped container
docker rm hij456klm789
```

**Expected Output:**
```
⚠️  Error: Container is still running!

Cannot remove running container hij456klm789.

💡 Solution: Stop it first, or use -f flag to force removal.

Try:
  docker stop hij456klm789
  docker rm hij456klm789

Or:
  docker rm -f hij456klm789
```

**Explanation:**
- Can't remove running containers (safety feature)
- Must stop first OR use force flag
- Good practice: stop gracefully first

---

```bash
# 7. Stop and remove
docker stop hij456klm789
docker rm hij456klm789
```

**Expected Output:**
```
✅ Container stopped!
⚓ Ship anchored.

✅ Container removed!
🗑️ Ship has been decommissioned and removed from the harbor.

Container hij456klm789 no longer exists.

🏗️ Harbor Metaphor: The ship is scrapped. To sail this route again,
you'll need to build a new ship from the blueprint (docker run).
```

**Explanation:**
- Two-step removal: stop, then remove
- Container completely deleted
- Free up resources
- Like scrapping a ship

---

```bash
# 8. Force remove (shortcut)
docker run -d nginx
# Get container ID: nop890qrs123
docker rm -f nop890qrs123
```

**Expected Output:**
```
✅ Container force-removed!

🗑️ Ship forcefully decommissioned and scrapped!

Container nop890qrs123:
1. Was forcefully stopped
2. Immediately removed
All in one command!

⚠️  Warning: Force removal doesn't allow graceful shutdown.
Use sparingly - prefer stopping first when possible.
```

**Explanation:**
- `-f` = force flag
- Stops AND removes in one command
- Less graceful but faster
- Use when container is stuck

---

### Session 2 Summary

**Commands Learned:**
- ✅ `docker run -d <image>` - Run in background
- ✅ `docker stop <id>` - Stop container
- ✅ `docker start <id>` - Restart stopped container
- ✅ `docker restart <id>` - Stop and start
- ✅ `docker rm <id>` - Remove stopped container
- ✅ `docker rm -f <id>` - Force remove

**Container Lifecycle:**
```
Created → Running → Stopped → Removed
   ↓         ↓          ↓
   └─────────┴──────────┘
   (Can restart at any stopped stage)
```

---

## Session 3: Working with Images

**Objective:** Understand and manage Docker images
**Duration:** 15 minutes
**Difficulty:** Intermediate

### Commands to Try

```bash
# 1. List available images
docker images
```

**Expected Output:**
```
✅ Listing ship blueprints in your shipyard...

REPOSITORY   TAG      IMAGE ID      CREATED       SIZE
nginx        latest   abc123def456  2 weeks ago   142MB

🏗️ Harbor Metaphor: These are the blueprints you have available
to build ships from. Each blueprint can create unlimited ships!
```

**Explanation:**
- Shows images stored locally
- Images are templates for containers
- Like a collection of ship blueprints

---

```bash
# 2. Pull a new image
docker pull redis
```

**Expected Output:**
```
✅ Downloading new ship blueprint!

📦 Pulling redis image from Docker Hub...
⬇️  Downloading layers...
   Layer 1/5 ████████████████ 100%
   Layer 2/5 ████████████████ 100%
   Layer 3/5 ████████████████ 100%
   Layer 4/5 ████████████████ 100%
   Layer 5/5 ████████████████ 100%

✅ Download complete!

🏗️ Harbor Metaphor: You've acquired a new ship blueprint (Redis)
from the central shipyard (Docker Hub). Ready to build ships from it!
```

**Explanation:**
- `docker pull` downloads an image
- Images come from Docker Hub (default registry)
- Downloading in layers (more efficient)

---

```bash
# 3. List images again
docker images
```

**Expected Output:**
```
✅ Ship blueprints available:

REPOSITORY   TAG      IMAGE ID      CREATED       SIZE
nginx        latest   abc123def456  2 weeks ago   142MB
redis        latest   def789ghi012  1 week ago    113MB

🏗️ Harbor Metaphor: Your blueprint collection is growing!
You can now build both Nginx ships and Redis ships.
```

---

```bash
# 4. Pull specific version (tag)
docker pull nginx:alpine
```

**Expected Output:**
```
✅ Downloading specific blueprint version!

📦 Pulling nginx:alpine...
(This is a lightweight version of Nginx)

Size: 23MB (much smaller than nginx:latest at 142MB!)

✅ Download complete!

🏗️ Harbor Metaphor: You got a "lightweight" version of the Nginx blueprint.
Think of it as a streamlined ship design - same function, less bulk!
```

**Explanation:**
- Tags specify image versions
- `:alpine` = lightweight Linux distribution
- Same app, smaller size
- Default tag is `:latest`

---

```bash
# 5. Run container from new image
docker run -d redis
```

**Expected Output:**
```
✅ New Redis ship launched!

🚢 Building ship from Redis blueprint...
⛵ Redis container now running!

Container ID: stu901vwx234

🏗️ Harbor Metaphor: You built and launched a ship from your new Redis blueprint!
This ship runs a Redis database, ready to store data.
```

---

### Session 3 Summary

**Commands Learned:**
- ✅ `docker images` - List local images
- ✅ `docker pull <image>` - Download image
- ✅ `docker pull <image>:<tag>` - Download specific version

**Key Concepts:**
- Images = Templates (blueprints)
- Containers = Instances (ships)
- Tags = Versions
- One image → Many containers

---

## Session 4: Advanced Container Operations

**Objective:** Use advanced Docker flags and options
**Duration:** 20 minutes
**Difficulty:** Intermediate-Advanced

### Commands to Try

```bash
# 1. Run with port mapping
docker run -d -p 8080:80 nginx
```

**Expected Output:**
```
✅ Container started with port mapping!

🚢 Nginx ship launched with custom port configuration!
Container ID: yza345bcd678

Port Mapping:
  Host Port 8080 → Container Port 80

Access at: http://localhost:8080

🏗️ Harbor Metaphor: The ship's dock (port 80) is connected to
harbor pier 8080. Traffic from pier 8080 goes to the ship's dock!
```

**Explanation:**
- `-p 8080:80` maps host:container ports
- Access container via localhost:8080
- Container still uses port 80 internally
- Like a gangway connecting pier to ship

---

```bash
# 2. Run with custom name
docker run -d --name my-nginx nginx
```

**Expected Output:**
```
✅ Container started with custom name!

🚢 Ship named "my-nginx" launched!
Container ID: efg789hij012

Now you can use the friendly name instead of the ID:
  docker stop my-nginx
  docker start my-nginx
  docker rm my-nginx

🏗️ Harbor Metaphor: You named your ship "my-nginx" instead of
just using its registration number. Much easier to remember!
```

**Explanation:**
- `--name` gives container a memorable name
- Easier than remembering random IDs
- Names must be unique
- Like naming a ship vs. hull number

---

```bash
# 3. Run with environment variables
docker run -d -e REDIS_PASSWORD=secret123 redis
```

**Expected Output:**
```
✅ Container started with environment variables!

🚢 Redis ship launched with custom configuration!

Environment Variables Set:
  REDIS_PASSWORD=secret123

The Redis container now requires this password for access.

🏗️ Harbor Metaphor: You gave special instructions to the ship's crew
(environment variables) that configure how they operate.
```

**Explanation:**
- `-e` sets environment variables
- Configure application behavior
- Pass secrets, settings, etc.
- Like ship operating instructions

---

```bash
# 4. View container logs
docker logs my-nginx
```

**Expected Output:**
```
✅ Retrieving container logs...

📋 Log entries from "my-nginx":

2024-01-15 10:30:45 [notice] nginx/1.21.0
2024-01-15 10:30:45 [notice] start worker processes
2024-01-15 10:30:46 [notice] worker process started, pid 25
2024-01-15 10:31:12 [info] 127.0.0.1 - GET / HTTP/1.1 200

🏗️ Harbor Metaphor: Reading the ship's log book to see what
happened during its voyage - when it started, what it did, any issues.
```

**Explanation:**
- `docker logs` shows container output
- Useful for debugging
- See application messages and errors
- Like a ship's log book

---

```bash
# 5. Inspect container details
docker inspect my-nginx
```

**Expected Output:**
```
✅ Detailed container inspection:

📊 Container: my-nginx
├─ ID: efg789hij012
├─ Image: nginx:latest
├─ Status: Running
├─ IP Address: 172.17.0.2
├─ Ports: 80/tcp
├─ Environment: PATH=/usr/local/sbin:...
├─ Created: 2024-01-15 10:30:45
└─ Started: 2024-01-15 10:30:45

(Full JSON output available in real Docker)

🏗️ Harbor Metaphor: Complete inspection report of the ship -
every detail about its construction, current state, and configuration.
```

**Explanation:**
- `docker inspect` shows ALL container details
- Returns JSON format (in real Docker)
- Useful for troubleshooting
- Complete technical specifications

---

### Session 4 Summary

**Commands Learned:**
- ✅ `docker run -p <host>:<container>` - Port mapping
- ✅ `docker run --name <name>` - Custom naming
- ✅ `docker run -e <VAR>=<value>` - Environment variables
- ✅ `docker logs <container>` - View logs
- ✅ `docker inspect <container>` - Detailed info

**Common Flag Combinations:**
```bash
# Web server with port mapping and name
docker run -d -p 8080:80 --name web nginx

# Database with environment variables
docker run -d -e MYSQL_ROOT_PASSWORD=secret --name db mysql

# Complete setup
docker run -d \
  -p 3000:3000 \
  --name myapp \
  -e NODE_ENV=production \
  myapp:latest
```

---

## Session 5: Real-World Scenarios

**Objective:** Apply commands to practical situations
**Duration:** 25 minutes
**Difficulty:** All levels

### Scenario 1: Setting Up a Web Server

**Goal:** Run an Nginx web server accessible on port 8080

```bash
# Step 1: Pull the image
docker pull nginx

# Step 2: Run with port mapping and name
docker run -d -p 8080:80 --name webserver nginx

# Step 3: Verify it's running
docker ps

# Step 4: Check logs
docker logs webserver

# Step 5: Test (in real environment, browse to localhost:8080)
```

**Result:** Web server running and accessible!

---

### Scenario 2: Database Setup

**Goal:** Run a Redis database with password

```bash
# Step 1: Pull Redis image
docker pull redis

# Step 2: Run with environment variable
docker run -d \
  --name redis-db \
  -e REDIS_PASSWORD=mypassword \
  -p 6379:6379 \
  redis

# Step 3: Verify
docker ps | grep redis-db

# Step 4: Check it started correctly
docker logs redis-db
```

**Result:** Secure Redis database running!

---

### Scenario 3: Development Workflow

**Goal:** Work with containers during development

```bash
# Morning: Start your dev environment
docker run -d -p 3000:3000 --name dev-app myapp

# Check logs during development
docker logs dev-app
docker logs -f dev-app  # Follow mode (continuous)

# Something wrong? Restart
docker restart dev-app

# End of day: Stop but keep container
docker stop dev-app

# Next morning: Resume
docker start dev-app

# Project done: Clean up
docker stop dev-app
docker rm dev-app
```

---

### Scenario 4: Running Multiple Services

**Goal:** Run a multi-tier application

```bash
# Database tier
docker run -d \
  --name database \
  -e POSTGRES_PASSWORD=secret \
  postgres

# Application tier
docker run -d \
  --name backend \
  -p 5000:5000 \
  mybackend

# Web tier
docker run -d \
  --name frontend \
  -p 80:80 \
  nginx

# View all services
docker ps

# Check specific service logs
docker logs backend
```

---

## Session 6: Troubleshooting Common Issues

### Problem 1: Port Already in Use

**Error:**
```
Error: port 8080 is already in use
```

**Solution:**
```bash
# Option 1: Use a different port
docker run -d -p 8081:80 nginx  # Use 8081 instead

# Option 2: Find and stop the conflicting container
docker ps
docker stop <container-using-8080>
docker run -d -p 8080:80 nginx
```

---

### Problem 2: Container Keeps Stopping

**Error:**
```
Container exits immediately after starting
```

**Solution:**
```bash
# Check logs for errors
docker logs <container-id>

# Common causes:
# 1. Application crashed - check logs
# 2. Missing environment variables
# 3. Incorrect command

# Run in foreground to see output (remove -d flag)
docker run nginx  # No -d flag
```

---

### Problem 3: Can't Remove Container

**Error:**
```
Error: container is running
```

**Solution:**
```bash
# Option 1: Stop first (graceful)
docker stop <container-id>
docker rm <container-id>

# Option 2: Force remove (quick)
docker rm -f <container-id>
```

---

### Problem 4: Too Many Stopped Containers

**Problem:** `docker ps -a` shows many old containers

**Solution:**
```bash
# Remove one
docker rm <container-id>

# Remove multiple
docker rm <id1> <id2> <id3>

# Remove all stopped containers (Docker 1.13+)
docker container prune

# Or force remove all (careful!)
docker rm -f $(docker ps -a -q)
```

---

## Quick Reference Commands

### Essential Commands

```bash
# View containers
docker ps           # Running only
docker ps -a        # All containers

# Run containers
docker run nginx                    # Foreground
docker run -d nginx                 # Background
docker run -d -p 8080:80 nginx     # With port mapping
docker run -d --name web nginx     # With custom name

# Control containers
docker stop <id>     # Stop
docker start <id>    # Start
docker restart <id>  # Restart
docker rm <id>       # Remove
docker rm -f <id>    # Force remove

# Inspect containers
docker logs <id>     # View logs
docker inspect <id>  # Detailed info

# Images
docker images        # List images
docker pull <image>  # Download image
```

### Useful Flags

```bash
-d                  # Detached mode (background)
-p <host>:<cont>   # Port mapping
--name <name>      # Custom name
-e <VAR>=<val>     # Environment variable
-f                 # Force
-a                 # All
```

---

## Practice Exercises

### Exercise 1: Complete Workflow

Try this complete workflow:

```bash
1. docker pull nginx
2. docker run -d -p 8080:80 --name practice nginx
3. docker ps
4. docker logs practice
5. docker stop practice
6. docker ps -a
7. docker start practice
8. docker restart practice
9. docker stop practice
10. docker rm practice
```

### Exercise 2: Multiple Containers

Run three different containers:

```bash
docker run -d --name web nginx
docker run -d --name cache redis
docker run -d --name db postgres
docker ps
docker logs web
docker stop web cache db
docker rm web cache db
```

### Exercise 3: Port Mapping Practice

```bash
docker run -d -p 8080:80 --name web1 nginx
docker run -d -p 8081:80 --name web2 nginx
docker run -d -p 8082:80 --name web3 nginx
docker ps
# Three web servers, three different ports!
```

---

**Happy Practicing! 🚢**

*These examples work in both Harbor Docker Learning simulator and real Docker environments*

*Last Updated: Phase 5, Step 43*
