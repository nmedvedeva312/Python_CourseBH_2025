'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''

def count_char(text):
    return {c: text.count(c) for c in set(text) if c.isalpha()}

print(count_char("Hello world! 123"))
# {'d': 1, 'r': 1, 'w': 1, 'o': 2, 'H': 1, 'e': 1, 'l': 3}

# set(text) — берёт только уникальные символы
# if c.isalpha() — фильтрует, оставляя только буквы (исключая пробелы, цифры, знаки)
# text.count(c) — считает, сколько раз каждая буква встречается

# or с учетом регистра и сортировки

def count_char(text):
    return {char: text.lower().count(char) for char in sorted(set(text.lower())) if char.isalpha()}

print(count_char("Привет, Как Дела? Привет!"))
# {'а': 2, 'в': 2, 'д': 1, 'е': 3, 'и': 2, 'к': 1, 'л': 1, 'п': 2, 'р': 2, 'т': 2}

# or

def count_char(text):
    result = {}
    for char in text.lower():
        if char.isalpha(): 
            result[char] = result.get(char, 0) + 1
    return dict(sorted(result.items()))

# text.lower() — переводим весь текст в нижний регистр
# char.isalpha() — фильтруем только буквы
# result.get(char, 0) + 1 — прибавляем 1 к существующему значению или начать с 0
# sorted(result.items()) — сортировка по алфавиту


print(count_char("Hi! I'm 007... Hello, World!"))
# Output:{'d': 1, 'e': 1, 'h': 2, 'i': 2, 'l': 3, 'm': 1, 'o': 2, 'r': 1, 'w': 1}



