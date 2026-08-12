from attackforge.scenario_models import (
    AttackScenario,
    SCENARIOS,
    ScenarioType,
)


class ScenarioRegistry:
    def __init__(self) -> None:
        self._scenarios = {
            scenario.id: scenario
            for scenario in SCENARIOS
        }

    def get(
        self,
        scenario_id: ScenarioType,
    ) -> AttackScenario | None:
        return self._scenarios.get(scenario_id)

    def list_all(self) -> list[AttackScenario]:
        return list(self._scenarios.values())


scenario_registry = ScenarioRegistry()