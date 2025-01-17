import heapq
from . import iter

from base64 import b16decode, b16encode
from itertools import islice, combinations, cycle
from statistics import fmean
from .text import hamming_distance, score
from typing import Iterable, Sequence


def xor16(s: str, key: str) -> str:
    try:
        s_bytes = b16decode(s, casefold=True)
        key_bytes = b16decode(key, casefold=True)
        xor_bytes = xor(s_bytes, key_bytes)
        return b16encode(xor_bytes).decode("utf-8").lower()
    except Exception as e:
        raise ValueError(f"error xoring {s} and {key}: {e}")


def xor(s: bytes, key: Iterable[int]) -> bytes:
    return bytes(x ^ y for x, y in zip(s, key))


def find_keysize(ctext: bytes, keyrange: Sequence[int], nresults=1) -> int | list[int]:
    distances: dict[int, float] = {}
    for key_size in keyrange:
        block_count = int(min(4, len(ctext) / key_size))
        blocks = islice(iter.blocks(ctext, key_size), block_count)
        avg_distance = fmean(
            [(hamming_distance(a, b) / key_size) for a, b in combinations(blocks, 2)]
        )
        distances[key_size] = avg_distance

    result = heapq.nsmallest(nresults, distances.keys(), key=lambda k: distances[k])
    return result[0] if nresults == 1 else result


def find_key(ctext: bytes, key_size: int) -> bytes:
    blocks = iter.transpose(ctext, key_size)
    key_guess = b""

    for block in blocks:
        key_scores: dict[int, float] = {}
        for key in range(256):
            xor_key = cycle(bytes([key]))
            ptext = xor(block, xor_key)
            key_scores[key] = score(ptext)
        best_key = heapq.nsmallest(1, key_scores.keys(), key=lambda k: key_scores[k])
        key_guess += bytes(best_key)

    return key_guess
