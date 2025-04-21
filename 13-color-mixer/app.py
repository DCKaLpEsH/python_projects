print("🎨 Color Mixer 🎨")

color1 = input("Enter the first color: ")
color2 = input("Enter the second color: ")

colors = ["red", "blue", "green", "yellow", "purple"]

while True:
    def mix_colors(color1, color2):
        if color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
            return "purple"
        elif color1 == "red" and color2 == "green" or color1 == "green" and color2 == "red":
            return "yellow"
        elif color1 == "blue" and color2 == "green" or color1 == "green" and color2 == "blue":
            return "cyan"
        else:
            raise ValueError("Invalid color combination")

    try:
        result = mix_colors(color1, color2)
        print(f"The result of mixing {color1} and {color2} is {result}")
        if not input("\nMix more colors? (y/n)").lower().startswith("y"):
            print("Goodbye! 👋")
            break
    except Exception as e:
        print(f"Error: {e}")
