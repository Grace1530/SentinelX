from threat_intelligence.mitre_mapper import map_to_mitre


def test_port_scan_mitre_mapping():
    assert map_to_mitre("PORT_SCAN") == "T1046"


def test_unknown_attack_returns_none():
    assert map_to_mitre("UNKNOWN") is None