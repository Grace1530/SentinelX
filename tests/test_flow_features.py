from feature_extraction.flow_features import (
    calculate_flow_features,
)


def test_flow_features():
    flow = {
        "packet_count": 10,
        "byte_count": 1000,
        "syn_count": 5,
        "ack_count": 3,
        "rst_count": 1,
        "fin_count": 1,
        "unique_destination_ports": 4,
    }

    result = calculate_flow_features(flow)

    assert result["packet_count"] == 10
    assert result["byte_count"] == 1000
    assert result["syn_count"] == 5
    assert result["unique_destination_ports"] == 4