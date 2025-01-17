from collections import Counter
from itertools import batched

def input() -> list[str]:
    with open("data/1-8.txt") as file:
        return [line for line in file]


def main() -> None:
    for ctext in input():
        blocks = list(batched(ctext.strip(), 16))
        c = Counter(blocks)
        c_elements = len(list(c))
        if c_elements < 20:
            print(ctext)
