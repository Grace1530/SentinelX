from typing import Any

from ai_engine.inference_service import (
    inference_service,
)
from backend.app.services.detection_service import (
    detection_service,
)


class AIDetectionService:
    def analyze(
        self,
        features: dict[str, float],
        whitelisted: bool = False,
    ) -> dict[str, Any]:
        prediction = inference_service.predict(
            features
        )

        result = detection_service.process(
            prediction=prediction,
            features=features,
            whitelisted=whitelisted,
        )

        return result

    def ready(self) -> bool:
        return inference_service.is_ready()


ai_detection_service = AIDetectionService()