from dataclasses import dataclass
from typing import Optional


@dataclass
class Threat:
    id: Optional[int]
    indicator: str
    indicator_type: str
    threat_type: Optional[str]
    severity: Optional[str]
    source: Optional[str]
    description: Optional[str]
    mitre_technique: Optional[str]