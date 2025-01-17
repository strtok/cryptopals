from cryptopals.xor import xor
from cryptopals.text import score
from base64 import b16decode


def input() -> list[str]:
    with open("data/1-4.txt") as file:
        return [line.strip() for line in file]


def main() -> None:
    for ctext in input():
        ctext_bytes = b16decode(ctext, casefold=True)

        for key in range(256):
            xor_key = bytes(key for _ in range(len(ctext_bytes)))
            ptext = xor(ctext_bytes, xor_key)
            if score(ptext) < 50:
                print(f"candidate key '0x{key:x}' for '{ctext}: '{ptext}'")
