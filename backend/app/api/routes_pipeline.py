from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from ai_engine.inference_service import inference_service
from attackforge.attackforge_engine import attackforge_engine
from feature_extraction.extractor import extract_features
from packet_capture.flow_tracker import FlowTracker
from ips_engine.response_engine import response_engine


router = APIRouter(
    prefix="/api/pipeline",
    tags=["Pipeline"],
)

flow_tracker = FlowTracker()


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


def _packet_to_dict(packet: Any) -> dict[str, Any]:
    if hasattr(packet, "__dict__"):
        return dict(packet.__dict__)

    if isinstance(packet, dict):
        return packet

    return {
        "timestamp": getattr(packet, "timestamp", ""),
        "source_ip": getattr(packet, "source_ip", ""),
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
        "scenario_id": getattr(
            packet,
            "scenario_id",
            "",
        ),
    }


def _build_explanation(
    prediction: dict[str, Any],
    features: dict[str, float],
) -> dict[str, Any]:

    label = str(
        prediction.get(
            "prediction",
            "NORMAL",
        )
    )

    confidence = float(
        prediction.get(
            "confidence",
            0.0,
        ) or 0.0
    )

    factors: list[str] = []

    if features.get(
        "unique_destination_ports",
        0,
    ) >= 5:
        factors.append(
            "Multiple destination ports observed"
        )

    if features.get(
        "flow_syn_count",
        0,
    ) >= 10:
        factors.append(
            "Repeated TCP SYN activity observed"
        )

    if features.get(
        "flow_rst_count",
        0,
    ) >= 5:
        factors.append(
            "Repeated TCP RST activity observed"
        )

    if features.get(
        "flow_packet_count",
        0,
    ) >= 50:
        factors.append(
            "High packet volume observed"
        )

    if not factors:
        factors.append(
            "Observed traffic does not match "
            "a known malicious behavior pattern"
        )

    return {
        "prediction": label,
        "confidence": confidence,
        "factors": factors,
    }


@router.post("/packet")
def analyze_packet(
    request: PacketRequest,
) -> dict[str, Any]:

    packet = request.packet

    flow = flow_tracker.update(packet)

    features = extract_features(
        packet,
        flow,
    )

    prediction = inference_service.predict(
        features
    )

    explanation = _build_explanation(
        prediction,
        features,
    )

    decision = response_engine.decide(
        prediction=prediction,
        source_ip=packet.get("source_ip"),
        whitelisted=False,
    )

    if not request.enable_prevention:
        decision = {
            **decision,
            "action": (
                "MONITOR"
                if decision["action"] == "BLOCK"
                else decision["action"]
            ),
            "prevention_enabled": False,
        }
    else:
        decision = {
            **decision,
            "prevention_enabled": True,
        }

    return {
        "packet": packet,
        "flow": flow,
        "features": features,
        "prediction": prediction,
        "explanation": explanation,
        "decision": decision,
    }


@router.post("/attackforge")
def run_attackforge(
    request: AttackForgeRequest,
) -> dict[str, Any]:

    try:
        simulation = attackforge_engine.start_scenario(
            scenario_id=request.scenario_id,
            packet_count=request.packet_count,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc

    results: list[dict[str, Any]] = []

    detections = 0
    blocked = 0

    for raw_packet in simulation.get(
        "packets",
        [],
    ):

        packet = _packet_to_dict(raw_packet)

        flow = flow_tracker.update(packet)

        features = extract_features(
            packet,
            flow,
        )

        prediction = inference_service.predict(
            features
        )

        explanation = _build_explanation(
            prediction,
            features,
        )

        decision = response_engine.decide(
            prediction=prediction,
            source_ip=packet.get("source_ip"),
            whitelisted=False,
        )

        if not request.enable_prevention:
            decision = {
                **decision,
                "action": (
                    "MONITOR"
                    if decision["action"] == "BLOCK"
                    else decision["action"]
                ),
                "prevention_enabled": False,
            }
        else:
            decision = {
                **decision,
                "prevention_enabled": True,
            }

        is_detection = (
            str(
                prediction.get(
                    "prediction",
                    "NORMAL",
                )
            ).upper()
            != "NORMAL"
        )

        is_blocked = (
            request.enable_prevention
            and decision["action"] == "BLOCK"
        )

        if is_detection:
            detections += 1

        if is_blocked:
            blocked += 1

        results.append(
            {
                "packet": packet,
                "flow": flow,
                "features": features,
                "prediction": prediction,
                "explanation": explanation,
                "decision": decision,
                "detected": is_detection,
                "blocked": is_blocked,
            }
        )

    return {
        "session": simulation["session"],
        "packets_processed": len(results),
        "detections": detections,
        "blocked": blocked,
        "prevention_enabled": (
            request.enable_prevention
        ),
        "results": results,
    }