"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def sub(a, b):
    """Return the difference of a and b."""
    return a - b

def mul(a, b):
    """Return the product of a and b."""
    return a * b

def div(a, b):
    """Return b divided by a. Raise ZeroDivisionError if a == 0."""
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    """Return the logarithm of b with base a. Raise ValueError for invalid inputs."""
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm.")
    return math.log(b, a)

def exp(a, b):
    """Return a raised to the power of b."""
    return a ** b
