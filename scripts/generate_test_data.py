from pathlib import Path

import pandas as pd


OUTPUT = Path("datasets") / "sentinelx_test_data.csv"


def main() -> None:
    data = pd.DataFrame(
        [
            {
                "packet_length": 64,
                "source_port": 50000,
                "destination_port": 80,
                "ttl": 64,
                "tcp_syn": 1,
                "tcp_ack": 0,
                "tcp_rst": 0,
                "tcp_fin": 0,
                "label": "NORMAL",
            },
            {
                "packet_length": 60,
                "source_port": 50001,
                "destination_port": 22,
                "ttl": 64,
                "tcp_syn": 1,
                "tcp_ack": 0,
                "tcp_rst": 0,
                "tcp_fin": 0,
                "label": "PORT_SCAN",
            },
        ]
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(OUTPUT, index=False)

    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()