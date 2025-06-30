'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...

'''

lst = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for i, word in enumerate(lst, start=1):
    # i — номер позиции в списке (с 1)
    # word — элемент списка
    # символ с индексом i-1 (т.к. индексация с 0)
    if i-1 < len(word):
        char = word[i-1]
    else:
        char = '?'  # если длина слова меньше номера позиции — выводим '?'

    print(f"{i} - {word} - {char}")