'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''

# 1 with docstring

def rectangle(a, b, operation):
    """
    Calculate the area or perimeter of a rectangle.

    Parameters:
    a (int or float): First side of the rectangle.
    b (int or float): Second side of the rectangle.
    operation (str): Must be either "area" or "perimeter".

    Returns:
    float or str: Result of the calculation or an error message.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: both sides must be numbers"

    if not isinstance(operation, str):
        return "Error: operation must be a string"

    if operation == "area":
        return a * b
    elif operation == "perimeter":
        return 2 * (a + b)
    else:
        return 'Error: operation must be either "area" or "perimeter"'
    
print(rectangle(5, 3, "area"))       # 15
print(rectangle(4, 2, "perimeter"))  # 12
print(rectangle(4, 2, "volume"))     # Error: operation must be either "area" or "perimeter"

    
# 2 with lambda

rectangle = lambda a, b, operation: (
    "Error: both sides must be numbers" if not (isinstance(a, (int, float)) and isinstance(b, (int, float))) else
    "Error: operation must be a string" if not isinstance(operation, str) else
    a * b if operation == "area" else
    2 * (a + b) if operation == "perimeter" else
    'Error: operation must be either "area" or "perimeter"'
)

print(rectangle(5, 3, "area"))       # 15
print(rectangle(4, 2, "perimeter"))  # 12
print(rectangle(4, 2, "volume"))     # Error: operation must be either "area" or "perimeter"
print(rectangle("4", 2, "area"))     # Error: both sides must be numbers



    