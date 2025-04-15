print("🔡 VOWEL COUNTER 🔡")

text = input("Enter some text (or 'quit'): ")

if (text != 'quit'):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for t in text:
        if (t.lower() in vowels):
            vowel_counter += 1
    print(f"Number of Vowels: {vowel_counter}")
else:
    print("Goodby")
