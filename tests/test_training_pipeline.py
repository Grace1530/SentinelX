from pathlib import Path

import pandas as pd
import pytest

from ai_engine.dataset_preprocessor import (
    DatasetPreprocessor,
)


def test_dataset_preprocessor():
    dataframe = pd.DataFrame(
        {
            "packet_length": [60, 100],
            "source_port": [50000, 50001],
            "destination_port": [80, 22],
            "ttl": [64, 64],
            "tcp_syn": [1, 1],
            "tcp_ack": [1, 0],
            "tcp_rst": [0, 0],
            "tcp_fin": [0, 0],
            "flow_packet_count": [2, 10],
            "flow_byte_count": [500, 1000],
            "flow_syn_count": [1, 10],
            "flow_ack_count": [1, 0],
            "flow_rst_count": [0, 1],
            "flow_fin_count": [0, 0],
            "unique_destination_ports": [1, 5],
            "label": [
                "NORMAL",
                "PORT_SCAN",
            ],
        }
    )

    processor = DatasetPreprocessor()

    features, target = processor.prepare(
        dataframe
    )

    assert features.shape == (2, 15)
    assert target.shape == (2,)
    assert set(target) == {
        "NORMAL",
        "PORT_SCAN",
    }


def test_missing_dataset_column():
    dataframe = pd.DataFrame(
        {
            "packet_length": [60],
            "label": ["NORMAL"],
        }
    )

    processor = DatasetPreprocessor()

    with pytest.raises(ValueError):
        processor.prepare(dataframe)