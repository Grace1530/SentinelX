def calculate_risk(
    confidence: float | None,
    severity: str,
) -> float:
    confidence = max(
        0.0,
        min(
            float(confidence or 0.0),
            1.0,
        ),
    )

    severity_multiplier = {
        "LOW": 0.25,
        "MEDIUM": 0.50,
        "HIGH": 0.75,
        "CRITICAL": 1.00,
    }.get(
        severity,
        0.25,
    )

    return round(
        confidence * severity_multiplier,
        4,
    )


def risk_category(score: float) -> str:
    if score >= 0.75:
        return "CRITICAL"

    if score >= 0.50:
        return "HIGH"

    if score >= 0.25:
        return "MEDIUM"

    return "LOW"