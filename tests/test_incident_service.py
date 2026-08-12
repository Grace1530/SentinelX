from backend.app.services.incident_service import (
    incident_service,
)


def test_incident_correlation():
    source_ip = "10.99.99.99"

    first = (
        incident_service.create_or_update_from_alert(
            detection_type="TEST_PORT_SCAN",
            severity="HIGH",
            source_ip=source_ip,
        )
    )

    second = (
        incident_service.create_or_update_from_alert(
            detection_type="TEST_PORT_SCAN",
            severity="HIGH",
            source_ip=source_ip,
        )
    )

    assert first["incident_id"] == second["incident_id"]
    assert second["alert_count"] == (
        first["alert_count"] + 1
    )