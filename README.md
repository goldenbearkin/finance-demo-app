# Finance App

This project consists of a frontend and backend for a Finance Application, containerized using Docker.

## 📦 Project Structure

- **Frontend:** React application served on port `8080`
- **Backend:** API service running on port `8000`
- **Elasticsearch:** Search engine running on port `9200`
- **Kibana:** Analytics and visualization platform running on port `5601`

## 🚀 Getting Started

### 🐳 Start All Services

To start all services (frontend, backend, Elasticsearch, and Kibana), run:

```bash
docker-compose up -d --build
```

This will:
- Build all Docker images
- Start all services in detached mode
- Set up the complete application stack

## 🌐 Access Points

- **Frontend:** http://localhost:8080
- **Backend API:** http://localhost:8000
- **Backend Swagger Documentation:** http://localhost:8000/doc
- **Kibana:** http://localhost:5601
- **Elasticsearch:** http://localhost:9200

## 👤 Test User Credentials

Two test users are available for testing:

1. **User 1**
   - Username: user1@test.com
   - Password: testtest1

2. **User 2**
   - Username: user2@test.com
   - Password: testtest2

## 📂 Expected File Structure

```
.
├── frontend/
│   └── Dockerfile
├── backend/
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🛑 Stopping Containers

To stop all running services:

```bash
docker-compose down
```

## 🔍 Setting Up Kibana (Audit logging)

After starting the services, follow these steps to set up Kibana:

1. Access Kibana at https://localhost:5601
2. Navigate to "Discover" in the left sidebar
3. Click on "Create data view"
4. Configure the data view with the following settings:
   - Name: `fastapi-logs`
   - Index pattern: `fastapi-logs`
   - Timestamp field: `timestamp`
5. Click "Create data view" to save the configuration

This will allow you to view and analyze the logs from your FastAPI backend in Kibana.

## ✅ Completeness Checklist

### Stock Analysis Page
- Ticker and price summary ✓
- Research Analysis ✓
- Earnings Estimate ✓
- Revenue Estimate ✓
- Growth Estimate ✓

### Custom Estimates
- User input and save functionality for custom estimates ✓
- Side-by-side display of Yahoo's data and custom estimates ✓
- Client-side validation feedback ✓
  - Email format validation
  - Password length validation (minimum 6 characters)
- Access control implementation ✓
  - Users can only update their own ticker sets
  - Restricted access to other users' data

## 🏗️ Infrastructure

### Production Deployment Plan

#### CI/CD Setup
- GitOps approach for infrastructure as code
- GitHub Workflows for automated testing and deployment
- Automated build and deployment pipelines
- Environment-specific deployment configurations

#### High Availability Architecture
- Azure Front Door for global load balancing and DDoS protection
- Content Delivery Network (CDN) for static assets
- Multi-region deployment for disaster recovery
- Auto-scaling capabilities

#### Cloud Infrastructure Components
- Azure Kubernetes Service (AKS) for container orchestration
- Azure AD B2C for identity and access management
- Azure Managed databases

#### Monitoring and Alerting
- ELK Stack (Elasticsearch, Logstash, Kibana) for centralized logging
- Health check endpoints for service monitoring
- Pingdom for uptime monitoring
- Alerta for service outage 

### Suggestions for Further Enhancements
- Implement blue-green deployments for zero-downtime updates
- Implement feature flags for controlled feature rollouts
- E2E testing
