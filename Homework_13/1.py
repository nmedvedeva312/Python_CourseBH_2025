"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import re
from datetime import datetime, timedelta
import random
import string

class User:
    def __init__(self, name, login, password=None):
        # Проверка имени: только русские буквы
        if not self.validate_name(name):
            raise ValueError("Имя должно содержать только буквы русского алфавита")
        self.name = name

        # Проверка логина: латиница, цифры, _, минимум 6 символов
        if not self.validate_login(login):
            raise ValueError("Логин должен содержать не менее 6 символов: латинские буквы, цифры или '_'")
        self.login = login

        # Если пароль передан — проверяем, иначе генерируем новый
        if password:
            if not self.validate_password(password):
                raise ValueError("Пароль не соответствует требованиям безопасности")
            self.password = password
        else:
            self.password = self.generate_password()
            print("Сгенерирован пароль:", self.password)

        self.is_blocked = False  # По умолчанию пользователь не заблокирован
        self.subscription_date = datetime.utcnow() + timedelta(days=30)  # Пробная подписка на 30 дней
        self.subscription_mode = "free"  # Тип подписки по умолчанию

    # -------------------- ВАЛИДАЦИИ -------------------- #

    @staticmethod
    def validate_name(name):
        """Имя: только кириллические буквы"""
        return bool(re.fullmatch(r"[А-Яа-яЁё]+", name))

    @staticmethod
    def validate_login(login):
        """Логин: латинские буквы, цифры и '_', минимум 6 символов"""
        return bool(re.fullmatch(r"[A-Za-z0-9_]{6,}", login))

    @staticmethod
    def validate_password(password):
        """
        Пароль:
        - минимум 6 символов
        - хотя бы одна строчная буква
        - хотя бы одна заглавная буква
        - хотя бы одна цифра
        - только латинские буквы и цифры
        """
        if len(password) < 6:
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.fullmatch(r"[A-Za-z0-9]+", password):
            return False
        return True

    @staticmethod
    def generate_password(length=8):
        """
        Генерация пароля по требованиям:
        - только латинские буквы и цифры
        - пока не удовлетворит всем условиям, продолжает генерацию
        """
        while True:
            pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if User.validate_password(pwd):
                return pwd

    # -------------------- МЕТОДЫ -------------------- #

    def block(self, flag: bool):
        """Блокировка или разблокировка пользователя"""
        self.is_blocked = flag

    def check_subscr(self, check_date=None):
        """
        Проверка подписки:
        - если дата не указана, берётся текущая
        - возвращает словарь с флагом активности, типом и количеством оставшихся дней
        """
        if check_date is None:
            check_date = datetime.utcnow()
        is_active = check_date <= self.subscription_date
        days_left = (self.subscription_date - check_date).days if is_active else 0
        return {
            "active": is_active,
            "mode": self.subscription_mode,
            "days_left": days_left
        }

    def change_pass(self, new_password=None):
        """
        Смена пароля:
        - если передан новый пароль — валидируем и сохраняем
        - если не передан — генерируем и выводим в консоль
        """
        if new_password:
            if not self.validate_password(new_password):
                raise ValueError("Новый пароль не соответствует требованиям")
            self.password = new_password
        else:
            self.password = self.generate_password()
            print("Сгенерирован новый пароль:", self.password)

    def get_info(self):
        """
        Информация о пользователе:
        - если заблокирован — сообщение
        - иначе — имя, логин, подписка
        """
        if self.is_blocked:
            return f"Пользователь {self.name} ({self.login}) заблокирован."
        else:
            return (f"Имя: {self.name}\n"
                    f"Логин: {self.login}\n"
                    f"Подписка до: {self.subscription_date.strftime('%Y-%m-%d')}\n"
                    f"Тип подписки: {self.subscription_mode}")

    def extend_subscription(self, extra_days):
        """
        Продление подписки:
        - увеличивает дату окончания подписки
        - меняет тип подписки на "paid"
        """
        self.subscription_date += timedelta(days=extra_days)
        self.subscription_mode = "paid"


# Создание нового пользователя без пароля
u1 = User("Ольга", "olga_test")
print(u1.get_info())

# Проверка подписки
status = u1.check_subscr()
print(status)

# Смена пароля
u1.change_pass()

# Блокировка
u1.block(True)
print(u1.get_info())

# Продление подписки
u1.extend_subscription(60)
print(u1.check_subscr())



