from dataclasses import dataclass
from typing import Literal


ScenarioType = Literal[
    "port_scan",
    "ssh_bruteforce",
    "syn_flood",
    "http_flood",
]


@dataclass(frozen=True)
class AttackScenario:
    id: ScenarioType
    name: str
    description: str
    difficulty: str
    target_protocol: str
    default_duration: int


SCENARIOS = [
    AttackScenario(
        id="port_scan",
        name="Port Scan",
        description="Controlled multi-port scanning simulation.",
        difficulty="EASY",
        target_protocol="TCP",
        default_duration=10,
    ),
    AttackScenario(
        id="ssh_bruteforce",
        name="SSH Brute Force",
        description="Controlled repeated SSH connection simulation.",
        difficulty="MEDIUM",
        target_protocol="TCP",
        default_duration=15,
    ),
    AttackScenario(
        id="syn_flood",
        name="Controlled SYN Flood",
        description="Synthetic high-volume SYN traffic simulation.",
        difficulty="MEDIUM",
        target_protocol="TCP",
        default_duration=10,
    ),
    AttackScenario(
        id="http_flood",
        name="Controlled HTTP Flood",
        description="Synthetic high-volume HTTP request simulation.",
        difficulty="MEDIUM",
        target_protocol="TCP",
        default_duration=10,
    ),
]