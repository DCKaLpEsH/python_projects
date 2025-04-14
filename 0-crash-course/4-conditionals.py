# This file contains examples of using conditionals in Python.

# 1. Basic if statement
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. if-elif-else statement
age = 18
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# 3. Nested if statement
age = 18
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")
    if age < 13:
        print("You are a child.")
    else:
        print("You are a teenager.")
# 4. Using logical operators
age = 18
if age >= 18 and age < 65:
    print("You are an adult.")
elif age < 18 or age >= 65:
    print("You are not an adult.")

# 5. Using the in operator
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list of fruits.")
else:
    print("Banana is not in the list of fruits.")

# 6. Using the not operator
fruits = ["apple", "banana", "cherry"]
if "banana" not in fruits:
    print("Banana is not in the list of fruits.")
else:
    print("Banana is in the list of fruits.")

# 7. Using the pass statement
age = 18
if age < 18:
    pass  # Do nothing for now
else:
    print("You are an adult.")

# 8. Using the assert statement: The assert keyword is used to test if a condition is true. If the condition is false, it raises an AssertionError with an optional message.
# This is useful for debugging and ensuring that certain conditions are met in your code.

age = 18
assert age >= 18, print("You must be at least 18 years old.")

# 9. Using the match-case statement (Python 3.10+): The match-case statement is a new feature in Python 3.10 that allows for pattern matching. It is similar to switch-case statements in other languages.


def match_case_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case _:
            print("Value is something else")


match_case_example(1)

# 10. Using the ternary operator: The ternary operator is a shorthand way to write an if-else statement in a single line.
age = 18
is_adult = "You are an adult." if age >= 18 else "You are a minor."
print(is_adult)

# 11. Using the conditional expression: The conditional expression is similar to the ternary operator and allows you to write an if-else statement in a single line.
age = 18
is_adult = "You are an adult." if age >= 18 else "You are a minor."
print(is_adult)

# 12. Using the if statement with a list comprehension: You can use an if statement with a list comprehension to filter elements from a list.
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]
