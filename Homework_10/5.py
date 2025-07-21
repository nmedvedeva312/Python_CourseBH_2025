"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def counter(start):
    count = start
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

# or

def counter(start):
    count = [start]
    return lambda: count.__setitem__(0, count[0] + 1) or count[0]

c1 = counter(1)
c10 = counter(10)

print(c1())  # 2
print(c1())  # 3
print(c1())  # 4

print(c10())  # 11
print(c10())  # 12
print(c10())  # 13