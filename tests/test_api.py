from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "SentinelX"


def test_attackforge_scenarios():
    response = client.get(
        "/api/attackforge/scenarios"
    )

    assert response.status_code == 200

    data = response.json()

    assert "scenarios" in data
    assert len(data["scenarios"]) == 4


def test_packets_endpoint():
    response = client.get("/api/packets")

    assert response.status_code == 200

    data = response.json()

    assert "items" in data
    assert "total" in data