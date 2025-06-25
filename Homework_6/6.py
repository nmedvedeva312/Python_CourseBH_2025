"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

# Вариант 1

a1 = 1.5
a2 = 2.3
a3 = "test"
a4 = 4

# 1 - все дробные числа (float)
all_float = all(type(x) == float for x in [a1, a2, a3, a4])
print(all_float)  # False, потому что a3 и a4 не float

# 2 - есть ли хотя бы одна строка (str)
any_str = any(type(x) == str for x in [a1, a2, a3, a4])
print(any_str)  # True, потому что a3 - строка

# 3 - есть ли пара из: (a1, a3), (a2, a4), (a3, a4), где обе переменные целые числа (int)
pairs = [(a1, a3), (a2, a4), (a3, a4)]
any_int_pair = any(type(x) == int and type(y) == int for x, y in pairs)
print(any_int_pair)  # False, потому что нет пары с двумя int


# Вариант 2

a1 = 1.2
a2 = 3.4
a3 = 5
a4 = "hello"

# 1. Все дробные числа (float)
all_floats = all(isinstance(x, float) for x in [a1, a2, a3, a4])
print("Все дробные:", all_floats)

# 2. Одна из переменных — строка
has_string = any(isinstance(x, str) for x in [a1, a2, a3, a4])
print("Одна строка:", has_string)

# 3. Одна из указанных пар состоит из двух целых чисел
pair1 = isinstance(a1, int) and isinstance(a3, int)
pair2 = isinstance(a2, int) and isinstance(a4, int)
pair3 = isinstance(a3, int) and isinstance(a4, int)
one_int_pair = pair1 or pair2 or pair3
print("Есть целочисленная пара:", one_int_pair)

# isinstance(..., float) — проверяет, что число дробное
# any(...) — проверяет, есть ли хотя бы одно совпадение
# all(...) — проверяет, что все значения соответствуют типу
# Для п.3 проверяются только допустимые пары