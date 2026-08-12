from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel

from ips_engine.response_engine import (
    response_engine,
)


router = APIRouter(
    prefix="/api/ips",
    tags=["IPS"],
)


class ResponseRequest(BaseModel):
    prediction: dict[str, Any]
    source_ip: str | None = None
    whitelisted: bool = False


@router.post("/decide")
def decide_response(
    request: ResponseRequest,
) -> dict[str, Any]:

    return response_engine.decide(
        prediction=request.prediction,
        source_ip=request.source_ip,
        whitelisted=request.whitelisted,
    )


@router.get("/status")
def ips_status() -> dict[str, Any]:

    return {
        "service": "SentinelX IPS Engine",
        "ready": True,
        "mode": "DETECTION_AND_RESPONSE",
    }