'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

brands = ['samsung', 'lg', 'xerox', 'bosch']

# Удаляем элемент 'xerox'
brands.remove('xerox')

# Вставляем 'indesit' на вторую позицию (индекс 1)
brands.insert(1, 'indesit')

print(brands)