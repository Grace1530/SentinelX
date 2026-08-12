from typing import Any

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from backend.app.services.incident_service import (
    incident_service,
)


router = APIRouter(
    prefix="/api/incidents",
    tags=["Incidents"],
)


class IncidentCreateRequest(BaseModel):
    title: str
    attack_type: str | None = None
    severity: str = "MEDIUM"
    source_ip: str | None = None
    alert_count: int = 0


class IncidentStatusRequest(BaseModel):
    status: str
    resolution: str | None = None


@router.post("")
def create_incident(
    request: IncidentCreateRequest,
) -> dict[str, Any]:

    return incident_service.create_incident(
        title=request.title,
        attack_type=request.attack_type,
        severity=request.severity,
        source_ip=request.source_ip,
        alert_count=request.alert_count,
    )


@router.get("")
def get_incidents(
    limit: int = Query(
        default=100,
        ge=1,
        le=1000,
    ),
) -> dict[str, Any]:

    incidents = incident_service.list_incidents(
        limit
    )

    return {
        "items": incidents,
        "total": len(incidents),
    }


@router.get("/{incident_id}")
def get_incident(
    incident_id: str,
) -> dict[str, Any]:

    incident = incident_service.get_incident(
        incident_id
    )

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found.",
        )

    return incident


@router.patch("/{incident_id}/status")
def update_incident_status(
    incident_id: str,
    request: IncidentStatusRequest,
) -> dict[str, Any]:

    incident = incident_service.update_status(
        incident_id=incident_id,
        status=request.status,
        resolution=request.resolution,
    )

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found.",
        )

    return incident