from typing import Any

from feature_extraction.extractor import extract_features


class FeaturePipeline:
    def transform(
        self,
        packet: dict[str, Any],
        flow: dict[str, Any] | None = None,
    ) -> dict[str, float]:
        return extract_features(
            packet,
            flow,
        )

    def to_vector(
        self,
        features: dict[str, float],
    ) -> list[float]:
        return list(features.values())