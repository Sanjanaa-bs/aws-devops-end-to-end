"""
Deployment Repository
Data access layer for deployments (in-memory for demo, would be DB in production)
"""
from typing import List, Optional
from datetime import datetime
import uuid
from app.models.deployment import Deployment, DeploymentStatus


class DeploymentRepository:
    """Repository for deployment data access"""
    
    def __init__(self):
        self._deployments: dict[str, Deployment] = {}
    
    def create(self, deployment: Deployment) -> Deployment:
        """Create a new deployment"""
        if not deployment.id:
            deployment.id = str(uuid.uuid4())
        
        deployment.created_at = datetime.utcnow()
        deployment.updated_at = datetime.utcnow()
        
        self._deployments[deployment.id] = deployment
        return deployment
    
    def get_by_id(self, deployment_id: str) -> Optional[Deployment]:
        """Get deployment by ID"""
        return self._deployments.get(deployment_id)
    
    def list_all(self, skip: int = 0, limit: int = 100) -> List[Deployment]:
        """List all deployments with pagination"""
        deployments = list(self._deployments.values())
        return deployments[skip:skip + limit]
    
    def update(self, deployment: Deployment) -> Deployment:
        """Update existing deployment"""
        deployment.updated_at = datetime.utcnow()
        self._deployments[deployment.id] = deployment
        return deployment
    
    def count(self) -> int:
        """Count total deployments"""
        return len(self._deployments)
    
    def count_by_status(self, status: DeploymentStatus) -> int:
        """Count deployments by status"""
        return sum(1 for d in self._deployments.values() if d.status == status)
