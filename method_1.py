"""
Division-Free Number Generator (Optimized)
Implements the first method described in the paper:
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


# Example usage
if __name__ == "__main__":
    D = [3, 5,7,11]
    print("Method 1 Results (Only Odd, Division-Free):", method1_lcm_offset_odd_only(D, 10))
   