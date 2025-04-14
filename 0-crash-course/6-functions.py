# This file contains examples of using functions in Python.

# 1. Basic function definition and call
def greet(name):
    print("Hello, " + name + "!")


greet("Kalpesh")  # Calls the function with the argument "Kalpesh"

# 2. Function with return value


def add(a, b):
    return a + b


result = add(5, 3)

# 3. Function with default parameter


def greet(name="World"):
    print("Hello, " + name + "!")


greet()  # Calls the function with the default parameter

# 4. Function with variable number of arguments


def add(*args):
    return sum(args)


add(1, 2, 3, 4, 5)  # Returns 15

# 5. Function with keyword arguments


def person_info(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)
    for key, value in kwargs.items():
        print(key + ":", value)


person_info("Kalpesh", 25, city="Pune", country="India")

# 6. Lambda function


def add(x, y): return x + y


result = add(5, 3)  # Returns 8

# 7. Function with list comprehension


def square_numbers(numbers):
    return [x**2 for x in numbers]


numbers = [1, 2, 3, 4, 5]

squared_numbers = square_numbers(numbers)  # Returns [1, 4, 9, 16, 25]
