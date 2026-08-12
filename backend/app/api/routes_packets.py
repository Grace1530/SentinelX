from fastapi import APIRouter, Query

from backend.app.services.packet_service import get_packets

router = APIRouter(
    prefix="/api/packets",
    tags=["Packets"],
)


@router.get("")
def list_packets(
    limit: int = Query(
        default=100,
        ge=1,
        le=1000,
    ),
) -> dict:
    packets = get_packets(limit)

    return {
        "items": packets,
        "total": len(packets),
    }


@router.get("/{packet_id}")
def get_packet(packet_id: int) -> dict:
    from backend.app.database.repository import repository

    query = """
        SELECT *
        FROM packets
        WHERE id = ?
        LIMIT 1
    """

    packet = repository.fetch_one(
        query,
        [packet_id],
    )

    if packet is None:
        return {
            "error": {
                "code": "PACKET_NOT_FOUND",
                "message": "Packet was not found.",
            }
        }

    return packet