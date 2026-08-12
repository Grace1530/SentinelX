from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_attackforge_scenario_api():
    response = client.get(
        "/api/attackforge/scenarios"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["scenarios"]) == 4


def test_attackforge_simulation_api():
    response = client.post(
        "/api/attackforge/simulate",
        json={
            "scenario_id": "port_scan",
            "packet_count": 5,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["session"]["status"] == "COMPLETED"
    assert data["session"]["packet_count"] == 5
    assert len(data["packets"]) == 5


def test_invalid_attackforge_scenario():
    response = client.post(
        "/api/attackforge/simulate",
        json={
            "scenario_id": "invalid",
            "packet_count": 5,
        },
    )

    assert response.status_code == 400