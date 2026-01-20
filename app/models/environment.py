"""
Environment Configuration Model
Represents deployment environment configuration
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class EnvironmentConfig(BaseModel):
    """Environment-specific configuration"""
    
    name: str = Field(..., description="Environment name (dev, staging, prod)")
    region: str = Field(default="us-east-1", description="AWS region")
    vpc_id: Optional[str] = Field(None, description="VPC ID")
    cluster_name: str = Field(..., description="ECS cluster name")
    task_count: int = Field(default=2, ge=1, le=10, description="Desired task count")
    cpu: str = Field(default="256", description="Task CPU units")
    memory: str = Field(default="512", description="Task memory (MB)")
    auto_scaling_enabled: bool = Field(default=True)
    min_tasks: int = Field(default=2, ge=1)
    max_tasks: int = Field(default=10, ge=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "prod",
                "region": "us-east-1",
                "cluster_name": "prod-cluster",
                "task_count": 2,
                "auto_scaling_enabled": True
            }
        }
