
from address import Address

class Network:
    def __init__(self, ip: str, prefix: int):
        if prefix < 0 or prefix > 32:
            raise ValueError('Prefix must be between 0 and 32')
        self.prefix = prefix
        self.address = Address(ip)
        self.ip_int = self.address.int
        self.block_size = 1 if prefix == 32 else 2 ** (32 - prefix)
        self.network_int = (self.ip_int // self.block_size) * self.block_size
        self.broadcast_int = self.network_int + (self.block_size - 1)
        self.mask_int = 0 if prefix == 0 else (2 ** 32 - 2 ** (32 - prefix))

    @property
    def network(self) -> str:
        return Address.int_to_dotted(self.network_int)

    @property
    def broadcast(self) -> str:
        return Address.int_to_dotted(self.broadcast_int)

    @property
    def hosts(self) -> int:
        return self.block_size

    @property
    def mask(self) -> str:
        return Address.int_to_dotted(self.mask_int)

    def to_dict(self):
        return {
            'network': self.network,
            'broadcast': self.broadcast,
            'hosts': str(self.hosts),
            'mask': self.mask,
            'prefix': str(self.prefix)
        }

