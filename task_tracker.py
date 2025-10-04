import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def mark_complete(tasks):
    list_tasks(tasks)
    choice = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["done"] = True
        save_tasks(tasks)

def delete_task(tasks):
    list_tasks(tasks)
    choice = int(input("Enter task number to delete: ")) - 1
    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task Tracker ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
