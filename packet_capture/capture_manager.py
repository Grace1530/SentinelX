from typing import Any

from packet_capture.capture import PacketCapture


class CaptureManager:
    def __init__(self) -> None:
        self.capture: PacketCapture | None = None

    def create_capture(
        self,
        interface: str | None = None,
        store_packets: bool = True,
    ) -> PacketCapture:
        self.capture = PacketCapture(
            interface=interface,
            packet_callback=self._on_packet,
            store_packets=store_packets,
        )

        return self.capture

    def _on_packet(self, packet: dict[str, Any]) -> None:
        print(
            "[PACKET] "
            f"{packet.get('source_ip')} -> "
            f"{packet.get('destination_ip')} "
            f"{packet.get('protocol')}"
        )

    def start(
        self,
        interface: str | None = None,
        packet_count: int = 0,
        store_packets: bool = True,
    ) -> None:
        if self.capture is None:
            self.create_capture(
                interface=interface,
                store_packets=store_packets,
            )

        if self.capture is None:
            raise RuntimeError(
                "Unable to initialize packet capture."
            )

        self.capture.start(packet_count=packet_count)

    def stop(self) -> None:
        if self.capture:
            self.capture.stop()

    def statistics(self) -> dict[str, int | bool]:
        if not self.capture:
            return {
                "running": False,
                "packet_count": 0,
                "flow_count": 0,
            }

        return self.capture.get_statistics()


capture_manager = CaptureManager()