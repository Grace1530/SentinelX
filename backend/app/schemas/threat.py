from typing import Optional

from pydantic import BaseModel


class ThreatResponse(BaseModel):
    id: int
    indicator: str
    indicator_type: str
    threat_type: Optional[str] = None
    severity: Optional[str] = None
    source: Optional[str] = None
    description: Optional[str] = None
    mitre_technique: Optional[str] = None