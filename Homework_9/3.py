
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''
def recursive_sum(a, b):
    if a > b:
        return 0
    return a + recursive_sum(a + 1, b)

# or

def recursive_sum(a, b): return 0 if a > b else a + recursive_sum(a + 1, b)

print(recursive_sum(3, 5))  # 12
print(recursive_sum(5, 9))  # 35	