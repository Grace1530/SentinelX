from typing import Any


class ThreatSummaryService:
    def build_summary(
        self,
        prediction: str,
        confidence: float | None,
        severity: str,
        risk_score: float,
        response: str,
    ) -> dict[str, Any]:
        confidence_percent = None

        if confidence is not None:
            confidence_percent = round(
                confidence * 100,
                2,
            )

        return {
            "threat": prediction,
            "confidence": confidence_percent,
            "severity": severity,
            "risk_score": round(
                risk_score,
                4,
            ),
            "recommended_response": response,
        }


threat_summary_service = ThreatSummaryService()