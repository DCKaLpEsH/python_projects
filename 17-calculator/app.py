print("==== 🧮 SIMPLE CALCULATOR 🧮 ====")

goodbye = "\n👋 Thanks for playing! Goodbye! 👋"

def try_again():
    play_again = input("\n🔁 Play again? (y/n): ").lower()
    if play_again != "y":
        print(goodbye)
        return
    else:
        print("\n🔄 Restarting the game... 🔄")
        play_game()

def play_game():
    print("\nChoose an operation:")
    print("1. ➕ Add")
    print("2. ➖ Subtract")
    print("3. ✖️ Multiply")
    print("4. ➗ Divide")
    print("5. ❌ Exit")

    try:
        operation = int(input("\nEnter the operation number: "))
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number. ❌")
        try_again()
    if operation == 5 or operation > 5 or operation < 1:
        print(goodbye)
        return

    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("\nEnter the second number: "))
    
    if operation == 1:
        print(f"\n{num1} + {num2} = {num1 + num2}")
    elif operation == 2:
        print(f"\n{num1} - {num2} = {num1 - num2}")
    elif operation == 3:
        print(f"\n{num1} * {num2} = {num1 * num2}")
    elif operation == 4:
        if(num2 == 0):
            print("\n❌ Cannot divide by zero. Please try again. ❌")
            try_again()
        else:
            print(f"\n{num1} / {num2} = {num1 / num2}")
    else:
        print("\n❌ Invalid operation. Please try again. ❌")
        try_again()
    
    try_again()

play_game()