"""
Dependency Injection Container
Manages application-wide dependencies and services
"""
from typing import Generator
from functools import lru_cache
from app.config import settings
from app.services.deployment_service import DeploymentService
from app.services.metrics_service import MetricsService
from app.repositories.deployment_repository import DeploymentRepository


@lru_cache()
def get_deployment_repository() -> DeploymentRepository:
    """Get deployment repository instance"""
    return DeploymentRepository()


@lru_cache()
def get_deployment_service() -> DeploymentService:
    """Get deployment service instance"""
    repo = get_deployment_repository()
    return DeploymentService(repository=repo)


@lru_cache()
def get_metrics_service() -> MetricsService:
    """Get metrics service instance"""
    return MetricsService()


def get_current_settings():
    """Dependency for accessing settings"""
    return settings
