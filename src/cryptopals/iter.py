def blocks(b: bytes, block_size: int):
    for i in range(0, len(b), block_size):
        yield b[i : i + block_size]


def transpose(b: bytes, block_size: int):
    truncated_length = len(b) - (len(b) % block_size)
    b = b[:truncated_length]
    return (bytes(block) for block in zip(*blocks(b, block_size)))
