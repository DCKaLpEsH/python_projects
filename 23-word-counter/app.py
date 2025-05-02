def count_sentences(text):
    # basic sentence counting: by periods, exclamation marks, and question marks
    sentence_endings = [".", "!", "?"]
    count = 0

    for char in text:
        if char in sentence_endings:
            count += 1

   # handling the edge case
    if count == 0 and text.strip():
        count = 1

    return count


def count_characters(text, include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))



def analyze_text(text):
    words = len(text.split())
    characters_with_spaces = count_characters(text, True)
    characters_without_spaces = count_characters(text, False)
    sentences = count_sentences(text)
    avg_words_per_sentence = round(words / sentences, 2)
    avg_characters_per_word = round(characters_without_spaces / words, 2)
    estimated_reading_time = round(words / avg_words_per_sentence, 2)

    print(f"• 📝 Words: {words}")
    print(f"• 🔤 Characters (with spaces): {characters_with_spaces}")
    print(f"• 🔡 Characters (without spaces): {characters_without_spaces}")
    print(f"• 📃 Sentences: {sentences}")
    print(f"• 📏 Average words per sentence: {avg_words_per_sentence}")
    print(f"• 📐 Average characters per word: {avg_characters_per_word}")

    reading_time_minutes = words / 225
    if reading_time_minutes < 1:
        reading_time_seconds = reading_time_minutes * 60
        print(
            f"• ⏱️ Estimated reading time: {reading_time_seconds:.0f} seconds")
    else:
        print(
            f"• ⏱️ Estimated reading time: {reading_time_minutes:.1f} minutes")
        

def main():
    print("==== Word Counter ====")
    print("Count words, characters, and sentences in your text.")

    while True:
        print("""Choose an option:
        1. 📄 Enter text to analyzer
        2. 🚪 Exit
        """)

        option = input("Enter your choice (1 or 2): ")

        if option == "1":
            text = input("Enter or paste your text below (press Enter twice to finish):\n")
            input()
            analyze_text(text)
        elif option == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

    return
main()
