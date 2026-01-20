# Cloud-Native DevOps Platform - Deployment Guide

## Quick Start Commands

### Local Development
```bash
# Setup virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r app/requirements.txt

# Run locally
cd app
python main.py
```

### Infrastructure Deployment
```bash
cd terraform
terraform init
terraform plan
terraform apply
terraform output application_url
```

### Docker Build & Test
```bash
docker build -t devops-platform:latest .
docker run -p 8000:8000 devops-platform:latest
```

## Architecture Summary

**46 Python files** organized in clean architecture:
- `api/` - REST endpoints (deployments, health, metrics)
- `services/` - Business logic (deployment, metrics, AWS, cache, notifications)
- `repositories/` - Data access layer
- `models/` - Domain entities
- `schemas/` - Request/response validation
- `middlewares/` - Request processing (logging, errors, request ID)
- `core/` - DI container, exceptions, events
- `config/` - Settings and logging
- `utils/` - Helpers (datetime, strings, validators, retry)
- `health/` - Kubernetes-style probes
- `metrics/` - Prometheus exporter

## Key Features Implemented

✅ Multi-AZ VPC with public/private subnets
✅ ECS Fargate with auto-scaling
✅ Application Load Balancer with health checks
✅ Zero-downtime rolling deployments
✅ CloudWatch monitoring and alarms
✅ IAM least privilege security
✅ Multi-stage Docker builds
✅ Non-root container execution
✅ GitHub Actions CI/CD
✅ Structured JSON logging
✅ Prometheus metrics
✅ Virtual environment (.venv)

## Production Checklist

- [ ] Create ECR repository
- [ ] Configure GitHub secrets (AWS credentials)
- [ ] Update Terraform variables (region, environment)
- [ ] Deploy infrastructure (`terraform apply`)
- [ ] Push Docker image to ECR
- [ ] Trigger GitHub Actions workflow
- [ ] Verify ALB health checks
- [ ] Test API endpoints
- [ ] Configure CloudWatch alarms
- [ ] Set up log retention policies

## Cost Estimate

Monthly cost in us-east-1:
- ECS Fargate (2 tasks): ~$30
- NAT Gateway: ~$35
- ALB: ~$20
- CloudWatch: ~$5
**Total: ~$90/month**

## Interview Talking Points

"I built a production-grade cloud-native platform on AWS with 46 Python files following clean architecture. The system uses Terraform modules to provision a multi-AZ VPC, deploys containerized FastAPI applications to ECS Fargate behind an ALB, implements zero-downtime rolling updates, auto-scales based on metrics, and includes comprehensive CloudWatch monitoring. Security is enforced through private subnets, IAM least privilege, and non-root containers. The entire CI/CD pipeline is automated via GitHub Actions."
