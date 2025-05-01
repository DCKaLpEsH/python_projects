# To run this file, you need to install the requests library.
# You have to use a virtual environment to install and use the requests library.
# To run the virtual environment in terminal, run the following command:
# source packages/venv/bin/activate
# It will open a new terminal window with the virtual environment activated.
# (venv) user@users-MacBook-Air python-projects % python 22-basic-chatbot/app.py


import time
import requests

print("🤖 Chatbot is starting up...")
time.sleep(2)
print("\n          🤖 Welcome to the chatbot! 🤖")

print("\n          I can chat about:")
print("          🎯'joke' - Hear a funny joke")
print("          🧠'fact' - Learn something new")
print("          🌈'color' - My favourite color")
print("          👋'bye' - End of our chat")

def greet_user():
    user_input = input("\n🧓 What's your name: ")
    print(f"🤖 Nice to meet you {user_input}! How can I help you today?")

def get_joke_from_api():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any")
        joke_data = response.json()
        
        if joke_data["type"] == "twopart":
            setup = joke_data["setup"]
            delivery = joke_data["delivery"]
            return setup, delivery
        else:
            # For single-part jokes
            return joke_data["joke"], ""
    except Exception as e:
        return f"Sorry, couldn't fetch a joke. Error: {e}", ""

def get_fact_from_api():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        fact_data = response.json()
        return fact_data["text"]
    except Exception as e:
        return f"Sorry, couldn't fetch a fact. Error: {e}", ""


greet_user()

while True:
    user_input = input("🧓 You: ")
    if "joke" in user_input.lower():
        setup, delivery = get_joke_from_api()
        print(f"\n{setup}")
        if delivery:
            time.sleep(1)
            print(f"{delivery}")
    elif user_input.lower() in ["fact", "facts"]:
        fact = get_fact_from_api()
        print(f"\n{fact}")
    elif user_input.lower() in ["color", "colors"]:
        print("\n🌈 My favourite color is blue!")
    elif user_input.lower() in ["bye", "exit"]:
        print("👋 Goodbye! Have a great day!")
        break
    else:
        print("🤖 I'm sorry, I don't understand that. Please try again.")
