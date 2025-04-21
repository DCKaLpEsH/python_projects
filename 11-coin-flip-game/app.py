import random

heads = "heads"
tails = "tails"

print("=== 🎮 COIN FLIP GAME 🎮 ===")
print(f"✨ Guess heads or {tails}! ✨")

while True:

    guess = input(f"🤔 Enter your guess ({heads}/{tails}): ")
    if (guess != heads and guess != tails):
        input("❌ Invalid Input! ➡️ Play again? (yes/no): ")
    print()

    # 0 - for heads, 1 - for tails

    heads_or_tails = random.randrange(0, 99)
    random_answer = heads_or_tails % 2

    head_tail_dict = {
        0: heads,
        1: tails
    }

    coin_flip_answer = head_tail_dict[random_answer]

    print(f"🌑 The coin shows: {coin_flip_answer} 🌑")
    congrats = "🎉 You guessed correctly! You win! 🏆"
    wrong = "😢 Sorry, wrong guess. Try again! 🍀"

    if (coin_flip_answer == guess.lower()):
        print(congrats)
    else:
        print(wrong)

    print()
    is_playing_again = input("🔁 Play again? (yes/no): ").lower()

    while True:
        if (is_playing_again != "yes" and is_playing_again != "no"):
            is_playing_again = input(
                "❌ Invalid Input! ➡️ Play again? (yes/no): ")
        else:
            break

    if (is_playing_again == "no"):
        print("Goodbye! 👋")
        break
