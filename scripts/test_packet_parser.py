from scapy.layers.inet import IP, TCP

from packet_capture.packet_parser import parse_packet


packet = IP(
    src="192.168.1.10",
    dst="192.168.1.20",
) / TCP(
    sport=50000,
    dport=80,
    flags="S",
)

result = parse_packet(packet)

print("\n=== SentinelX Packet Parser ===")
print(f"Source       : {result['source_ip']}")
print(f"Destination  : {result['destination_ip']}")
print(f"Source Port  : {result['source_port']}")
print(f"Dest Port    : {result['destination_port']}")
print(f"Protocol     : {result['protocol']}")
print(f"TCP Flags    : {result['tcp_flags']}")
print(f"Packet Length: {result['packet_length']}")
print(f"TTL          : {result['ttl']}")