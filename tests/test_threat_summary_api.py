from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_threat_summary():

    response = client.get(
        "/api/threats/summary"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "operational"

    assert "PORT_SCAN" in (
        data["supported_threats"]
    )