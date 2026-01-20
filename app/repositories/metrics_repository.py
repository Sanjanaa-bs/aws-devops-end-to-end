"""
Metrics Repository
Collects and stores application metrics
"""
from datetime import datetime
from typing import List
from app.models.metrics import SystemMetrics, ApplicationMetrics, DeploymentMetrics


class MetricsRepository:
    """Repository for metrics data"""
    
    def __init__(self):
        self._request_count = 0
        self._error_count = 0
        self._response_times: List[float] = []
    
    def increment_request_count(self) -> None:
        """Increment request counter"""
        self._request_count += 1
    
    def increment_error_count(self) -> None:
        """Increment error counter"""
        self._error_count += 1
    
    def record_response_time(self, time_ms: float) -> None:
        """Record response time"""
        self._response_times.append(time_ms)
        # Keep only last 1000 entries
        if len(self._response_times) > 1000:
            self._response_times = self._response_times[-1000:]
    
    def get_application_metrics(self) -> ApplicationMetrics:
        """Get current application metrics"""
        avg_response_time = (
            sum(self._response_times) / len(self._response_times)
            if self._response_times else 0.0
        )
        
        return ApplicationMetrics(
            request_count=self._request_count,
            error_count=self._error_count,
            average_response_time_ms=avg_response_time,
            active_connections=0,  # Would track actual connections
            timestamp=datetime.utcnow()
        )
