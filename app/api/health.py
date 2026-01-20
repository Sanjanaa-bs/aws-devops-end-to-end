"""
Health Check API Endpoints
Kubernetes-style health probes
"""
from fastapi import APIRouter, status
from app.schemas.metrics_schema import HealthCheckResponse
from app.health.health_service import HealthCheckService
from app.config import settings

router = APIRouter(prefix="/health", tags=["health"])
health_service = HealthCheckService()


@router.get(
    "",
    response_model=HealthCheckResponse,
    summary="Basic health check"
)
async def health_check() -> HealthCheckResponse:
    """Basic health check endpoint for ALB"""
    return HealthCheckResponse(
        status="healthy",
        version=settings.app_version,
        environment=settings.environment
    )


@router.get(
    "/live",
    status_code=status.HTTP_200_OK,
    summary="Liveness probe"
)
async def liveness_probe():
    """
    Kubernetes liveness probe
    Indicates if the application is running
    """
    return health_service.check_liveness()


@router.get(
    "/ready",
    status_code=status.HTTP_200_OK,
    summary="Readiness probe"
)
async def readiness_probe():
    """
    Kubernetes readiness probe
    Indicates if the application is ready to serve traffic
    """
    return health_service.check_readiness()


@router.get(
    "/startup",
    status_code=status.HTTP_200_OK,
    summary="Startup probe"
)
async def startup_probe():
    """
    Kubernetes startup probe
    Indicates if the application has finished starting
    """
    return health_service.check_startup()
