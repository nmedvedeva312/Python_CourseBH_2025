"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""

def check_brackets(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# or

def check_brackets(s):
    c = 0
    for ch in s:
        c += ch == '('
        c -= ch == ')'
        if c < 0: return False
    return c == 0

print(check_brackets("(()())"))                 # True
print(check_brackets("(()()()"))                # False
print(check_brackets("(hello(2)ver()(33)python)"))  # True
print(check_brackets("(hello(2()ver(33)python))"))  # True
print(check_brackets("(hello(2()ver(33)python)"))   # False