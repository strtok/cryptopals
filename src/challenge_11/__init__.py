from collections import Counter
from cryptopals.aes import aes_oracle
from itertools import batched, repeat


def main() -> None:
    mode_counter = Counter()
    for _ in range(1000):
        ptext = bytes(repeat(42, 0x10 * 32))
        ctext = aes_oracle(ptext)
        counter = Counter(batched(ctext, 0x10))
        if len(counter) < 10:
            mode_counter["ebc"] += 1
        else:
            mode_counter["cbc"] += 1
    print(mode_counter)
