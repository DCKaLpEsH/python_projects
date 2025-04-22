import time

print("=== ⏱️ COUNTDOWN TIMER ⏱️ ===\n")

def try_again():
    play_again = input("\n🔁 Play again? (y/n): ").lower()
    if play_again != "y":
        print("\n👋 Thanks for playing! Goodbye! 👋")
    else:
        print("\n🔄 Restarting the game... 🔄")
        play_game()

def countdown(seconds):
    while seconds > 0:
        print(f"⏰ {seconds} seconds remaining...")
        seconds -= 1
        time.sleep(1)
    print("\nTime's up!")
    try_again()

def play_game():
    seconds = int(input("\nEnter the number of seconds to countdown: "))
    print()
    if(seconds <= 0):
        print("\n ❌ Please enter a positive number. ❌")
        print()
        play_game()
    countdown(seconds)

play_game()