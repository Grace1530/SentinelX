from typing import Any

from decision_engine.decision import DecisionEngine
from explainability.explanation_engine import (
    ExplanationEngine,
)


class DetectionService:
    def __init__(self) -> None:
        self.decision_engine = DecisionEngine()
        self.explanation_engine = ExplanationEngine()

    def process(
        self,
        prediction: dict[str, Any],
        features: dict[str, float],
        whitelisted: bool = False,
    ) -> dict[str, Any]:
        explanation = (
            self.explanation_engine.generate(
                prediction,
                features,
            )
        )

        decision = self.decision_engine.evaluate(
            prediction,
            whitelisted=whitelisted,
        )

        return {
            "prediction": prediction,
            "explanation": explanation,
            "decision": decision,
        }


detection_service = DetectionService()