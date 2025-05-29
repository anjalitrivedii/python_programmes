import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]


def check_winner():
    # check rows and columns
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] != "":
            return True
    # check diagonals

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False
def is_full():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def on_click(row,col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over",f"Player {current_player} wins!")
            reset_board()
        elif is_full():
            messagebox.showinfo("Game Over","It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_board():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"]=""

#Create buttons and place them in the grid
for i in range(3):
    for j in range(3):
        button = tk.Button(root,text="",font=("Ariel",24),width=5,height=2,
                           command=lambda row=i, col=j: on_click(row,col))
        button.grid(row=i, column=j)
        buttons[i][j] = button

#start the GUI event loop
root.mainloop()