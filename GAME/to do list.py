import tkinter as tk
from tkinter import messagebox

# -------------------- Core Logic --------------------

tasks = []


def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        tasks.remove(task)
        update_tasks()
    except IndexError:
        messagebox.showwarning("Selection Eroor", "Please select  a task  to delete.")


def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


# -------------------- UI Setup --------------------
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Entry box
task_entry = tk.Entry(root, width=25, font=('Ariel',14))
task_entry.pack(pady=10)

#Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root,text="Delete Task",width=15,command=delete_task)
delete_button.pack(pady=5)

#Task list
task_listbox = tk.Listbox(root , width=40 , height=15)
task_listbox.pack(pady=10)

#Start app
root.mainloop()
