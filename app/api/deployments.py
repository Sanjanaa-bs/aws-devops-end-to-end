"""
Deployment API Endpoints
RESTful API for deployment management
"""
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
import logging

from app.schemas.deployment_schema import (
    DeploymentCreateRequest,
    DeploymentResponse,
    DeploymentListResponse
)
from app.services.deployment_service import DeploymentService
from app.core.dependencies import get_deployment_service
from app.core.exceptions import DeploymentNotFoundError

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/deployments", tags=["deployments"])


@router.post(
    "",
    response_model=DeploymentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new deployment"
)
async def create_deployment(
    request: DeploymentCreateRequest,
    service: DeploymentService = Depends(get_deployment_service)
) -> DeploymentResponse:
    """Create a new deployment"""
    deployment = service.create_deployment(
        application=request.application,
        version=request.version,
        environment=request.environment,
        deployed_by=request.deployed_by
    )
    return DeploymentResponse.model_validate(deployment)


@router.get(
    "",
    response_model=DeploymentListResponse,
    summary="List all deployments"
)
async def list_deployments(
    page: int = 1,
    page_size: int = 20,
    service: DeploymentService = Depends(get_deployment_service)
) -> DeploymentListResponse:
    """List all deployments with pagination"""
    deployments, total = service.list_deployments(page=page, page_size=page_size)
    
    return DeploymentListResponse(
        deployments=[DeploymentResponse.model_validate(d) for d in deployments],
        total=total,
        page=page,
        page_size=page_size
    )


@router.get(
    "/{deployment_id}",
    response_model=DeploymentResponse,
    summary="Get deployment by ID"
)
async def get_deployment(
    deployment_id: str,
    service: DeploymentService = Depends(get_deployment_service)
) -> DeploymentResponse:
    """Get a specific deployment by ID"""
    try:
        deployment = service.get_deployment(deployment_id)
        return DeploymentResponse.model_validate(deployment)
    except DeploymentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post(
    "/{deployment_id}/start",
    response_model=DeploymentResponse,
    summary="Start a deployment"
)
async def start_deployment(
    deployment_id: str,
    service: DeploymentService = Depends(get_deployment_service)
) -> DeploymentResponse:
    """Start a pending deployment"""
    try:
        deployment = service.start_deployment(deployment_id)
        return DeploymentResponse.model_validate(deployment)
    except DeploymentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post(
    "/{deployment_id}/complete",
    response_model=DeploymentResponse,
    summary="Complete a deployment"
)
async def complete_deployment(
    deployment_id: str,
    success: bool = True,
    error: str = None,
    service: DeploymentService = Depends(get_deployment_service)
) -> DeploymentResponse:
    """Mark a deployment as complete"""
    try:
        deployment = service.complete_deployment(deployment_id, success=success, error=error)
        return DeploymentResponse.model_validate(deployment)
    except DeploymentNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
