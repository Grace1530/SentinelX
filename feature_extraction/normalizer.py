from typing import Iterable

import numpy as np


class FeatureNormalizer:
    def __init__(self) -> None:
        self.mean: np.ndarray | None = None
        self.std: np.ndarray | None = None

    def fit(self, values: Iterable[Iterable[float]]) -> None:
        array = np.asarray(list(values), dtype=float)

        if array.ndim != 2:
            raise ValueError(
                "Feature values must be a 2D collection."
            )

        self.mean = array.mean(axis=0)
        self.std = array.std(axis=0)

        self.std[self.std == 0] = 1.0

    def transform(
        self,
        values: Iterable[Iterable[float]],
    ) -> np.ndarray:
        if self.mean is None or self.std is None:
            raise RuntimeError(
                "Normalizer must be fitted before transform."
            )

        array = np.asarray(list(values), dtype=float)

        return (array - self.mean) / self.std

    def fit_transform(
        self,
        values: Iterable[Iterable[float]],
    ) -> np.ndarray:
        values_list = list(values)

        self.fit(values_list)

        return self.transform(values_list)