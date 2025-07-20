"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

# 1

def yes_or_no(numbers):
    if not all(isinstance(n, int) for n in numbers):
        return False

    seen = set()
    result = []

    for n in numbers:
        if n in seen:
            result.append('yes')
        else:
            result.append('no')
            seen.add(n)
    return result

# 2

def yes_or_no(numbers):
    if not all(isinstance(x, int) for x in numbers):
        return False
    seen = set()
    return ["yes" if x in seen or seen.add(x) else "no" for x in numbers]
# если число уже в seen, добавляем 'yes', если встречаем впервые — добавляем 'no'

# Print

print(yes_or_no([1, 2, 3, 1, 4]))
# ➜ ['no', 'no', 'no', 'yes', 'no']

print(yes_or_no([1, 2, '3', 1]))
# ➜ False, так как есть нецелое число



