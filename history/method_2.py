"""
Division-Free Number Generator (Optimized)
Implements the second method described in the paper:
"A Division-Free Constructive Framework for Number Generation under Divisibility Constraints"
"""

from math import gcd, lcm
from typing import List, Tuple

def method_lcm_power_offset(divisors: List[int], count: int, base: int = 2) -> Tuple[List[int], List[Tuple[int, str]], float]:
    L = lcm(*divisors)
    results = []
    combinations = []
    valid = 0
    total_tested = 0
    
    max_power = 100 # Safety limit to prevent infinite loops
    power_range = range(1, max_power + 1)
    
    for p in power_range:
        if len(results) >= count:
            break
        
        # Test both addition and subtraction
        for op in ['+', '-']:
            if op == '+':
                val = L + (base ** p)
            else:
                val = abs(L - (base ** p))  # Absolute value to keep positive
                
            total_tested += 1
            if all(val % d != 0 for d in divisors):
                valid += 1
                results.append(val)
                combinations.append((val, f"LCM{divisors} {op} {base}^{p}"))
                
                if len(results) >= count:
                    break
    
    success_rate = (valid / total_tested) * 100 if total_tested > 0 else 0
    
    return results, combinations, success_rate

def validate_results(results: List[int], divisors: List[int]) -> Tuple[int, float]:
    errors = [n for n in results if any(n % d == 0 for d in divisors)]
    error_percent = (len(errors) / len(results)) * 100 if results else 0
    return len(errors), error_percent

# Example usage
divisors = [3, 5, 7,11,13,17,19,23,29,31,37,41,43,47]
count = 1000

numbers, comb_descriptions, success_rate = method_lcm_power_offset(divisors, count)
error_count, error_percent = validate_results(numbers, divisors)

print("Generated Numbers (LCM ± 2^p):")
for i, (num, desc) in enumerate(zip(numbers, comb_descriptions), 1):
    print(f"{i}. {desc} = {num}")

print(f"\nSuccess Rate: {success_rate:.2f}% of tested combinations were valid")
print(f"Validation: {error_count} errors ({error_percent:.2f}%) in final results")

print("\nStatistics:")
print(f"Total generated: {len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Average: {sum(numbers)/len(numbers):.2f}")