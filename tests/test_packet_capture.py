from packet_capture.interface import get_available_interfaces
from packet_capture.packet_parser import parse_packet


def test_interfaces_returns_list():
    interfaces = get_available_interfaces()

    assert isinstance(interfaces, list)


def test_parse_empty_packet():
    from scapy.packet import Packet

    packet = Packet()
    result = parse_packet(packet)

    assert "timestamp" in result
    assert "packet_length" in result