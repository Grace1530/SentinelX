from abc import ABC, abstractmethod

from ips_engine.models import BlockResult


class FirewallAdapter(ABC):
    @abstractmethod
    def block_ip(
        self,
        ip_address: str,
        reason: str,
    ) -> BlockResult:
        raise NotImplementedError

    @abstractmethod
    def unblock_ip(
        self,
        ip_address: str,
    ) -> BlockResult:
        raise NotImplementedError