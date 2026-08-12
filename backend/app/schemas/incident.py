from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class IncidentResponse(BaseModel):
    id: int
    incident_id: str
    title: str
    attack_type: Optional[str] = None
    severity: Optional[str] = None
    source_ip: Optional[str] = None
    status: str
    first_seen: Optional[datetime] = None
    last_seen: Optional[datetime] = None
    alert_count: int
    resolution: Optional[str] = None