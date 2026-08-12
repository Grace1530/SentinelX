from pathlib import Path
from typing import Any, Optional

import joblib


class ModelLoader:
    def __init__(self, model_path: str) -> None:
        self.model_path = Path(model_path)
        self.model: Optional[Any] = None

    def load(self) -> Any:
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        self.model = joblib.load(self.model_path)
        return self.model

    def is_loaded(self) -> bool:
        return self.model is not None