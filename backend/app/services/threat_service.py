from backend.app.database.repository import repository


def get_packets(limit: int = 100) -> list[dict]:
    query = """
        SELECT *
        FROM packets
        ORDER BY timestamp DESC
        LIMIT ?
    """

    return repository.fetch_all(query, [limit])