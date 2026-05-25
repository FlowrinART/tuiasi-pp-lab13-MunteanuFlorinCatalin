# functional_ops.py
"""
Prelucrare HashMap cu funcții de nivel superior.
"""

from functools import reduce


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    return all(map(lambda d: n % d != 0, range(2, int(n ** 0.5) + 1)))


def make_even(n: int) -> int:
    return n * 2 if n % 2 != 0 else n


def process_hashmap(data: dict[str, int]) -> dict[str, int]:
    return dict(
        map(
            lambda item: (item[0], make_even(item[1])),
            filter(
                lambda item: not is_prime(item[1]),
                data.items()
            )
        )
    )