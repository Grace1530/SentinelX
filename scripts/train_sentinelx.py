from pathlib import Path
import json

from ai_engine.train_model import ModelTrainer


DATASET_PATH = (
    Path("datasets")
    / "sentinelx_training.csv"
)


def main() -> None:
    trainer = ModelTrainer()

    result = trainer.train(
        DATASET_PATH
    )

    print("\n=== SentinelX Model Training ===")
    print(
        f"Model       : {result['model']}"
    )
    print(
        f"Accuracy    : {result['accuracy']:.4f}"
    )
    print(
        f"Train       : {result['training_samples']}"
    )
    print(
        f"Test        : {result['testing_samples']}"
    )
    print(
        f"Model path  : {result['model_path']}"
    )

    report_path = (
        Path("reports")
        / "model_training_report.json"
    )

    report_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with report_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            result,
            file,
            indent=2,
            default=str,
        )

    print(
        f"Report saved: {report_path}"
    )


if __name__ == "__main__":
    main()