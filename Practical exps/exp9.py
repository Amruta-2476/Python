import tkinter as tk
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_tasks_display()
        task_entry.delete(0, tk.END)

def complete_task(index):
    tasks_completed.append(tasks.pop(index))
    update_tasks_display()

def delete_task(index):
    tasks.pop(index)
    update_tasks_display()

def update_tasks_display():
    tasks_display.delete(0, tk.END)
    for index, task in enumerate(tasks):
        tasks_display.insert(tk.END, f"{index + 1}. {task}")

def update_completed_display():
    completed_display.delete(0, tk.END)
    for index, task in enumerate(tasks_completed):
        completed_display.insert(tk.END, f"{index + 1}. {task}")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create widgets
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

tasks_display = tk.Listbox(root, width=50, height=10)
tasks_display.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

completed_display = tk.Listbox(root, width=50, height=5)
completed_display.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

# Initialize task lists
tasks = []
tasks_completed = []

# Update initial display
update_tasks_display()
update_completed_display()

# Create bindings for completing and deleting tasks
tasks_display.bind("<<ListboxSelect>>", lambda event: complete_task(tasks_display.curselection()[0]))
completed_display.bind("<<ListboxSelect>>", lambda event: delete_task(completed_display.curselection()[0]))

# Run the Tkinter event loop
root.mainloop()



