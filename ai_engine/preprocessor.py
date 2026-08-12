from typing import Iterable

import numpy as np


class ModelPreprocessor:
    def __init__(self) -> None:
        self.feature_names: list[str] = []

    def fit(
        self,
        feature_names: Iterable[str],
    ) -> None:
        self.feature_names = list(feature_names)

    def transform(
        self,
        features: dict[str, float],
    ) -> np.ndarray:
        if not self.feature_names:
            raise RuntimeError(
                "Preprocessor has not been fitted."
            )

        values = [
            float(features.get(name, 0.0))
            for name in self.feature_names
        ]

        return np.asarray(
            [values],
            dtype=float,
        )