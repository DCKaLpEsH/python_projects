# This file contains examples of using loops in Python.

# 1. Basic for loop
for i in range(5):
    print("Iteration", i)

# 2. for loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# 3. for loop with a string
name = "Kalpesh"
for char in name:
    print("Character:", char)

# 4. for loop with enumerate: enumerate keyword is used to get the index and value of each item in the list
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)

# 5. while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 6. while loop with a break statement
count = 0
while count < 5:
    if count == 3:
        break
    print("Count:", count)
    count += 1

# 7. while loop with a continue statement
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("Count:", count)

# 8. Nested loops
for i in range(3):
    for j in range(i+1):
        print(i, j, end=" ")
    print()

# 9. Looping through a dictionary
person = {"name": "Kalpesh", "age": 25, "city": "Pune"}
for key, value in person.items():
    print(key + ":", value)

# 10. List comprehension
squares = [x**2 for x in range(10)]
print(squares)

# 11. Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

# 12. Set comprehension
squares_set = {x**2 for x in range(10)}
print(squares_set)
