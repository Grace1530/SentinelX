from typing import Any


class ResponseEngine:
    def decide(
        self,
        prediction: dict[str, Any],
        source_ip: str | None = None,
        whitelisted: bool = False,
    ) -> dict[str, Any]:

        label = str(
            prediction.get("prediction", "NORMAL")
        ).upper()

        confidence = float(
            prediction.get("confidence") or 0.0
        )

        if label == "NORMAL":
            return {
                "action": "MONITOR",
                "severity": "LOW",
                "risk_score": round(
                    confidence * 0.25,
                    4,
                ),
                "source_ip": source_ip,
                "whitelisted": whitelisted,
                "reason": (
                    "Traffic matches normal "
                    "behavior."
                ),
            }

        if whitelisted:
            return {
                "action": "MONITOR",
                "severity": "MEDIUM",
                "risk_score": round(
                    confidence * 0.5,
                    4,
                ),
                "source_ip": source_ip,
                "whitelisted": True,
                "reason": (
                    "Threat detected but source "
                    "is whitelisted."
                ),
            }

        severity = "HIGH"

        if confidence < 0.70:
            severity = "MEDIUM"

        if confidence < 0.50:
            severity = "LOW"

        risk_score = round(
            min(
                1.0,
                confidence * 0.75 + 0.25,
            ),
            4,
        )

        return {
            "action": "BLOCK",
            "severity": severity,
            "risk_score": risk_score,
            "source_ip": source_ip,
            "whitelisted": False,
            "reason": (
                f"Detected malicious traffic: "
                f"{label}."
            ),
        }


response_engine = ResponseEngine()