"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""

def dict_from_args(*args, **kwargs):
    if not all(isinstance(i, int) for i in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")
    if not all(isinstance(k, str) for k in kwargs):
        raise TypeError("Все аргументы - ключевые слова должны быть строками")
    return {"args_sum": sum(args), "kwargs_max_len": max(map(len, kwargs), default=0)}

print(dict_from_args(1, 2, 3, name="Tom", login="admin"))
# {'args_sum': 6, 'kwargs_max_len': 5}