"""
Cloud-Native DevOps Platform - Application Entry Point
Production-grade FastAPI application with structured architecture
"""
import uvicorn
from app.app_factory import create_application
from app.config import settings

# Create application instance
app = create_application()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
