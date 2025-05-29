import random

colors = ["Red", "Green", "Blue", "Yellow"]
values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "skip", "Reverse", "Draw Two"]
wild_cards = ["Wild", "Wild Draw Four"]

# Generate the full UNO deck
def create_deck():
    deck = []
    for color in colors:
        deck.append((color, "0"))  # one "0" per color
        for value in values[1:]:
            deck.append((color, value))
            deck.append((color, value))
    for _ in range(4):
        deck.append(("Black", "Wild"))
        deck.append(("Black", "Wild Draw Four"))
    random.shuffle(deck)
    return deck

# Check if a card can be played on top of the current card
def is_playable(card, top_card):
    return card[0] == top_card[0] or card[1] == top_card[1] or card[0] == "Black"

# Print player's hand
def display_hand(hand):
    for idx, card in enumerate(hand):
        print(f"[{idx}]: {card[0]} {card[1]}")

# Main game logic
def play_uno():
    deck = create_deck()
    player_hands = [[], []]  # Two players
    for i in range(2):
        for _ in range(7):
            player_hands[i].append(deck.pop())

    top_card = deck.pop()
    while top_card[0] == "Black":
        deck.insert(0, top_card)
        top_card = deck.pop()

    current_player = 0
    direction = 1  # 1 = clockwise, -1 = counter-clockwise

    while True:
        print(f"\nTop card: {top_card[0]} {top_card[1]}")
        print(f"Player {current_player + 1}'s turn:")
        display_hand(player_hands[current_player])

        playable_cards = [card for card in player_hands[current_player] if is_playable(card, top_card)]

        if not playable_cards:
            print("No playable cards. Drawing one...")
            drawn_card = deck.pop()
            player_hands[current_player].append(drawn_card)
            if is_playable(drawn_card, top_card):
                print(f"Drawn card is playable! Playing {drawn_card[0]} {drawn_card[1]}")
                top_card = drawn_card
                player_hands[current_player].remove(drawn_card)
        else:
            try:
                choice_index = int(input("Enter card index to play: "))
                chosen_card = player_hands[current_player][choice_index]
                if is_playable(chosen_card, top_card):
                    top_card = chosen_card
                    player_hands[current_player].remove(chosen_card)

                    if chosen_card[1] == "Reverse":
                        direction *= -1
                    elif chosen_card[1] == "skip":
                        current_player = (current_player + direction) % 2
                    elif chosen_card[1] == "Draw Two":
                        next_player = (current_player + direction) % 2
                        for _ in range(2):
                            player_hands[next_player].append(deck.pop())
                    elif chosen_card[1] == "Wild Draw Four":
                        next_player = (current_player + direction) % 2
                        for _ in range(4):
                            player_hands[next_player].append(deck.pop())
                        print("Choose a color: Red, Green, Blue, Yellow")
                        chosen_color = input().capitalize()
                        top_card = (chosen_color, "Wild")
                        continue
                    elif chosen_card[1] == "Wild":
                        print("Choose a color: Red, Green, Blue, Yellow")
                        chosen_color = input().capitalize()
                        top_card = (chosen_color, "Wild")
                        continue
                else:
                    print("Invalid card. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue

        # Check for win
        if not player_hands[current_player]:
            print(f"\nPlayer {current_player + 1} wins!")
            break

        current_player = (current_player + direction) % 2

# Run the game
play_uno()
