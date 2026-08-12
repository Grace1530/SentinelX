from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.app.services.traffic_analysis_service import (
    traffic_analysis_service,
)


router = APIRouter(
    prefix="/api/traffic",
    tags=["Traffic Analysis"],
)


class TrafficAnalysisRequest(BaseModel):
    source_ip: str | None = None

    features: dict[str, float] = Field(
        default_factory=dict
    )

    create_alert: bool = True


@router.post("/analyze")
def analyze_traffic(
    request: TrafficAnalysisRequest,
) -> dict[str, Any]:
    return traffic_analysis_service.analyze_features(
        features=request.features,
        source_ip=request.source_ip,
        create_alert=request.create_alert,
    )