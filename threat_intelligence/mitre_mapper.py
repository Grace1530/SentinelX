MITRE_MAPPING = {
    "PORT_SCAN": "T1046",
    "SSH_BRUTE_FORCE": "T1110",
    "SYN_FLOOD": "T1499",
    "HTTP_FLOOD": "T1499",
}


def map_to_mitre(detection_type: str) -> str | None:
    return MITRE_MAPPING.get(detection_type)