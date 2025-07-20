"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 

"""

# 1

def print_n(text):  
    if not hasattr(print_n, "counter"):
        print_n.counter = 1 # создаём атрибут при первом вызове
    else:
        print_n.counter += 1

    print(f"{print_n.counter}: {text}")

print_n("Hello")
print_n("How are you?")
print_n("Goodbye")

# 2

def print_n(text):
    print(f"{getattr(print_n, 'counter', 1)}: {text}")
    print_n.counter = getattr(print_n, 'counter', 1) + 1



