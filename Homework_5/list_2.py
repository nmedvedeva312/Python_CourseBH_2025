'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

# Вариант 1 через for

names = []

# Запрашиваем 5 имен подряд
for _ in range(5):
    name = input("Введите имя: ")
    names.append(name)

# Сортируем список
names.sort()

# Выводим отсортированный список
print(names)

# Проверяем, есть ли имя 'Вася'
print("Вася" in names)


# Вариант без for
names = []

names.append(input("Введите имя 1: "))
names.append(input("Введите имя 2: "))
names.append(input("Введите имя 3: "))
names.append(input("Введите имя 4: "))
names.append(input("Введите имя 5: "))

names.sort()

print(names)
print("Вася" in names)