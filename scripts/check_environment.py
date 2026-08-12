import importlib.util
import sys


REQUIRED_PACKAGES = [
    "fastapi",
    "uvicorn",
    "scapy",
    "pandas",
    "numpy",
    "sklearn",
    "xgboost",
    "joblib",
    "pydantic_settings",
]


def main() -> None:
    print("=== SentinelX Environment Check ===")
    print(f"Python: {sys.version}")

    failed = False

    for package in REQUIRED_PACKAGES:
        available = (
            importlib.util.find_spec(package)
            is not None
        )

        status = "OK" if available else "MISSING"

        print(
            f"{package:<20} {status}"
        )

        if not available:
            failed = True

    if failed:
        print("\nEnvironment check FAILED.")
        raise SystemExit(1)

    print("\nEnvironment check PASSED.")


if __name__ == "__main__":
    main()