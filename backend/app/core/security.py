from ipaddress import ip_address, ip_network
from typing import Optional


def is_valid_ip(value: str) -> bool:
    try:
        ip_address(value)
        return True
    except ValueError:
        return False


def is_ip_in_network(ip: str, network: str) -> bool:
    try:
        return ip_address(ip) in ip_network(network, strict=False)
    except ValueError:
        return False


def validate_lab_target(
    target: str,
    lab_network: Optional[str],
) -> bool:
    if not is_valid_ip(target):
        return False

    if not lab_network:
        return False

    return is_ip_in_network(target, lab_network)