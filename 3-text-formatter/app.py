print("📢 TEXT CAPITALIZER 📢")

text_input = input("🤷 ♂︎ Enter text you want to format: ")

print("1. UPPERCASE\n")
print("2. lowercase\n")
print("3. Title Case\n")
print("4. Sentence Case\n")

try:
    formatting_input = int(input("Choose a format (1-4): "))
    match(formatting_input):
        case 1:
            print(text_input.upper())
        case 2:
            print(text_input.lower())
        case 3:
            print(text_input.title())
        case 4:
            print(text_input.capitalize())
        case default:
            print("❌ Input should be between 1 to 4 ❌")
except:
    print("🙏 Please enter a number as your choice. 🙏")
