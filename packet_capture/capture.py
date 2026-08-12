from collections.abc import Callable
from typing import Any, Optional

from scapy.all import sniff

from packet_capture.flow_tracker import FlowTracker
from packet_capture.packet_parser import parse_packet
from packet_capture.packet_store import packet_store


class PacketCapture:
    def __init__(
        self,
        interface: Optional[str] = None,
        packet_callback: Optional[Callable[[dict[str, Any]], None]] = None,
        store_packets: bool = True,
    ) -> None:
        self.interface = interface
        self.packet_callback = packet_callback
        self.store_packets = store_packets

        self.flow_tracker = FlowTracker()

        self.running = False
        self.packet_count = 0

    def _process_packet(self, raw_packet: Any) -> None:
        parsed_packet = parse_packet(raw_packet)

        flow = self.flow_tracker.update(parsed_packet)

        parsed_packet["flow_id"] = flow["flow_id"]
        parsed_packet["interface"] = self.interface

        self.packet_count += 1

        if self.store_packets:
            packet_store.save(parsed_packet)

        if self.packet_callback:
            self.packet_callback(parsed_packet)

    def start(self, packet_count: int = 0) -> None:
        self.running = True

        try:
            sniff(
                iface=self.interface,
                prn=self._process_packet,
                count=packet_count,
                store=False,
            )
        finally:
            self.running = False

    def stop(self) -> None:
        self.running = False

    def get_statistics(self) -> dict[str, int | bool]:
        return {
            "running": self.running,
            "packet_count": self.packet_count,
            "flow_count": self.flow_tracker.count(),
        }