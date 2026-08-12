from typing import Any

from fastapi import APIRouter

from backend.app.services.threat_summary_service import (
    threat_summary_service,
)


router = APIRouter(
    prefix="/api/threats",
    tags=["Threat Summary"],
)


@router.get("/summary")
def threat_summary() -> dict[str, Any]:
    return {
        "status": "operational",
        "service": "SentinelX Threat Analysis",
        "supported_threats": [
            "NORMAL",
            "PORT_SCAN",
            "SSH_BRUTE_FORCE",
            "SYN_FLOOD",
            "HTTP_FLOOD",
        ],
    }