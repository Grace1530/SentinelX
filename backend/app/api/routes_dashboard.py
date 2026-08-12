from fastapi import APIRouter

from backend.app.database.repository import repository

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/overview")
def dashboard_overview() -> dict:
    packet_result = repository.fetch_one(
        "SELECT COUNT(*) AS count FROM packets"
    )

    alert_result = repository.fetch_one(
        """
        SELECT COUNT(*) AS count
        FROM alerts
        WHERE status = 'OPEN'
        """
    )

    blocked_result = repository.fetch_one(
        """
        SELECT COUNT(*) AS count
        FROM blocked_ips
        WHERE active = 1
        """
    )

    packet_count = (
        packet_result["count"]
        if packet_result
        else 0
    )

    alert_count = (
        alert_result["count"]
        if alert_result
        else 0
    )

    blocked_count = (
        blocked_result["count"]
        if blocked_result
        else 0
    )

    if alert_count >= 10:
        threat_level = "CRITICAL"
    elif alert_count >= 5:
        threat_level = "HIGH"
    elif alert_count >= 1:
        threat_level = "MEDIUM"
    else:
        threat_level = "LOW"

    return {
        "threat_level": threat_level,
        "packets_per_second": 0,
        "total_packets": packet_count,
        "active_alerts": alert_count,
        "blocked_ips": blocked_count,
        "network_health": (
            "DEGRADED"
            if alert_count >= 10
            else "HEALTHY"
        ),
    }


@router.get("/traffic")
def dashboard_traffic() -> dict:
    query = """
        SELECT
            substr(timestamp, 1, 16) AS timestamp,
            COUNT(*) AS packets,
            COALESCE(SUM(packet_length), 0) AS bytes
        FROM packets
        GROUP BY substr(timestamp, 1, 16)
        ORDER BY timestamp DESC
        LIMIT 60
    """

    rows = repository.fetch_all(query)

    return {
        "data": list(reversed(rows)),
    }