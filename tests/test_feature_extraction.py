from feature_extraction.extractor import extract_features


def test_feature_extraction():
    packet = {
        "packet_length": 100,
        "source_port": 1234,
        "destination_port": 80,
        "ttl": 64,
        "tcp_flags": "S",
    }

    features = extract_features(packet)

    assert features["packet_length"] == 100
    assert features["source_port"] == 1234
    assert features["destination_port"] == 80
    assert features["ttl"] == 64
    assert features["tcp_syn"] == 1