from typing import Any

from decision_engine.response_policy import (
    determine_response,
)
from decision_engine.risk_engine import (
    calculate_risk,
)
from decision_engine.severity import (
    determine_severity,
)


class DecisionEngine:
    def evaluate(
        self,
        prediction: dict[str, Any],
        whitelisted: bool = False,
    ) -> dict[str, Any]:
        detection_type = str(
            prediction.get(
                "prediction",
                "NORMAL",
            )
        )

        confidence = prediction.get(
            "confidence"
        )

        severity = determine_severity(
            detection_type,
            confidence,
        )

        risk_score = calculate_risk(
            confidence,
            severity,
        )

        response = determine_response(
            detection_type,
            severity,
            whitelisted,
        )

        return {
            "detection_type": detection_type,
            "confidence": confidence,
            "severity": severity,
            "risk_score": risk_score,
            "response": response,
            "whitelisted": whitelisted,
        }