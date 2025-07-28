# Скрипт для начального наполнения базы (пользователи, услуги)

from db import users_col, services_col
from datetime import datetime, timedelta

def init_services():
    # Услуги, которые добавим
    services = [
        {"name": "Базовая подписка", "type": 0, "cost": 0, "period_days": 30},
        {"name": "Премиум", "type": 1, "cost": 500, "period_days": 30},
        {"name": "VIP", "type": 1, "cost": 1200, "period_days": 90},
    ]
    # Удаляем старые записи, чтобы не дублировать
    services_col.delete_many({})
    # Вставляем новые
    services_col.insert_many(services)
    print("Услуги созданы")

def init_users():
    # Удаляем всех пользователей для чистоты
    users_col.delete_many({})

    # Добавляем двух пользователей с услугами
    users = [
        {
            "name": "Алина",
            "login": "alina123",
            "password": "Pass123",  # В реальности пароли хранятся по-другому
            "is_blocked": False,
            "subscription_date": datetime.now() + timedelta(days=30),
            "subscription_mode": "free",
            "services": [
                {
                    "name": "Базовая подписка",
                    "start_date": datetime.now(),
                    "end_date": datetime.now() + timedelta(days=30)
                }
            ]
        },
        {
            "name": "Иван",
            "login": "ivan_ivan",
            "password": "IvanPass1",
            "is_blocked": False,
            "subscription_date": datetime.now() + timedelta(days=30),
            "subscription_mode": "paid",
            "services": []
        }
    ]
    users_col.insert_many(users)
    print("Пользователи созданы")

if __name__ == "__main__":
    init_services()
    init_users()