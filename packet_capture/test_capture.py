from scapy.layers.inet import IP, TCP

from packet_capture.flow_tracker import FlowTracker
from packet_capture.packet_parser import parse_packet


def test_tcp_packet_parsing():
    packet = IP(
        src="192.168.1.10",
        dst="192.168.1.20",
    ) / TCP(
        sport=50000,
        dport=80,
        flags="S",
    )

    result = parse_packet(packet)

    assert result["source_ip"] == "192.168.1.10"
    assert result["destination_ip"] == "192.168.1.20"
    assert result["source_port"] == 50000
    assert result["destination_port"] == 80
    assert result["protocol"] == "TCP"
    assert result["tcp_flags"] == "S"


def test_flow_tracker():
    tracker = FlowTracker()

    packet = {
        "source_ip": "192.168.1.10",
        "destination_ip": "192.168.1.20",
        "source_port": 50000,
        "destination_port": 80,
        "protocol": "TCP",
        "packet_length": 60,
        "tcp_flags": "S",
    }

    result = tracker.update(packet)

    assert result["packet_count"] == 1
    assert result["byte_count"] == 60
    assert result["syn_count"] == 1
    assert result["unique_destination_ports"] == 1