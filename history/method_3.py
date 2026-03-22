"""
Division-Free Number Generator (Optimized)
Implements the third method described in the paper:
"A Division-Free Constructive Framework for Number Generation under Divisibility Constraints"
"""

from itertools import combinations
from typing import Set, List, Tuple

def generate_valid_combinations(D: Set[int], count: int = 10) -> Tuple[List[int], List[Tuple[str, str]]]:
    results = []
    comb_descriptions = []
    primes_in_D = sorted(D)
    powers_of_2 = [2**p for p in [1, 2, 3 ,4]]  # 2, 4, 8
    
    # Generate all possible partitions of primes in D
    for r in range(1, len(primes_in_D)):
        for left_primes in combinations(primes_in_D, r):
            left_primes = list(left_primes)
            right_primes = [p for p in primes_in_D if p not in left_primes]
            
            # Case 1: 2 is in left term (2^a * product(left_primes))
            for power_2 in powers_of_2:
                for left_power in [1, 2 , 3,4]:
                    left_term = power_2
                    for p in left_primes:
                        left_term *= p**left_power
                    
                    for right_power in [1, 2 , 3,4]:
                        right_term = 1
                        for p in right_primes:
                            right_term *= p**right_power
                        
                        total = left_term + right_term
                        if all(total % d != 0 for d in D):
                            results.append(total)
                            desc = (f"{power_2}*{'*'.join(f'{p}^{left_power}' for p in left_primes)}", 
                                    f"{'*'.join(f'{p}^{right_power}' for p in right_primes)}")
                            comb_descriptions.append(desc)
                            if len(results) >= count:
                                return results, comb_descriptions
            
            # Case 2: 2 is in right term (product(left_primes) + 2^a*product(right_primes))
            for power_2 in powers_of_2:
                for left_power in [1, 2 ,3 ,4]:
                    left_term = 1
                    for p in left_primes:
                        left_term *= p**left_power
                    
                    for right_power in [1, 2 ,3,4]:
                        right_term = power_2
                        for p in right_primes:
                            right_term *= p**right_power
                        
                        total = left_term + right_term
                        if all(total % d != 0 for d in D):
                            results.append(total)
                            desc = (f"{'*'.join(f'{p}^{left_power}' for p in left_primes)}", 
                                    f"{power_2}*{'*'.join(f'{p}^{right_power}' for p in right_primes)}")
                            comb_descriptions.append(desc)
                            if len(results) >= count:
                                return results, comb_descriptions
    return results, comb_descriptions

def validate_results(results: List[int], D: Set[int]) -> Tuple[int, float]:
    errors = [n for n in results if any(n % d == 0 for d in D)]
    return len(errors), (len(errors)/len(results))*100 if results else 0

# Example usage
D = {3, 5, 7 , 11 , 13 , 17 , 19 , 23 , 29}
numbers, descriptions = generate_valid_combinations(D, count=10000)

print("Valid Combinations:")
for i, (num, (left, right)) in enumerate(zip(numbers, descriptions), 1):
    print(f"{i}. {left} + {right} = {num}")

error_count, error_percent = validate_results(numbers, D)
print(f"\nValidation: {error_count} errors ({error_percent:.2f}%)")

print("\nStatistics:")
print(f"Generated: {len(numbers)} numbers")
print(f"Min: {min(numbers)}, Max: {max(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")