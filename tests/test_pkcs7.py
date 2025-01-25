from cryptopals.pkcs7 import pad, unpad


def test_pad():
    assert pad(b"", 3) == b"\x03\x03\x03"
    assert pad(b"f", 3) == b"f\x02\x02"
    assert pad(b"fo", 3) == b"fo\x01"
    assert pad(b"foo", 3) == b"foo\x03\x03\x03"
    assert pad(b"foob", 3) == b"foob\x02\x02"
    assert pad(b"fooba", 3) == b"fooba\x01"
    assert pad(b"foobar", 3) == b"foobar\x03\x03\x03"


def test_unpad():
    assert unpad(pad(b"", 3), 3) == b""
    assert unpad(pad(b"f", 3), 3) == b"f"
    assert unpad(pad(b"fo", 3), 3) == b"fo"
    assert unpad(pad(b"foo", 3), 3) == b"foo"
    assert unpad(pad(b"foob", 3), 3) == b"foob"
    assert unpad(pad(b"fooba", 3), 3) == b"fooba"
    assert unpad(pad(b"foobar", 3), 3) == b"foobar"
