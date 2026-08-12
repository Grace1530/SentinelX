from pathlib import Path

import pytest

from ai_engine.model_config import MODEL_PATH
from ai_engine.inference_service import (
    InferenceService,
)


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_ai_prediction():
    service = InferenceService()

    result = service.predict(
        {
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
    )

    assert "prediction" in result
    assert "confidence" in result
    assert "model" in result