from typing import Any

from attackforge.lab_session import (
    lab_session_manager,
)
from attackforge.scenario_registry import (
    scenario_registry,
)
from attackforge.simulator import AttackSimulator


class AttackForgeEngine:
    def __init__(self) -> None:
        self.simulator = AttackSimulator()

    def list_scenarios(self) -> list[dict[str, Any]]:
        return [
            {
                "id": scenario.id,
                "name": scenario.name,
                "description": scenario.description,
                "difficulty": scenario.difficulty,
                "target_protocol": scenario.target_protocol,
                "default_duration": scenario.default_duration,
            }
            for scenario in scenario_registry.list_all()
        ]

    def start_scenario(
        self,
        scenario_id: str,
        packet_count: int = 20,
    ) -> dict[str, Any]:
        scenario = scenario_registry.get(
            scenario_id
        )

        if scenario is None:
            raise ValueError(
                f"Unknown scenario: {scenario_id}"
            )

        session = lab_session_manager.start(
            scenario_id
        )

        packets = self.simulator.generate(
            scenario_id,
            packet_count,
        )

        session.packet_count = len(packets)

        lab_session_manager.complete(
            session.session_id,
            len(packets),
        )

        return {
            "session": {
                "session_id": session.session_id,
                "scenario_id": session.scenario_id,
                "status": session.status,
                "packet_count": session.packet_count,
                "started_at": session.started_at,
            },
            "packets": [
                packet.__dict__
                for packet in packets
            ],
        }


attackforge_engine = AttackForgeEngine()