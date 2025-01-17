from itertools import repeat

def pad(b: bytes, block_size: int) -> bytes:
    padding_bytes = block_size - (len(b) % block_size)
    return b + bytes(repeat(padding_bytes, padding_bytes))
