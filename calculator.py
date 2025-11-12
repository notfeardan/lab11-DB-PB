"""
calculator.py
- Defines functions used to create a simple calculator

Includes arithmetic, exponential, logarithmic, and geometric operations.
"""

import math

def square_root(a):
    """Return the square root of a. Raise ValueError if a < 0."""
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    """Return the hypotenuse given sides a and b. Negative numbers are allowed."""
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise ValueError(f"Invalid input for hypotenuse: {e}")

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def mul(a, b):
    """Return the product of a and b."""
    return a * b

def div(a, b):
    """Return b divided by a. Raise ZeroDivisionError if a == 0."""
    try:
        if a == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return b / a
    except ZeroDivisionError as e:
        raise e

def logarithm(a, b):
    """Return the logarithm of b with base a. Raise ValueError for invalid inputs."""
    try:
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError("Invalid input for logarithm.")
        return math.log(b, a)
    except ValueError as e:
        raise e

def exp(a, b):
    """Return a raised to the power of b."""
    return a ** b
