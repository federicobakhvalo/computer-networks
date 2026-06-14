
from typing import Tuple

class Address:
    def __init__(self, ip: str):
        self.ip = ip.strip()
        self.octets = self._parse(self.ip)
        self.int = self._to_int(self.octets)

    @staticmethod
    def _parse(ip: str) -> Tuple[int, int, int, int]:
        parts = ip.split('.')
        if len(parts) != 4:
            raise ValueError(f"Invalid IP address: {ip}")
        octets = []
        for p in parts:
            if not p.isdigit():
                raise ValueError(f"Invalid octet: {p}")
            n = int(p)
            if n < 0 or n > 255:
                raise ValueError(f"Octet out of range: {p}")
            octets.append(n)
        return tuple(octets)

    @staticmethod
    def _to_int(octets: Tuple[int, int, int, int]) -> int:
        return (octets[0] * 256**3) + (octets[1] * 256**2) + (octets[2] * 256) + octets[3]

    @staticmethod
    def int_to_dotted(val: int) -> str:
        if val < 0 or val > 256**4 - 1:
            raise ValueError("Integer out of IPv4 range")
        o1 = val // 256**3
        rem = val % 256**3
        o2 = rem // 256**2
        rem = rem % 256**2
        o3 = rem // 256
        o4 = rem % 256
        return f"{o1}.{o2}.{o3}.{o4}"

    def __str__(self):
        return self.ip

