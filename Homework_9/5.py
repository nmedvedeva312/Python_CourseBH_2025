'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12

'''

# Рекурсивная функция

def list_recursive(lst, indent=0, indent_char='-'):
    for el in lst:
        if isinstance(el, list):
            list_recursive(el, indent + 2, indent_char)
        else:
            print(indent_char * indent + str(el))

# Без рекурсии

def list_iterative(lst, indent_char='-'):
    stack = [(lst, 0)]  # кортеж (текущий список, текущий отступ)
    
    while stack:
        current_lst, indent = stack.pop()
        for el in reversed(current_lst):
            if isinstance(el, list):
                stack.append((el, indent + 2))
            else:
                print(indent_char * indent + str(el))

# Использование

some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]

print("Recursive:")
list_recursive(some_list)

print("\nIterative:")
list_iterative(some_list)
