from pathlib import Path


RANDOM_STATE = 42

TEST_SIZE = 0.20

TARGET_COLUMN = "label"

DATASET_DIR = (
    Path(__file__).resolve().parents[1]
    / "datasets"
)

MODEL_OUTPUT_DIR = (
    Path(__file__).resolve().parent
    / "models"
)

MODEL_OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)