from datetime import datetime, timezone
from typing import Any

from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.packet import Packet


PROTOCOL_MAP = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
}


def _get_protocol(packet: Packet) -> str | None:
    if TCP in packet:
        return "TCP"

    if UDP in packet:
        return "UDP"

    if ICMP in packet:
        return "ICMP"

    if IP in packet:
        return PROTOCOL_MAP.get(packet[IP].proto, str(packet[IP].proto))

    return None


def _get_tcp_flags(packet: Packet) -> str | None:
    if TCP not in packet:
        return None

    return str(packet[TCP].flags)


def _get_source_port(packet: Packet) -> int | None:
    if TCP in packet:
        return int(packet[TCP].sport)

    if UDP in packet:
        return int(packet[UDP].sport)

    return None


def _get_destination_port(packet: Packet) -> int | None:
    if TCP in packet:
        return int(packet[TCP].dport)

    if UDP in packet:
        return int(packet[UDP].dport)

    return None


def parse_packet(packet: Packet) -> dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()

    result: dict[str, Any] = {
        "timestamp": timestamp,
        "source_ip": None,
        "destination_ip": None,
        "source_port": None,
        "destination_port": None,
        "protocol": None,
        "packet_length": len(packet),
        "tcp_flags": None,
        "ttl": None,
        "interface": None,
    }

    if IP not in packet:
        return result

    result["source_ip"] = packet[IP].src
    result["destination_ip"] = packet[IP].dst
    result["ttl"] = int(packet[IP].ttl)
    result["protocol"] = _get_protocol(packet)
    result["source_port"] = _get_source_port(packet)
    result["destination_port"] = _get_destination_port(packet)
    result["tcp_flags"] = _get_tcp_flags(packet)

    return result