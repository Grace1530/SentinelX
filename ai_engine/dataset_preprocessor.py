from typing import Any

import pandas as pd

from feature_extraction.feature_schema import (
    FEATURE_NAMES,
)


class DatasetPreprocessor:
    def prepare(
        self,
        dataframe: pd.DataFrame,
        target_column: str = "label",
    ) -> tuple[pd.DataFrame, pd.Series]:
        required = [
            *FEATURE_NAMES,
            target_column,
        ]

        missing = [
            column
            for column in required
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                "Dataset is missing columns: "
                + ", ".join(missing)
            )

        features = dataframe[
            FEATURE_NAMES
        ].copy()

        target = dataframe[
            target_column
        ].copy()

        features = features.fillna(0)

        for column in features.columns:
            features[column] = pd.to_numeric(
                features[column],
                errors="coerce",
            ).fillna(0)

        target = target.astype(str)

        return features, target

    def class_distribution(
        self,
        target: pd.Series,
    ) -> dict[str, int]:
        counts = target.value_counts()

        return {
            str(label): int(count)
            for label, count in counts.items()
        }