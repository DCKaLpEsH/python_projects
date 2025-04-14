# This file contains examples of error handling in Python.

# 1. Basic Exception Handling
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Error: {e}")

# 2. Catching Multiple Exceptions
try:
    # Code that may raise an exception
    result = int("abc")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    # Handle the exception
    print(f"Error: {e}")
# 3. Using Finally Block
try:
    # Code that may raise an exception
    result = 10 / 2
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Error: {e}")
finally:
    # This block will always execute
    print("This block always executes, regardless of exceptions.")

# 4. Raising Exceptions


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


try:
    divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
