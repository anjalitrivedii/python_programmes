import tkinter as tk
from tkinter import messagebox

def record_mood(mood):
    messagebox.showinfo("Mood Tracker",f"💬 you selected:{mood}")

root = tk.Tk()
root.title("Mood Tracker 🌸")
root.geometry("300x200")
root.config(bg="#f3e5f5")

moods = {
    "😊 Happy": "#f8bbd0",
    "😔 Sad": "#b39ddb",
    "😡 Angry":"#ef9a9a",
    "😌 Calm":"#a5d6a7"
}
tk.Label(root,text="How are you feeling today?🌸", bg="#f3e5f5",font=("Comic sans MS",)).pack(pady=10)

for mood,color in moods.items():
    tk.Button(root,text=mood,command=lambda m=mood: record_mood(m),
              bg=color, width=15, font=("Comic sans MS",10)).pack(pady=5)
root.mainloop()