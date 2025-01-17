from Crypto.Cipher import AES
from base64 import b64decode


def input() -> bytes:
    with open("data/1-7.txt") as file:
        return b64decode("".join([line.strip() for line in file]))


def main() -> None:
    aes_key = b"YELLOW SUBMARINE"
    ctext = input()
    cipher = AES.new(aes_key, AES.MODE_ECB)
    ptext = cipher.decrypt(ctext)
    print(ptext)
