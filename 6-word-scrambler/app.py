import random


print("🔤 WORD SCRAMBER 🔤")

word = input("Enter a word to scramble (or 'quit'): ")

if (word.lower() == "quit"):
    print("👋 Goodbye")
else:
    letters = list(word)
    random.shuffle(letters)
    print("".join(letters))
