import random
# Music Recommender
# This is a simple music recommender program that suggests songs based on the user's favorite genre.

print("🎵 Music Recommender 🎵")

genre = input("Enter your favorite genre (rock/pop/hip-hop): ")


genres = {
    "rock": ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"],
    "pop": ["Blinding Lights", "Bad Guy", "Shape of You"],
    "hip-hop": ["Sicko Mode", "HUMBLE.", "God's Plan"]
}
if genre not in genres:
    print("Invalid genre. Please enter one of the following: rock, pop, hip-hop.")
else:
    if genre == "rock":
        print(random.choice(genres[genre]))
    elif genre == "pop":
        print(random.choice(genres[genre]))
    elif genre == "hip-hop":
        print(random.choice(genres[genre]))
    print("🕺 Enjoy your music! 🕺")
