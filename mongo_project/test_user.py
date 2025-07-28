from user import User
import service

# Создаём нескольких пользователей
u1 = User("Ирина", "irina01", "Irina123")
u2 = User("Павел", "pavel_dev", "Pavel321")
u3 = User("Ольга", "olga_test")  # пароль сгенерируется

# Проверяем работу с услугами для пользователя u3
print("\nРабота с услугами для пользователя Ольга:")

# Добавляем услугу "Премиум"
service.add_service_to_user(u3, "Премиум")

# Продлеваем услугу "Премиум"
service.extend_service_for_user(u3, "Премиум")

# Удаляем услугу "Премиум"
service.remove_service_from_user(u3, "Премиум")