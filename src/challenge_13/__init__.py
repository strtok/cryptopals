from Crypto.Cipher import AES
from cryptopals.text import profile_for, obj_decode
from cryptopals.pkcs7 import pad, unpad
from secrets import token_bytes


class AESOracle:
    def __init__(self):
        self.cipher = AES.new(token_bytes(16), AES.MODE_ECB)

    def make_profile(self, email: str) -> bytes:
        ptext = profile_for(email)
        ptext = pad(bytes(ptext, "utf-8"), 16)
        print(ptext)
        return self.cipher.encrypt(ptext)

    def read_profile(self, ctext: bytes):
        ptext = self.cipher.decrypt(ctext)
        ptext = unpad(ptext, 16)
        return obj_decode(str(ptext, "utf-8"))


def main() -> None:
    oracle = AESOracle()
    ctext = oracle.make_profile("strtok@gmail.com")
    print(oracle.read_profile(ctext))
