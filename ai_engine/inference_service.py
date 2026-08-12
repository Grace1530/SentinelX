from typing import Any

from ai_engine.model_config import MODEL_PATH
from ai_engine.model_manager import ModelManager
from feature_extraction.feature_schema import FEATURE_NAMES


class InferenceService:
    def __init__(self) -> None:
        self.model_manager = ModelManager(
            MODEL_PATH
        )

    def is_ready(self) -> bool:
        return self.model_manager.is_loaded() or (
            MODEL_PATH.exists()
        )

    def predict(
        self,
        features: dict[str, float],
    ) -> dict[str, Any]:
        values = [
            float(features.get(name, 0.0))
            for name in FEATURE_NAMES
        ]

        matrix = [values]

        prediction = self.model_manager.predict(
            matrix
        )[0]

        confidence = None
        probabilities = (
            self.model_manager.predict_proba(
                matrix
            )
        )

        if probabilities is not None:
            confidence = float(
                max(probabilities[0])
            )

        return {
            "prediction": str(prediction),
            "confidence": confidence,
            "model": "sentinelx-random-forest",
            "model_version": "0.1.0",
            "feature_version": "0.1.0",
        }


inference_service = InferenceService()