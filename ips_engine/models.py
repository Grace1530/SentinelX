from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class BlockRequest:
    ip_address: str
    reason: str
    detection_type: Optional[str] = None
    severity: Optional[str] = None


@dataclass
class BlockResult:
    success: bool
    ip_address: str
    action: str
    message: str
    timestamp: datetime