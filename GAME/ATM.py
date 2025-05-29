from random import choice


class ATM:
    def __init__(self, card_number, pin):  # fixed constructor
        self.balance = 1000  # Initial balance
        self.notes = {100: 10, 50: 20, 20: 30, 10: 50}  # Initial note count
        self.card_number = card_number
        self.pin = pin
        self.authenticated = False

    def authenticate(self, entered_card_number, entered_pin):
        if self.card_number == entered_card_number and self.pin == entered_pin:
            self.authenticated = True
            print("Authentication successful!")
        else:
            print("Invalid card number or PIN. Please try again.")

    def check_balance(self):
        if self.authenticated:
            print(f"Your current balance is: ${self.balance}")
        else:
            print("Please authenticate first.")

    def deposit(self, amount):
        if self.authenticated:
            self.balance += amount
            self.update_notes(amount, "deposit")
            print(f"${amount} deposited successfully.")
            self.check_balance()
        else:
            print("Please authenticate first.")

    def withdraw(self, amount):
        if self.authenticated:
            if amount > self.balance:
                print("Insufficient balance!")
                return
            if not self.can_dispense(amount):
                print("Cannot dispense the exact amount with available notes!")
                return
            self.balance -= amount
            self.update_notes(amount, "withdraw")
            print(f"${amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("Please authenticate first.")

    def can_dispense(self, amount):
        temp_notes = self.notes.copy()
        for note in sorted(temp_notes.keys(), reverse=True):
            while amount >= note and temp_notes[note] > 0:
                amount -= note
                temp_notes[note] -= 1
        return amount == 0

    def update_notes(self, amount, transaction_type):
        if transaction_type == "deposit":
            for note in sorted(self.notes.keys(), reverse=True):
                while amount >= note:
                    amount -= note
                    self.notes[note] += 1
        elif transaction_type == "withdraw":
            for note in sorted(self.notes.keys(), reverse=True):
                while amount >= note and self.notes[note] > 0:
                    amount -= note
                    self.notes[note] -= 1

    def count_notes(self):
        if self.authenticated:
            print("Note count:")
            for note, count in self.notes.items():
                print(f"${note}: {count} notes")
        else:
            print("Please authenticate first.")


# Main program
atm = ATM("12345678", "1234")  # Provide default card and pin

while True:
    print("\n1. Insert Card")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Count Notes")
    print("6. Exit")

    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_choice == 1:
        card_number = input("Enter card number: ")
        pin = input("Enter PIN: ")
        atm.authenticate(card_number, pin)
    elif user_choice == 2:
        atm.check_balance()
    elif user_choice == 3:
        amount = int(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif user_choice == 4:
        amount = int(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif user_choice == 5:
        atm.count_notes()
    elif user_choice == 6:
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice! Please try again.")

