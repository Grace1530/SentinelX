from collections import defaultdict
from datetime import datetime, timezone
from threading import Lock
from typing import Any


class FlowTracker:
    def __init__(self) -> None:
        self._flows: dict[str, dict[str, Any]] = defaultdict(
            self._create_flow
        )
        self._behavior_flows: dict[str, dict[str, Any]] = defaultdict(
            self._create_flow
        )
        self._lock = Lock()

    @staticmethod
    def _create_flow() -> dict[str, Any]:
        return {
            "packet_count": 0,
            "byte_count": 0,
            "first_seen": None,
            "last_seen": None,
            "syn_count": 0,
            "ack_count": 0,
            "rst_count": 0,
            "fin_count": 0,
            "unique_destination_ports": set(),
        }

    @staticmethod
    def create_flow_id(
        packet: dict[str, Any]
    ) -> str:
        source_ip = packet.get("source_ip") or ""
        destination_ip = packet.get("destination_ip") or ""
        source_port = packet.get("source_port") or 0
        destination_port = packet.get("destination_port") or 0
        protocol = packet.get("protocol") or ""

        endpoints = [
            f"{source_ip}:{source_port}",
            f"{destination_ip}:{destination_port}",
        ]

        endpoints.sort()

        return (
            f"{protocol}|"
            f"{endpoints[0]}|"
            f"{endpoints[1]}"
        )

    @staticmethod
    def create_behavior_id(
        packet: dict[str, Any]
    ) -> str:
        source_ip = packet.get("source_ip") or ""
        destination_ip = packet.get("destination_ip") or ""
        protocol = packet.get("protocol") or ""

        return (
            f"{protocol}|"
            f"{source_ip}|"
            f"{destination_ip}"
        )

    @staticmethod
    def _update_flow(
        flow: dict[str, Any],
        packet: dict[str, Any],
        now: str,
    ) -> None:
        flow["packet_count"] += 1

        flow["byte_count"] += int(
            packet.get("packet_length") or 0
        )

        if flow["first_seen"] is None:
            flow["first_seen"] = now

        flow["last_seen"] = now

        flags = str(
            packet.get("tcp_flags") or ""
        )

        if "S" in flags:
            flow["syn_count"] += 1

        if "A" in flags:
            flow["ack_count"] += 1

        if "R" in flags:
            flow["rst_count"] += 1

        if "F" in flags:
            flow["fin_count"] += 1

        destination_port = packet.get(
            "destination_port"
        )

        if destination_port is not None:
            flow[
                "unique_destination_ports"
            ].add(int(destination_port))

    @staticmethod
    def _serialize_flow(
        flow: dict[str, Any]
    ) -> dict[str, Any]:
        return {
            "packet_count": flow["packet_count"],
            "byte_count": flow["byte_count"],
            "first_seen": flow["first_seen"],
            "last_seen": flow["last_seen"],
            "syn_count": flow["syn_count"],
            "ack_count": flow["ack_count"],
            "rst_count": flow["rst_count"],
            "fin_count": flow["fin_count"],
            "unique_destination_ports": len(
                flow["unique_destination_ports"]
            ),
        }

    def update(
        self,
        packet: dict[str, Any]
    ) -> dict[str, Any]:

        flow_id = self.create_flow_id(packet)
        behavior_id = self.create_behavior_id(packet)

        now = datetime.now(
            timezone.utc
        ).isoformat()

        with self._lock:

            flow = self._flows[flow_id]

            self._update_flow(
                flow,
                packet,
                now,
            )

            behavior_flow = (
                self._behavior_flows[behavior_id]
            )

            self._update_flow(
                behavior_flow,
                packet,
                now,
            )

            result = self._serialize_flow(
                behavior_flow
            )

            result["flow_id"] = flow_id
            result["behavior_id"] = behavior_id

            return result

    def get_flow(
        self,
        flow_id: str
    ) -> dict[str, Any] | None:

        with self._lock:

            flow = self._flows.get(flow_id)

            if flow is None:
                return None

            result = self._serialize_flow(flow)

            result["flow_id"] = flow_id

            return result

    def get_behavior_flow(
        self,
        behavior_id: str
    ) -> dict[str, Any] | None:

        with self._lock:

            flow = self._behavior_flows.get(
                behavior_id
            )

            if flow is None:
                return None

            result = self._serialize_flow(flow)

            result["behavior_id"] = behavior_id

            return result

    def clear(self) -> None:

        with self._lock:
            self._flows.clear()
            self._behavior_flows.clear()

    def count(self) -> int:

        with self._lock:
            return len(self._flows)

    def behavior_count(self) -> int:

        with self._lock:
            return len(
                self._behavior_flows
            )