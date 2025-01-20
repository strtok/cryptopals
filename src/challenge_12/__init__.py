from Crypto.Cipher import AES
from base64 import b64decode
from cryptopals.text import print_hexdump
from itertools import repeat
from math import ceil
from cryptopals.pkcs7 import pad
from secrets import token_bytes

class AESOracle:
    def __init__(self):
        self.cipher = AES.new(token_bytes(16), AES.MODE_ECB)
        self.sekret = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg\
                       aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq\
                       dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg\
                       YnkK"

    def encrypt(self, ptext: bytes) -> bytes:
        ptext = pad(ptext + b64decode(self.sekret), 16)
        return self.cipher.encrypt(ptext)


# detect block size by finding when a padding block
# is added, and returning the padding block size
def detect_block_size(oracle: AESOracle) -> int:
    for n in range(255):
        diff = len(oracle.encrypt(bytes(n + 1))) - len(oracle.encrypt(bytes(n)))
        if diff > 1:
            return diff
    return 0

def decrypt_suffix(oracle: AESOracle, block_size: int) -> bytes:
    slen = len(oracle.encrypt(b""))
    plen = ceil(slen / block_size) * 16
    solution = bytearray()
    for i in range(1, slen):
        prefix = bytes(repeat(0x41, plen - i))
        ctext = oracle.encrypt(prefix)
        target_block = ctext[plen - 16:plen]
        for j in range(0, 256):
            prefix = bytes(repeat(0x41, plen - i)) + bytes(solution) + bytes([j])
            ctext = oracle.encrypt(prefix)
            if ctext[plen - 16:plen] == target_block:
                solution += bytes([j])
                break
    return bytes(solution)

def main() -> None:
    oracle = AESOracle()
    block_size = detect_block_size(oracle)
    print(f"block_size={block_size}")
    ptext = decrypt_suffix(oracle, block_size)
    print("=== solution ===")
    print_hexdump(ptext)
