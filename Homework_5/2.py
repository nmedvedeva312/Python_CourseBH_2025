"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
"""


# Создаем данные о сотрудниках в виде списка словарей
employees = [
    {
        "ФИО": "Иванов Иван Иванович",
        "должность": "менеджер",
        "год_рождения": 1980,
        "навыки": ["управление", "коммуникации", "продажи"],
        "дети": [
            {"имя": "Аня", "год_рождения": 2010},
            {"имя": "Миша", "год_рождения": 2013},
        ],
    },
    {
        "ФИО": "Петрова Мария Сергеевна",
        "должность": "разработчик",
        "год_рождения": 1990,
        "навыки": ["Python", "Django", "SQL"],
        "дети": [
            {"имя": "Коля", "год_рождения": 2015},
        ],
    },
    {
        "ФИО": "Сидоров Алексей Николаевич",
        "должность": "дизайнер",
        "год_рождения": 1985,
        "навыки": ["Photoshop", "Illustrator", "Figma"],
        "дети": [],
    },
]

# Запрашиваем ФИО
search_name = input("Введите ФИО сотрудника: ")

# Ищем и выводим информацию
for emp in employees:
    if emp["ФИО"] == search_name:
        print(f"ФИО: {emp['ФИО']}")
        print(f"Должность: {emp['должность']}")
        print(f"Год рождения: {emp['год_рождения']}")
        print("Навыки:", ", ".join(emp['навыки']))
        if emp['дети']:
            print("Дети:")
            for child in emp['дети']:
                print(f"  - {child['имя']}, год рождения: {child['год_рождения']}")
        else:
            print("Дети отсутствуют")
        break
else:
    print("Сотрудник не найден")
