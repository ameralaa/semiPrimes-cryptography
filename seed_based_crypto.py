"""
Seed-Based Random Function Cryptography Framework
Implements:
- Random polynomial function generator (seed-driven)
- Encrypt/Decrypt using user-defined or auto-generated functions
- Keyfile saving and loading via JSON
Author: Amer Alaa Eldin Attia Gomaa
Date: May 2025
"""

import secrets
import json
from typing import Dict, List, Callable

# --------------------------------------------------
# Polynomial Generator
# --------------------------------------------------

def generate_polynomial_function(seeds: List[int]) -> Callable[[int], int]:
    """
    Constructs a polynomial function F(x) = Σ seeds[i] * x^i.
    """
    def F(x: int) -> int:
        return sum(coef * (x ** i) for i, coef in enumerate(seeds))
    return F

# --------------------------------------------------
# Inverse Function (Lookup Table)
# --------------------------------------------------

def build_inverse_function(func: Callable[[int], int], domain: range = range(128)) -> Callable[[int], int]:
    """
    Builds inverse function using a lookup table for values in given domain (default: ASCII).
    """
    table = {func(i): i for i in domain}
    def inverse(y: int) -> int:
        if y not in table:
            raise ValueError(f"Decryption failed: {y} not found in map.")
        return table[y]
    return inverse

# --------------------------------------------------
# Encryption / Decryption
# --------------------------------------------------

def encrypt_message(message: str, func: Callable[[int], int]) -> List[int]:
    return [func(ord(c)) for c in message]

def decrypt_message(cipher: List[int], inv_func: Callable[[int], int]) -> str:
    return ''.join(chr(inv_func(c)) for c in cipher)

# --------------------------------------------------
# Seed Management
# --------------------------------------------------

def generate_seeds(degree: int = 3, bit_length: int = 16) -> List[int]:
    max_val = (1 << bit_length) - 1
    return [secrets.randbelow(max_val) for _ in range(degree + 1)]

def save_keyfile(seeds: List[int], cipher: List[int], filename: str = "keyfile.json") -> None:
    data = {
        "seeds": seeds,
        "cipher": cipher
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_keyfile(filename: str = "keyfile.json") -> Dict[str, List[int]]:
    with open(filename, 'r') as f:
        return json.load(f)

# --------------------------------------------------
# Full Encrypt/Decrypt Workflow
# --------------------------------------------------

def encrypt_and_store(plaintext: str, keyfile: str = "keyfile.json"):
    seeds = generate_seeds(degree=3, bit_length=16)
    enc_func = generate_polynomial_function(seeds)
    ciphertext = encrypt_message(plaintext, enc_func)
    save_keyfile(seeds, ciphertext, keyfile)
    print("✅ Encryption complete.")
    print("Plaintext:", plaintext)
    print("Seeds:", seeds)
    print("Encrypted:", ciphertext)

def decrypt_from_file(keyfile: str = "keyfile.json"):
    data = load_keyfile(keyfile)
    seeds = data["seeds"]
    cipher = data["cipher"]
    enc_func = generate_polynomial_function(seeds)
    dec_func = build_inverse_function(enc_func)
    plaintext = decrypt_message(cipher, dec_func)
    print("✅ Decryption complete.")
    print("Encrypted:", cipher)
    print("Seeds:", seeds)
    print("Decrypted:", plaintext)

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    print("=== SEED CRYPTO FRAMEWORK ===")
    choice = input("1 = Encrypt, 2 = Decrypt: ").strip()
    if choice == '1':
        msg = input("Enter message to encrypt: ").strip()
        encrypt_and_store(msg)
    elif choice == '2':
        decrypt_from_file()
    else:
        print("Invalid selection.")
