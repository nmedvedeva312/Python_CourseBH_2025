'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Only non-negative integers are allowed.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))  # Выведет 6

# or

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))  # Выведет 120
