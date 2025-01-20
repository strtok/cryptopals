from base64 import b64encode
from cryptopals.aes import aes_cbc_encrypt, aes_cbc_decrypt
from cryptopals.pkcs7 import pad
from itertools import repeat
from pytest import raises


def test_cbc_throws_on_valid_iv():
    with raises(ValueError):
        aes_cbc_encrypt(b"short iv", bytes(repeat(0, 16)), b"")
    with raises(ValueError):
        aes_cbc_encrypt(bytes(repeat(0, 16)), b"short key", b"")


def test_cbc_encrypt():
    iv = bytes(repeat(0, 16))
    ptext = b"puppies like waffles"
    key = b"YELLOW SUBMARINE"
    ctext = aes_cbc_encrypt(iv, key, ptext)
    assert b64encode(ctext) == b"AwGVgw0q5T1LVG0CR87L4gpjVQd3UMEgTqqdHT0YKhI="
    assert aes_cbc_decrypt(iv, key, ctext) == pad(b"puppies like waffles", 0x10)
