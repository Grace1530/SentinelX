from pathlib import Path
from typing import Any

import joblib

from ai_engine.detector import Detector
from ai_engine.model_config import MODEL_PATH
from ai_engine.predictor import Predictor


class AIEngine:
    def __init__(
        self,
        model_path: Path = MODEL_PATH,
    ) -> None:
        self.model_path = Path(model_path)
        self.model: Any = None
        self.detector: Detector | None = None

    def load_model(self) -> None:
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        self.model = joblib.load(
            self.model_path
        )

        self.detector = Detector(
            Predictor(self.model)
        )

    def is_ready(self) -> bool:
        return self.detector is not None

    def predict(
        self,
        features: dict[str, float],
    ) -> dict[str, Any]:
        if self.detector is None:
            raise RuntimeError(
                "AI engine model has not been loaded."
            )

        return self.detector.detect(features)