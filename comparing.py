import gmpy2
from gmpy2 import mpz, mpfr, is_integer

# Set high precision for floating-point operations
gmpy2.get_context().precision = 50000  # ~30,000 digits, adjust if needed

def safe_convert(line):
    """Converts a line to mpz if it represents an integer, otherwise to mpfr."""
    val = mpz(line.strip())
    return mpz(val) if is_integer(val) else val

def read_numbers(filepath, limit):
    """Reads up to 'limit' lines from a file and safely converts them to mpz or mpfr."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [safe_convert(line) for line in lines[:limit]]

def main():
    file1_numbers = read_numbers("powers_of_two_1_to_20.txt", 200)
    file2_divisors = read_numbers("primes_2_to_1m.txt", 132000)

    with open("10k_comparing_results.txt", "w") as result_file:
        for num in file1_numbers:
            divisible = False
            for div in file2_divisors:
                if div == 0:
                    continue  # Avoid division by zero

                # Use exact integer modulus if both are mpz
                if isinstance(num, mpz) and isinstance(div, mpz):
                    if num % div == 0:
                        result_file.write(f"is divisible by {div}: True\n")
                        divisible = True
                        break
                else:
                    # Fallback to float division + is_integer()
                    q = mpfr(num) / mpfr(div)
                    if is_integer(q):
                        result_file.write(f" is divisible by {div}: True\n")
                        divisible = True
                        break

            if not divisible:
                result_file.write("is not divisible by any in list: False\n")

    print("Divisibility check complete. Results saved to results.txt")


if __name__ == "__main__":
    main()
