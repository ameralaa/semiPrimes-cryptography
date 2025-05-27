"""
Division-Free Number Generator (Optimized)
Implements the second method described in the paper:
"A Division-Free Constructive Framework for Number Generation under Divisibility Constraints"
"""

from math import gcd
from functools import reduce
from typing import List, Tuple
from sympy import primerange

# Custom LCM for multiple integers
def lcm(*numbers: int) -> int:
    return reduce(lambda x, y: x * y // gcd(x, y), numbers)

def enhanced_lcm_method(
    main_divisors: List[int],
    extra_primes: List[int],
    count: int = 20,
    max_power: int = 10,
    max_prime_power: int = 5
) -> Tuple[List[int], List[str], dict]:
    """
    Generates numbers using:
    (2^a * LCM(main_divisors)) ± (prime^b), where b ∈ [1, max_prime_power]
    """
    L = lcm(*main_divisors)
    results = []
    formulas = []
    stats = {
        'tested': 0,
        'valid': 0,
        'added': 0,
        'subtracted': 0,
        'min_power': float('inf'),
        'max_power': 0
    }

    # Ensure extra primes aren't in main divisors
    clean_primes = [p for p in extra_primes if p not in main_divisors]

    for power in range(1, max_power + 1):
        lcm_multiple = (2 ** power) * L
        for prime in clean_primes:
            for p_exp in range(1, max_prime_power + 1):
                prime_power = prime ** p_exp

                stats['tested'] += 2  # Test both + and -

                # Addition case
                val_add = lcm_multiple + prime_power
                if all(val_add % d != 0 for d in main_divisors):
                    results.append(val_add)
                    formulas.append(
                        f"(2^{power}×LCM{main_divisors}) + {prime}^{p_exp} = {val_add}"
                    )
                    stats['valid'] += 1
                    stats['added'] += 1
                    stats['min_power'] = min(stats['min_power'], power)
                    stats['max_power'] = max(stats['max_power'], power)

                # Subtraction case (negative results allowed)
                val_sub = lcm_multiple - prime_power
                if all(val_sub % d != 0 for d in main_divisors):
                    results.append(val_sub)
                    formulas.append(
                        f"(2^{power}×LCM{main_divisors}) - {prime}^{p_exp} = {val_sub}"
                    )
                    stats['valid'] += 1
                    stats['subtracted'] += 1
                    stats['min_power'] = min(stats['min_power'], power)
                    stats['max_power'] = max(stats['max_power'], power)

                if len(results) >= count:
                    stats['success_rate'] = (stats['valid'] / stats['tested']) * 100
                    return results[:count], formulas[:count], stats

    stats['success_rate'] = (stats['valid'] / stats['tested']) * 100
    return results, formulas, stats

def validate_results(results: List[int], divisors: List[int]) -> dict:
    error_indices = []
    for i, num in enumerate(results):
        if any(num % d == 0 for d in divisors):
            error_indices.append(i)

    return {
        'total': len(results),
        'errors': len(error_indices),
        'error_rate': (len(error_indices) / len(results)) * 100 if results else 0,
        'error_indices': error_indices
    }

# Example usage
main_divisors = list(primerange(3, 20)) 
extra_primes = list(primerange(21, 50))  # Primes <50 not in main divisors
count = 1000

numbers, formulas, gen_stats = enhanced_lcm_method(
    main_divisors,
    extra_primes,
    count=count,
    max_power=20,
    max_prime_power=10
)
validation = validate_results(numbers, main_divisors)

print("ENHANCED LCM METHOD RESULTS\n")
print("Generated Numbers:")
for i, formula in enumerate(formulas, 1):
    print(f"{i}. {formula}")

print("\nGeneration Statistics:")
print(f"Tested combinations: {gen_stats['tested']}")
print(f"Valid results found: {gen_stats['valid']}")
print(f"Success rate: {gen_stats['success_rate']:.2f}%")
print(f"Added cases: {gen_stats['added']}")
print(f"Subtracted cases: {gen_stats['subtracted']}")
print(f"Power of 2 range: {gen_stats['min_power']} to {gen_stats['max_power']}")

print("\nValidation Results:")
print(f"Total numbers: {validation['total']}")
print(f"Invalid numbers: {validation['errors']}")
print(f"Error rate: {validation['error_rate']:.2f}%")
if validation['error_indices']:
    print(f"Error positions: {validation['error_indices']}")

print("\nNumber Statistics:")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")
