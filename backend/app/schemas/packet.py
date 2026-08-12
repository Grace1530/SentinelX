from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PacketResponse(BaseModel):
    id: int
    timestamp: datetime
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    source_port: Optional[int] = None
    destination_port: Optional[int] = None
    protocol: Optional[str] = None
    packet_length: Optional[int] = None
    tcp_flags: Optional[str] = None
    ttl: Optional[int] = None
    interface: Optional[str] = None
    flow_id: Optional[str] = None