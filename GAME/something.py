import tkinter as tk
from tkinter import ttk

# Dictionary mapping moods to emojis
mood_emoji = {
    "Happy": "😊",
    "Sad": "😢",
    "Angry": "😠",
    "Excited": "🤩",
    "Tired": "😴",
    "Love": "😍",
    "Anxious": "😰"
}

def update_emoji(*args):
    mood = selected_mood.get()
    emoji_label.config(text=mood_emoji.get(mood, ""))

# Create the main window
root = tk.Tk()
root.title("Mood Emoji Display")
root.geometry("600x400")
root.configure(bg="white")

# Dropdown to select mood
selected_mood = tk.StringVar()
selected_mood.set("Happy")  # default mood
dropdown = ttk.Combobox(root, textvariable=selected_mood, values=list(mood_emoji.keys()), font=("Arial", 16), state="readonly")
dropdown.pack(pady=20)

# Big emoji label
emoji_label = tk.Label(root, text=mood_emoji[selected_mood.get()], font=("Arial", 120), bg="white")
emoji_label.pack(pady=50)

# Update emoji when selection changes
selected_mood.trace("w", update_emoji)

# Start the GUI event loop
root.mainloop()
