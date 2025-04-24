
import random
import time


print("=== 🔁 WORD ASSOCIATION GAME 🔁 ===")
print("Welcome to the Word Association Game!")
print("You will be given a word, and you need to associate it with another word that is related to it.")
print("Let's start!")

def calculate_points(time_taken):
    if time_taken > 5:
        return 1
    else:
        return round(5 - time_taken, 2)

related_words = {
    "apple": ["fruit", "red", "sweet"],
    "banana": ["fruit", "yellow", "sweet"],
    "carrot": ["vegetable", "orange", "healthy"],
    "dog": ["pet", "loyal", "bark"],
    "cat": ["pet", "independent", "meow"],
    "house": ["building", "home", "roof"],
    "tree": ["plant", "green", "leaves", "leaf"],
    "water": ["liquid", "h2o", "hydrogen", "oxygen"],
    "fire": ["flame", "heat", "burn", "smoke"],
    "book": ["reading", "story", "novel", "author"],
    "computer": ["technology", "screen", "internet", "laptop"],
    "music": ["sound", "instrument", "song", "band"],
    "sky": ["blue", "sky", "cloud", "skyline"],
}
while True:
    current_score = 0
    score = 5
    prompt_word = random.choice(list(related_words.keys()))
    print(f"🔤 PROMPT WORD: {prompt_word}")
    start = time.time()
    word = input("Quick! Type a word related to this prompt!\n> ")
    end = time.time()
    time_taken = end - start
    if word in related_words[prompt_word]:
        print(f"\nResponse Time: {time_taken} seconds")
        points = calculate_points(time_taken)
        print("👍 CORRECT! You're a word wizard!")
        current_score += points
        print(f"💯 Score: {current_score}/{score}\n")
        score += 5
    else:
        print("👎 WRONG! Try again!\n")

    play_again = input("Do you want to play again? (y/n)\n> ")
    if play_again == "n":
        print(f"👋 Thanks for playing! Your final score is {current_score}/{score}")
        break

