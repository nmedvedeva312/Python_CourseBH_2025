'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''

original = [1,2,3,4,5,6,7,8,9]

copy1 = list(map(lambda x: x**2, original))
copy2 = list(map(lambda x: x + 3 if x % 2 == 0 else x, original))
copy3 = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, original))

print("Original:", original)
print("Squared:", copy1)
print("Add 3 to evens:", copy2)
print("Multiply evens by 2, odds by 3:", copy3)