
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial():
    n = 1
    fact = 1
    while True:
        fact *= n
        yield fact
        n += 1

# or

def factorial():
    fact = 1
    for n in range(1, 10**9):
        fact *= n
        yield fact

factorial_gen = factorial()

print(next(factorial_gen))  # 1
print(next(factorial_gen))  # 2
print(next(factorial_gen))  # 6
print(next(factorial_gen))  # 24

# n — текущее число, факториал которого мы считаем
# fact — текущее значение факториала
# yield возвращает значение и "замораживает" выполнение до следующего next()