import random
import string

print("🌟===🔐 Password Generator ====🔐🌟")
print("✨ Generate super strong and secure passwords with ease ✨")

def check_password_strength(password):
    score = min(len(password) / 16, 1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_digit + has_special) / 4.0

    final_score = (score * 0.6) + (variety * 0.4)

    if final_score >= 0.8:
        return "🔥 ULTRA STRONG 🔥"
    elif final_score >= 0.6:
        return "💪 STRONG 💪"
    elif final_score >= 0.4:
        return "👍 DECENT 👍"
    else:
        return "😬 NEEDS IMPROVEMENT 😬"

def main():
    print("\n🔑 How many characters do you want in your password? (8-30): ")
    try:
        length = int(input())
        if length < 8 or length > 30:
            print("Please enter a number between 8 and 30.")
            exit()
    except ValueError:
        print("Please enter a valid number.")
        exit()

    print("\n🔠 Do you want to include uppercase letters? (y/n): ")
    include_uppercase = input().lower() == "y"

    print("\n🔡 Do you want to include lowercase letters? (y/n): ")
    include_lowercase = input().lower() == "y"

    print("\n🔢 Do you want to include numbers? (y/n): ")
    include_numbers = input().lower() == "y"

    print("\n🔣 Do you want to include special characters? (y/n): ")
    include_special = input().lower() == "y"

    if not include_uppercase and not include_lowercase and not include_numbers and not include_special:
        print("You must include at least one character type.")
        exit()

    characters = ""

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    print("\n🔑 Here is your new password:")
    print(password)

    strength = check_password_strength(password)
    print(f"\n🔑 Password Strength: {strength}")

    print("\n📝===== PASSWORD TIPS =====📝")
    print("🚫 Never use the same password for multiple accounts")
    print("🗄️ Consider using a password manager")
    print("🔄 Change important passwords every few months")
    print("🛡️ Even strong passwords need to be kept secret!")

    print("\n🔑 Thank you for using the Password Generator! 🔑")

main()