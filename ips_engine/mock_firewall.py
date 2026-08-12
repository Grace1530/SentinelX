from datetime import datetime, timezone

from ips_engine.base_firewall import FirewallAdapter
from ips_engine.models import BlockResult


class MockFirewall(FirewallAdapter):
    def __init__(self) -> None:
        self.blocked_ips: set[str] = set()

    def block_ip(
        self,
        ip_address: str,
        reason: str,
    ) -> BlockResult:
        self.blocked_ips.add(ip_address)

        return BlockResult(
            success=True,
            ip_address=ip_address,
            action="BLOCKED",
            message=(
                "Mock firewall recorded the block request: "
                f"{reason}"
            ),
            timestamp=datetime.now(timezone.utc),
        )

    def unblock_ip(
        self,
        ip_address: str,
    ) -> BlockResult:
        self.blocked_ips.discard(ip_address)

        return BlockResult(
            success=True,
            ip_address=ip_address,
            action="UNBLOCKED",
            message="Mock firewall removed the block.",
            timestamp=datetime.now(timezone.utc),
        )