from typing import Any


def calculate_flow_features(
    flow: dict[str, Any],
) -> dict[str, float]:
    packet_count = float(
        flow.get("packet_count") or 0
    )

    byte_count = float(
        flow.get("byte_count") or 0
    )

    duration = 0.0

    first_seen = flow.get("first_seen")
    last_seen = flow.get("last_seen")

    if first_seen and last_seen:
        try:
            from datetime import datetime

            first = datetime.fromisoformat(
                str(first_seen)
            )
            last = datetime.fromisoformat(
                str(last_seen)
            )

            duration = max(
                (last - first).total_seconds(),
                0.0,
            )
        except ValueError:
            duration = 0.0

    packets_per_second = (
        packet_count / duration
        if duration > 0
        else packet_count
    )

    bytes_per_second = (
        byte_count / duration
        if duration > 0
        else byte_count
    )

    return {
        "flow_duration": duration,
        "packets_per_second": packets_per_second,
        "bytes_per_second": bytes_per_second,
        "packet_count": packet_count,
        "byte_count": byte_count,
        "syn_count": float(
            flow.get("syn_count") or 0
        ),
        "ack_count": float(
            flow.get("ack_count") or 0
        ),
        "rst_count": float(
            flow.get("rst_count") or 0
        ),
        "fin_count": float(
            flow.get("fin_count") or 0
        ),
        "unique_destination_ports": float(
            flow.get("unique_destination_ports") or 0
        ),
    }