from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
)

from ai_engine.dataset_loader import (
    DatasetLoader,
)
from ai_engine.dataset_preprocessor import (
    DatasetPreprocessor,
)
from ai_engine.training_config import (
    RANDOM_STATE,
    TEST_SIZE,
    TARGET_COLUMN,
    MODEL_OUTPUT_DIR,
)
from feature_extraction.feature_schema import (
    FEATURE_NAMES,
)


class ModelTrainer:
    def __init__(
        self,
        model_output_dir: Path = MODEL_OUTPUT_DIR,
    ) -> None:
        self.model_output_dir = Path(
            model_output_dir
        )

        self.model_output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def train(
        self,
        dataset_path: str | Path,
    ) -> dict:
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

        if target.nunique() < 2:
            raise ValueError(
                "Training requires at least two classes."
            )

        x_train, x_test, y_train, y_test = (
            train_test_split(
                features,
                target,
                test_size=TEST_SIZE,
                random_state=RANDOM_STATE,
                stratify=target,
            )
        )

        model = RandomForestClassifier(
            n_estimators=200,
            random_state=RANDOM_STATE,
            n_jobs=-1,
            class_weight="balanced",
        )

        model.fit(
            x_train,
            y_train,
        )

        predictions = model.predict(
            x_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions,
        )

        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0,
        )

        model_path = (
            self.model_output_dir
            / "sentinelx_random_forest.joblib"
        )

        joblib.dump(
            model,
            model_path,
        )

        return {
            "model": "RandomForest",
            "model_path": str(model_path),
            "accuracy": float(accuracy),
            "features": FEATURE_NAMES,
            "classes": [
                str(value)
                for value in model.classes_
            ],
            "classification_report": report,
            "training_samples": len(x_train),
            "testing_samples": len(x_test),
        }