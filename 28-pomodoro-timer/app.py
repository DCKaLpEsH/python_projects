import time

def start_timer(seconds):
    for remaining in range(seconds, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
    print("Time's up!")

def main():
    print("==== 🍅 Pomodoro Timer 🍅 ====")
    print("Use default settings (25 min work, 5 min break, 15 min long break)? (yes/no): ")
    use_default = input("yes/no: ").lower() == "yes"

    if not use_default:
        work_minutes = int(input("Enter work session length (minutes): "))
        break_minutes = int(input("Enter break length (minutes): "))
        long_break_minutes = int(input("Enter long break length (minutes): "))

    else:
        work_minutes = 25
        break_minutes = 5
        long_break_minutes = 15

    print("Starting Pomodoro Timer with:")
    print(f"- Work: {work_minutes} minutes")
    print(f"- Break: {break_minutes} minutes")
    print(f"- Long Break: {long_break_minutes} minutes")
    print("Press Ctrl+C at any time to exit")
    print("Press Enter to start...")
    input()
    while True:
        print("\n=== Work Session ===")
        start_timer(work_minutes * 60)
        print("\n=== Break ===")
        start_timer(break_minutes * 60)
        break



main()

