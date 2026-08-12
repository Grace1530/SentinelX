from typing import Any

from fastapi import APIRouter, Query

from backend.app.services.alert_service import (
    alert_service,
)


router = APIRouter(
    prefix="/api/alerts",
    tags=["Alerts"],
)


@router.get("")
def get_alerts(
    limit: int = Query(
        default=100,
        ge=1,
        le=1000,
    ),
) -> dict[str, Any]:
    alerts = alert_service.list_alerts(
        limit
    )

    return {
        "items": alerts,
        "total": len(alerts),
    }