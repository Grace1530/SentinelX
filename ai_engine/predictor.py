from typing import Any


class Predictor:
    def __init__(self, model: Any) -> None:
        self.model = model

    def predict(
        self,
        features: list[list[float]],
    ) -> dict[str, Any]:
        prediction = self.model.predict(
            features
        )[0]

        result: dict[str, Any] = {
            "prediction": str(prediction),
            "confidence": None,
        }

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(
                features
            )[0]

            result["confidence"] = float(
                max(probabilities)
            )

        return result