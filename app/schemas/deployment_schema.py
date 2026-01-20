"""
Deployment Request/Response Schemas
Pydantic schemas for API validation
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.models.deployment import DeploymentStatus


class DeploymentCreateRequest(BaseModel):
    """Request schema for creating a deployment"""
    
    application: str = Field(..., min_length=1, max_length=100)
    version: str = Field(..., min_length=1, max_length=50)
    environment: str = Field(..., pattern="^(dev|staging|prod)$")
    deployed_by: Optional[str] = Field(default="system", max_length=100)


class DeploymentResponse(BaseModel):
    """Response schema for deployment"""
    
    id: str
    application: str
    version: str
    environment: str
    status: DeploymentStatus
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    deployed_by: str
    
    class Config:
        from_attributes = True


class DeploymentListResponse(BaseModel):
    """Response schema for deployment list"""
    
    deployments: list[DeploymentResponse]
    total: int
    page: int
    page_size: int
