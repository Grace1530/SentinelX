from typing import Any

from backend.app.services.ai_detection_service import (
    ai_detection_service,
)


class TrafficAnalysisService:
    def analyze_features(
        self,
        features: dict[str, float],
        source_ip: str | None = None,
        create_alert: bool = True,
    ) -> dict[str, Any]:
        result = ai_detection_service.analyze(
            features=features,
            whitelisted=False,
        )

        return {
            "source_ip": source_ip,
            "analysis": result,
            "alert_requested": create_alert,
        }


traffic_analysis_service = TrafficAnalysisService()