from pathlib import Path

import pandas as pd


class DatasetLoader:
    def load_csv(
        self,
        path: str | Path,
    ) -> pd.DataFrame:
        dataset_path = Path(path)

        if not dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {dataset_path}"
            )

        if dataset_path.suffix.lower() != ".csv":
            raise ValueError(
                "Only CSV datasets are currently supported."
            )

        dataframe = pd.read_csv(dataset_path)

        if dataframe.empty:
            raise ValueError(
                "Dataset is empty."
            )

        return dataframe

    def validate_columns(
        self,
        dataframe: pd.DataFrame,
        required_columns: list[str],
    ) -> None:
        missing = [
            column
            for column in required_columns
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                "Missing required columns: "
                + ", ".join(missing)
            )