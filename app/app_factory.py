"""
FastAPI Application Factory
Creates and configures the FastAPI application instance
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.core.events import startup_event, shutdown_event
from app.middlewares.request_id import RequestIDMiddleware
from app.middlewares.logging_middleware import LoggingMiddleware
from app.middlewares.error_handler import error_handler_middleware
from app.api import root, health, deployments, metrics


def create_application() -> FastAPI:
    """
    Application factory pattern
    Creates and configures the FastAPI application
    """
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="Production-grade Cloud-Native DevOps Platform API",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Custom middlewares
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.middleware("http")(error_handler_middleware)
    
    # Register routers
    app.include_router(root.router)
    app.include_router(health.router)
    app.include_router(deployments.router, prefix="/api/v1")
    app.include_router(metrics.router, prefix="/api/v1")
    
    # Lifecycle events
    @app.on_event("startup")
    async def on_startup():
        await startup_event(app)
    
    @app.on_event("shutdown")
    async def on_shutdown():
        await shutdown_event(app)
    
    return app
