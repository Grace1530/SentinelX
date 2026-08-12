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
def test_ai_status():
    response = client.get(
        "/api/ai/status"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["ready"] is True
    assert "model" in data


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_ai_predict():
    response = client.post(
        "/api/ai/predict",
        json={
            "features": {
                "packet_length": 60,
                "source_port": 50000,
                "destination_port": 80,
                "ttl": 64,
                "tcp_syn": 1,
                "tcp_ack": 0,
                "tcp_rst": 0,
                "tcp_fin": 0,
                "flow_packet_count": 20,
                "flow_byte_count": 1200,
                "flow_syn_count": 15,
                "flow_ack_count": 0,
                "flow_rst_count": 0,
                "flow_fin_count": 0,
                "unique_destination_ports": 10,
            }
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data["prediction"]
    assert "model" in data["prediction"]