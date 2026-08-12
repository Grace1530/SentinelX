from typing import Any

from ai_engine.predictor import Predictor


class Detector:
    def __init__(self, predictor: Predictor) -> None:
        self.predictor = predictor

    def detect(
        self,
        features: dict[str, float],
    ) -> dict[str, Any]:
        return self.predictor.predict(
            [list(features.values())]
        )