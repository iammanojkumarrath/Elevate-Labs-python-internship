# todo.py

TASKS_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Show menu
def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":  # View tasks
            if not tasks:
                print("\nNo tasks found!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":  # Add task
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"Task '{new_task}' added successfully!")

        elif choice == "3":  # Remove task
            if not tasks:
                print("\nNo tasks to remove!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_no = int(input("Enter task number to remove: "))
                    if 1 <= task_no <= len(tasks):
                        removed = tasks.pop(task_no - 1)
                        save_tasks(tasks)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":  # Exit
            print("Goodbye! Your tasks are saved.")
            break

        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
