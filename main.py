import os
import json

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task_description):
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx}. {task['description']} [{status}]")

def mark_task_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
