from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class LabSession:
    session_id: str
    scenario_id: str
    status: str
    started_at: str
    packet_count: int = 0
    metadata: dict = field(default_factory=dict)


class LabSessionManager:
    def __init__(self) -> None:
        self.sessions: dict[str, LabSession] = {}

    def start(
        self,
        scenario_id: str,
    ) -> LabSession:
        session = LabSession(
            session_id=str(uuid4()),
            scenario_id=scenario_id,
            status="RUNNING",
            started_at=datetime.now(
                timezone.utc
            ).isoformat(),
        )

        self.sessions[session.session_id] = session

        return session

    def complete(
        self,
        session_id: str,
        packet_count: int,
    ) -> LabSession:
        session = self.sessions.get(session_id)

        if session is None:
            raise KeyError(
                f"Unknown lab session: {session_id}"
            )

        session.status = "COMPLETED"
        session.packet_count = packet_count

        return session

    def stop(
        self,
        session_id: str,
    ) -> LabSession:
        session = self.sessions.get(session_id)

        if session is None:
            raise KeyError(
                f"Unknown lab session: {session_id}"
            )

        session.status = "STOPPED"

        return session

    def get(
        self,
        session_id: str,
    ) -> LabSession | None:
        return self.sessions.get(session_id)


lab_session_manager = LabSessionManager()