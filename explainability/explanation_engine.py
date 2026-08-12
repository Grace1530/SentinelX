from typing import Any

from explainability.explainer import Explainer


class ExplanationEngine:
    def __init__(self) -> None:
        self.explainer = Explainer()

    def generate(
        self,
        prediction: dict[str, Any],
        features: dict[str, float],
    ) -> dict[str, Any]:
        return self.explainer.explain_prediction(
            prediction,
            features,
        )