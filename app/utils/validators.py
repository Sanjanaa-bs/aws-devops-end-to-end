"""
Validation Utilities
"""
import re
from typing import Optional


def is_valid_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_semver(version: str) -> bool:
    """Validate semantic version format (e.g., 1.0.0)"""
    pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?$'
    return bool(re.match(pattern, version))


def is_valid_environment(env: str) -> bool:
    """Validate environment name"""
    valid_envs = {'dev', 'staging', 'prod', 'production', 'development'}
    return env.lower() in valid_envs


def validate_port(port: int) -> bool:
    """Validate port number"""
    return 1 <= port <= 65535
