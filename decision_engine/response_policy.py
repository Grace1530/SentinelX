def determine_response(
    detection_type: str,
    severity: str,
    whitelisted: bool = False,
) -> str:
    if detection_type == "NORMAL":
        return "MONITOR"

    if whitelisted:
        return "ALERT_ONLY"

    if severity in {
        "HIGH",
        "CRITICAL",
    }:
        return "BLOCK"

    return "ALERT"