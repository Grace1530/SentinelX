from scapy.all import get_if_list


def get_available_interfaces() -> list[str]:
    return get_if_list()


def is_valid_interface(interface: str) -> bool:
    return interface in get_available_interfaces()