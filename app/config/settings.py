"""
Application Settings and Configuration Management
Loads configuration from environment variables with sensible defaults
"""
from typing import Optional
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment"""
    
    # Application
    app_name: str = "DevOps Platform API"
    app_version: str = "1.0.0"
    environment: str = "production"
    debug: bool = False
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # API
    api_prefix: str = "/api/v1"
    
    # CORS
    cors_origins: list[str] = ["*"]
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "json"
    
    # Monitoring
    enable_metrics: bool = True
    metrics_port: int = 9090
    
    # Database (placeholder for future expansion)
    database_url: Optional[str] = None
    
    # AWS
    aws_region: str = "us-east-1"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


settings = get_settings()
