# ☁️ Cloud-Native DevOps Deployment Platform

> **Production-grade AWS infrastructure with automated CI/CD, containerized microservices, and enterprise observability**

A fully production-ready DevOps platform demonstrating real-world cloud engineering practices on Amazon Web Services. This project showcases Infrastructure as Code (Terraform), containerization (Docker), orchestration (ECS Fargate), automated CI/CD (GitHub Actions), and comprehensive monitoring (CloudWatch).

---

## 🎯 Project Overview

This platform implements a complete cloud-native deployment pipeline that:

- **Provisions AWS infrastructure** using modular, reusable Terraform
- **Deploys containerized applications** to ECS Fargate with zero-downtime rolling updates
- **Automates the entire CI/CD pipeline** from code commit to production deployment
- **Monitors and scales** applications automatically based on CPU/Memory metrics
- **Ensures security** through IAM least privilege, private subnets, and non-root containers
- **Optimizes costs** while maintaining high availability across multiple AZs

**This is not a tutorial project—it's a production-ready system built to enterprise standards.**

---

## 🏗️ Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────────┐
│                         AWS Cloud (us-east-1)                    │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    VPC (10.0.0.0/16)                        │ │
│  │                                                              │ │
│  │  ┌──────────────────┐        ┌──────────────────┐          │ │
│  │  │  Public Subnet   │        │  Public Subnet   │          │ │
│  │  │   (us-east-1a)   │        │   (us-east-1b)   │          │ │
│  │  │                  │        │                  │          │ │
│  │  │  ┌────────────┐  │        │                  │          │ │
│  │  │  │    ALB     │◄─┼────────┼──────────────────┼─ HTTPS   │ │
│  │  │  └─────┬──────┘  │        │                  │          │ │
│  │  │        │         │        │  ┌────────────┐  │          │ │
│  │  │        │         │        │  │ NAT Gateway│  │          │ │
│  │  └────────┼─────────┘        └──┴──────┬─────┴──┘          │ │
│  │           │                             │                   │ │
│  │  ┌────────▼─────────┐        ┌─────────▼──────────┐        │ │
│  │  │ Private Subnet   │        │ Private Subnet     │        │ │
│  │  │  (us-east-1a)    │        │  (us-east-1b)      │        │ │
│  │  │                  │        │                    │        │ │
│  │  │  ┌────────────┐  │        │  ┌────────────┐   │        │ │
│  │  │  │ ECS Task   │  │        │  │ ECS Task   │   │        │ │
│  │  │  │ (Fargate)  │  │        │  │ (Fargate)  │   │        │ │
│  │  │  └────────────┘  │        │  └────────────┘   │        │ │
│  │  └──────────────────┘        └────────────────────┘        │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   ECR        │  │  CloudWatch  │  │     IAM      │          │
│  │ (Container   │  │  (Logs &     │  │  (Roles &    │          │
│  │  Registry)   │  │   Metrics)   │  │  Policies)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└───────────────────────────────────────────────────────────────────┘

         ▲                                    │
         │                                    │
    GitHub Actions                       Deployment
    (Build & Deploy)                      Artifacts
