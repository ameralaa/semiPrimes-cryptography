import gmpy2
from gmpy2 import mpz,mpfr , get_context

gmpy2.get_context().precision = 1000000

def read_mpfr_from_file(path):
    with open(path, 'r') as f:
        content = f.read().strip()
        return mpz(content)
    
    
main_list = list(range(10000000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000001000))  # Example range from 1 to 11, you can change this


a = read_mpfr_from_file("testvalues10k.txt")
even_a = mpz(1)
odd_a = mpz(2)
#even_part= even_a / a
#odd_part= odd_a / a

def modify_value(x):
    if x % 2 == 0:  # even
        modi_x= mpz(x) 
       # modi_inter= modi_x * modi_x * mpfr(16)
        intermidiate = modi_x * a
        modified = intermidiate + even_a # Add 2.5 for even
    else:  # odd
        modi_x= mpz(x)
        #modi_inter= modi_x * modi_x * mpfr(17)
        intermidiate = modi_x * a
        modified = intermidiate + odd_a # Add 2.5 for even # Add 1.5 for odd


    return modified  # Return the decimal value as is

# Modify all values in main_list and store the modified list
modified_list = [modify_value(x) for x in main_list]


# Save the cleaned-up final modified list to a text file after filtering
with open('resultstest10k.txt', 'w') as file:
    for value in modified_list:
        file.write(str(value) + '\n')

# Print the final list
print("Final filtered modified list after removing divisible numbers:")