from typing import Any


class Explainer:
    def explain(
        self,
        prediction: str,
        features: dict[str, float],
    ) -> list[str]:
        factors: list[str] = []

        if prediction == "PORT_SCAN":
            if features.get("unique_destination_ports", 0) > 3:
                factors.append(
                    "Multiple destination ports observed"
                )

            if features.get("flow_syn_count", 0) > 3:
                factors.append(
                    "Repeated TCP SYN activity observed"
                )

            if features.get("tcp_syn", 0) == 1:
                factors.append(
                    "TCP SYN activity detected"
                )

        elif prediction == "SSH_BRUTE_FORCE":
            if features.get("destination_port", 0) == 22:
                factors.append(
                    "SSH destination port observed"
                )

            if features.get("flow_packet_count", 0) > 5:
                factors.append(
                    "Repeated connection activity observed"
                )

        elif prediction == "SYN_FLOOD":
            if features.get("tcp_syn", 0) == 1:
                factors.append(
                    "TCP SYN activity detected"
                )

            if features.get("flow_syn_count", 0) > 10:
                factors.append(
                    "High SYN count observed"
                )

        elif prediction == "HTTP_FLOOD":
            if features.get("destination_port", 0) in {
                80,
                443,
            }:
                factors.append(
                    "HTTP/HTTPS destination port observed"
                )

            if features.get("flow_packet_count", 0) > 20:
                factors.append(
                    "High request activity observed"
                )

        elif prediction == "NORMAL":
            factors.append(
                "Observed traffic does not match a known "
                "malicious behavior pattern"
            )

        if not factors:
            factors.append(
                "No specific supporting factor identified"
            )

        return factors

    def explain_prediction(
        self,
        prediction_result: dict[str, Any],
        features: dict[str, float],
    ) -> dict[str, Any]:
        prediction = str(
            prediction_result.get(
                "prediction",
                "UNKNOWN",
            )
        )

        confidence = prediction_result.get(
            "confidence"
        )

        return {
            "prediction": prediction,
            "confidence": confidence,
            "factors": self.explain(
                prediction,
                features,
            ),
        }