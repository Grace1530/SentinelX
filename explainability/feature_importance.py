from typing import Any


def get_feature_importance(
    model: Any,
    feature_names: list[str],
) -> dict[str, float]:
    if not hasattr(model, "feature_importances_"):
        return {}

    importances = model.feature_importances_

    return {
        name: float(value)
        for name, value in zip(
            feature_names,
            importances,
        )
    }


def get_top_features(
    model: Any,
    feature_names: list[str],
    limit: int = 5,
) -> list[dict[str, float | str]]:
    importance = get_feature_importance(
        model,
        feature_names,
    )

    ranked = sorted(
        importance.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return [
        {
            "feature": name,
            "importance": round(value, 6),
        }
        for name, value in ranked[:limit]
    ]