```

### Component Breakdown

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Networking** | VPC, Subnets, NAT Gateway | Network isolation and internet access |
| **Compute** | ECS Fargate | Serverless container orchestration |
| **Load Balancing** | Application Load Balancer | Traffic distribution and health checks |
| **Container Registry** | Amazon ECR | Private Docker image storage |
| **CI/CD** | GitHub Actions | Automated build and deployment |
| **Monitoring** | CloudWatch | Logs, metrics, and alarms |
| **Security** | IAM, Security Groups | Access control and network security |
| **IaC** | Terraform | Infrastructure provisioning |

---

## 🛠️ Technology Stack

### Infrastructure
- **Cloud Provider**: Amazon Web Services (AWS)
- **IaC Tool**: Terraform 1.0+ (Modular architecture)
- **Regions**: Multi-AZ deployment (us-east-1a, us-east-1b)

### Application
- **Language**: Python 3.11
- **Framework**: FastAPI (async, high-performance)
- **Architecture**: Clean Architecture (46 Python files across 12 modules)
- **Containerization**: Docker (multi-stage builds)

### DevOps
- **CI/CD**: GitHub Actions
- **Orchestration**: Amazon ECS (Fargate)
- **Registry**: Amazon ECR
- **Monitoring**: CloudWatch Logs, Metrics, Alarms
- **Metrics**: Prometheus-compatible endpoints

---

## 📂 Project Structure

```
devops/
├── .github/
│   └── workflows/
│       └── deploy.yml              # CI/CD pipeline
├── app/                            # Python application (46 files)
│   ├── api/                        # REST API endpoints
│   │   ├── deployments.py          # Deployment management API
│   │   ├── health.py               # Health check endpoints
│   │   ├── metrics.py              # Metrics API
│   │   └── root.py                 # Root endpoints
│   ├── config/                     # Configuration management
│   │   ├── settings.py             # Pydantic settings
│   │   └── logging_config.py       # Structured logging
│   ├── core/                       # Core application logic
│   │   ├── dependencies.py         # Dependency injection
│   │   ├── events.py               # Lifecycle events
│   │   └── exceptions.py           # Custom exceptions
│   ├── middlewares/                # HTTP middlewares
│   │   ├── request_id.py           # Request tracking
│   │   ├── logging_middleware.py   # Request/response logging
│   │   └── error_handler.py        # Global error handling
│   ├── models/                     # Domain models
│   │   ├── deployment.py           # Deployment entity
│   │   ├── metrics.py              # Metrics models
│   │   ├── application.py          # Application entity
│   │   └── environment.py          # Environment config
│   ├── schemas/                    # Pydantic schemas (validation)
│   │   ├── deployment_schema.py    # Deployment DTOs
│   │   └── metrics_schema.py       # Metrics DTOs
│   ├── services/                   # Business logic layer
│   │   ├── deployment_service.py   # Deployment operations
│   │   ├── metrics_service.py      # Metrics collection
│   │   ├── aws_service.py          # AWS integrations
│   │   ├── notification_service.py # Alerting
│   │   └── cache_service.py        # In-memory caching
│   ├── repositories/               # Data access layer
│   │   ├── deployment_repository.py
│   │   └── metrics_repository.py
│   ├── utils/                      # Utility functions
│   │   ├── datetime_utils.py       # Date/time helpers
│   │   ├── string_utils.py         # String manipulation
│   │   ├── validators.py           # Validation logic
│   │   ├── constants.py            # Application constants
│   │   └── retry.py                # Retry with backoff
│   ├── health/                     # Health check services
│   │   └── health_service.py       # Liveness/readiness probes
│   ├── metrics/                    # Metrics collection
│   │   └── prometheus_metrics.py   # Prometheus exporter
│   ├── main.py                     # Application entry point
│   ├── app_factory.py              # FastAPI factory
│   └── requirements.txt            # Python dependencies
├── terraform/                      # Infrastructure as Code
│   ├── modules/
│   │   ├── vpc/                    # VPC, subnets, routing
│   │   ├── security/               # Security groups, IAM
│   │   ├── alb/                    # Load balancer
│   │   ├── ecs/                    # ECS cluster, service, tasks
│   │   └── observability/          # CloudWatch alarms
│   ├── main.tf                     # Root module
│   ├── variables.tf                # Input variables
│   └── outputs.tf                  # Output values
├── Dockerfile                      # Multi-stage container build
├── .dockerignore                   # Docker build exclusions
├── .gitignore                      # Git exclusions
├── .env.example                    # Environment variables template
└── README.md                       # This file
```

**Total Python Files**: 46 (organized across 12 logical modules)

---

## 🚀 Getting Started

### Prerequisites

- **AWS Account** with programmatic access
- **AWS CLI** configured (`aws configure`)
- **Terraform** >= 1.0.0
- **Docker** >= 20.10
- **Python** 3.11+
- **Git** and **GitHub** account

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/devops-platform.git
cd devops-platform
```

#### 2. Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt
```

#### 3. Configure Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

#### 4. Run Application Locally

```bash
cd app
python main.py
```

Visit `http://localhost:8000/docs` for interactive API documentation.

---

## 🏗️ Infrastructure Deployment

### Step 1: Initialize Terraform

```bash
cd terraform
terraform init
```

### Step 2: Review Infrastructure Plan

```bash
terraform plan
```

### Step 3: Deploy Infrastructure

```bash
terraform apply
# Type 'yes' to confirm
```

**Expected Resources Created**:
- 1 VPC
- 4 Subnets (2 public, 2 private)
- 1 Internet Gateway
- 1 NAT Gateway
- 2 Route Tables
- 3 Security Groups
- 2 IAM Roles
- 1 Application Load Balancer
- 1 Target Group
- 1 ECS Cluster
- 1 ECS Task Definition
- 1 ECS Service
- 3 CloudWatch Alarms

### Step 4: Get Application URL

```bash
terraform output application_url
# Example: http://devops-alb-123456789.us-east-1.elb.amazonaws.com
```

---

## 🐳 Docker Build & Push

### Build Locally

```bash
docker build -t devops-platform:latest .
```

### Test Container

```bash
docker run -p 8000:8000 devops-platform:latest
```

### Push to ECR

