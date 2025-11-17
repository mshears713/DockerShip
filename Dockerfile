# ============================================================================
# Harbor Docker Learning - Dockerfile
# ============================================================================
#
# 🎓 EDUCATIONAL META-MOMENT 🎓
# This is a Dockerfile for a Docker learning application!
# You're using the very technology you're learning about to deploy the app.
#
# Just as this app uses the harbor metaphor to teach Docker concepts,
# this Dockerfile demonstrates real-world containerization practices.
#
# ============================================================================

# ----------------------------------------------------------------------------
# Base Image Selection
# ----------------------------------------------------------------------------
# Educational Note: We use Python's official image as our "ship blueprint"
# The 'slim' variant is smaller and more secure than the full version
FROM python:3.11-slim

# Educational Note: The alpine variant would be even smaller, but we use
# slim for better compatibility and faster builds (fewer compilation issues)

# ----------------------------------------------------------------------------
# Metadata Labels
# ----------------------------------------------------------------------------
# Educational Note: Labels provide metadata about the image
# Think of them as the ship's registration information
LABEL maintainer="Harbor Docker Learning Contributors"
LABEL version="1.0.0"
LABEL description="Interactive Streamlit app teaching Docker concepts through harbor metaphor"
LABEL educational.purpose="teaching-docker-fundamentals"

# ----------------------------------------------------------------------------
# Working Directory
# ----------------------------------------------------------------------------
# Educational Note: Set the working directory inside the container
# All subsequent commands run from this directory
# Like setting the ship's home port
WORKDIR /app

# Educational Note: WORKDIR creates the directory if it doesn't exist
# It's better than using RUN mkdir + cd because it's clearer and safer

# ----------------------------------------------------------------------------
# System Dependencies
# ----------------------------------------------------------------------------
# Educational Note: Update package lists and install system dependencies
# The --no-install-recommends flag keeps the image smaller
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Build essentials for any packages that need compilation
    build-essential \
    # Clean up to reduce image size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Educational Note: We combine these into one RUN command to reduce layers
# Each RUN creates a new layer, and fewer layers = smaller image

# ----------------------------------------------------------------------------
# Python Dependencies
# ----------------------------------------------------------------------------
# Educational Note: Copy requirements first for better Docker cache utilization
# If requirements.txt doesn't change, Docker reuses the cached layer
COPY requirements.txt .

# Educational Note: Upgrade pip first for security and compatibility
RUN pip install --no-cache-dir --upgrade pip

# Educational Note: Install Python packages
# --no-cache-dir reduces image size by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt

# Educational Note: Why copy requirements.txt before the rest of the code?
# Docker caches layers. If code changes but requirements don't, Docker
# reuses the pip install layer, making builds much faster!
# This is a Docker best practice called "layer caching optimization"

# ----------------------------------------------------------------------------
# Application Code
# ----------------------------------------------------------------------------
# Educational Note: Copy the entire application into the container
COPY . .

# Educational Note: We use COPY instead of ADD because:
# - COPY is more transparent (only copies files)
# - ADD has extra features (auto-extraction, URL support) we don't need
# - COPY is preferred for simple file copying

# ----------------------------------------------------------------------------
# Database Initialization
# ----------------------------------------------------------------------------
# Educational Note: Initialize the database with tutorial content
# This ensures the app has data when it starts
RUN python -c "from data.database import init_database; from data.seed_data import seed_database; init_database(); seed_database()"

# Educational Note: We do this during build (not runtime) because:
# - Faster container startup
# - Database is ready immediately
# - Same data in every container instance

# ----------------------------------------------------------------------------
# Port Configuration
# ----------------------------------------------------------------------------
# Educational Note: Expose the port Streamlit uses
# This is documentary - it tells users which port the app uses
EXPOSE 8501

# Educational Note: EXPOSE doesn't actually publish the port!
# It's documentation. You still need -p flag when running:
# docker run -p 8501:8501 harbor-docker-learning
#
# Think of EXPOSE as marking the ship's communication channel,
# but you still need to connect the gangway (port mapping)

# ----------------------------------------------------------------------------
# Health Check
# ----------------------------------------------------------------------------
# Educational Note: Define a health check to monitor container health
# Docker can restart unhealthy containers automatically
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

# Educational Note: Health checks help with:
# - Automatic recovery from failures
# - Load balancer integration
# - Monitoring and alerting
# Like a ship's regular status reports to harbor control

# ----------------------------------------------------------------------------
# User Configuration (Security Best Practice)
# ----------------------------------------------------------------------------
# Educational Note: Create a non-root user for security
# Running as root in containers is a security risk
RUN useradd -m -u 1000 harboruser && \
    chown -R harboruser:harboruser /app

# Educational Note: Switch to non-root user
USER harboruser

# Educational Note: Why not run as root?
# - Principle of least privilege
# - Limits damage if container is compromised
# - Many orchestrators (Kubernetes) require non-root
# Like giving ship crew appropriate permissions, not making everyone captain

