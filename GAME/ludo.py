import tkinter as tk
import random

# Constants (will be updated dynamically)
TOKEN_RADIUS_RATIO = 0.03  # Token radius as fraction of canvas width
GRID_SIZE = 6  # 6x6 board

# Define the path around the board edges (6x6 grid)
PATH = [(i, 0) for i in range(GRID_SIZE)] + [(GRID_SIZE-1, i) for i in range(1, GRID_SIZE)] + \
       [(i, GRID_SIZE-1) for i in range(GRID_SIZE-2, -1, -1)] + [(0, i) for i in range(GRID_SIZE-2, 0, -1)]

# Define home areas for each player (colored squares)
HOMES = {
    "red": [(0, 0), (1, 0), (0, 1), (1, 1)],
    "blue": [(4, 0), (5, 0), (4, 1), (5, 1)],
    "green": [(4, 4), (5, 4), (4, 5), (5, 5)],
    "yellow": [(0, 4), (1, 4), (0, 5), (1, 5)]
}

PLAYER_COLORS = ["red", "blue", "green", "yellow"]

class LudoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ludo Game - 4 Players")
        self.root.state('zoomed')  # Maximize window (Windows). For fullscreen, use attributes('-fullscreen', True)

        # Responsive canvas
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.dice_label = tk.Label(root, text="Roll the dice!", font=("Arial", 16))
        self.dice_label.pack(pady=10)

        self.roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=self.roll_dice)
        self.roll_button.pack()

        self.turn_label = tk.Label(root, text="Player RED's Turn", font=("Arial", 14))
        self.turn_label.pack(pady=10)

        self.dice = 0
        self.turn = 0  # 0 to 3 for 4 players
        self.positions = [-1, -1, -1, -1]  # Start at home

        self.tokens = [None, None, None, None]

        # Bind canvas resize event
        self.canvas.bind("<Configure>", self.on_resize)

        # Initial draw parameters
        self.cell_size = 0
        self.token_radius = 0

    def on_resize(self, event):
        # Update drawing parameters
        size = min(event.width, event.height)
        self.cell_size = size / GRID_SIZE
        self.token_radius = self.cell_size * TOKEN_RADIUS_RATIO

        # Redraw everything on resize
        self.draw_board()
        self.draw_tokens()

    def draw_board(self):
        self.canvas.delete("all")

        # Draw grid lines
        for i in range(GRID_SIZE + 1):
            # Vertical
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.cell_size * GRID_SIZE, fill="gray")
            # Horizontal
            self.canvas.create_line(0, i * self.cell_size, self.cell_size * GRID_SIZE, i * self.cell_size, fill="gray")

        # Highlight path squares in light yellow
        for x, y in PATH:
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                fill="lightyellow"
            )

        # Highlight home areas
        for color, squares in HOMES.items():
            for x, y in squares:
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color
                )

    def draw_tokens(self):
        # Remove old tokens
        for token in self.tokens:
            if token:
                self.canvas.delete(token)

        for i in range(4):
            pos = self.positions[i]
            color = PLAYER_COLORS[i]

            if pos == -1:
                # Token at home: place inside first home square center
                home_squares = HOMES[color]
                x, y = home_squares[0]
                center_x = x * self.cell_size + self.cell_size / 2
                center_y = y * self.cell_size + self.cell_size / 2
            else:
                # Token on path
                x, y = PATH[pos]
                center_x = x * self.cell_size + self.cell_size / 2
                center_y = y * self.cell_size + self.cell_size / 2

            self.tokens[i] = self.canvas.create_oval(
                center_x - self.token_radius, center_y - self.token_radius,
                center_x + self.token_radius, center_y + self.token_radius,
                fill=color, outline="black", width=2
            )

    def roll_dice(self):
        self.dice = random.randint(1, 6)
        current_color = PLAYER_COLORS[self.turn]
        self.dice_label.config(text=f"Player {current_color.upper()} rolled: {self.dice}")

        pos = self.positions[self.turn]

        if pos == -1:
            # Must roll 6 to enter path
            if self.dice == 6:
                self.positions[self.turn] = 0
        else:
            # Move forward
            self.positions[self.turn] += self.dice
            if self.positions[self.turn] >= len(PATH):
                self.positions[self.turn] = len(PATH) - 1
                self.dice_label.config(text=f"Player {current_color.upper()} wins!")
                self.roll_button.config(state=tk.DISABLED)

        self.draw_tokens()

        # Next turn if no 6
        if self.dice != 6:
            self.turn = (self.turn + 1) % 4

        next_color = PLAYER_COLORS[self.turn]
        self.turn_label.config(text=f"Player {next_color.upper()}'s Turn")

# Run the game
root = tk.Tk()
game = LudoGame(root)
root.mainloop()

