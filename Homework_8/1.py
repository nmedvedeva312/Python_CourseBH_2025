"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев

"""

def short_name(full_name: str, reverse: bool = False) -> str:

    parts_name = full_name.split()
    if len(parts_name) != 3:
        raise ValueError("Full name must consist of exactly three parts: Last, First, Middle.")
    
    last, first, middle = parts_name
    first_initial = first[0].upper() + '.'
    middle_initial = middle[0].upper() + '.'
    
    if reverse:
        return f"{first_initial}{middle_initial}{last}"
    else:
        return f"{last} {first_initial}{middle_initial}"
    
# Ввод пользователя отдельно
user_input = input("Enter full name (Last First Middle): ")
print(short_name(user_input))


