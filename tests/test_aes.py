from base64 import b64encode
from cryptopals.aes import aes_cbc_encrypt
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
    assert (
        b64encode(aes_cbc_encrypt(iv, key, ptext))
        == b"AwGVgw0q5T1LVG0CR87L4gpjVQd3UMEgTqqdHT0YKhI="
    )
