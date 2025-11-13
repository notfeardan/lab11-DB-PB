# https://github.com/notfeardan/lab11-DB-PB
# Partner 1: Daniil Baturyn
# Partner 2: Pavel Baturyn
"""
calculator.py
- Defines functions used to create a simple calculator

Includes arithmetic, exponential, logarithmic, and geometric operations.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a, b):   
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    """Return a divided by b. Raise ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

