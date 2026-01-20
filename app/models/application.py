"""
Application Model
Represents an application that can be deployed
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Application(BaseModel):
    """Application domain model"""
    
    id: str = Field(..., description="Unique application identifier")
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    repository_url: Optional[str] = Field(None, description="Git repository URL")
    docker_image: str = Field(..., description="Docker image name")
    current_version: Optional[str] = Field(None, description="Currently deployed version")
    environments: List[str] = Field(default_factory=list, description="Available environments")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "app-123",
                "name": "api-service",
                "description": "Main API service",
                "docker_image": "my-ecr-repo/api-service",
                "current_version": "1.2.3",
                "environments": ["dev", "staging", "prod"]
            }
        }
