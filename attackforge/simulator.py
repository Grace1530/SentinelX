from typing import Callable

from attackforge.synthetic_traffic import (
    SyntheticPacket,
    generate_http_flood,
    generate_port_scan,
    generate_ssh_bruteforce,
    generate_syn_flood,
)


class AttackSimulator:
    def __init__(
        self,
        source_ip: str = "192.168.56.101",
        destination_ip: str = "192.168.56.102",
    ) -> None:
        self.source_ip = source_ip
        self.destination_ip = destination_ip

    def generate(
        self,
        scenario_id: str,
        count: int = 20,
    ) -> list[SyntheticPacket]:
        generators: dict[
            str,
            Callable[..., list[SyntheticPacket]],
        ] = {
            "port_scan": generate_port_scan,
            "ssh_bruteforce": generate_ssh_bruteforce,
            "syn_flood": generate_syn_flood,
            "http_flood": generate_http_flood,
        }

        generator = generators.get(scenario_id)

        if generator is None:
            raise ValueError(
                f"Unknown AttackForge scenario: {scenario_id}"
            )

        return generator(
            source_ip=self.source_ip,
            destination_ip=self.destination_ip,
            count=count,
        )