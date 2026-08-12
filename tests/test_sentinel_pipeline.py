from pathlib import Path

import pytest

from ai_engine.model_config import MODEL_PATH
from backend.app.services.sentinel_pipeline import (
    SentinelPipeline,
)


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_pipeline_port_scan():

    pipeline = SentinelPipeline()

    packet = {
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
    }

    result = pipeline.process_packet(
        packet,
        create_alert=False,
        enable_prevention=False,
    )

    assert "features" in result
    assert "prediction" in result
    assert "explanation" in result
    assert "decision" in result

    assert result["prediction"]["prediction"] in {
        "NORMAL",
        "PORT_SCAN",
        "SSH_BRUTE_FORCE",
        "SYN_FLOOD",
        "HTTP_FLOOD",
    }


@pytest.mark.skipif(
    not Path(MODEL_PATH).exists(),
    reason="Trained model not available.",
)
def test_attackforge_pipeline():

    pipeline = SentinelPipeline()

    result = pipeline.run_attackforge_scenario(
        scenario_id="port_scan",
        packet_count=10,
        enable_prevention=False,
    )

    assert result["packets_processed"] == 10
    assert "detections" in result
    assert "blocked" in result
    assert "results" in result

    assert len(result["results"]) == 10