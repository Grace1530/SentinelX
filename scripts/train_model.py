from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


DATASET = Path("datasets") / "sentinelx_test_data.csv"
MODEL_DIR = Path("ai_engine") / "models"
MODEL_PATH = MODEL_DIR / "sentinelx_baseline.joblib"

FEATURES = [
    "packet_length",
    "source_port",
    "destination_port",
    "ttl",
    "tcp_syn",
    "tcp_ack",
    "tcp_rst",
    "tcp_fin",
]


def main() -> None:
    if not DATASET.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET}"
        )

    data = pd.read_csv(DATASET)

    x = data[FEATURES]
    y = data["label"]

    if len(data) < 4:
        raise ValueError(
            "Test dataset is intentionally small and is not "
            "suitable for real model training yet."
        )

    x_train, _, y_train, _ = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
    )

    model.fit(x_train, y_train)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()