print("⌨️ Enter a character to check it's type ⌨️")

char = input("Enter single character: ")

if (len(char) != 1):
    print("❌ Enter a single character ❌")
else:
    if char.isalpha():
        print("This is a letter 🔡")
    elif char.isdigit():
        print("This is a number 🔢")
    else:
        print("This is a special character 🔣")
