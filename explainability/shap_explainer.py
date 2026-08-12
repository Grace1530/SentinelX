from typing import Any


class SHAPExplainer:
    def __init__(self, model: Any) -> None:
        self.model = model
        self._explainer: Any = None

    def initialize(self) -> None:
        try:
            import shap

            self._explainer = shap.TreeExplainer(
                self.model
            )
        except Exception:
            self._explainer = None

    def explain(
        self,
        values: list[list[float]],
        feature_names: list[str],
    ) -> list[dict[str, float | str]]:
        if self._explainer is None:
            return []

        try:
            shap_values = self._explainer.shap_values(
                values
            )

            if isinstance(shap_values, list):
                selected = shap_values[0][0]
            else:
                selected = shap_values[0]

            result = [
                {
                    "feature": name,
                    "impact": float(value),
                }
                for name, value in zip(
                    feature_names,
                    selected,
                )
            ]

            result.sort(
                key=lambda item: abs(
                    float(item["impact"])
                ),
                reverse=True,
            )

            return result

        except Exception:
            return []