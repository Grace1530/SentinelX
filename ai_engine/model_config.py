from pathlib import Path

MODEL_NAME = "sentinelx-random-forest"
MODEL_VERSION = "0.1.0"

MODEL_DIR = (
    Path(__file__).resolve().parent / "models"
)

MODEL_PATH = (
    MODEL_DIR / "sentinelx_random_forest.joblib"
)

SUPPORTED_CLASSES = [
    "NORMAL",
    "PORT_SCAN",
    "SSH_BRUTE_FORCE",
    "SYN_FLOOD",
    "HTTP_FLOOD",
]

FEATURE_VERSION = "0.1.0"