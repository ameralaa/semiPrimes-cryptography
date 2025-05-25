
import sys
sys.set_int_max_str_digits(10000000)

def multiply_numbers_with_limit(input_file: str, output_file: str, limit: int):
    try:
        # Read numbers from the input file
        with open(input_file, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip().isdigit()]

        if limit > len(numbers):
            print(f"Limit {limit} exceeds the number of available entries ({len(numbers)}). Using all numbers.")
            limit = len(numbers)

        # Multiply first `limit` numbers
        product = 1
        for num in numbers[:limit]:
            product *= num

        # Calculate length of the result
        result_length = len(str(product))

        # Write results to the output file
        with open(output_file, 'w') as f:
            f.write(f"Length: {result_length}\n")
            f.write(f"Result: {product}\n")

        print(f"Successfully saved result to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as ve:
        print(f"Invalid number in file: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_file = "primes_2_to_1m.txt"
    output_file = "testvalues10k.txt"
    try:
        limit = int(input("Enter how many numbers to multiply (limit): "))
        multiply_numbers_with_limit(input_file, output_file, limit)
    except ValueError:
        print("Please enter a valid integer for the limit.")
