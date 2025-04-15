print("🔁 REVERSE NAME GENERATOR 🔁")

while (True):
    name = input("Enter a name: ")
    # Q. How does name[::-1] work?
    # -> It reverses the string by slicing it from the end to the beginning.
    print(f"In a parallel universe, they call you {name[::-1]}!")

    another_name = input("Try another name? (y/n): ")
    if another_name.lower() != 'y':
        print("Goodbye!")
        break
