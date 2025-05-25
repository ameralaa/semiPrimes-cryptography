# Generate 2^1 to 2^20 and save in a text file

with open("powers_of_two_1_to_20.txt", "w") as file:
    for i in range(1, 200):
        value = 15 ** i + 14
        file.write(f"{value}\n")
