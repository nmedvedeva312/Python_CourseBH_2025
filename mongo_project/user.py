# Класс User и его методы

import service 
from datetime import datetime, timedelta  # Для работы с датами
from db import users_col                  # Коллекция пользователей из db.py
from utils import (                       # Импортируем функции из utils.py
    validate_name,
    validate_login,
    validate_password,
    generate_password
)

class User:
    def __init__(self, name, login, password=None):
        # Проверка: имя должно содержать только русские буквы
        if not validate_name(name):
            raise ValueError("Имя должно содержать только русские буквы")
        self.name = name

        # Проверка: логин — латиница, цифры, нижнее подчёркивание, не менее 6 символов
        if not validate_login(login):
            raise ValueError("Логин должен быть не менее 6 символов и содержать только латинские буквы, цифры или _")
        self.login = login

        # Если пароль передан — валидируем его
        if password:
            if not validate_password(password):
                raise ValueError("Пароль не соответствует требованиям")
            self.password = password
        else:
            # Иначе — генерируем корректный пароль
            self.password = generate_password()
            print("Сгенерирован пароль:", self.password)

        self.is_blocked = False  # Пользователь не заблокирован по умолчанию

        # Пробная подписка на 30 дней от текущей даты
        self.subscription_date = datetime.utcnow() + timedelta(days=30)

        self.subscription_mode = "free"  # Вид подписки по умолчанию — бесплатный

        self.services = []  # Список подключённых услуг (пока пуст)

        self.save()  # Сохраняем пользователя в базу данных

    def save(self):
        """
        Метод сохраняет или обновляет пользователя в MongoDB.
        Использует login как уникальный идентификатор.        
        """
        users_col.update_one(
            {"login": self.login},       # По логину
            {"$set": self.__dict__},     # Обновляем все атрибуты с помощью $set
            upsert=True                  # Если нет такого пользователя — создать
        )
        print(f"Пользователь '{self.login}' сохранён в базе.")

    def block(self, flag: bool):
        """
        Заблокировать или разблокировать пользователя.
        :param flag: True — заблокировать, False — разблокировать
        """
        self.is_blocked = flag
        self.save()

    def add_service(self, service_name):
        """
        Добавить услугу пользователю.
        Использует функцию из service.py.
        :param service_name: название услуги (строка)
        """
        # вызываем функцию, передавая логин пользователя и имя услуги
        result = service.add_service_to_user(self.login, service_name)
        print(result)  # выводим результат операции

    def extend_service(self, service_name):
        """
        Продлить услугу пользователя.
        Если услуга неактивна — добавляет её.
        """
        result = service.extend_service_for_user(self.login, service_name)
        print(result)

    def remove_service(self, service_name):
        """
        Удалить услугу у пользователя.
        """
        result = service.remove_service_from_user(self.login, service_name)
        print(result)

    