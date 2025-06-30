'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"

num = input("Введите любое число: ").strip()

result = ""

for digit in num:
    if digit.isdigit():
        index = int(digit) - 1  # номер в алфавите с 0
        if 0 <= index < len(alphabet):
            result += alphabet[index]
        else:
            result += "?"  # если цифра вне 1-26, ставим ?
    else:
        result += digit  # если не цифра, оставляем как есть

print(result)