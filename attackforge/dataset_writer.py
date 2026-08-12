import csv
from pathlib import Path

from attackforge.synthetic_traffic import SyntheticPacket


class AttackForgeDatasetWriter:
    def __init__(
        self,
        output_dir: str = "datasets/attackforge",
    ) -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(
        self,
        packets: list[SyntheticPacket],
        filename: str,
    ) -> Path:
        output_path = self.output_dir / filename

        with output_path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)

            writer.writerow(
                [
                    "timestamp",
                    "source_ip",
                    "destination_ip",
                    "source_port",
                    "destination_port",
                    "protocol",
                    "packet_length",
                    "tcp_flags",
                    "scenario_id",
                ]
            )

            for packet in packets:
                writer.writerow(
                    [
                        packet.timestamp,
                        packet.source_ip,
                        packet.destination_ip,
                        packet.source_port,
                        packet.destination_port,
                        packet.protocol,
                        packet.packet_length,
                        packet.tcp_flags,
                        packet.scenario_id,
                    ]
                )

        return output_path