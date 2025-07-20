"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

users = [
    {"name": "Alice", "login": "alice_1", "password": "12345"},
    {"name": "Bob", "login": "bob!", "password": "pwd"},
    {"name": "Tom", "login": "tom99", "password": "secret"}
]

# Фильтр по паролю
valid_passwords = list(filter(lambda u: len(u["password"]) >= 5, users))

# Фильтр по логину (только латиница, цифры, _)
def is_valid_login(login):
    return all(ch.isalnum() or ch == '_' for ch in login)

valid_logins = list(filter(lambda u: is_valid_login(u["login"]) or print(
    f"Уважаемый {u['name']}, ваш логин {u['login']} не является корректным."), users))

