from cryptopals.pkcs7 import pad

def test_pad():
    assert pad(b"", 3) == b"\x03\x03\x03"
    assert pad(b"f", 3) == b"f\x02\x02"
    assert pad(b"fo", 3) == b"fo\x01"
    assert pad(b"foo", 3) == b"foo\x03\x03\x03"
    assert pad(b"foob", 3) == b"foob\x02\x02"
    assert pad(b"fooba", 3) == b"fooba\x01"
    assert pad(b"foobar", 3) == b"foobar\x03\x03\x03"
