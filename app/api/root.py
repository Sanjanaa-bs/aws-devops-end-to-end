"""
Root API Endpoints
Welcome and version information
"""
from fastapi import APIRouter
from app.config import settings

router = APIRouter(tags=["root"])


@router.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "environment": settings.environment,
        "docs": "/docs",
        "health": "/health"
    }


@router.get("/version")
async def version():
    """Get API version"""
    return {
        "version": settings.app_version,
        "app_name": settings.app_name
    }
