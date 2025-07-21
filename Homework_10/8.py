"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def safe_run(log_to='console'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                msg = f"Ошибка в {func.__name__}: {e}"
                if log_to == 'console':
                    print(msg)
                else:
                    with open(log_to, 'a') as f:
                        f.write(msg + '\n')
        return wrapper
    return decorator

@safe_run(log_to='log.txt')
def divide(a, b):
    return a / b

divide(5, 0)

# Ошибка в divide: division by zero