import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


from ai_engine.evaluate_model import ModelEvaluator


DATASET_PATH = (
    ROOT_DIR
    / "datasets"
    / "sentinelx_training.csv"
)

MODEL_PATH = (
    ROOT_DIR
    / "ai_engine"
    / "models"
    / "sentinelx_random_forest.joblib"
)


def main() -> None:
    evaluator = ModelEvaluator()

    result = evaluator.evaluate(
        MODEL_PATH,
        DATASET_PATH,
    )

    print("\n=== SentinelX Model Evaluation ===")
    print(
        f"Accuracy: {result['accuracy']:.4f}"
    )
    print(
        f"Samples : {result['samples']}"
    )

    import json

    report_path = (
        ROOT_DIR
        / "reports"
        / "model_evaluation.json"
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
        )

    print(
        f"Report saved: {report_path}"
    )


if __name__ == "__main__":
    main()