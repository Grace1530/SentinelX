from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from ai_engine.model_config import MODEL_PATH
from backend.app.main import app


client = TestClient(app)


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_pipeline_packet_api():

    response = client.post(
        "/api/pipeline/packet",
        json={
            "packet": {
                "timestamp": (
                    "2026-08-10T20:00:00+00:00"
                ),
                "source_ip": "192.168.56.101",
                "destination_ip": "192.168.56.102",
                "source_port": 50000,
                "destination_port": 80,
                "protocol": "TCP",
                "packet_length": 60,
                "tcp_flags": "S",
                "ttl": 64,
                "interface": "test",
            },
            "create_alert": False,
            "enable_prevention": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "decision" in data
    assert "explanation" in data


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_attackforge_pipeline_api():

    response = client.post(
        "/api/pipeline/attackforge",
        json={
            "scenario_id": "port_scan",
            "packet_count": 5,
            "enable_prevention": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["packets_processed"] == 5
    assert "detections" in data
    assert "results" in data