from cryptopals.iter import blocks, transpose


def test_blocks():
    assert list(blocks(b"foobar", 3)) == [b"foo", b"bar"]
    assert list(blocks(b"foobarba", 3)) == [b"foo", b"bar", b"ba"]


def test_transpose():
    assert list(transpose(b"foobar", 3)) == [b"fb", b"oa", b"or"]
    assert list(transpose(b"foobarba", 3)) == [b"fb", b"oa", b'or']
