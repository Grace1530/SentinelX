from backend.app.database.repository import repository


def check_ip(ip_address: str) -> dict:
    query = """
        SELECT *
        FROM threat_intelligence
        WHERE indicator = ?
        LIMIT 1
    """

    result = repository.fetch_one(query, [ip_address])

    if not result:
        return {
            "indicator": ip_address,
            "known": False,
        }

    return {
        "indicator": ip_address,
        "known": True,
        "threat_type": result.get("threat_type"),
        "confidence": result.get("confidence"),
        "source": result.get("source"),
    }