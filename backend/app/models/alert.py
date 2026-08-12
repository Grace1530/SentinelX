from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Alert:
    id: Optional[int]
    timestamp: datetime
    source_ip: Optional[str]
    destination_ip: Optional[str]
    source_port: Optional[int]
    destination_port: Optional[int]
    protocol: Optional[str]
    detection_type: str
    severity: str
    confidence: Optional[float]
    explanation: Optional[str]
    mitre_technique: Optional[str]
    status: str = "OPEN"