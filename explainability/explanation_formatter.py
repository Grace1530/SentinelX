from typing import Any


def format_explanation(
    prediction: str,
    confidence: float | None,
    factors: list[str],
    top_features: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "prediction": prediction,
        "confidence": confidence,
        "factors": factors,
        "top_features": top_features or [],
    }