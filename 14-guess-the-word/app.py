import random

print("=== 🔤 WORD SCRAMBLE GAME 🔤 ===")

words = ["learn", "python", "code", "program", "language", "computer", "science", "programming", "developer", "software"]

while True:

    word = random.choice(words)

    scrambled_word = ''.join(random.sample(word, len(word)))

    print(f"🔡 Unscramble the word: {scrambled_word}")

    guess = input("👀 Enter your guess: ")

    if guess == word:
        print("🎉 Congratulations! You guessed the word correctly. 🏆")
    else:
        print(f"😢 Sorry, the word was: {word}.")

    play_again = input("🔁 Play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye! 👋")
        break
