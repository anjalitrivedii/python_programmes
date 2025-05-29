import tkinter as tk
import random

# Define card colors and values
colors = ["Red", "Green", "Blue", "Yellow"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]

# Create the full UNO deck
def create_deck():
    deck = []
    for color in colors:
        deck.append((color, "0"))  # One 0 per color
        for value in values[1:]:
            deck.extend([(color, value), (color, value)])  # Two of each 1-9 and action cards
    for _ in range(4):
        deck.extend([("Black", "Wild"), ("Black", "Wild Draw Four")])  # 4 of each Wild card
    random.shuffle(deck)
    return deck

# Check if a card is playable
def is_playable(card, top_card):
    return card[0] == top_card[0] or card[1] == top_card[1] or card[0] == "Black"

# Main UNO Game class
class UnoGame:
    def __init__(self, root):  # <-- Fixed constructor
        self.root = root
        self.root.title("UNO Game")
        self.deck = create_deck()
        self.player_hand = [self.deck.pop() for _ in range(7)]
        self.computer_hand = [self.deck.pop() for _ in range(7)]
        self.top_card = self.deck.pop()
        while self.top_card[0] == "Black":
            self.deck.append(self.top_card)
            self.top_card = self.deck.pop()

        # Game status label
        self.status = tk.Label(root, text="Your turn", font=("Arial", 14))
        self.status.pack(pady=10)

        # Display top card
        self.top_card_label = tk.Label(
            root, text=self.card_text(self.top_card),
            font=("Arial", 16), bg=self.get_color(self.top_card[0]), width=20
        )
        self.top_card_label.pack(pady=10)

        # Frame for player's hand
        self.cards_frame = tk.Frame(root)
        self.cards_frame.pack()

        # Draw card button
        self.draw_button = tk.Button(root, text="Draw Card", command=self.draw_card)
        self.draw_button.pack(pady=5)

        self.update_hand()

    def card_text(self, card):
        return f"{card[0]} {card[1]}"

    def get_color(self, color_name):
        return {
            "Red": "#ff4d4d",
            "Green": "#85e085",
            "Blue": "#80b3ff",
            "Yellow": "#ffff99",
            "Black": "#d9d9d9"
        }.get(color_name, "#ffffff")

    def update_hand(self):
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        for i, card in enumerate(self.player_hand):
            btn = tk.Button(
                self.cards_frame, text=self.card_text(card),
                bg=self.get_color(card[0]), command=lambda i=i: self.play_card(i)
            )
            btn.grid(row=0, column=i, padx=5)

    def play_card(self, index):
        card = self.player_hand[index]
        if is_playable(card, self.top_card):
            self.top_card = card
            self.player_hand.pop(index)
            self.update_display(f"You played {self.card_text(card)}")

            if not self.player_hand:
                self.status.config(text="🎉 You win! 🎉")
                self.disable_all()
                return

            self.update_hand()
            self.top_card_label.config(
                text=self.card_text(self.top_card),
                bg=self.get_color(self.top_card[0])
            )
            self.root.after(1000, self.computer_turn)
        else:
            self.update_display("Can't play that card.")

    def draw_card(self):
        if not self.deck:
            self.update_display("Deck is empty!")
            return
        card = self.deck.pop()
        self.player_hand.append(card)
        self.update_display(f"You drew {self.card_text(card)}")
        self.update_hand()

    def computer_turn(self):
        for card in self.computer_hand:
            if is_playable(card, self.top_card):
                self.top_card = card
                self.computer_hand.remove(card)
                self.update_display(f"Computer played {self.card_text(card)}")
                self.top_card_label.config(
                    text=self.card_text(self.top_card),
                    bg=self.get_color(self.top_card[0])
                )
                if not self.computer_hand:
                    self.status.config(text="😞 Computer wins!")
                    self.disable_all()
                    return
                self.status.config(text="Your turn")
                return

        if self.deck:
            drawn_card = self.deck.pop()
            self.computer_hand.append(drawn_card)
            self.update_display("Computer drew a card.")
        else:
            self.update_display("Deck is empty! Computer skips turn.")
        self.status.config(text="Your turn")

    def disable_all(self):
        self.draw_button.config(state="disabled")
        for widget in self.cards_frame.winfo_children():
            widget.config(state="disabled")

    def update_display(self, msg):
        self.status.config(text=msg)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = UnoGame(root)
    root.mainloop()
