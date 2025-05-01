

def print_menu():
    print("\n==== Task Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("0. Exit")
    print("=" * 50)

# Using a dictionary to store tasks and their completion status
# { "Do Laundry": False, "Buy Groceries": False, "Finish Course": False }
# { "Do Laundry": True, "Buy Groceries": False, "Finish Course": False }

tasks = {}

def add_task():
    task = input("Enter a task: ")
    tasks[task] = False
    print(f"Task '{task}' added successfully.\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Tasks:")
        task_completed = "[x]"
        task_not_completed = "[ ]"
        for idx, (task, completed) in enumerate(tasks.items(), start=1):
            print(f"{idx}. {task_completed if completed else task_not_completed} {task}\n")

def mark_task_as_completed():
    view_tasks()
    task_idx = int(input("\nEnter the number of the task to mark as completed: "))
    if 1 <= task_idx <= len(tasks):
        task = list(tasks.keys())[task_idx - 1]
        tasks[task] = True
        print(f"Task '{task}' marked as completed.\n")
    else:
        print("Invalid task number.\n")

def remove_task():
    view_tasks()    
    task_idx = int(input("\nEnter the number of the task to remove: "))
    if 1 <= task_idx <= len(tasks):
        removed_task = list(tasks.keys())[task_idx - 1]
        tasks.pop(removed_task)
        print(f"Task '{removed_task}' removed successfully.\n")
    else:
        print("Invalid task number.\n")

while True:
    print_menu()
    choice = input("\nEnter your choice(0-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_as_completed()
    elif choice == "4":
        remove_task()
    elif choice == "0":
        break


