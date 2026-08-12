from contextlib import asynccontextmanager

from fastapi import FastAPI
from backend.app.api.routes_ips import router as ips_router
from backend.app.api.routes_alerts import (
    router as alerts_router,
)
from backend.app.api.routes_attackforge import (
    router as attackforge_router,
)
from backend.app.api.routes_dashboard import (
    router as dashboard_router,
)
from backend.app.api.routes_detection import (
    router as detection_router,
)
from backend.app.api.routes_ai import (
    router as ai_router,
)
from backend.app.api.routes_ai_alerts import (
    router as analysis_router,
)
from backend.app.api.routes_packets import (
    router as packets_router,
)
from backend.app.api.routes_threats import (
    router as threats_router,
)
from backend.app.api.routes_traffic import (
    router as traffic_router,
)
from backend.app.api.routes_threat_summary import (
    router as threat_summary_router,
)
from backend.app.api.routes_pipeline import (
    router as pipeline_router,
)

from backend.app.database.connection import (
    initialize_database,
)
from backend.app.api.routes_incidents import (
    router as incidents_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="SentinelX API",
    description=(
        "Explainable AI-Based Intrusion Detection "
        "and Prevention Platform"
    ),
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(alerts_router)
app.include_router(attackforge_router)
app.include_router(dashboard_router)
app.include_router(detection_router)
app.include_router(ai_router)
app.include_router(analysis_router)
app.include_router(packets_router)
app.include_router(threats_router)
app.include_router(traffic_router)
app.include_router(threat_summary_router)
app.include_router(pipeline_router)
app.include_router(ips_router)
app.include_router(incidents_router)

@app.get(
    "/api/health",
    tags=["System"],
)
def health_check() -> dict:
    return {
        "status": "ok",
        "service": "SentinelX",
        "version": "1.0.0",
    }