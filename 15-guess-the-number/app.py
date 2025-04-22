import random


def try_again():
    play_again = input("🔁 Play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye! 👋")
    else:
        print("🔄 Restarting the game... 🔄")
        play_game()

def play_game(): 
    print("🎮 Welcome to the NUMBER GUESSING GAME! 🎮")
    print("I'm thinking of a number between 1 and 100.  ")
    number = random.randint(1, 100)
    tries = 1
    while True:
        guess = int(input(f"🎯 Attempt {tries}/10 👀 Enter your guess: "))
        if(tries == 10):
            print("🤔 You've reached the maximum number of tries. 🤔")
            try_again()
            break
        elif(guess == number):
            print(f"🎉 Congratulations! You guessed the number in {tries} tries! 🎉")
            try_again()
            break
        elif(guess < number):
            print("🤔 Too low! Try again. 🤔")
        else:
            print("🤔 Too high! Try again. 🤔")
        tries += 1

play_game()
