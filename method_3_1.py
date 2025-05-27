"""
Division-Free Number Generator (Optimized)
Implements the third method described in the paper:
"A Division-Free Constructive Framework for Number Generation under Divisibility Constraints"
"""

from math import gcd
from typing import Set, List

def is_valid_combination(a1: int, p1: int, a2: int, p2: int, P1: int, P2: int, divisors: Set[int]) -> bool:
    x1 = (a1 * p1) ** P1
    x2 = (a2 * p2) ** P2
    total = x1 + x2

    return (
        p1 not in divisors and  # p₁ ∉ D
        p2 not in divisors and  # p₂ ∉ D
        gcd(a1 * p1, a2 * p2) == 1 and  # Terms are coprime
        ((a1 * p1) % 2 == 0 or (a2 * p2) % 2 == 0) and  # One term is even
        all(total % d != 0 for d in divisors)  # Sum avoids all d ∈ D
    )

def generate_method3_values(divisors: Set[int], count: int = 10) -> List[int]:
    results = set()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    allowed_primes = [p for p in primes if p not in divisors]  # Primes not in D

    # Generate combinations systematically
    for a1 in [1, 2, 3, 4,5,6]:  # Small multipliers
        for a2 in [1, 2, 3, 4,5,6]:
            for p1 in allowed_primes:
                for p2 in allowed_primes:
                    if p1 == p2:  # Ensure terms are coprime
                        continue
                    for P1 in [1, 2, 3 , 4 ,5 ,6 ]:  # Small exponents
                        for P2 in [1, 2, 3 , 4 ,5 ,6 ]:
                            if is_valid_combination(a1, p1, a2, p2, P1, P2, divisors):
                                x1 = (a1 * p1) ** P1
                                x2 = (a2 * p2) ** P2
                                results.add(x1 + x2)
                                if len(results) >= count:
                                    return sorted(results)
    return sorted(results)

def validate_results(results: List[int], divisors: Set[int]) -> float:
    error_count = 0
    for num in results:
        if any(num % d == 0 for d in divisors):
            error_count += 1
    error_percent = (error_count / len(results)) * 100 if results else 0
    return error_percent

# Example Usage
D = {3, 5, 7 , 11,13,17}
results = generate_method3_values(D, count=100000)
error_percent = validate_results(results, D)
print(f"Generated {len(results)} numbers. Error rate: {error_percent:.2f}%")
print("Sample results:", results[:100])