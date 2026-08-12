from pathlib import Path
from typing import Any

import joblib


class ModelManager:
    def __init__(
        self,
        model_path: str | Path,
    ) -> None:
        self.model_path = Path(
            model_path
        )
        self.model: Any = None

    def load(self) -> Any:
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        self.model = joblib.load(
            self.model_path
        )

        return self.model

    def is_loaded(self) -> bool:
        return self.model is not None

    def predict(
        self,
        features,
    ):
        if self.model is None:
            self.load()

        return self.model.predict(
            features
        )

    def predict_proba(
        self,
        features,
    ):
        if self.model is None:
            self.load()

        if not hasattr(
            self.model,
            "predict_proba",
        ):
            return None

        return self.model.predict_proba(
            features
        )