```bash
# Authenticate to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag devops-platform:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo:latest

# Push
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/my-ecr-repo:latest
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

The `.github/workflows/deploy.yml` pipeline automates:

1. **Checkout** code from `main` branch
2. **Authenticate** to AWS using secrets
3. **Build** Docker image
4. **Push** to Amazon ECR
5. **Update** ECS task definition
6. **Deploy** to ECS with rolling update
7. **Wait** for service stability

### Required GitHub Secrets

Add these secrets to your GitHub repository:

```
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
```

### Trigger Deployment

```bash
git add .
git commit -m "Deploy new version"
git push origin main
```

The pipeline automatically triggers and deploys to ECS.

---

## 📊 Monitoring & Observability

### CloudWatch Logs

All application logs are streamed to CloudWatch:

```bash
aws logs tail /ecs/prod-app --follow
```

### CloudWatch Alarms

Configured alarms:
- **CPU > 85%**: Triggers when task CPU exceeds threshold
- **Memory > 85%**: Triggers when task memory exceeds threshold

### Metrics Endpoints

- **Health Check**: `GET /health`
- **Liveness Probe**: `GET /health/live`
- **Readiness Probe**: `GET /health/ready`
- **Application Metrics**: `GET /api/v1/metrics`
- **Prometheus Metrics**: `GET /api/v1/metrics/prometheus`

---

## 🔐 Security Best Practices

### Network Security
- **Private Subnets**: Application containers run in private subnets with no direct internet access
- **Security Groups**: Strict ingress/egress rules (ALB → ECS only)
- **NAT Gateway**: Outbound internet access for pulling images and updates

### IAM Security
- **Least Privilege**: Task roles have minimal permissions
- **Separation of Duties**: Execution role (AWS operations) vs Task role (application operations)
- **No Hardcoded Credentials**: All secrets managed via environment variables

### Container Security
- **Non-Root User**: Application runs as `appuser` (UID 1000)
- **Multi-Stage Builds**: Minimal attack surface (no build tools in final image)
- **Image Scanning**: ECR scans images for vulnerabilities

---

## ⚖️ Scalability & Cost Optimization

### Auto Scaling

ECS Service auto-scales based on:
- **CPU Utilization**: Target 60%
- **Memory Utilization**: Target 60%
- **Min Tasks**: 2
- **Max Tasks**: 10

### Cost Optimization Strategies

1. **Fargate Spot** (future): Save up to 70% on compute costs
2. **Single NAT Gateway**: Reduces NAT costs (trade-off: single point of failure)
3. **Right-Sized Tasks**: 256 CPU / 512 MB memory (adjust based on load)
4. **Log Retention**: 30 days (balance cost vs compliance)

**Estimated Monthly Cost** (us-east-1):
- **ECS Fargate** (2 tasks): ~$30
- **NAT Gateway**: ~$35
- **ALB**: ~$20
- **CloudWatch**: ~$5
- **Total**: ~$90/month

---

## 🧪 Testing the Deployment

### 1. Health Check

```bash
curl http://<alb-dns>/health
```

Expected response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "environment": "prod"
}
```

### 2. Create Deployment

```bash
curl -X POST http://<alb-dns>/api/v1/deployments \
  -H "Content-Type: application/json" \
  -d '{
    "application": "api-service",
    "version": "1.2.3",
    "environment": "prod"
  }'
```

### 3. View Metrics

```bash
curl http://<alb-dns>/api/v1/metrics
```

---

## 🎓 Interview Preparation

### Key Talking Points

**"Tell me about a DevOps project you've built"**

> "I built a production-grade cloud-native deployment platform on AWS that demonstrates end-to-end DevOps practices. The system uses Terraform to provision a multi-AZ VPC with public and private subnets, deploys containerized applications to ECS Fargate behind an Application Load Balancer, and implements fully automated CI/CD via GitHub Actions. The architecture ensures zero-downtime deployments through rolling updates, auto-scales based on CPU/Memory metrics, and includes comprehensive monitoring with CloudWatch. Security is enforced through IAM least privilege, private subnet isolation, and non-root containers. The Python application follows clean architecture with 46 files across 12 modules, demonstrating separation of concerns and production-grade code organization."

**Technical Highlights**:
- Multi-AZ high availability
- Zero-downtime rolling deployments
- Infrastructure as Code (Terraform modules)
- Containerization with multi-stage Docker builds
- Automated CI/CD pipeline
- Auto-scaling and cost optimization
- Security best practices (IAM, SGs, private subnets)
- Structured logging and metrics (Prometheus-compatible)

---

## 📚 Additional Resources

- [AWS ECS Best Practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Multi-Stage Builds](https://docs.docker.com/build/building/multi-stage/)

---

## 🤝 Contributing

This is a portfolio/demonstration project. For suggestions or improvements, please open an issue.

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👤 Author

**Your Name**
- Portfolio: [your-portfolio.com](https://your-portfolio.com)
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- GitHub: [@yourusername](https://github.com/yourusername)

---

**Built with ❤️ for production-grade DevOps engineering**
