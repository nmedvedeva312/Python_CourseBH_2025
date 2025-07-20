'''
Написать функцию, которая вычисляет факториал переданного в нее числа без рекурсии.

'''

# 1 Без рекурсии

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


number = int(input("Enter a number: ") or 0)
print("Factorial:", factorial(number))
print(factorial(5))   # 120
print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(-3))  # Ошибка


# 2 С рекурсией

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)