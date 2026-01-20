"""
Global Error Handler Middleware
Catches and formats all application exceptions
"""
import logging
from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.core.exceptions import ApplicationError

logger = logging.getLogger(__name__)


async def error_handler_middleware(request: Request, call_next):
    """Global error handling middleware"""
    try:
        return await call_next(request)
    except ApplicationError as exc:
        logger.error(
            f"Application error: {exc.message}",
            extra={
                "error_code": exc.code,
                "request_id": getattr(request.state, "request_id", None),
            }
        )
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "error": exc.code,
                "message": exc.message,
                "request_id": getattr(request.state, "request_id", None),
            }
        )
    except Exception as exc:
        logger.exception(
            "Unhandled exception",
            extra={"request_id": getattr(request.state, "request_id", None)}
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "error": "INTERNAL_SERVER_ERROR",
                "message": "An unexpected error occurred",
                "request_id": getattr(request.state, "request_id", None),
            }
        )
