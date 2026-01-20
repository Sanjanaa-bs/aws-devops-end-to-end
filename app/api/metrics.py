"""
Metrics API Endpoints
Exposes application and system metrics
"""
from fastapi import APIRouter, Depends, Response
from app.schemas.metrics_schema import MetricsResponse
from app.services.metrics_service import MetricsService
from app.core.dependencies import get_metrics_service, get_deployment_repository
from app.metrics.prometheus_metrics import metrics as prom_metrics
from prometheus_client import CONTENT_TYPE_LATEST

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.get(
    "",
    response_model=MetricsResponse,
    summary="Get application metrics"
)
async def get_metrics(
    metrics_service: MetricsService = Depends(get_metrics_service),
    deployment_repo = Depends(get_deployment_repository)
) -> MetricsResponse:
    """Get comprehensive application metrics"""
    system_metrics = metrics_service.get_system_metrics()
    app_metrics = metrics_service.get_application_metrics()
    deployment_metrics = metrics_service.get_deployment_metrics(deployment_repo)
    
    return MetricsResponse(
        system=system_metrics,
        application=app_metrics,
        deployment=deployment_metrics
    )


@router.get(
    "/prometheus",
    summary="Prometheus metrics endpoint"
)
async def prometheus_metrics():
    """Export metrics in Prometheus format"""
    return Response(
        content=prom_metrics.export_metrics(),
        media_type=CONTENT_TYPE_LATEST
    )
