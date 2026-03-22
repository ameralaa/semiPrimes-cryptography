import secrets
from typing import List, Callable

def generate_polynomial_function(seeds: List[int]) -> Callable[[int], int]:
    def F(x: int) -> int:
        return sum(coef * (x ** i) for i, coef in enumerate(seeds))
    return F

def encrypt_message(message: str, func: Callable[[int], int]) -> List[int]:
    return [func(ord(c)) for c in message]

def generate_seeds(degree: int = 3, bit_length: int = 16) -> List[int]:
    max_val = (1 << bit_length) - 1
    return [secrets.randbelow(max_val) for _ in range(degree + 1)]
