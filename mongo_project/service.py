# Работа с услугами (создание, поиск)

from datetime import datetime, timedelta
from db import services_col, users_col

def get_all_services():
    """
    Возвращает список всех услуг из базы.
    """
    return list(services_col.find())

def get_service_by_name(name):
    """
    Ищет услугу по имени, возвращает её документ или None.
    """
    return services_col.find_one({"name": name})

def add_service_to_user(user, service_name):
    """
    Добавляет услугу пользователю.
    Принимает объект User, извлекает логин.
    Если услуга уже есть и не закончилась — ничего не делает.
    Иначе — добавляет новую с периодом из услуги.
    """
    user_login = user.login  # берём логин из объекта User

    user_data = users_col.find_one({"login": user_login})
    if not user_data:
        return "Пользователь не найден"

    service = get_service_by_name(service_name)
    if not service:
        return "Услуга не найдена"

    now = datetime.utcnow()

    # Проверяем есть ли активная услуга у пользователя
    active_services = [s for s in user_data.get("services", []) if s["name"] == service_name and s["end_date"] > now]

    if active_services:
        return "Услуга уже активна"

    # Добавляем новую услугу с текущей датой и периодом из услуги
    new_service = {
        "name": service_name,
        "start_date": now,
        "end_date": now + timedelta(days=service["period_days"])
    }
    users_col.update_one({"login": user_login}, {"$push": {"services": new_service}})
    return "Услуга добавлена"

def extend_service_for_user(user, service_name):
    """
    Продлевает услугу пользователя.
    Принимает объект User.
    Если услуга активна — продлевает её на период услуги.
    Если нет — добавляет новую.
    """
    user_login = user.login

    user_data = users_col.find_one({"login": user_login})
    if not user_data:
        return "Пользователь не найден"

    service = get_service_by_name(service_name)
    if not service:
        return "Услуга не найдена"

    now = datetime.utcnow()
    services_list = user_data.get("services", [])

    for s in services_list:
        if s["name"] == service_name:
            if s["end_date"] > now:
                # Продлеваем с текущей даты окончания
                new_end = s["end_date"] + timedelta(days=service["period_days"])
                users_col.update_one(
                    {"login": user_login, "services.name": service_name},
                    {"$set": {"services.$.end_date": new_end}}
                )
                return "Услуга продлена"
            else:
                # Услуга закончилась — добавляем новую
                break

    # Если не нашли активную услугу, добавляем новую
    return add_service_to_user(user, service_name)

def remove_service_from_user(user, service_name):
    """
    Удаляет услугу у пользователя.
    Принимает объект User.
    """
    user_login = user.login

    result = users_col.update_one(
        {"login": user_login},
        {"$pull": {"services": {"name": service_name}}}
    )
    if result.modified_count:
        return "Услуга удалена"
    else:
        return "Услуга не найдена у пользователя"