from pathlib import Path

from ai_engine.model_config import MODEL_PATH
from backend.app.services.sentinel_pipeline import (
    SentinelPipeline,
)


def main() -> None:

    if not Path(MODEL_PATH).exists():
        raise FileNotFoundError(
            "Train the SentinelX model first."
        )

    pipeline = SentinelPipeline()

    print(
        "\n======================================"
    )
    print(
        " SENTINELX END-TO-END TEST"
    )
    print(
        "======================================"
    )

    result = pipeline.run_attackforge_scenario(
        scenario_id="port_scan",
        packet_count=10,
        enable_prevention=True,
    )

    print(
        f"\nScenario          : "
        f"{result['session']['scenario_id']}"
    )

    print(
        f"Packets processed : "
        f"{result['packets_processed']}"
    )

    print(
        f"Threat detections : "
        f"{result['detections']}"
    )

    print(
        f"Prevention actions: "
        f"{result['blocked']}"
    )

    if result["results"]:

        first = result["results"][0]

        print(
            f"\nPrediction        : "
            f"{first['prediction']['prediction']}"
        )

        print(
            f"Confidence        : "
            f"{first['prediction']['confidence']}"
        )

        print(
            f"Severity          : "
            f"{first['decision']['severity']}"
        )

        print(
            f"Risk score        : "
            f"{first['decision']['risk_score']}"
        )

        print(
            f"Response          : "
            f"{first['decision']['response']}"
        )

        print(
            "\nExplanation:"
        )

        for factor in first[
            "explanation"
        ]["factors"]:
            print(
                f"  - {factor}"
            )

    print(
        "\n======================================"
    )
    print(
        " TEST COMPLETE"
    )
    print(
        "======================================"
    )


if __name__ == "__main__":
    main()