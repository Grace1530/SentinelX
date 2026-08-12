from datetime import datetime, timezone
from typing import Any

from backend.app.database.repository import repository


class AlertService:
    def create_alert(
        self,
        source_ip: str | None,
        detection_type: str,
        severity: str,
        confidence: float | None,
        risk_score: float,
        explanation: list[str],
    ) -> dict[str, Any]:
        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        query = """
            INSERT INTO alerts (
                timestamp,
                source_ip,
                detection_type,
                severity,
                confidence,
                risk_score,
                explanation,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        alert_id = repository.execute(
            query,
            [
                timestamp,
                source_ip,
                detection_type,
                severity,
                confidence,
                risk_score,
                " | ".join(explanation),
                "OPEN",
            ],
        )

        return {
            "id": alert_id,
            "timestamp": timestamp,
            "source_ip": source_ip,
            "detection_type": detection_type,
            "severity": severity,
            "confidence": confidence,
            "risk_score": risk_score,
            "explanation": explanation,
            "status": "OPEN",
        }

    def list_alerts(
        self,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        query = """
            SELECT *
            FROM alerts
            ORDER BY id DESC
            LIMIT ?
        """

        return repository.fetch_all(
            query,
            [limit],
        )


alert_service = AlertService()