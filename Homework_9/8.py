'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''

data = [123, "hello", True, False, 3.14, "world", None, True, 42, "Python"]

# Отфильтровать только строки
only_strings = list(filter(lambda x: isinstance(x, str), data))

# Отфильтровать только логические значения (bool)
only_bools = list(filter(lambda x: isinstance(x, bool), data))

print("Strings:", only_strings)
print("Booleans:", only_bools)

