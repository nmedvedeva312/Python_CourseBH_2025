# Вспомогательные функции (валидация, генерация пароля)

import re
import random
import string

def validate_name(name):
    """
    Проверка, что имя содержит только русские буквы.
    """
    return bool(re.fullmatch(r'[А-Яа-яЁё]+', name))

def validate_login(login):
    """
    Проверка логина:
    - Только латинские буквы, цифры и _
    - Минимум 6 символов
    """
    return bool(re.fullmatch(r'[A-Za-z0-9_]{6,}', login))

def validate_password(password):
    """
    Пароль должен содержать:
    - Минимум 6 символов
    - хотя бы одну строчную букву
    - хотя бы одну заглавную букву
    - хотя бы одну цифру
    - Только латинские буквы и цифры
    """
    if len(password) < 6:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.fullmatch(r'[A-Za-z0-9]+', password):
        return False
    return True

def generate_password(length=8):
    """
    Генерация пароля по правилам:
    - длина length (по умолчанию 8)
    - должен проходить validate_password
    """
    while True:
        pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if validate_password(pwd):
            return pwd