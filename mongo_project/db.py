# подключение к базе, коллекции users и services

from pymongo import MongoClient

# Подключение к MongoDB (по умолчанию: localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Создание базы данных (если её нет — она создастся автоматически)
db = client["mydb"]

# Создание коллекции пользователей
users_col = db["users"]
# Создание коллекции услуг
services_col = db["services"]

print("Коллекция users:", users_col.name)
print("Коллекция services:", services_col.name)

