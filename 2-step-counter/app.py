print("🏃 Welcome to STEP COUNTER 🏃")

total_steps = int(input("\n 🤷 What is our daily step goal?\n-> "))
steps_taken = int(input("\n ✨ How many steps have you taken today?\n-> "))

steps = total_steps - steps_taken

if (steps > 0):
    print(f"💪 You need {steps} more steps to reach you goal!")
elif (steps == 0):
    print(f"🎉 Congratulations! You have achieved your goal")
else:
    print(
        f"🎉 Congratulations! You have exceed your goal by {-steps} steps!"
    )
