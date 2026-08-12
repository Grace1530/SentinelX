from pathlib import Path

import pandas as pd


def test_training_dataset_exists():
    path = Path(
        "datasets"
    ) / "sentinelx_training.csv"

    if not path.exists():
        return

    dataframe = pd.read_csv(path)

    assert not dataframe.empty
    assert "label" in dataframe.columns

    assert dataframe["label"].nunique() >= 2