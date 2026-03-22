"""
Cryptographic Strength Tester for Seed-Based Polynomial Encryption
Simulates brute-force and known-plaintext attacks against:
"A Custom Function-Based Seed-Driven Framework for Cryptographic Encryption"
"""

import time
import secrets
from typing import Callable, List
from seed_crypto_framework import generate_polynomial_function, encrypt_message, generate_seeds

# --------------------------------------------------
# Constants
# --------------------------------------------------

ASCII_RANGE = range(128)
SEED_BIT_LENGTH = 16  # Match encryption strength
MAX_GUESSES = 100_000  # Max simulated brute-force attempts

# --------------------------------------------------
# Attack Simulations
# --------------------------------------------------

def brute_force_seed_guess(cipher: List[int], target_plain: str, degree: int = 3) -> float:
    """
    Try to guess the correct seed function by brute-force. Simulates how long it takes
    to find a function that maps the target plaintext to the ciphertext.
    Returns percentage of success (0% = secure under tested guesses).
    """
    attempts = 0
    for _ in range(MAX_GUESSES):
        guess_seeds = generate_seeds(degree, SEED_BIT_LENGTH)
        f_guess = generate_polynomial_function(guess_seeds)
        guess_cipher = encrypt_message(target_plain, f_guess)
        attempts += 1
        if guess_cipher == cipher:
            return 100.0 * (1 / attempts)  # Succeeded (rare!)
    return 0.0  # No match found → very strong

def collision_test(func: Callable[[int], int], domain: range = ASCII_RANGE) -> float:
    """
    Tests how many collisions occur in the output range of the encryption function.
    Returns percentage of unique outputs (100% = injective function).
    """
    outputs = [func(i) for i in domain]
    unique_outputs = set(outputs)
    return 100.0 * len(unique_outputs) / len(outputs)

def known_plaintext_attack(cipher: List[int], known_char: str, degree: int = 3) -> float:
    """
    Try to match a single known character's ciphertext to its value in cipher.
    Returns likelihood of randomly guessing the correct polynomial by single char.
    """
    x = ord(known_char)
    y_target = cipher[0]

    matches = 0
    for _ in range(MAX_GUESSES):
        seeds = generate_seeds(degree, SEED_BIT_LENGTH)
        f = generate_polynomial_function(seeds)
        if f(x) == y_target:
            matches += 1
    return 100.0 * matches / MAX_GUESSES

# --------------------------------------------------
# Test Runner
# --------------------------------------------------

def run_crypto_strength_tests():
    message = "A"  # Known plaintext
    degree = 3

    print("🔐 Testing Seed-Based Polynomial Encryption Strength")
    print(f"Message: {message}")
    print(f"Polynomial degree: {degree}")
    print(f"Max brute-force attempts: {MAX_GUESSES}")
    print(f"Seed bit length: {SEED_BIT_LENGTH}\n")

    # Setup
    seeds = generate_seeds(degree, SEED_BIT_LENGTH)
    f = generate_polynomial_function(seeds)
    cipher = encrypt_message(message, f)

    # Run attacks
    start = time.time()
    brute_percent = brute_force_seed_guess(cipher, message, degree)
    brute_time = time.time() - start

    collision_percent = collision_test(f)
    known_plain_percent = known_plaintext_attack(cipher, message[0], degree)

    # Report
    print("🧪 Results:")
    print(f"Brute-force attack success rate: {brute_percent:.6f}%")
    print(f"Brute-force test time: {brute_time:.2f} seconds")
    print(f"Function injectivity (collision resistance): {collision_percent:.2f}%")
    print(f"Known-plaintext attack match rate: {known_plain_percent:.6f}%")

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    run_crypto_strength_tests()
