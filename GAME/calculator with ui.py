import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        evaluate()
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def evaluate(event=None):  # Allow calling with or without event (keyboard or button)
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)
entry.bind("<Return>", evaluate)  # Bind Enter key

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()
# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Creating buttons
for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18")
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
