from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.app.services.ai_detection_service import (
    ai_detection_service,
)


router = APIRouter(
    prefix="/api/ai",
    tags=["AI Detection"],
)


class AIDetectionRequest(BaseModel):
    features: dict[str, float] = Field(
        default_factory=dict
    )
    whitelisted: bool = False


@router.get("/status")
def ai_status() -> dict[str, Any]:
    return {
        "service": "SentinelX AI Engine",
        "ready": ai_detection_service.ready(),
        "model": "sentinelx-random-forest",
        "version": "0.1.0",
    }


@router.post("/predict")
def ai_predict(
    request: AIDetectionRequest,
) -> dict[str, Any]:
    if not ai_detection_service.ready():
        raise HTTPException(
            status_code=503,
            detail="AI model is not available.",
        )

    try:
        return ai_detection_service.analyze(
            features=request.features,
            whitelisted=request.whitelisted,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"AI inference failed: {exc}",
        ) from exc