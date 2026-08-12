from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AlertResponse(BaseModel):
    id: int
    timestamp: datetime
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    source_port: Optional[int] = None
    destination_port: Optional[int] = None
    protocol: Optional[str] = None
    detection_type: str
    severity: str
    confidence: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )
    explanation: Optional[str] = None
    mitre_technique: Optional[str] = None
    status: str