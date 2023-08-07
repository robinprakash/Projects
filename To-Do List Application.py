import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.load_tasks()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.task_listbox.itemconfig(index, {'bg': 'light green'})
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")
    
    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task_info in self.tasks:
                f.write(f"{task_info['task']},{task_info['completed']}\n")
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task, completed = line.strip().split(",")
                    self.tasks.append({"task": task, "completed": completed == "True"})
                    self.task_listbox.insert(tk.END, task)
                    if completed == "True":
                        self.task_listbox.itemconfig(tk.END, {'bg': 'light green'})
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
