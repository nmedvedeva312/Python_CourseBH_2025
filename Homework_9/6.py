"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

data = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

# Сортировка по возрастанию
sorted_asc = dict(sorted(data.items(), key=lambda item: item[1]))

# Сортировка по убыванию
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", sorted_asc)
print("Descending:", sorted_desc)

# Ascending: {'day3': 7, 'day4': 11, 'day5': 14, 'day1': 18, 'day2': 22}
# Descending: {'day2': 22, 'day1': 18, 'day5': 14, 'day4': 11, 'day3': 7}
