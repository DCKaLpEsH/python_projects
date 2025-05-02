import requests
import random
def fetch_categories():
    try:
        url = "https://opentdb.com/api_category.php"
        response = requests.get(url)
        data = response.json()
        return data["trivia_categories"]
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return []

def display_welcome():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE ULTIMATE QUIZ CHALLENGE! 🎮".center(50))
    print("=" * 50)
    print("\n📜 Instructions:")
    print("- Choose a quiz category")
    print("- Answer multiple-choice questions")
    print("- Each correct answer is worth 10 points")
    print("- See your final score at the end")
    print("- Have fun and learn something new!")


def display_categories():
    categories = fetch_categories()
    print("\n🗂️  Quiz Categories:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category['name']}")
    
    return categories

def get_user_choice(max_categories):
    while True:
        try:
            return int(input(f"🎮 Enter your choice(1 - {max_categories}): "))
        except ValueError:
            print("� Invalid input. Please enter a number between 1 and 5.")

def fetch_questions(category_id):
    try:
        url = f"https://opentdb.com/api.php?amount=5&category={category_id}&type=multiple"
        response = requests.get(url)
        data = response.json()
        return data["results"]
    except Exception as e:
        print(f"Error fetching questions: {e}")
        return []


def get_user_answer(num_options):
    while True:
        try:
            return int(input(f"🎮 Enter your choice(1 - {num_options}): "))
        except ValueError:
            print("� Invalid input. Please enter a number between 1 and 5.")

def start_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        print(f"\n🎮 Question: {question['question']}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        answer = get_user_answer(len(options))
        if answer == question['correct_answer']:
            print("✅ Correct! You earned 10 points!")
            score += 10
        else:
            print(f"❌ Incorrect. The correct answer is: {question['correct_answer']}")

    print(f"\n🎉 Quiz completed! Your score is: {score}/{total_questions}")
    if score >= 30:
        print("🏆 You've earned a certificate!")
    else:
        print("💔 Better luck next time!")



def main():
    display_welcome()
    categories =display_categories()
    category_choice = get_user_choice(len(categories))
    selected_category = categories[category_choice - 1]
    print(f"\n🎮 Selected Category: {selected_category['name']}")
    print(f"\n🎮 Fetching questions for {selected_category['name']}...")
    questions = fetch_questions(selected_category['id'])
    print("QUESTIONS", questions)
    start_quiz(questions)

main()