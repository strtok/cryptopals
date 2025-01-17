from base64 import b64decode
from cryptopals.xor import find_key, find_keysize, xor
from itertools import cycle


def input() -> bytes:
    with open("data/1-6.txt") as file:
        return b64decode("".join([line.strip() for line in file]))


def main() -> None:
    ctext = input()
    keysize = find_keysize(ctext, range(2, 42))
    key = find_key(ctext, keysize)
    print(f"key={key}")
    ptext = xor(ctext, cycle(key))
    print(ptext)
