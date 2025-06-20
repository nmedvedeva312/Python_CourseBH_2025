'''
запросить цену закупки телефона и выдать следующую информацию.
	- цена продажи (+30% к цене закупке)
	- цена продажи со скидкой 5%
	- цена продажи со скидкой 10%
	- цена продажи со скидкой 15%
'''

# 1й вариант
purchase_price = float(input("Введите цену закупки телефона: "))

# Цена продажи с наценкой 30%
selling_price = purchase_price * 1.3

# Цены со скидками
discount_5 = selling_price * 0.95
discount_10 = selling_price * 0.90
discount_15 = selling_price * 0.85

print(f"Цена продажи (+30%): {selling_price:.2f} руб.")
print(f"Цена со скидкой 5%: {discount_5:.2f} руб.")
print(f"Цена со скидкой 10%: {discount_10:.2f} руб.")
print(f"Цена со скидкой 15%: {discount_15:.2f} руб.")

# 2й вариант
purchase = float(input("Закупочная цена: "))
sale = purchase * 1.3

# через округление
print(round(sale * 0.95, 2))
print(round(sale * 0.90, 2))
print(round(sale * 0.85, 2))

# через формат .2f для float
print(
    f"Продажа: {sale:.2f} | "
    f"-5%: {sale * 0.95:.2f} | "
    f"-10%: {sale * 0.90:.2f} | "
    f"-15%: {sale * 0.85:.2f}"
)

# в одну строку
print(f"{sale*0.95}\n{sale*0.90}\n{sale*0.85}")

# без повторов sale, через map()
print(*map(lambda x: round(sale * x, 2), [0.95, 0.90, 0.85]))

# через генератор
print(*(round(sale * d, 2) for d in (0.95, 0.90, 0.85)))
