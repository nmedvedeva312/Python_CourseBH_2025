'''
запросить у пользователя два числа 
вернуть значение где первое число возведено в степень второго числа

'''

# Вариант 1 — с использованием **
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(a ** b)

# Вариант 2 — с использованием pow()
# pow() — встроенная функция в Python, которая возводит число в степень
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(pow(a, b))

# Вариант 3 — с использованием функции
def exponent():
    a = int(input("Введите число: "))
    b = int(input("Введите степень: "))
    return a ** b

print(exponent())

# Вариант 4 — Одной строкой (внутри print):
print(int(input("Введите число: ")) ** int(input("Введите степень: "))) 
print(int(input()) ** int(input())) # не дает подсказок для введения