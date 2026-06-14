"""Facade calculator using Address and Network classes."""
from typing import Dict
from network import Network


class IPCalculator:
    def compute(self, input_str: str) -> Dict[str, str]:
        if '/' not in input_str:
            raise ValueError("Input must be in form 'x.x.x.x/NN'")
        ip_part, prefix_part = input_str.split('/')
        ip_part = ip_part.strip()
        prefix_part = prefix_part.strip()
        if not prefix_part.isdigit():
            raise ValueError('Prefix must be an integer')
        prefix = int(prefix_part)
        net = Network(ip_part, prefix)
        return net.to_dict()
