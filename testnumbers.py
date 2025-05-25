import math
from decimal import Decimal, getcontext
getcontext().prec = 100000000 # Set precision as needed
# Initialize the main lis
main_list = list(range(1, 50000))  # Example range from 1 to 11, you can change this

def modify_value(x):
    if x % 2 == 0:  # even
        modified = (x + 1/5) * 5  # Add 2.5 for even
    else:  # odd
        modified = (x + 2/5)  * 5 # Add 1.5 for odd

    # If the decimal part is very close to zero or one, round it to the nearest integer
    if math.isclose(modified % 1, 0, abs_tol=1e-7) or math.isclose(modified % 1, 1, abs_tol=1e-7):
        return round(modified)  # Round to the nearest integer
    return modified  # Return the decimal value as is

# Modify all values in main_list and store the modified list
modified_list = [modify_value(x) for x in main_list]

# Filter out:
# 1. Any numbers with a decimal part
# 2. Numbers greater than 5 that end in 5 (e.g., 15, 25)
filtered_list = []
for item in modified_list:
    # Check if the number is an integer (int or a float that is very close to an integer)
    if isinstance(item, int) or (isinstance(item, float) and item.is_integer()):
        # Convert to integer and check if it is greater than 5 and ends in 5
        int_item = int(item)
        if not (int_item > 5 and str(int_item).endswith('5')):
            filtered_list.append(int_item)

# Function to check if the number matches the ending rule
def check_last_digit_condition(item, other_item):
    item_last_digit = item 
    other_last_digit = other_item 

    if item_last_digit == 1 or item_last_digit == 3 or item_last_digit == 7 or item_last_digit == 9:
        return other_last_digit in {1, 7,3, 9}
    return False

# New filter based on the last digit rules and remove numbers divisible by others
final_list = filtered_list.copy()  # Make a copy to iterate over
for item in filtered_list:
    for other_item in filtered_list:
        if item != other_item and other_item < item:
            if item % other_item == 0:  # Check divisibility
                if item in final_list:
                    final_list.remove(item)
                break  # Stop checking once we remove the divisible number

# Save the cleaned-up final modified list to a text file after filtering
with open('55.txt', 'w') as file:
    for value in final_list:
        file.write(str(value) + '\n')

# Print the final list
print("Final filtered modified list after removing divisible numbers:", final_list)