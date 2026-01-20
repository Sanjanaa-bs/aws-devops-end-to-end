"""
Application Lifecycle Events
Startup and shutdown event handlers
"""
import logging
from fastapi import FastAPI
from app.config import settings
from app.config.logging_config import setup_logging

logger = logging.getLogger(__name__)


async def startup_event(app: FastAPI) -> None:
    """Execute on application startup"""
    setup_logging(settings.log_level, settings.log_format)
    
    logger.info(
        "Application starting",
        extra={
            "app_name": settings.app_name,
            "version": settings.app_version,
            "environment": settings.environment,
        }
    )
    
    # Initialize connections, caches, etc.
    logger.info("Startup complete")


async def shutdown_event(app: FastAPI) -> None:
    """Execute on application shutdown"""
    logger.info("Application shutting down")
    
    # Close connections, cleanup resources
    logger.info("Shutdown complete")
