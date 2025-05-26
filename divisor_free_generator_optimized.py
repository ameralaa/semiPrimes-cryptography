"""
Division-Free Number Generator (Optimized)
Implements the 3 methods described in the paper:
"A Division-Free Constructive Framework for Number Generation under Divisibility Constraints"
"""

from math import gcd, lcm
from typing import List, Set

def method1_lcm_offset_odd_only(divisors: List[int], count: int) -> List[int]:
    L = lcm(*divisors)
    results = []
    i = 1
    while len(results) < count:
        # Alternate multipliers: odd index gets +2, even index gets +1
        if i % 2 == 1:
            val = i * L + 2
        else:
            val = i * L + 1

        if all(val % d != 0 for d in divisors) and val % 2 == 1:
            results.append(val)
        i += 1
    return results

def method2_power_offset(divisors: List[int], count: int, base: int = 2) -> List[int]:
    L = lcm(*divisors)
    Mo = 1
    results = []
    p = 1
    while len(results) < count:
        val = Mo * L + (base ** p)
        if all(val % d != 0 for d in divisors):
            results.append(val)
        p += 1
    return results


def is_valid_combination(a1, p1, a2, p2, P1, P2, divisors: Set[int]) -> bool:
    x1 = (a1 * p1) ** P1
    x2 = (a2 * p2) ** P2
    total = x1 + x2

    return (
        gcd(a1 * p1, a2 * p2) == 1 and
        p1 not in divisors and
        p2 not in divisors and
        ((a1 * p1) % 2 == 0 or (a2 * p2) % 2 == 0) and
        all(total % d != 0 for d in divisors)
    )

def generate_method3_values(divisors: Set[int], count: int = 10) -> List[int]:
    results = set()
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    factors = range(1, 6)  # Small multipliers
    powers = range(1, 4)   # Try exponents P1 and P2 from 1 to 3

    for a1 in factors:
        for a2 in factors:
            for p1 in primes:
                for p2 in primes:
                    for P1 in powers:
                        for P2 in powers:
                            if len(results) >= count:
                                return sorted(results)
                            if is_valid_combination(a1, p1, a2, p2, P1, P2, divisors):
                                x1 = (a1 * p1) ** P1
                                x2 = (a2 * p2) ** P2
                                results.add(x1 + x2)

    return sorted(results)

# Example usage
if __name__ == "__main__":
    D = [3, 5]
    print("Corrected Method 1 Results (Only Odd, Division-Free):", method1_lcm_offset_odd_only(D, 10))
    print("Method 2 Results:", method2_power_offset([3, 5], 10))
    D = {3, 5, 7}
    values = generate_method3_values(divisors=D, count=10)
    print("Generated Values Using Method 3 (Dynamic):", values)
