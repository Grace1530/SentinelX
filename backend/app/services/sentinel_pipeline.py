from typing import Any

from attackforge.attackforge_engine import (
    attackforge_engine,
)
from decision_engine.decision import DecisionEngine
from explainability.explanation_engine import (
    ExplanationEngine,
)
from feature_extraction.extractor import (
    extract_features,
)
from ips_engine.ips_manager import IPSManager
from packet_capture.flow_tracker import FlowTracker

from ai_engine.inference_service import (
    inference_service,
)

from backend.app.services.alert_service import (
    alert_service,
)

from backend.app.services.incident_service import (
    incident_service,
)


class SentinelPipeline:

    def __init__(self) -> None:
        self.flow_tracker = FlowTracker()
        self.decision_engine = DecisionEngine()
        self.explanation_engine = ExplanationEngine()
        self.ips_manager = IPSManager()

    def process_packet(
        self,
        packet: dict[str, Any],
        create_alert: bool = True,
        enable_prevention: bool = True,
    ) -> dict[str, Any]:

        flow = self.flow_tracker.update(packet)

        features = extract_features(
            packet,
            flow,
        )

        prediction = inference_service.predict(
            features
        )

        explanation = (
            self.explanation_engine.generate(
                prediction,
                features,
            )
        )

        decision = self.decision_engine.evaluate(
            prediction
        )

        alert = None
        incident = None

        if (
            create_alert
            and decision["detection_type"] != "NORMAL"
        ):
            alert = alert_service.create_alert(
                source_ip=packet.get("source_ip"),
                detection_type=(
                    decision["detection_type"]
                ),
                severity=decision["severity"],
                confidence=decision["confidence"],
                risk_score=decision["risk_score"],
                explanation=explanation["factors"],
            )

            incident = (
                incident_service.create_or_update_from_alert(
                    detection_type=(
                        decision["detection_type"]
                    ),
                    severity=decision["severity"],
                    source_ip=packet.get("source_ip"),
                )
            )

        prevention = None

        if (
            enable_prevention
            and decision["response"] == "BLOCK"
            and packet.get("source_ip")
        ):
            result = self.ips_manager.block(
                packet["source_ip"],
                (
                    f"SentinelX detected "
                    f"{decision['detection_type']}"
                ),
            )

            prevention = {
                "success": result.success,
                "ip_address": result.ip_address,
                "action": result.action,
                "message": result.message,
                "timestamp": result.timestamp.isoformat(),
            }

        return {
            "packet": packet,
            "flow": flow,
            "features": features,
            "prediction": prediction,
            "explanation": explanation,
            "decision": decision,
            "alert": alert,
            "incident": incident,
            "prevention": prevention,
        }

    def process_packets(
        self,
        packets: list[dict[str, Any]],
        create_alert: bool = True,
        enable_prevention: bool = True,
    ) -> list[dict[str, Any]]:

        return [
            self.process_packet(
                packet,
                create_alert=create_alert,
                enable_prevention=enable_prevention,
            )
            for packet in packets
        ]

    def run_attackforge_scenario(
        self,
        scenario_id: str,
        packet_count: int = 20,
        enable_prevention: bool = True,
    ) -> dict[str, Any]:

        simulation = (
            attackforge_engine.start_scenario(
                scenario_id=scenario_id,
                packet_count=packet_count,
            )
        )

        results = self.process_packets(
            simulation["packets"],
            create_alert=True,
            enable_prevention=enable_prevention,
        )

        detections = [
            result
            for result in results
            if result["decision"]["detection_type"]
            != "NORMAL"
        ]

        blocked = [
            result
            for result in results
            if result["prevention"] is not None
        ]

        return {
            "session": simulation["session"],
            "packets_processed": len(results),
            "detections": len(detections),
            "blocked": len(blocked),
            "results": results,
        }


sentinel_pipeline = SentinelPipeline()