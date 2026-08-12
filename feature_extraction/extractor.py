from typing import Any

from feature_extraction.feature_schema import (
    FEATURE_NAMES,
)


def _flag_present(
    flags: str,
    flag: str,
) -> float:
    return float(flag in flags)


def extract_features(
    packet: dict[str, Any],
    flow: dict[str, Any] | None = None,
) -> dict[str, float]:

    flow = flow or {}

    flags = str(
        packet.get("tcp_flags") or ""
    )

    features = {
        "packet_length": float(
            packet.get("packet_length") or 0
        ),

        "source_port": float(
            packet.get("source_port") or 0
        ),

        "destination_port": float(
            packet.get("destination_port") or 0
        ),

        "ttl": float(
            packet.get("ttl") or 0
        ),

        "tcp_syn": _flag_present(
            flags,
            "S",
        ),

        "tcp_ack": _flag_present(
            flags,
            "A",
        ),

        "tcp_rst": _flag_present(
            flags,
            "R",
        ),

        "tcp_fin": _flag_present(
            flags,
            "F",
        ),

        "flow_packet_count": float(
            flow.get("packet_count") or 0
        ),

        "flow_byte_count": float(
            flow.get("byte_count") or 0
        ),

        "flow_syn_count": float(
            flow.get("syn_count") or 0
        ),

        "flow_ack_count": float(
            flow.get("ack_count") or 0
        ),

        "flow_rst_count": float(
            flow.get("rst_count") or 0
        ),

        "flow_fin_count": float(
            flow.get("fin_count") or 0
        ),

        "unique_destination_ports": float(
            flow.get(
                "unique_destination_ports"
            ) or 0
        ),
    }

    return {
        name: features.get(
            name,
            0.0,
        )
        for name in FEATURE_NAMES
    }