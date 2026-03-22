def collatz_variant(n, a, max_steps=100000):
    """
    n : الرقم الابتدائي
    a : المعامل في الخطوة الفردية (زي 3 أو 5 أو 7)
    max_steps : حد أقصى للخطوات عشان نتجنب اللوب اللانهائي
    """
    steps = 0

    while n != 1 and steps < max_steps:
        if n % 2 == 0:
            n = n // 2
        else:
            n = a * n + 1

        steps += 1

    return n == 1, steps


def test_ranges(start_numbers, multipliers):
    for a in multipliers:
        print(f"\n=== تجربة المعامل a = {a} ===")

        for n in start_numbers:
            reached_one, steps = collatz_variant(n, a)

            if reached_one:
                print(f"الرقم {n} وصل لـ 1 بعد {steps} خطوة")
            else:
                print(f"الرقم {n} لم يصل لـ 1 خلال الحد الأقصى من الخطوات")


# أرقام للتجربة
numbers = range(2, 1000)

# معاملات مختلفة
multipliers = [3]

test_ranges(numbers, multipliers)
