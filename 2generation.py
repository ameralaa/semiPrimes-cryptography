import gmpy2

numbers = []
n = 1

while len(numbers) <10:
    exponent = 2 ** n
    try:
        base = gmpy2.mpz(5)
        value = base ** exponent 
        prime = value + 2 # or: pow(base, exponent)
        numbers.append(prime)
    except Exception as e:
        print(f"Error at n={n}: {e}")
        break
    n += 1

# Save to a text file
with open("powers_of_power_two.txt", "w") as file:
    for num in numbers:
        file.write(f"{num}\n")
