from random import randrange
import sys
sys.set_int_max_str_digits(10000000)
import gmpy2
from gmpy2 import mpz,mpfr , get_context, is_prime


# تحميل الأرقام من ملف
def get_number_from_file(filename, index):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return mpz(lines[index].strip())

# مثال: قراءة الرقم السابع من الملف (index = 6)
filename = "powers_of_two_1_to_20.txt"
index = 15 # الرقم السابع
number = get_number_from_file(filename, index)

# اختبار أولية الرقم
if is_prime(number,5):
    print("true")
    
else:
    print("false")