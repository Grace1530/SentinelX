import sqlite3
from pathlib import Path

from backend.app.core.config import settings


def get_database_path() -> Path:
    path = Path(settings.database_path)
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    return path


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(
        get_database_path(),
        check_same_thread=False,
    )

    connection.row_factory = sqlite3.Row
    connection.execute(
        "PRAGMA foreign_keys = ON"
    )

    return connection


def initialize_database() -> None:
    schema_path = (
        Path(__file__).resolve().parents[3]
        / "database"
        / "schema.sql"
    )

    if not schema_path.exists():
        return

    schema = schema_path.read_text(
        encoding="utf-8"
    )

    with get_connection() as connection:
        connection.executescript(schema)

        columns = connection.execute(
            "PRAGMA table_info(alerts)"
        ).fetchall()

        column_names = {
            row["name"]
            for row in columns
        }

        if "risk_score" not in column_names:
            connection.execute(
                "ALTER TABLE alerts "
                "ADD COLUMN risk_score REAL"
            )

        connection.commit()