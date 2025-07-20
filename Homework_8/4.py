'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.

'''

def format_money(value):
    try:
        number = float(value)
        int_part = str(int(number))
        dec_part = str(round(number % 1 * 100)).zfill(2)
        int_with_spaces = ' '.join([int_part[max(i - 3, 0):i] for i in range(len(int_part), 0, -3)][::-1])
        return int_with_spaces + '.' + dec_part + ' руб.'
    except:
        return 'Error: invalid input'
    
print(format_money(1234567))       # 1 234 567.00 руб.
print(format_money(98765.4))       # 98 765.40 руб.
print(format_money("1000000"))     # 1 000 000.00 руб.
print(format_money("abc"))         # Error: invalid input


