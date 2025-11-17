# 🚀 Harbor Docker Learning - Deployment Guide

**Complete deployment instructions for various environments**

---

## 📋 Table of Contents

1. [Deployment Options Overview](#deployment-options-overview)
2. [Local Development Deployment](#local-development-deployment)
3. [Docker Deployment](#docker-deployment)
4. [Cloud Platform Deployments](#cloud-platform-deployments)
5. [Environment Variables](#environment-variables)
6. [Production Best Practices](#production-best-practices)
7. [Monitoring and Maintenance](#monitoring-and-maintenance)

---

## Deployment Options Overview

| Option | Complexity | Cost | Use Case |
|--------|-----------|------|----------|
| **Local Python** | Low | Free | Development, Testing |
| **Docker Local** | Medium | Free | Testing, Learning Docker |
| **Streamlit Cloud** | Low | Free tier | Quick sharing, Small teams |
| **Heroku** | Medium | Free tier | Hobby projects |
| **AWS ECS/Fargate** | High | Pay per use | Production, Scale |
| **Google Cloud Run** | Medium | Pay per use | Production, Serverless |
| **DigitalOcean** | Medium | $5+/month | Production, VPS |
| **Kubernetes** | Very High | Variable | Enterprise, High scale |

---

## Local Development Deployment

### Option 1: Direct Python Execution

**Best for:** Development, quick testing

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/harbor-docker-learning.git
cd harbor-docker-learning

# 2. Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python -c "from data.database import init_database; from data.seed_data import seed_database; init_database(); seed_database()"

# 5. Run the application
streamlit run app.py
```

**Access:** http://localhost:8501

**Pros:**
- ✅ Fastest setup
- ✅ Easy to modify code
- ✅ No Docker required

**Cons:**
- ❌ Not isolated
- ❌ Manual dependency management
- ❌ Environment-specific issues

---

### Option 2: Using Docker Locally

**Best for:** Testing containerization, learning Docker

```bash
# 1. Clone repository
git clone https://github.com/yourusername/harbor-docker-learning.git
cd harbor-docker-learning

# 2. Build Docker image
docker build -t harbor-docker-learning .

# 3. Run container
docker run -d -p 8501:8501 --name harbor harbor-docker-learning

# 4. View logs
docker logs -f harbor

# 5. Stop container
docker stop harbor
docker rm harbor
```

**Access:** http://localhost:8501

**Pros:**
- ✅ Isolated environment
- ✅ Consistent across systems
- ✅ Production-like setup

**Cons:**
- ❌ Requires Docker installed
- ❌ Slower rebuild cycles
- ❌ More disk space needed

---

## Docker Deployment

### Docker Compose Setup

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  harbor-learning:
    build: .
    container_name: harbor-docker-learning
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    volumes:
      # Optional: Persist database (if you want user progress to survive container recreation)
      - ./data:/app/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

# Optional: Add a reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - harbor-learning
    restart: unless-stopped
```

**Deploy:**
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

---

### Nginx Reverse Proxy Configuration

Create `nginx.conf`:

```nginx
events {
    worker_connections 1024;
}

http {
    upstream streamlit {
        server harbor-learning:8501;
    }

    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://streamlit;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /_stcore/stream {
            proxy_pass http://streamlit/_stcore/stream;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
        }
    }
}
```

---

## Cloud Platform Deployments

### Streamlit Community Cloud

**Best for:** Quick sharing, educational use, free hosting

**Steps:**

1. **Prepare Repository:**
   ```bash
   # Ensure these files are in your repo:
   # - app.py
   # - requirements.txt
   # - data/ directory with all files

   git add .
   git commit -m "Prepare for Streamlit Cloud"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select repository: `yourusername/harbor-docker-learning`
   - Main file path: `app.py`
   - Click "Deploy"

3. **Configuration:**
   - No additional configuration needed
   - Database will be initialized automatically
   - App URL: `https://yourusername-harbor-docker-learning.streamlit.app`

**Pros:**
- ✅ Free hosting
- ✅ Automatic HTTPS
- ✅ Easy sharing
- ✅ Auto-deploys from Git

**Cons:**
- ❌ Resource limits
- ❌ Public repos only (free tier)
- ❌ Limited customization

---

### Heroku Deployment

**Best for:** Hobby projects, learning cloud deployment

**Prerequisites:**
```bash
# Install Heroku CLI
# macOS:
brew tap heroku/brew && brew install heroku

# Login
heroku login
```

**Setup Files:**

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
#!/bin/bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

**Deploy:**
```bash
# Create Heroku app
heroku create harbor-docker-learning

# Set buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku main

# Initialize database
heroku run python -c "from data.database import init_database; from data.seed_data import seed_database; init_database(); seed_database()"

# Open app
heroku open
```

**Pros:**
- ✅ Easy deployment
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Good documentation

**Cons:**
- ❌ App sleeps after 30 min inactivity (free tier)
- ❌ Limited free hours/month
- ❌ Slower cold starts

---

### AWS ECS/Fargate Deployment

**Best for:** Production, scalability, enterprise

**Prerequisites:**
- AWS Account
- AWS CLI installed and configured
- Docker installed locally

**Steps:**

1. **Push Image to ECR:**
   ```bash
   # Login to ECR
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

   # Create repository
   aws ecr create-repository --repository-name harbor-docker-learning

   # Tag image
   docker tag harbor-docker-learning:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/harbor-docker-learning:latest

   # Push image
   docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/harbor-docker-learning:latest
   ```

2. **Create ECS Task Definition:**

   Create `task-definition.json`:
   ```json
   {
     "family": "harbor-docker-learning",
     "networkMode": "awsvpc",
     "requiresCompatibilities": ["FARGATE"],
     "cpu": "512",
     "memory": "1024",
     "containerDefinitions": [
       {
         "name": "harbor-app",
         "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/harbor-docker-learning:latest",
         "portMappings": [
           {
             "containerPort": 8501,
             "protocol": "tcp"
           }
         ],
         "environment": [
           {"name": "STREAMLIT_SERVER_PORT", "value": "8501"},
           {"name": "STREAMLIT_SERVER_ADDRESS", "value": "0.0.0.0"}
         ],
         "logConfiguration": {
           "logDriver": "awslogs",
           "options": {
             "awslogs-group": "/ecs/harbor-docker-learning",
             "awslogs-region": "us-east-1",
             "awslogs-stream-prefix": "ecs"
           }
         }
       }
     ]
   }
   ```

3. **Deploy to ECS:**
   ```bash
   # Register task definition
   aws ecs register-task-definition --cli-input-json file://task-definition.json

   # Create ECS service
   aws ecs create-service \
     --cluster default \
     --service-name harbor-service \
     --task-definition harbor-docker-learning \
     --desired-count 1 \
     --launch-type FARGATE \
     --network-configuration "awsvpcConfiguration={subnets=[subnet-xxx],securityGroups=[sg-xxx],assignPublicIp=ENABLED}"
   ```

**Cost:** ~$15-30/month for minimal setup

---

### Google Cloud Run Deployment

**Best for:** Serverless, auto-scaling, pay-per-use

**Prerequisites:**
```bash
# Install Google Cloud SDK
# macOS:
brew install --cask google-cloud-sdk

# Login and set project
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

**Deploy:**
```bash
# Build and submit to Cloud Build
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/harbor-docker-learning

# Deploy to Cloud Run
gcloud run deploy harbor-docker-learning \
  --image gcr.io/YOUR_PROJECT_ID/harbor-docker-learning \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501 \
  --memory 512Mi \
  --timeout 300

# Get URL
gcloud run services describe harbor-docker-learning --platform managed --region us-central1 --format 'value(status.url)'
```

**Pros:**
- ✅ Serverless (scales to zero)
- ✅ Pay only for usage
- ✅ Automatic HTTPS
- ✅ Fast deployment

**Cons:**
- ❌ Cold starts
- ❌ Request timeout limits
- ❌ Learning curve

**Cost:** ~$0-5/month for light usage

---

### DigitalOcean Droplet Deployment

**Best for:** Full control, predictable pricing, learning

**Setup:**

1. **Create Droplet:**
   - Choose Ubuntu 22.04 LTS
   - Select plan: $6/month (1GB RAM) or higher
   - Add SSH key
   - Create droplet

2. **SSH into Droplet:**
   ```bash
   ssh root@your-droplet-ip
   ```

3. **Install Docker:**
   ```bash
   # Update system
   apt update && apt upgrade -y

   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh

   # Install Docker Compose
   apt install docker-compose -y
   ```

4. **Deploy Application:**
   ```bash
   # Clone repository
   git clone https://github.com/yourusername/harbor-docker-learning.git
   cd harbor-docker-learning

   # Run with Docker Compose
   docker-compose up -d

   # Check status
   docker-compose ps
   ```

5. **Configure Firewall:**
   ```bash
   ufw allow 22    # SSH
   ufw allow 80    # HTTP
   ufw allow 443   # HTTPS
   ufw enable
   ```

6. **Setup Domain (Optional):**
   - Point domain DNS to droplet IP
   - Install Certbot for HTTPS:
   ```bash
   apt install certbot python3-certbot-nginx -y
   certbot --nginx -d yourdomain.com
   ```

**Cost:** $6-12/month

---

## Environment Variables

### Available Environment Variables

| Variable | Default | Description | Required |
|----------|---------|-------------|----------|
| `STREAMLIT_SERVER_PORT` | `8501` | Port for Streamlit server | No |
| `STREAMLIT_SERVER_ADDRESS` | `0.0.0.0` | Server address (0.0.0.0 for Docker) | No |
| `STREAMLIT_SERVER_HEADLESS` | `true` | Run without browser | No |
| `STREAMLIT_BROWSER_GATHER_USAGE_STATS` | `false` | Disable telemetry | No |
| `STREAMLIT_SERVER_ENABLE_CORS` | `false` | Enable CORS | No |
| `STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION` | `true` | XSRF protection | No |

### Setting Environment Variables

**Docker Run:**
```bash
docker run -d \
  -p 8501:8501 \
  -e STREAMLIT_SERVER_PORT=8501 \
  -e STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
  harbor-docker-learning
```

**Docker Compose:**
```yaml
environment:
  - STREAMLIT_SERVER_PORT=8501
  - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

**Heroku:**
```bash
heroku config:set STREAMLIT_SERVER_PORT=8501
```

**Local (.env file):**
```bash
# Create .env file
STREAMLIT_SERVER_PORT=8501
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Load in app (add python-dotenv to requirements.txt)
from dotenv import load_dotenv
load_dotenv()
```

---

## Production Best Practices

### Security

1. **Use HTTPS:**
   - Always use HTTPS in production
   - Use Let's Encrypt for free certificates
   - Configure Nginx/Traefik as reverse proxy

2. **Environment Variables:**
   - Never commit secrets to Git
   - Use secret management services
   - Rotate credentials regularly

3. **Container Security:**
   - Run as non-root user (already configured)
   - Scan images for vulnerabilities: `docker scan harbor-docker-learning`
   - Use minimal base images
   - Keep dependencies updated

4. **Network Security:**
   - Use firewall rules
   - Limit exposed ports
   - Use VPC/private networks

### Performance

1. **Resource Limits:**
   ```yaml
   # docker-compose.yml
   deploy:
     resources:
       limits:
         cpus: '0.5'
         memory: 512M
       reservations:
         cpus: '0.25'
         memory: 256M
   ```

2. **Caching:**
   - Already implemented in app (Streamlit caching)
   - Use CDN for static assets if needed
   - Enable browser caching

3. **Database:**
   - Regular backups
   - Monitor size growth
   - Consider external database for high traffic

### Monitoring

1. **Health Checks:**
   - Already configured in Dockerfile
   - Monitor health check status
   - Set up alerts for failures

2. **Logging:**
   ```bash
   # View logs
   docker logs -f harbor-docker-learning

   # Save logs to file
   docker logs harbor-docker-learning > app.log

   # Use log aggregation (ELK, Splunk, CloudWatch)
   ```

3. **Metrics:**
   - Monitor CPU/Memory usage
   - Track request counts
   - Monitor response times
   - Set up uptime monitoring (UptimeRobot, Pingdom)

### Backup and Recovery

1. **Database Backup:**
   ```bash
   # Backup SQLite database
   docker cp harbor-docker-learning:/app/data/tutorials.sqlite ./backup-$(date +%Y%m%d).sqlite

   # Restore database
   docker cp ./backup-20240115.sqlite harbor-docker-learning:/app/data/tutorials.sqlite
   docker restart harbor-docker-learning
   ```

2. **Automated Backups:**
   ```bash
   # Add to crontab
   0 2 * * * docker cp harbor-docker-learning:/app/data/tutorials.sqlite /backups/tutorials-$(date +\%Y\%m\%d).sqlite
   ```

3. **Disaster Recovery:**
   - Document recovery procedures
   - Test recovery regularly
   - Keep backups in multiple locations

---

## Monitoring and Maintenance

### Uptime Monitoring

**Free Services:**
- UptimeRobot: https://uptimerobot.com
- Freshping: https://www.freshworks.com/website-monitoring/
- StatusCake: https://www.statuscake.com

**Setup:**
1. Create account
2. Add URL: http://your-app-url.com
3. Set check interval: 5 minutes
4. Configure alerts: email, SMS, Slack

### Log Monitoring

**View Recent Logs:**
```bash
docker logs --tail 100 harbor-docker-learning
```

**Follow Logs:**
```bash
docker logs -f harbor-docker-learning
```

**Search Logs:**
```bash
docker logs harbor-docker-learning 2>&1 | grep ERROR
```

### Updates and Maintenance

**Update Application:**
```bash
# Pull latest code
git pull origin main

# Rebuild image
docker-compose build

# Restart services
docker-compose up -d

# Or one-liner
git pull && docker-compose up -d --build
```

**Update Dependencies:**
```bash
# Update requirements.txt
pip install --upgrade streamlit pandas

# Rebuild container
docker-compose up -d --build
```

**Database Maintenance:**
```bash
# Check database size
docker exec harbor-docker-learning ls -lh /app/data/tutorials.sqlite

# Vacuum database (optimize)
docker exec harbor-docker-learning sqlite3 /app/data/tutorials.sqlite "VACUUM;"
```

---

## Troubleshooting Common Deployment Issues

### Issue: Container Keeps Restarting

**Check logs:**
```bash
docker logs harbor-docker-learning
```

**Common causes:**
- Port already in use
- Database initialization failed
- Missing dependencies
- Memory limit too low

### Issue: App Slow or Unresponsive

**Check resources:**
```bash
docker stats harbor-docker-learning
```

**Solutions:**
- Increase memory limit
- Check for memory leaks
- Optimize database queries
- Enable caching

### Issue: Can't Access from Internet

**Checklist:**
- [ ] Port is exposed in Dockerfile
- [ ] Port mapping correct in docker run
- [ ] Firewall allows port
- [ ] Router port forwarding configured
- [ ] DNS points to correct IP

---

## Deployment Checklist

Before deploying to production:

### Pre-Deployment
- [ ] Test locally thoroughly
- [ ] Run Docker build successfully
- [ ] Test container locally
- [ ] Review security settings
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Document deployment steps

### During Deployment
- [ ] Build and push image
- [ ] Deploy container
- [ ] Verify health checks pass
- [ ] Test all functionality
- [ ] Check logs for errors
- [ ] Verify database initialized
- [ ] Test from external network

### Post-Deployment
- [ ] Monitor metrics for 24 hours
- [ ] Set up uptime monitoring
- [ ] Configure log aggregation
- [ ] Schedule regular backups
- [ ] Document any issues
- [ ] Update documentation
- [ ] Notify users of URL

---

## Support and Resources

### Official Documentation
- **Streamlit:** https://docs.streamlit.io/
- **Docker:** https://docs.docker.com/
- **Streamlit Cloud:** https://docs.streamlit.io/streamlit-community-cloud

### Community
- GitHub Issues: https://github.com/yourusername/harbor-docker-learning/issues
- Streamlit Forum: https://discuss.streamlit.io/
- Docker Community: https://forums.docker.com/

---

**Deployment Status: Ready for Production 🚀**

*Choose the deployment option that best fits your needs and follow the corresponding guide above.*

*Last Updated: Phase 5, Step 49*
