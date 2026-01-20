"""
Metrics Domain Model
Represents application and infrastructure metrics
"""
from datetime import datetime
from typing import Dict, Any
from pydantic import BaseModel, Field


class SystemMetrics(BaseModel):
    """System-level metrics"""
    
    cpu_usage_percent: float = Field(..., ge=0, le=100)
    memory_usage_percent: float = Field(..., ge=0, le=100)
    disk_usage_percent: float = Field(..., ge=0, le=100)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ApplicationMetrics(BaseModel):
    """Application-level metrics"""
    
    request_count: int = Field(default=0, ge=0)
    error_count: int = Field(default=0, ge=0)
    average_response_time_ms: float = Field(default=0.0, ge=0)
    active_connections: int = Field(default=0, ge=0)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class DeploymentMetrics(BaseModel):
    """Deployment-related metrics"""
    
    total_deployments: int = Field(default=0, ge=0)
    successful_deployments: int = Field(default=0, ge=0)
    failed_deployments: int = Field(default=0, ge=0)
    average_deployment_time_seconds: float = Field(default=0.0, ge=0)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
