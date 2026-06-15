class Scrambler:
    def __init__(self, taps: tuple):
        self.taps = taps
        self.memory = max(taps)

        self.state = [0] * self.memory

    def process_bit(self, bit: int):
        if bit not in (0, 1):
            raise ValueError("Bit must be 0 or 1")
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[-tap]
        output = bit ^ feedback
        # Сдвиг регистра
        self.state.pop(0)
        self.state.append(output)
        return output

    def process_bits(self, bits: list[int]) -> list[int]:
        return [self.process_bit(b) for b in bits]

    def reset(self):
        self.state = [0] * self.memory

    def process_string(self, string: str):
        result = ''
        for char in string:
            result += str(self.process_bit(int(char)))
        return result


class Descrambler(Scrambler):
    def process_bit(self, bit: int):
        # Дескремблирование - это просто обратный процесс
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[-tap]
        output = bit ^ feedback
        # Сдвиг регистра
        self.state.pop(0)
        self.state.append(bit)  # Используем входной бит для сдвига
        return output
