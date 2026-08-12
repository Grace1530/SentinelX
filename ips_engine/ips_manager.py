from ips_engine.ip_validator import validate_ip
from ips_engine.mock_firewall import MockFirewall
from ips_engine.models import BlockResult


class IPSManager:
    def __init__(self) -> None:
        self.firewall = MockFirewall()

    def block(
        self,
        ip_address: str,
        reason: str,
    ) -> BlockResult:
        if not validate_ip(ip_address):
            raise ValueError(
                f"Invalid IP address: {ip_address}"
            )

        return self.firewall.block_ip(
            ip_address,
            reason,
        )

    def unblock(
        self,
        ip_address: str,
    ) -> BlockResult:
        if not validate_ip(ip_address):
            raise ValueError(
                f"Invalid IP address: {ip_address}"
            )

        return self.firewall.unblock_ip(
            ip_address
        )