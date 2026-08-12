from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from backend.app.database.repository import repository


class IncidentService:

    def create_incident(
        self,
        title: str,
        attack_type: str | None = None,
        severity: str = "MEDIUM",
        source_ip: str | None = None,
        alert_count: int = 0,
    ) -> dict[str, Any]:

        incident_id = f"INC-{uuid4().hex[:10].upper()}"
        timestamp = datetime.now(timezone.utc).isoformat()

        query = """
            INSERT INTO incidents (
                incident_id,
                title,
                attack_type,
                severity,
                source_ip,
                status,
                first_seen,
                last_seen,
                alert_count
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        database_id = repository.execute(
            query,
            [
                incident_id,
                title,
                attack_type,
                severity,
                source_ip,
                "OPEN",
                timestamp,
                timestamp,
                alert_count,
            ],
        )

        return {
            "id": database_id,
            "incident_id": incident_id,
            "title": title,
            "attack_type": attack_type,
            "severity": severity,
            "source_ip": source_ip,
            "status": "OPEN",
            "first_seen": timestamp,
            "last_seen": timestamp,
            "alert_count": alert_count,
        }

    def list_incidents(
        self,
        limit: int = 100,
    ) -> list[dict[str, Any]]:

        query = """
            SELECT *
            FROM incidents
            ORDER BY created_at DESC
            LIMIT ?
        """

        return repository.fetch_all(query, [limit])

    def get_incident(
        self,
        incident_id: str,
    ) -> dict[str, Any] | None:

        query = """
            SELECT *
            FROM incidents
            WHERE incident_id = ?
        """

        return repository.fetch_one(
            query,
            [incident_id],
        )

    def find_open_incident(
        self,
        attack_type: str,
        source_ip: str | None,
    ) -> dict[str, Any] | None:

        query = """
            SELECT *
            FROM incidents
            WHERE attack_type = ?
              AND source_ip = ?
              AND status = 'OPEN'
            ORDER BY created_at DESC
            LIMIT 1
        """

        return repository.fetch_one(
            query,
            [attack_type, source_ip],
        )

    def add_alert_to_incident(
        self,
        incident_id: str,
        severity: str | None = None,
    ) -> dict[str, Any] | None:

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        if severity is None:
            query = """
                UPDATE incidents
                SET alert_count = alert_count + 1,
                    last_seen = ?
                WHERE incident_id = ?
            """

            parameters = [
                timestamp,
                incident_id,
            ]

        else:
            query = """
                UPDATE incidents
                SET alert_count = alert_count + 1,
                    severity = ?,
                    last_seen = ?
                WHERE incident_id = ?
            """

            parameters = [
                severity,
                timestamp,
                incident_id,
            ]

        repository.execute(
            query,
            parameters,
        )

        return self.get_incident(incident_id)

    def create_or_update_from_alert(
        self,
        detection_type: str,
        severity: str,
        source_ip: str | None,
    ) -> dict[str, Any]:

        existing = self.find_open_incident(
            attack_type=detection_type,
            source_ip=source_ip,
        )

        if existing is not None:
            updated = self.add_alert_to_incident(
                incident_id=existing["incident_id"],
                severity=severity,
            )

            if updated is not None:
                return updated

        return self.create_incident(
            title=f"{detection_type} detected",
            attack_type=detection_type,
            severity=severity,
            source_ip=source_ip,
            alert_count=1,
        )

    def update_status(
        self,
        incident_id: str,
        status: str,
        resolution: str | None = None,
    ) -> dict[str, Any] | None:

        query = """
            UPDATE incidents
            SET status = ?,
                resolution = ?,
                last_seen = ?
            WHERE incident_id = ?
        """

        timestamp = datetime.now(
            timezone.utc
        ).isoformat()

        repository.execute(
            query,
            [
                status,
                resolution,
                timestamp,
                incident_id,
            ],
        )

        return self.get_incident(incident_id)


incident_service = IncidentService()