from ipaddress import ip_address


def validate_ip(value: str) -> bool:
    try:
        ip_address(value)
        return True
    except ValueError:
        return False