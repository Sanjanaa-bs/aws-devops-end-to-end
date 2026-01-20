"""
Metrics Service
Business logic for metrics collection and aggregation
"""
import psutil
from datetime import datetime
from app.models.metrics import SystemMetrics, ApplicationMetrics, DeploymentMetrics
from app.repositories.metrics_repository import MetricsRepository


class MetricsService:
    """Service for metrics operations"""
    
    def __init__(self):
        self.repository = MetricsRepository()
    
    def get_system_metrics(self) -> SystemMetrics:
        """Collect current system metrics"""
        return SystemMetrics(
            cpu_usage_percent=psutil.cpu_percent(interval=1),
            memory_usage_percent=psutil.virtual_memory().percent,
            disk_usage_percent=psutil.disk_usage('/').percent,
            timestamp=datetime.utcnow()
        )
    
    def get_application_metrics(self) -> ApplicationMetrics:
        """Get application metrics"""
        return self.repository.get_application_metrics()
    
    def get_deployment_metrics(self, deployment_repository) -> DeploymentMetrics:
        """Calculate deployment metrics"""
        from app.models.deployment import DeploymentStatus
        
        total = deployment_repository.count()
        successful = deployment_repository.count_by_status(DeploymentStatus.SUCCESS)
        failed = deployment_repository.count_by_status(DeploymentStatus.FAILED)
        
        return DeploymentMetrics(
            total_deployments=total,
            successful_deployments=successful,
            failed_deployments=failed,
            average_deployment_time_seconds=0.0,  # Would calculate from actual data
            timestamp=datetime.utcnow()
        )
    
    def record_request(self) -> None:
        """Record a request"""
        self.repository.increment_request_count()
    
    def record_error(self) -> None:
        """Record an error"""
        self.repository.increment_error_count()
    
    def record_response_time(self, time_ms: float) -> None:
        """Record response time"""
        self.repository.record_response_time(time_ms)
