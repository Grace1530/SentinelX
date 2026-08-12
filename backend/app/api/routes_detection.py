from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.app.services.detection_service import (
    detection_service,
)


router = APIRouter(
    prefix="/api/detection",
    tags=["Detection"],
)


class DetectionRequest(BaseModel):
    prediction: str
    confidence: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )

    features: dict[str, float] = {}

    whitelisted: bool = False


@router.post("/evaluate")
def evaluate_detection(
    request: DetectionRequest,
) -> dict[str, Any]:
    prediction = {
        "prediction": request.prediction,
        "confidence": request.confidence,
    }

    return detection_service.process(
        prediction=prediction,
        features=request.features,
        whitelisted=request.whitelisted,
    )