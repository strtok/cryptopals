from secrets import token_bytes, randbelow

from Crypto.Cipher import AES
from .iter import blocks
from .pkcs7 import pad
from .xor import xor


def aes_cbc_encrypt(iv: bytes, key: bytes, ptext: bytes) -> bytes:
    if len(iv) != 0x10 or len(key) != 0x10:
        raise ValueError("key and iv must be 128 bits")

    ptext = pad(ptext, 0x10)
    ctext = bytes()
    cipher = AES.new(key, AES.MODE_ECB)

    for block in blocks(ptext, 0x10):
        iv = xor(block, iv)
        iv = cipher.encrypt(iv)
        ctext += iv

    return ctext


def aes_cbc_decrypt(iv: bytes, key: bytes, ctext: bytes) -> bytes:
    if len(iv) != 0x10 or len(key) != 0x10:
        raise ValueError("key and iv must be 128 bits")

    ptext = bytes()
    cipher = AES.new(key, AES.MODE_ECB)

    for block in blocks(ctext, 0x10):
        decrypted = cipher.decrypt(block)
        ptext += xor(decrypted, iv)
        iv = block

    return ptext


def aes_oracle(ptext: bytes):
    key = aes_key()
    ptext = pad(token_bytes(randbelow(5) + 5) + ptext + token_bytes(randbelow(5) + 5), 0x10)

    if randbelow(2) == 1:
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv=aes_key())

    return cipher.encrypt(ptext)


def aes_key() -> bytes:
    return token_bytes(16)
