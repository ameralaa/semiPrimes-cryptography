# Seed-Based Custom Function Cryptography

This repository contains a prototype implementation of the cryptographic model described in:

> **A Custom Function-Based Seed-Driven Framework for Cryptographic Encryption**  
> Author: Amer Alaa Eldin Attia Gomaa  
> Assistant: Habib Mohamed Attia Gomaa  
> Date: May 2025

The model proposes using customizable encryption functions defined by private seed values. This offers increased obfuscation, structural flexibility, and theoretical resistance to quantum cryptanalysis.

---

## 🔐 Key Concept

Instead of using standard encryption structures like RSA (`cipher = message^e mod n`), this system encrypts values using user-defined mathematical functions:

### Example:
A polynomial-based function:
```
F(x) = s1 * x + s2 * x^2 + s3 * x^3 + s4
```

Where `x` is the ASCII code of the character and `s1, s2, s3, s4` are secret seeds.

---

## 🚀 Features

- Custom encryption function (e.g., polynomial).
- Multiple seed values to increase entropy.
- Works per-character (like stream encryption).
- Function structure and seeds can be user-defined.

---

## 📄 File Structure

| File | Description |
|------|-------------|
| `seed_based_crypto.py` | Main implementation: polynomial encryption using private seeds |

---

## 📌 Example Usage

```bash
$ python seed_based_crypto.py
Plaintext: Hello
Encrypted: [494728, 680704, 794984, 794984, 1044376]
```

---

## 🔧 Customize

You can modify the encryption logic by changing the function `custom_polynomial_encrypt()` or writing a new one with a different mathematical structure (e.g., modular, exponential, recursive). Just ensure the function accepts `x` and `seeds` as parameters.

---

## ⚠️ Disclaimer

This implementation is **for educational and research purposes**. Production-grade systems must implement:

- Secure seed management
- Encrypted storage of function logic
- Formal security audits

---

## 📩 Contact

For academic use or feedback:

- 📧 Email: ameralaah99@gmail.com
- 📅 Date: May 2025

---

## 📚 Related Work

This implementation supports the theoretical foundations presented in the paper:
**A Custom Function-Based Seed-Driven Framework for Cryptographic Encryption**
