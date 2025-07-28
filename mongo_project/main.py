# запуск консольного меню и взаимодействие с пользователем

# mongo_project/
# │
# ├── main.py             # Запуск программы (меню и основная логика)
# ├── db.py               # Подключение к MongoDB, работа с коллекциями
# ├── user.py             # Класс User и его методы
# ├── service.py          # Работа с услугами (создание, поиск)
# ├── utils.py            # Вспомогательные функции (валидация, генерация пароля)
# ├── data_init.py        # Скрипт для начального наполнения базы (пользователи, услуги)
# └── requirements.txt    # Список зависимостей (например, pymongo)

from user import User
from db import users_col
import service

def find_user_by_login(login):
    """
    Найти пользователя по логину и вернуть как объект User.
    """
    data = users_col.find_one({"login": login})
    if not data:
        print("Пользователь не найден.")
        return None
    return User(data["name"], data["login"], data["password"])

def show_services(login):
    """
    Показать все услуги пользователя.
    """
    data = users_col.find_one({"login": login})
    if not data or "services" not in data or not data["services"]:
        print("Нет подключённых услуг.")
        return
    print(f"Услуги пользователя {login}:")
    for s in data["services"]:
        print(f"- {s['name']}: с {s['start_date']} до {s['end_date']}")

def main():
    while True:
        print("\nМеню:")
        print("1. Создать пользователя")
        print("2. Заблокировать/разблокировать пользователя")
        print("3. Добавить услугу")
        print("4. Продлить услугу")
        print("5. Удалить услугу")
        print("6. Показать услуги пользователя")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Имя (только русские буквы): ")
            login = input("Логин (латиница, цифры, _): ")
            password = input("Пароль (Enter — сгенерировать): ").strip() or None
            try:
                user = User(name, login, password)
            except ValueError as e:
                print("Ошибка:", e)

        elif choice == "2":
            login = input("Логин пользователя: ")
            user = find_user_by_login(login)
            if user:
                flag = input("Заблокировать? (y/n): ").lower() == "y"
                user.block(flag)
                print("Статус блокировки обновлён.")

        elif choice == "3":
            login = input("Логин пользователя: ")
            user = find_user_by_login(login)
            if user:
                name = input("Название услуги: ")
                user.add_service(name)

        elif choice == "4":
            login = input("Логин пользователя: ")
            user = find_user_by_login(login)
            if user:
                name = input("Название услуги: ")
                user.extend_service(name)

        elif choice == "5":
            login = input("Логин пользователя: ")
            user = find_user_by_login(login)
            if user:
                name = input("Название услуги: ")
                user.remove_service(name)

        elif choice == "6":
            login = input("Логин пользователя: ")
            show_services(login)

        elif choice == "7":
            print("Выход.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()