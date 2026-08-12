from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.app.services.ai_detection_service import (
    ai_detection_service,
)
from backend.app.services.alert_service import (
    alert_service,
)


router = APIRouter(
    prefix="/api/analyze",
    tags=["Analysis"],
)


class AnalyzeRequest(BaseModel):
    source_ip: str | None = None

    features: dict[str, float] = Field(
        default_factory=dict
    )

    whitelisted: bool = False

    create_alert: bool = True


@router.post("")
def analyze(
    request: AnalyzeRequest,
) -> dict[str, Any]:
    if not ai_detection_service.ready():
        raise HTTPException(
            status_code=503,
            detail="AI model is not available.",
        )

    result = ai_detection_service.analyze(
        features=request.features,
        whitelisted=request.whitelisted,
    )

    alert = None

    decision = result["decision"]

    if (
        request.create_alert
        and decision["detection_type"] != "NORMAL"
    ):
        alert = alert_service.create_alert(
            source_ip=request.source_ip,
            detection_type=(
                decision["detection_type"]
            ),
            severity=decision["severity"],
            confidence=decision["confidence"],
            risk_score=decision["risk_score"],
            explanation=result[
                "explanation"
            ]["factors"],
        )

    return {
        **result,
        "alert": alert,
    }