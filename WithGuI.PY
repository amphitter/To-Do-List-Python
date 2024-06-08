import tkinter as tk
from tkinter import messagebox
import json
import os

class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})

    def view_tasks(self):
        return self.tasks

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True
        else:
            print("Invalid task number")

    def delete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            print("Invalid task number")

    def save_tasks(self, file_path='tasks.json'):
        with open(file_path, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self, file_path='tasks.json'):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)

class TodoApp:
    def __init__(self, root):
        self.todo_list = Todolist()
        self.todo_list.load_tasks()

        self.root = root
        self.root.title("To-Do Application")

        self.setup_ui()
        self.update_task_list()

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.create_task_entry()
        self.create_task_listbox()
        self.create_buttons()

    def create_task_entry(self):
        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=10)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1)

    def create_task_listbox(self):
        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, pady=10)

    def create_buttons(self):
        self.mark_done_button = tk.Button(self.frame, text="Mark as Done", command=self.mark_task_done)
        self.mark_done_button.grid(row=2, column=0, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.quit_app)
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_task_done(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.mark_task_done(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.todo_list.delete(index)
            self.update_task_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for index, task in enumerate(self.todo_list.view_tasks(), start=1):
            status = "Done" if task['done'] else "Not Done"
            self.tasks_listbox.insert(tk.END, f"{index}. {task['task']} - {status}")
            if task['done']:
                self.tasks_listbox.itemconfig(tk.END, {'bg':'light green'})

    def quit_app(self):
        self.todo_list.save_tasks()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

