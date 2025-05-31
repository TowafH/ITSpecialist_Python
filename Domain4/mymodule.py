# mymodule.py

def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first.

    Parameters:
    a (int or float): The number to subtract from.
    b (int or float): The number to subtract.

    Returns:
    int or float: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    float: The quotient of a and b.

    Raises:
    ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
