from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    app_name: str = "SentinelX"
    app_env: str = "development"

    api_host: str = "127.0.0.1"
    api_port: int = 8000

    database_path: str = str(
        PROJECT_ROOT / "database" / "sentinelx.db"
    )

    model_path: str = str(
        PROJECT_ROOT / "ai_engine" / "models"
    )

    monitor_interface: str = ""
    lab_network: str = ""
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()