"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"{self.brand}-{self.model} - Звонит {name}")

    def get_info(self):
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"


p = Phone("Samsung", "Galaxy S21", 2021)

p.receive_call("Алексей")
# Samsung-Galaxy S21 - Звонит Алексей

print(p.get_info())
# ('Samsung', 'Galaxy S21', 2021)

print(p)
# Бренд: Samsung
# Модель: Galaxy S21
# Год выпуска: 2021

# или с  None, если не знаем, будут ли переданы все параметры

class Phone:
    def __init__(self, brand=None, model=None, issue_year=None):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"{self.brand}-{self.model} - Звонит {name}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"
    
p1 = Phone()
print(p1)
# Бренд: None
# Модель: None
# Год выпуска: None

p2 = Phone("Samsung", "Galaxy S24", 2024)
p2.receive_call("Алиса")
# Samsung-Galaxy S24 - Звонит Алиса

# или с именованными аргументами **kwargs

class Phone:
    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand", "Unknown")
        self.model = kwargs.get("model", "Unknown")
        self.issue_year = kwargs.get("issue_year", None)

    def receive_call(self, name):
        print(f"{self.brand}-{self.model} - Звонит {name}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"
    
p1 = Phone(brand="Apple", model="iPhone 13", issue_year=2021)
p2 = Phone(model="Galaxy S22")

print(p1)
print(p2)