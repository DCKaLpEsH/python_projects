# This file contains examples of using lists and dictionaries in Python.
# 1 - List
# 1.2 - Basic list creation and access
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing the first element

# 1.2 - List slicing
print(fruits[1:3])  # Accessing a slice of the list, returns a list
print(fruits[:2])  # Accessing the first two elements
print(fruits[1:])  # Accessing all elements from index 1
print(fruits[-1])  # Accessing the last element
print(fruits[-2:])  # Accessing the last two elements

# 1.3 - List methods
fruits.append("orange")  # Adding an element to the end of the list
print("Appending new element", fruits)
fruits.insert(1, "kiwi")  # Inserting an element at index 1
print("Inserting element at index 1", fruits)
fruits.remove("banana")  # Removing an element by value
print("Removing banana", fruits)
fruits.pop()  # Removing the last element
print("Removing last element", fruits)
fruits.pop(0)  # Removing the first element
print("Removing first element", fruits)
fruits.sort()  # Sorting the list
print("Sorting list", fruits)
fruits.reverse()  # Reversing the list
print("Reversing list", fruits)
fruits.clear()  # Clearing the list
print("Clearing list", fruits)

# 1.4 - List comprehension
squares = [x**2 for x in range(10)]  # Creating a list of squares
print("List comprehension", squares)

# 1.5 - Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list", nested_list)
# Accessing an element in a nested list
print("Accessing nested list", nested_list[1][2])

# 1.6 - List unpacking
a, b, c = [1, 2, 3]  # Unpacking a list into variables
print("List unpacking", a, b, c)

# 1.7 - List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2  # Concatenating two lists
print("List concatenation", list3)

# 1.8 - List repetition
list4 = list1 * 2  # Repeating a list
print("List repetition", list4)

# 1.9 - List membership
print("Membership", 2 in list1)  # Checking if an element is in a list
print("Membership", 7 not in list1)  # Checking if an element is not in a list

# 1.10 - List length
print("List length", len(list1))  # Getting the length of a list

# 1.11 - List copying
list5 = list1.copy()  # Copying a list
print("List copying", list5)

# 1.12 - List iteration
for fruit in fruits:
    print("Iterating through list", fruit)  # Iterating through a list


# 2 - Dictionary
# 2.1 - Basic dictionary creation and access
person = {"name": "Kalpesh", "age": 25, "city": "Pune"}
print("Basic dictionary", person)

# 2.2 - Dictionary methods
person["country"] = "India"  # Adding a key-value pair
print("Adding key-value pair", person)

person["age"] = 26  # Updating a value
print("Updating value", person)
person.pop("city")  # Removing a key-value pair
print("Removing key-value pair", person)

print("Accessing value", person["name"])  # Accessing a value by key
# Accessing a value with get method
print("Accessing value with get", person.get("age"))

# Accessing a value with default value
print("Accessing value with get", person.get("city", "Not found"))

print("Accessing all keys", person.keys())  # Accessing all keys
print("Accessing all values", person.values())  # Accessing all values
# Accessing all items (key-value pairs)
print("Accessing all items", person.items())

# 2.3 - Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}  # Creating a dictionary of squares
print("Dictionary comprehension", squares_dict)

# 2.4 - Nested dictionaries
nested_dict = {"person1": {"name": "Kalpesh", "age": 25},
               "person2": {"name": "John", "age": 30}}
print("Nested dictionary", nested_dict)
# Accessing a value in a nested dictionary
print("Accessing nested dictionary", nested_dict["person1"]["name"])

# 2.5 - Dictionary unpacking
person1 = {"name": "Kalpesh", "age": 25}
person2 = {"city": "Pune", "country": "India"}
person3 = {**person1, **person2}  # Unpacking dictionaries
print("Dictionary unpacking", person3)

# 2.6 - Dictionary iteration
for key, value in person.items():
    # Iterating through a dictionary
    print("Iterating through dictionary", key, value)

# 2.7 - Dictionary membership
print("Membership", "name" in person)  # Checking if a key is in a dictionary
# Checking if a key is not in a dictionary
print("Membership", "country" not in person)

# 2.8 - Dictionary length
print("Dictionary length", len(person))  # Getting the length of a dictionary
