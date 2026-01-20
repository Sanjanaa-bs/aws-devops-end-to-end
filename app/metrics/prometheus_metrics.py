"""
Prometheus Metrics Collector
Exposes application metrics in Prometheus format
"""
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from typing import Dict


class PrometheusMetrics:
    """Prometheus metrics collector"""
    
    def __init__(self):
        # Request metrics
        self.request_count = Counter(
            'http_requests_total',
            'Total HTTP requests',
            ['method', 'endpoint', 'status']
        )
        
        self.request_duration = Histogram(
            'http_request_duration_seconds',
            'HTTP request duration',
            ['method', 'endpoint']
        )
        
        # Deployment metrics
        self.deployment_count = Counter(
            'deployments_total',
            'Total deployments',
            ['status', 'environment']
        )
        
        self.deployment_duration = Histogram(
            'deployment_duration_seconds',
            'Deployment duration',
            ['environment']
        )
        
        # System metrics
        self.cpu_usage = Gauge('cpu_usage_percent', 'CPU usage percentage')
        self.memory_usage = Gauge('memory_usage_percent', 'Memory usage percentage')
        self.active_tasks = Gauge('active_ecs_tasks', 'Number of active ECS tasks')
    
    def record_request(self, method: str, endpoint: str, status: int, duration: float):
        """Record HTTP request metrics"""
        self.request_count.labels(method=method, endpoint=endpoint, status=status).inc()
        self.request_duration.labels(method=method, endpoint=endpoint).observe(duration)
    
    def record_deployment(self, status: str, environment: str, duration: float):
        """Record deployment metrics"""
        self.deployment_count.labels(status=status, environment=environment).inc()
        self.deployment_duration.labels(environment=environment).observe(duration)
    
    def update_system_metrics(self, cpu: float, memory: float):
        """Update system metrics"""
        self.cpu_usage.set(cpu)
        self.memory_usage.set(memory)
    
    def export_metrics(self) -> bytes:
        """Export metrics in Prometheus format"""
        return generate_latest()


# Global metrics instance
metrics = PrometheusMetrics()
