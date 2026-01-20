"""
Date and Time Utilities
"""
from datetime import datetime, timezone
from typing import Optional


def utcnow() -> datetime:
    """Get current UTC time"""
    return datetime.now(timezone.utc)


def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format datetime to string"""
    return dt.strftime(fmt)


def parse_datetime(dt_str: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> Optional[datetime]:
    """Parse datetime from string"""
    try:
        return datetime.strptime(dt_str, fmt)
    except ValueError:
        return None


def calculate_duration_seconds(start: datetime, end: datetime) -> float:
    """Calculate duration between two datetimes in seconds"""
    return (end - start).total_seconds()
