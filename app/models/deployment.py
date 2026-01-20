"""
Deployment Domain Model
Represents a deployment entity in the system
"""
from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class DeploymentStatus(str, Enum):
    """Deployment status enumeration"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


class Deployment(BaseModel):
    """Deployment domain model"""
    
    id: str = Field(..., description="Unique deployment identifier")
    application: str = Field(..., description="Application name")
    version: str = Field(..., description="Version being deployed")
    environment: str = Field(..., description="Target environment")
    status: DeploymentStatus = Field(default=DeploymentStatus.PENDING)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    error_message: Optional[str] = None
    deployed_by: str = Field(default="system")
    
    class Config:
        use_enum_values = True
