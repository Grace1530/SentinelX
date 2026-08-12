from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Packet:
    id: Optional[int]
    timestamp: datetime
    source_ip: Optional[str]
    destination_ip: Optional[str]
    source_port: Optional[int]
    destination_port: Optional[int]
    protocol: Optional[str]
    packet_length: Optional[int]
    tcp_flags: Optional[str]
    ttl: Optional[int]
    interface: Optional[str]
    flow_id: Optional[str]