from pathlib import Path

import joblib
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from ai_engine.dataset_loader import (
    DatasetLoader,
)
from ai_engine.dataset_preprocessor import (
    DatasetPreprocessor,
)
from ai_engine.training_config import (
    TARGET_COLUMN,
)


class ModelEvaluator:
    def evaluate(
        self,
        model_path: str | Path,
        dataset_path: str | Path,
    ) -> dict:
        model = joblib.load(
            model_path
        )

        loader = DatasetLoader()
        preprocessor = DatasetPreprocessor()

        dataframe = loader.load_csv(
            dataset_path
        )

        features, target = (
            preprocessor.prepare(
                dataframe,
                TARGET_COLUMN,
            )
        )

        predictions = model.predict(
            features
        )

        accuracy = accuracy_score(
            target,
            predictions,
        )

        report = classification_report(
            target,
            predictions,
            output_dict=True,
            zero_division=0,
        )

        matrix = confusion_matrix(
            target,
            predictions,
        )

        return {
            "accuracy": float(accuracy),
            "classification_report": report,
            "confusion_matrix": matrix.tolist(),
            "samples": len(target),
        }