# ----------------------------------------------------------------------------
# Runtime Configuration
# ----------------------------------------------------------------------------
# Educational Note: Set Streamlit configuration via environment variables
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Educational Note: Why these settings?
# - PORT: Standard Streamlit port
# - ADDRESS 0.0.0.0: Listen on all interfaces (needed for Docker)
# - HEADLESS: Don't try to open browser (there isn't one in container)
# - STATS: Disable telemetry for privacy

# ----------------------------------------------------------------------------
# Startup Command
# ----------------------------------------------------------------------------
# Educational Note: Define the command to run when container starts
# CMD is the default command, can be overridden at runtime
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Educational Note: We use JSON array syntax (exec form) instead of shell form
# Exec form: ["streamlit", "run", "app.py"]
# Shell form: streamlit run app.py
#
# Exec form is preferred because:
# - No shell wrapper process
# - Better signal handling (SIGTERM works correctly)
# - Container stops gracefully

# Educational Note: Why CMD and not ENTRYPOINT?
# - CMD can be easily overridden: docker run ... custom-command
# - ENTRYPOINT is harder to override (requires --entrypoint flag)
# - For this app, CMD provides good flexibility

# ============================================================================
# Build and Run Instructions
# ============================================================================
#
# Build the image:
# ---------------
# docker build -t harbor-docker-learning .
#
# Educational Note: The -t flag tags the image with a name
# The . at the end is the build context (current directory)
#
# Run the container:
# ------------------
# docker run -p 8501:8501 harbor-docker-learning
#
# Educational Note: The -p flag maps host port to container port
# Format: -p <host-port>:<container-port>
# This is the "gangway" connecting the ship to the pier!
#
# Run in detached mode (background):
# ----------------------------------
# docker run -d -p 8501:8501 --name my-harbor harbor-docker-learning
#
# Educational Note:
# - -d runs in background (detached)
# - --name gives container a friendly name
# - Now check logs with: docker logs my-harbor
#
# Run with volume for persistent data:
# ------------------------------------
# docker run -d -p 8501:8501 -v $(pwd)/data:/app/data harbor-docker-learning
#
# Educational Note: Volumes persist data outside the container
# If container is removed, data remains on host
# Like storing ship cargo in the warehouse, not on the ship
#
# ============================================================================

# ============================================================================
# Multi-Stage Build Alternative (Advanced)
# ============================================================================
#
# For production, consider a multi-stage build to reduce image size:
#
# FROM python:3.11-slim as builder
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --user --no-cache-dir -r requirements.txt
#
# FROM python:3.11-slim
# WORKDIR /app
# COPY --from=builder /root/.local /root/.local
# COPY . .
# ENV PATH=/root/.local/bin:$PATH
# CMD ["streamlit", "run", "app.py"]
#
# Educational Note: Multi-stage builds:
# - Build dependencies in first stage
# - Copy only needed artifacts to final stage
# - Result: Much smaller final image
# - Like building a ship in a shipyard, then moving only the ship (not the tools)
#
# ============================================================================

# ============================================================================
# Docker Compose Alternative
# ============================================================================
#
# For easier deployment, create docker-compose.yml:
#
# version: '3.8'
# services:
#   harbor-learning:
#     build: .
#     ports:
#       - "8501:8501"
#     volumes:
#       - ./data:/app/data
#     environment:
#       - STREAMLIT_SERVER_PORT=8501
#     restart: unless-stopped
#
# Then run with: docker-compose up -d
#
# Educational Note: Docker Compose makes multi-container setups easy
# It's like a fleet management system for ships!
#
# ============================================================================

# ============================================================================
# Image Size Optimization Tips
# ============================================================================
#
# 1. Use smaller base images (alpine, slim)
# 2. Combine RUN commands to reduce layers
# 3. Use .dockerignore to exclude unnecessary files
# 4. Clean up in the same RUN command that installs
# 5. Use multi-stage builds for complex applications
# 6. Don't install unnecessary packages
# 7. Use --no-cache-dir with pip
#
# Current image size: ~500MB (with python:3.11-slim)
# With alpine: ~200MB (but requires more compilation)
# With multi-stage: ~400MB
#
# ============================================================================

# ============================================================================
# Security Best Practices Implemented
# ============================================================================
#
# ✅ Run as non-root user
# ✅ Use official base images
# ✅ Pin version tags (python:3.11-slim, not python:latest)
# ✅ Minimize installed packages
# ✅ Use COPY instead of ADD
# ✅ Don't expose unnecessary ports
# ✅ Include health checks
# ✅ Clean up package manager caches
# ✅ Use .dockerignore file
# ✅ Scan images for vulnerabilities (use: docker scan harbor-docker-learning)
#
# Educational Note: Container security is crucial!
# Every ship needs proper security measures.
#
# ============================================================================

# 🎓 CONGRATULATIONS! 🎓
# You've just read a comprehensive, educational Dockerfile!
# This demonstrates real-world Docker best practices while teaching you
# the concepts through comments and metaphors.
#
# Now you're ready to build and run this container - using the very
# technology you're learning about!
#
# That's the beauty of Docker: Learn it by using it! 🚢
