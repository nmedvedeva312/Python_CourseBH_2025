'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******



* - елочка со снегом
'''

while True:
    height_input = input("Введите высоту ёлочки (от 3 до 20): ").strip()
    if not height_input.isdigit():
        print("Ошибка: введите число.")
        continue
    height = int(height_input)
    if height < 3 or height > 20:
        print("Ошибка: число должно быть от 3 до 20.")
        continue
    break

for i in range(1, height + 1):
    stars = 2 * i - 1            # количество звёздочек в строке
    spaces = height - i           # количество пробелов слева
    print(" " * spaces + "*" * stars)
