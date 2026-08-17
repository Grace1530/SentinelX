from datetime import datetime, timezone

import requests
from scapy.all import IP, TCP, UDP, sniff


SENTINELX_URL = (
    "http://192.168.83.1:8000/api/pipeline/packet"
)

CREATE_ALERTS = False
ENABLE_PREVENTION = False


def packet_to_dict(packet):
    if not packet.haslayer(IP):
        return None

    ip = packet[IP]

    protocol = "OTHER"
    source_port = 0
    destination_port = 0
    tcp_flags = ""

    if packet.haslayer(TCP):
        protocol = "TCP"
        source_port = int(packet[TCP].sport)
        destination_port = int(packet[TCP].dport)
        tcp_flags = str(packet[TCP].flags)

    elif packet.haslayer(UDP):
        protocol = "UDP"
        source_port = int(packet[UDP].sport)
        destination_port = int(packet[UDP].dport)

    return {
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),
        "source_ip": ip.src,
        "destination_ip": ip.dst,
        "source_port": source_port,
        "destination_port": destination_port,
        "protocol": protocol,
        "packet_length": len(packet),
        "tcp_flags": tcp_flags,
        "ttl": int(ip.ttl),
        "interface": "eth0",
    }


def send_to_sentinelx(packet_data):
    payload = {
        "packet": packet_data,
        "create_alert": CREATE_ALERTS,
        "enable_prevention": ENABLE_PREVENTION,
    }

    try:
        response = requests.post(
            SENTINELX_URL,
            json=payload,
            timeout=5,
        )

        if response.ok:
            print(
                "[SentinelX]",
                response.status_code,
                response.json(),
            )
        else:
            print(
                "[SentinelX]",
                f"HTTP {response.status_code}:",
                response.text,
            )

    except requests.RequestException as exc:
        print(
            "[SentinelX] Connection error:",
            exc,
        )


def process_packet(packet):
    packet_data = packet_to_dict(packet)

    if packet_data is None:
        return

    print(
        "[Packet]",
        packet_data["source_ip"],
        "->",
        packet_data["destination_ip"],
        "|",
        packet_data["protocol"],
        "|",
        packet_data["source_port"],
        "->",
        packet_data["destination_port"],
    )

    send_to_sentinelx(packet_data)


def main():
    print("==========================================")
    print("SentinelX Kali Packet Sensor")
    print("==========================================")
    print("SentinelX:", SENTINELX_URL)
    print("Interface: eth0")
    print("Create alerts:", CREATE_ALERTS)
    print("Prevention:", ENABLE_PREVENTION)
    print("Press Ctrl+C to stop.")
    print("==========================================")

    sniff(
        iface="eth0",
        prn=process_packet,
        store=False,
        filter=(
            "ip and not "
            "(host 192.168.83.1 and port 8000)"
        ),
    )


if __name__ == "__main__":
    main()