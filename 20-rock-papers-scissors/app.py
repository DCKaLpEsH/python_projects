import random
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")

def calculate_winner(player_choice, computer_choice):
    rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if player_choice == computer_choice:
        return "tie"
    elif rules[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"

def play_again():
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 🎉")
        return False
    else:
        clear_screen()
        play_game()
        return True

def play_game():
    print("====== Rock, Paper, Scissors ======")
    print("🪨 📄 ✂️")

    print("Rules:")
    print("- Rock beats Scissors")
    print("- Paper beats Rock")
    print("- Scissors beats Paper")
    print("- First to win 3 rounds is the champion! 🏆\n")

    print("-" * 50)
    print("")

    choices = { "rock": "🪨", "paper": "📄", "scissors": "✂️" }

    computer_score = 0
    player_score = 0
    round = 0

    while True:
        round += 1
        print(f"====== Round {round} ======")
        print("Rock, Paper, Scissors, Shoot!")
        player_choice = input("Enter your choice: ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"You chose {player_choice}{choices[player_choice]}, computer chose {computer_choice}{choices[computer_choice]}")

        winner = calculate_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print(f"\n📝 Score: Player {player_score} - Computer {computer_score}")

        if player_score == 3:
            print("\nYou win the game! 🏆")
            if play_again():
                continue
            else:
                return
        elif computer_score == 3:
            print("\nComputer wins the game! 🏆")
            if play_again():
                continue
            else:
                return

play_game()
