from backend.app.database.repository import repository


def is_blacklisted(ip_address: str) -> bool:
    query = """
        SELECT id
        FROM blocked_ips
        WHERE ip_address = ?
        AND active = 1
        LIMIT 1
    """

    return repository.fetch_one(query, [ip_address]) is not None


def add_to_blacklist(
    ip_address: str,
    reason: str,
    detection_type: str,
    severity: str,
) -> int:
    query = """
        INSERT OR IGNORE INTO blocked_ips (
            ip_address,
            reason,
            detection_type,
            severity,
            active
        )
        VALUES (?, ?, ?, ?, 1)
    """

    return repository.execute(
        query,
        [
            ip_address,
            reason,
            detection_type,
            severity,
        ],
    )