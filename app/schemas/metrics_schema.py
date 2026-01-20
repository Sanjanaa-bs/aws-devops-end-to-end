"""
Metrics Response Schemas
"""
from pydantic import BaseModel
from app.models.metrics import SystemMetrics, ApplicationMetrics, DeploymentMetrics


class MetricsResponse(BaseModel):
    """Combined metrics response"""
    
    system: SystemMetrics
    application: ApplicationMetrics
    deployment: DeploymentMetrics


class HealthCheckResponse(BaseModel):
    """Health check response schema"""
    
    status: str
    version: str
    environment: str
