"""
String Utilities
"""
import re
from typing import Optional


def sanitize_string(value: str, max_length: int = 255) -> str:
    """Sanitize string input"""
    # Remove leading/trailing whitespace
    value = value.strip()
    
    # Truncate if too long
    if len(value) > max_length:
        value = value[:max_length]
    
    return value


def slugify(value: str) -> str:
    """Convert string to slug format"""
    value = value.lower()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[-\s]+', '-', value)
    return value.strip('-')


def mask_sensitive_data(value: str, visible_chars: int = 4) -> str:
    """Mask sensitive data, showing only last N characters"""
    if len(value) <= visible_chars:
        return '*' * len(value)
    
    masked_part = '*' * (len(value) - visible_chars)
    visible_part = value[-visible_chars:]
    
    return masked_part + visible_part
