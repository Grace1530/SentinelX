SEVERITY_ORDER = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4,
}


def determine_severity(
    detection_type: str,
    confidence: float | None,
) -> str:
    confidence = confidence or 0.0

    if detection_type == "NORMAL":
        return "LOW"

    if confidence >= 0.95:
        return "HIGH"

    if confidence >= 0.80:
        return "MEDIUM"

    return "LOW"


def escalate_severity(
    current: str,
    new: str,
) -> str:
    current_value = SEVERITY_ORDER.get(
        current,
        1,
    )

    new_value = SEVERITY_ORDER.get(
        new,
        1,
    )

    return (
        new
        if new_value > current_value
        else current
    )