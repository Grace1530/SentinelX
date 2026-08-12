from pathlib import Path

from ai_engine.model_registry import (
    ModelMetadata,
    ModelRegistry,
)


def test_model_registry():
    registry = ModelRegistry()

    metadata = ModelMetadata(
        name="test-model",
        version="0.1.0",
        path=Path("test.joblib"),
        classes=("NORMAL", "PORT_SCAN"),
    )

    registry.register(metadata)

    result = registry.get("test-model")

    assert result is not None
    assert result.name == "test-model"
    assert result.version == "0.1.0"