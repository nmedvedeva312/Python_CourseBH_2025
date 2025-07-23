"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

class Student:
    def __init__(self, surname, name, group, grades=None):
        self.surname = surname
        self.name = name
        self.group = group
        self.grades = grades if grades else []

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def add_grade(self, *grades):
        for grade in grades:
            if 1 <= grade <= 10:
                self.grades.append(grade)

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2) if self.grades else 0

    def __str__(self):
        return f"{self.name} {self.surname} (Group {self.group}) - Avg: {self.average_grade()}"

# список из 5 студентов с оценками
students = [
    Student("Ivanov", "Ivan", "101", [9, 8, 10]),
    Student("Petrova", "Anna", "101", [7, 8, 7]),
    Student("Sidorov", "Petr", "102", [10, 10, 9]),
    Student("Smirnov", "Alexey", "102", [5, 6, 7]),
    Student("Volkov", "Sergey", "101", [8, 9, 9]),
]

# список студентов, отсортированных по возрастанию среднего балла
print("По возрастанию:")
for s in sorted(students):
    print(s)

print("\nПо убыванию:")
# По убыванию
for s in sorted(students, reverse=True):
    print(s)

print("\nСтуденты со средним баллом выше 8:")
# Студенты со средним баллом > 8
for s in students:
    if s.average_grade() > 8:
        print(s)