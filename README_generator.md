# Divisor-Free Number Generator

This repository provides Python implementations of three mathematically proven methods to generate integer sequences that **exclude all values divisible by a given set of divisors**, without using division (`/`) or modulo (`%`) operations. These methods are based on the research paper:

> **A Division-Free Constructive Framework for Number Generation under Divisibility Constraints**  
> Author: Amer Alaa Eldin Attia Gomaa  
> Date: May 20, 2025

## Methods Implemented

### Method 1: LCM-Multiplier with Constant Offset
Generates odd numbers of the form:  
`f(x) = Mo × LCM + Co` or `f(x) = Me × LCM + Ce`  
Where Co and Ce are constants such that the result is **not divisible** by any number in D.  
Corrected to always return **odd results**.

> Example:  
> For D = {3, 5}, LCM = 15  
> f(1) = 1×15 + 2 = 17  
> f(2) = 2×15 + 1 = 31  
> → Output: 17, 31, 47, ...

### Method 2: Power-Based Offset with LCM
Constructs values like:  
`f(x) = Mo × LCM + 2^P`  
Where `2^P` ensures the result avoids all divisors.  

> Example:  
> f(1) = 15 + 2^1 = 17  
> f(2) = 15 + 2^2 = 19  
> f(3) = 15 + 2^3 = 23  

### Method 3: Coprime Multiplicative Product Summation
Generates values as:  
`f(x) = (a₁ × p₁)^P1 + (a₂ × p₂)^P2`  
Where:
- `gcd(a₁·p₁, a₂·p₂) = 1`
- `p₁, p₂ ∉ D`
- At least one term is even
- The result is not divisible by any `d ∈ D`

> Example:  
> f(x) = (2×3)^1 + (5×7)^1 = 6 + 35 = 41  

The dynamic version explores all such valid combinations.

---

## Files

| File | Description |
|------|-------------|
| `method_1.py` |  Method 1 (returns only odd results) |
| `method_3_1.py`    | Dynamic version of Method 3 to generate all combinations values |
  `method_3.py`    | Dynamic version of Method 3 to generate all lcm combinations values |
| `divisor_free_generator_optimized.py` | All methods (optimized) in one script |
| `method_2_1.py`   | Direct implementation of Method 2 with fixed parameters using 2 with powers|
| `method_2.py`   | Direct implementation of Method 2 with fixed parameters using odd numbers with powers|

---

## Requirements

- Python 3.7+
- No external libraries required (uses only `math` and `typing`)

---

## Example Usage

```bash
$ python method1_lcm_offset_corrected.py
Corrected Method 1 Results (Only Odd, Division-Free): [17, 31, 47, 61, 77, 91, 107, 121, 137, 151]
```

---

## Reference

This repository supports the results and theory discussed in the attached paper:  
**A Division-Free Constructive Framework for Number Generation under Divisibility Constraints**

---

## Contact

For any inquiries or academic use:

- Email: ameralaah99@gmail.com
- Date of Publication: May 20, 2025
