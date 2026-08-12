from dataclasses import dataclass
from datetime import datetime, timezone
from random import randint


@dataclass
class SyntheticPacket:
    timestamp: str
    source_ip: str
    destination_ip: str
    source_port: int
    destination_port: int
    protocol: str
    packet_length: int
    tcp_flags: str
    scenario_id: str


def _timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def generate_port_scan(
    source_ip: str,
    destination_ip: str,
    count: int = 20,
) -> list[SyntheticPacket]:
    packets = []

    for port in range(
        20,
        20 + max(count, 1),
    ):
        packets.append(
            SyntheticPacket(
                timestamp=_timestamp(),
                source_ip=source_ip,
                destination_ip=destination_ip,
                source_port=randint(30000, 60000),
                destination_port=port,
                protocol="TCP",
                packet_length=60,
                tcp_flags="S",
                scenario_id="port_scan",
            )
        )

    return packets


def generate_ssh_bruteforce(
    source_ip: str,
    destination_ip: str,
    count: int = 10,
) -> list[SyntheticPacket]:
    return [
        SyntheticPacket(
            timestamp=_timestamp(),
            source_ip=source_ip,
            destination_ip=destination_ip,
            source_port=randint(30000, 60000),
            destination_port=22,
            protocol="TCP",
            packet_length=74,
            tcp_flags="S",
            scenario_id="ssh_bruteforce",
        )
        for _ in range(max(count, 1))
    ]


def generate_syn_flood(
    source_ip: str,
    destination_ip: str,
    count: int = 50,
) -> list[SyntheticPacket]:
    return [
        SyntheticPacket(
            timestamp=_timestamp(),
            source_ip=source_ip,
            destination_ip=destination_ip,
            source_port=randint(30000, 60000),
            destination_port=randint(1, 65535),
            protocol="TCP",
            packet_length=60,
            tcp_flags="S",
            scenario_id="syn_flood",
        )
        for _ in range(max(count, 1))
    ]


def generate_http_flood(
    source_ip: str,
    destination_ip: str,
    count: int = 50,
) -> list[SyntheticPacket]:
    return [
        SyntheticPacket(
            timestamp=_timestamp(),
            source_ip=source_ip,
            destination_ip=destination_ip,
            source_port=randint(30000, 60000),
            destination_port=80,
            protocol="TCP",
            packet_length=512,
            tcp_flags="PA",
            scenario_id="http_flood",
        )
        for _ in range(max(count, 1))
    ]