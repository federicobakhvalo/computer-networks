from scrambler import Descrambler, Scrambler


class ScramblerApp:
    def __init__(self, taps: tuple):
        self.scrambler = Scrambler(taps)
        self.descrambler = Descrambler(taps)

    def scramble_bits(self, bits: list[int]) -> list[int]:
        return self.scrambler.process_bits(bits)

    def descramble_bits(self, bits: list[int]) -> list[int]:
        return self.descrambler.process_bits(bits)

    def scramble_string(self, data: str) -> str:
        return self.scrambler.process_string(data)

    def descramble_string(self, data: str) -> str:
        return self.descrambler.process_string(data)

    def reset(self):
        self.scrambler.reset()
        self.descrambler.reset()


if __name__ == "__main__":
    app = ScramblerApp(taps=(3, 5))
    original = "1111111000111100100000101"
    # scrambled = app.scramble_string(original)
    descrambled = app.descramble_string(scrambled)
    # как мне проверить правильность Scrambler и Descrembler
    print(f"Original:   {original}")
    print(f"Scrambled:  {scrambled}")
    print(f"Descrambled: {descrambled}")
