from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_detection_evaluation():
    response = client.post(
        "/api/detection/evaluate",
        json={
            "prediction": "PORT_SCAN",
            "confidence": 0.98,
            "features": {
                "unique_destination_ports": 10,
                "flow_syn_count": 15,
                "tcp_syn": 1,
            },
            "whitelisted": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"]["prediction"] == "PORT_SCAN"
    assert data["decision"]["severity"] == "HIGH"
    assert data["decision"]["response"] == "BLOCK"
    assert len(data["explanation"]["factors"]) > 0