from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Incident:
    id: Optional[int]
    incident_id: str
    title: str
    attack_type: Optional[str]
    severity: Optional[str]
    source_ip: Optional[str]
    status: str
    first_seen: Optional[datetime]
    last_seen: Optional[datetime]
    alert_count: int
    resolution: Optional[str]