from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from attackforge.attackforge_engine import (
    attackforge_engine,
)
from backend.app.services.sentinel_pipeline import (
    sentinel_pipeline,
)


router = APIRouter(
    prefix="/api/pipeline",
    tags=["Pipeline"],
)


class PacketRequest(BaseModel):
    packet: dict[str, Any]
    create_alert: bool = False
    enable_prevention: bool = False


class AttackForgeRequest(BaseModel):
    scenario_id: str
    packet_count: int = Field(
        default=20,
        ge=1,
        le=1000,
    )
    enable_prevention: bool = False


def _packet_to_dict(
    packet: Any,
) -> dict[str, Any]:
    if hasattr(packet, "__dict__"):
        return dict(packet.__dict__)

    if isinstance(packet, dict):
        return packet

    return {
        "timestamp": getattr(
            packet,
            "timestamp",
            "",
        ),
        "source_ip": getattr(
            packet,
            "source_ip",
            "",
        ),
        "destination_ip": getattr(
            packet,
            "destination_ip",
            "",
        ),
        "source_port": getattr(
            packet,
            "source_port",
            0,
        ),
        "destination_port": getattr(
            packet,
            "destination_port",
            0,
        ),
        "protocol": getattr(
            packet,
            "protocol",
            "",
        ),
        "packet_length": getattr(
            packet,
            "packet_length",
            0,
        ),
        "tcp_flags": getattr(
            packet,
            "tcp_flags",
            "",
        ),
        "ttl": getattr(
            packet,
            "ttl",
            0,
        ),
        "interface": getattr(
            packet,
            "interface",
            "",
        ),
        "scenario_id": getattr(
            packet,
            "scenario_id",
            "",
        ),
    }


@router.post("/packet")
def analyze_packet(
    request: PacketRequest,
) -> dict[str, Any]:
    """
    Process one packet through the central
    SentinelX detection pipeline.
    """

    return sentinel_pipeline.process_packet(
        packet=request.packet,
        create_alert=request.create_alert,
        enable_prevention=request.enable_prevention,
    )


@router.post("/attackforge")
def run_attackforge(
    request: AttackForgeRequest,
) -> dict[str, Any]:
    """
    Run an AttackForge scenario through the
    central SentinelX pipeline.
    """

    try:
        simulation = (
            attackforge_engine.start_scenario(
                scenario_id=request.scenario_id,
                packet_count=request.packet_count,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    packets = [
        _packet_to_dict(packet)
        for packet in simulation.get(
            "packets",
            [],
        )
    ]

    results = sentinel_pipeline.process_packets(
        packets,
        create_alert=True,
        enable_prevention=(
            request.enable_prevention
        ),
    )

    detections = [
        result
        for result in results
        if (
            result["decision"]["detection_type"]
            != "NORMAL"
        )
    ]

    blocked = [
        result
        for result in results
        if result["prevention"] is not None
    ]

    return {
        "session": simulation["session"],
        "packets_processed": len(results),
        "detections": len(detections),
        "blocked": len(blocked),
        "prevention_enabled": (
            request.enable_prevention
        ),
        "results": results,
    }