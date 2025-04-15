import random
print("🧬🧬 NAME GENERATOR 🧬🧬")

number_of_names = int(
    input("Enter the number of names you want to generate: "))

# List of names
first_names = ["Alice", "Bob", "Charlie", "Diana",
               "Ethan", "Fiona", "George", "Hannah", "Ian", "Jasmine"]
last_names = ["Smith", "Johnson", "Williams", "Jones",
              "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
# Generate random names
generated_names = []
for _ in range(number_of_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    name = f"{first_name} {last_name}"
    generated_names.append(name)
    print(name)
