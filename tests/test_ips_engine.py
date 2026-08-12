from ips_engine.response_engine import (
    ResponseEngine,
)


def test_normal_traffic_is_monitored():

    engine = ResponseEngine()

    result = engine.decide(
        prediction={
            "prediction": "NORMAL",
            "confidence": 0.95,
        },
        source_ip="192.168.1.10",
    )

    assert result["action"] == "MONITOR"
    assert result["severity"] == "LOW"
    assert result["whitelisted"] is False


def test_attack_is_blocked():

    engine = ResponseEngine()

    result = engine.decide(
        prediction={
            "prediction": "PORT_SCAN",
            "confidence": 0.99,
        },
        source_ip="192.168.1.50",
    )

    assert result["action"] == "BLOCK"
    assert result["severity"] == "HIGH"
    assert result["risk_score"] > 0


def test_whitelisted_attack_is_monitored():

    engine = ResponseEngine()

    result = engine.decide(
        prediction={
            "prediction": "PORT_SCAN",
            "confidence": 0.99,
        },
        source_ip="192.168.1.50",
        whitelisted=True,
    )

    assert result["action"] == "MONITOR"
    assert result["whitelisted"] is True


def test_low_confidence_attack():

    engine = ResponseEngine()

    result = engine.decide(
        prediction={
            "prediction": "PORT_SCAN",
            "confidence": 0.60,
        }
    )

    assert result["action"] == "BLOCK"
    assert result["severity"] == "MEDIUM"