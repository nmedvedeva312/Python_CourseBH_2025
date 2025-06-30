"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""
grades = []

while True:
    grade = input("Оценка (1-5), 0 — выход: ").strip()
    if not grade.isdigit():
        print("Ошибка: введите число.")
        continue
    grade = int(grade)
    if grade == 0:
        break
    if grade < 1 or grade > 5:
        print("Ошибка: оценка от 1 до 5.")
        continue
    grades.append(grade)

if grades:
    print(f"Средний балл: {sum(grades)/len(grades):.2f}")
else:
    print("Нет оценок.")

# strip() убирает пробелы в начале и конце


