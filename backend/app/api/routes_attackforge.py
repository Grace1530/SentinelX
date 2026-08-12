from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from attackforge.attackforge_engine import (
    attackforge_engine,
)


router = APIRouter(
    prefix="/api/attackforge",
    tags=["AttackForge"],
)


class ScenarioRunRequest(BaseModel):
    scenario_id: str
    packet_count: int = Field(
        default=20,
        ge=1,
        le=500,
    )


@router.get("/scenarios")
def get_scenarios() -> dict[str, Any]:
    return {
        "scenarios": (
            attackforge_engine.list_scenarios()
        )
    }


@router.post("/simulate")
def simulate_scenario(
    request: ScenarioRunRequest,
) -> dict[str, Any]:
    try:
        return attackforge_engine.start_scenario(
            scenario_id=request.scenario_id,
            packet_count=request.packet_count,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc