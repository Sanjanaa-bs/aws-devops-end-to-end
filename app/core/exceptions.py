"""
Custom Application Exceptions
Domain-specific exceptions for better error handling
"""


class ApplicationError(Exception):
    """Base application exception"""
    
    def __init__(self, message: str, code: str = "APP_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class DeploymentNotFoundError(ApplicationError):
    """Raised when deployment is not found"""
    
    def __init__(self, deployment_id: str):
        super().__init__(
            message=f"Deployment {deployment_id} not found",
            code="DEPLOYMENT_NOT_FOUND"
        )


class DeploymentFailedError(ApplicationError):
    """Raised when deployment fails"""
    
    def __init__(self, reason: str):
        super().__init__(
            message=f"Deployment failed: {reason}",
            code="DEPLOYMENT_FAILED"
        )


class ValidationError(ApplicationError):
    """Raised when validation fails"""
    
    def __init__(self, message: str):
        super().__init__(message=message, code="VALIDATION_ERROR")


class ServiceUnavailableError(ApplicationError):
    """Raised when external service is unavailable"""
    
    def __init__(self, service: str):
        super().__init__(
            message=f"Service {service} is unavailable",
            code="SERVICE_UNAVAILABLE"
        )
