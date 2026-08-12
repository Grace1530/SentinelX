from attackforge.attackforge_engine import (
    AttackForgeEngine,
)


def test_attackforge_scenarios():
    engine = AttackForgeEngine()

    scenarios = engine.list_scenarios()

    assert len(scenarios) == 4

    ids = {
        scenario["id"]
        for scenario in scenarios
    }

    assert "port_scan" in ids
    assert "ssh_bruteforce" in ids
    assert "syn_flood" in ids
    assert "http_flood" in ids


def test_port_scan_simulation():
    engine = AttackForgeEngine()

    result = engine.start_scenario(
        scenario_id="port_scan",
        packet_count=10,
    )

    assert result["session"]["status"] == "COMPLETED"
    assert result["session"]["packet_count"] == 10
    assert len(result["packets"]) == 10

    for packet in result["packets"]:
        assert packet["scenario_id"] == "port_scan"
        assert packet["protocol"] == "TCP"
        assert packet["tcp_flags"] == "S"


def test_ssh_simulation():
    engine = AttackForgeEngine()

    result = engine.start_scenario(
        scenario_id="ssh_bruteforce",
        packet_count=5,
    )

    assert len(result["packets"]) == 5

    for packet in result["packets"]:
        assert packet["destination_port"] == 22


def test_invalid_scenario():
    engine = AttackForgeEngine()

    try:
        engine.start_scenario(
            scenario_id="invalid",
            packet_count=5,
        )

        assert False

    except ValueError:
        assert True