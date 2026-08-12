from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelMetadata:
    name: str
    version: str
    path: Path
    classes: tuple[str, ...]


class ModelRegistry:
    def __init__(self) -> None:
        self._models: dict[str, ModelMetadata] = {}

    def register(
        self,
        metadata: ModelMetadata,
    ) -> None:
        self._models[metadata.name] = metadata

    def get(
        self,
        name: str,
    ) -> ModelMetadata | None:
        return self._models.get(name)

    def list_models(self) -> list[ModelMetadata]:
        return list(self._models.values())