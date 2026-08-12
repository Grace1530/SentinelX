from typing import Any, Iterable, Optional

from backend.app.database.connection import get_connection


class Repository:
    def fetch_all(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> list[dict]:
        with get_connection() as connection:
            cursor = connection.execute(query, tuple(parameters))
            rows = cursor.fetchall()

        return [dict(row) for row in rows]

    def fetch_one(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> Optional[dict]:
        with get_connection() as connection:
            cursor = connection.execute(query, tuple(parameters))
            row = cursor.fetchone()

        return dict(row) if row else None

    def execute(
        self,
        query: str,
        parameters: Iterable[Any] = (),
    ) -> int:
        with get_connection() as connection:
            cursor = connection.execute(query, tuple(parameters))
            connection.commit()

            return cursor.lastrowid

    def execute_many(
        self,
        query: str,
        parameters: Iterable[Iterable[Any]],
    ) -> None:
        with get_connection() as connection:
            connection.executemany(query, parameters)
            connection.commit()


repository = Repository()