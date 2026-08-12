import random
from pathlib import Path

import pandas as pd

from feature_extraction.feature_schema import (
    FEATURE_NAMES,
)


RANDOM_SEED = 42

OUTPUT_PATH = (
    Path("datasets")
    / "sentinelx_training.csv"
)


def normal_sample() -> dict:
    return {
        "packet_length": random.randint(60, 500),
        "source_port": random.randint(1024, 65535),
        "destination_port": random.choice(
            [53, 80, 443, 123, 8080]
        ),
        "ttl": random.randint(50, 128),
        "tcp_syn": 1,
        "tcp_ack": 1,
        "tcp_rst": 0,
        "tcp_fin": 0,
        "flow_packet_count": random.randint(1, 10),
        "flow_byte_count": random.randint(
            100,
            5000,
        ),
        "flow_syn_count": random.randint(1, 3),
        "flow_ack_count": random.randint(1, 10),
        "flow_rst_count": 0,
        "flow_fin_count": random.randint(0, 2),
        "unique_destination_ports": random.randint(
            1,
            2,
        ),
        "label": "NORMAL",
    }


def port_scan_sample() -> dict:
    return {
        "packet_length": random.randint(40, 80),
        "source_port": random.randint(
            30000,
            60000,
        ),
        "destination_port": random.randint(
            1,
            1024,
        ),
        "ttl": random.randint(40, 128),
        "tcp_syn": 1,
        "tcp_ack": 0,
        "tcp_rst": random.randint(0, 1),
        "tcp_fin": 0,
        "flow_packet_count": random.randint(
            10,
            100,
        ),
        "flow_byte_count": random.randint(
            500,
            8000,
        ),
        "flow_syn_count": random.randint(
            10,
            100,
        ),
        "flow_ack_count": random.randint(
            0,
            3,
        ),
        "flow_rst_count": random.randint(
            0,
            20,
        ),
        "flow_fin_count": 0,
        "unique_destination_ports": random.randint(
            8,
            100,
        ),
        "label": "PORT_SCAN",
    }


def ssh_bruteforce_sample() -> dict:
    return {
        "packet_length": random.randint(
            60,
            120,
        ),
        "source_port": random.randint(
            30000,
            60000,
        ),
        "destination_port": 22,
        "ttl": random.randint(40, 128),
        "tcp_syn": 1,
        "tcp_ack": random.randint(0, 1),
        "tcp_rst": random.randint(0, 1),
        "tcp_fin": 0,
        "flow_packet_count": random.randint(
            10,
            80,
        ),
        "flow_byte_count": random.randint(
            1000,
            10000,
        ),
        "flow_syn_count": random.randint(
            8,
            50,
        ),
        "flow_ack_count": random.randint(
            1,
            10,
        ),
        "flow_rst_count": random.randint(
            1,
            20,
        ),
        "flow_fin_count": random.randint(
            0,
            5,
        ),
        "unique_destination_ports": 1,
        "label": "SSH_BRUTE_FORCE",
    }


def syn_flood_sample() -> dict:
    return {
        "packet_length": random.randint(
            40,
            80,
        ),
        "source_port": random.randint(
            30000,
            60000,
        ),
        "destination_port": random.randint(
            1,
            65535,
        ),
        "ttl": random.randint(40, 128),
        "tcp_syn": 1,
        "tcp_ack": 0,
        "tcp_rst": 0,
        "tcp_fin": 0,
        "flow_packet_count": random.randint(
            100,
            500,
        ),
        "flow_byte_count": random.randint(
            5000,
            50000,
        ),
        "flow_syn_count": random.randint(
            100,
            500,
        ),
        "flow_ack_count": random.randint(
            0,
            5,
        ),
        "flow_rst_count": random.randint(
            0,
            5,
        ),
        "flow_fin_count": 0,
        "unique_destination_ports": random.randint(
            1,
            5,
        ),
        "label": "SYN_FLOOD",
    }


def http_flood_sample() -> dict:
    return {
        "packet_length": random.randint(
            400,
            1500,
        ),
        "source_port": random.randint(
            30000,
            60000,
        ),
        "destination_port": random.choice(
            [80, 443]
        ),
        "ttl": random.randint(40, 128),
        "tcp_syn": random.randint(0, 1),
        "tcp_ack": 1,
        "tcp_rst": 0,
        "tcp_fin": 0,
        "flow_packet_count": random.randint(
            100,
            500,
        ),
        "flow_byte_count": random.randint(
            50000,
            500000,
        ),
        "flow_syn_count": random.randint(
            1,
            5,
        ),
        "flow_ack_count": random.randint(
            100,
            500,
        ),
        "flow_rst_count": 0,
        "flow_fin_count": random.randint(
            0,
            5,
        ),
        "unique_destination_ports": 1,
        "label": "HTTP_FLOOD",
    }


def main() -> None:
    random.seed(RANDOM_SEED)

    generators = [
        normal_sample,
        port_scan_sample,
        ssh_bruteforce_sample,
        syn_flood_sample,
        http_flood_sample,
    ]

    rows = []

    for generator in generators:
        for _ in range(500):
            rows.append(
                generator()
            )

    dataframe = pd.DataFrame(rows)

    columns = [
        *FEATURE_NAMES,
        "label",
    ]

    dataframe = dataframe[columns]

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print(
        f"Generated {len(dataframe)} samples."
    )

    print(
        dataframe["label"].value_counts()
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()