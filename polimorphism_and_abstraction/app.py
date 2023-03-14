import tkinter as tk
import random

class SlotMachine:
    def __init__(self):
        self.icons = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓', '🌍']
        self.bet = 0
        self.balance = 0

    def play(self):
        # Check if player has enough money to make a bet
        if self.balance <= 0:
            self.result_label.config(text="Sorry, you don't have enough money to play.")
            return

        # Get player's bet
        try:
            self.bet = int(self.bet_entry.get())
            if self.bet <= 0 or self.bet > self.balance:
                raise ValueError
        except ValueError:
            self.result_label.config(text="Invalid bet. Please enter a number between 1 and " + str(self.balance))
            return

        # Spin the reels
        reels = [random.choice(self.icons) for i in range(3)]
        self.reels_label.config(text=" ".join(reels))

        # Calculate winnings
        if reels[0] == reels[1] == reels[2]:
            winnings = self.bet * 10
            self.result_label.config(text="JACKPOT!!! You won " + str(winnings) + " coins!")
        elif reels[0] == reels[1] or reels[1] == reels[2]:
            winnings = self.bet * 2
            self.result_label.config(text="You won " + str(winnings) + " coins!")
        else:
            winnings = 0
            self.result_label.config(text="Sorry, you didn't win this time.")

        # Update balance
        self.balance += winnings - self.bet
        self.balance_label.config(text="Your balance: " + str(self.balance))

    def add_money(self, amount):
        self.balance += amount
        self.balance_label.config(text="Your balance: " + str(self.balance))
        self.result_label.config(text="Added " + str(amount) + " coins to your balance.")

    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.balance_label.config(text="Your balance: " + str(self.balance))
            self.result_label.config(text="Removed " + str(amount) + " coins from your balance.")
        else:
            self.result_label.config(text="Sorry, you don't have enough money.")

    def create_widgets(self):
        # Create window and frames
        self.window = tk.Tk()
        self.window.title("Slot Machine Game")

        self.top_frame = tk.Frame(self.window)
        self.top_frame.pack(side=tk.TOP)

        self.middle_frame = tk.Frame(self.window)
        self.middle_frame.pack(side=tk.TOP)

        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.pack(side=tk.TOP)

        # Create widgets
        self.reels_label = tk.Label(self.top_frame, text=" ".join(["  "]*3), font=("Arial", 72))
        self.reels_label.pack(side=tk.TOP)

        self.balance_label = tk.Label(self.middle_frame, text="Your balance: 0", font=("Arial", 16))
        self.balance_label.pack(side=tk.LEFT)

        self.add_money_button = tk.Button(self.middle_frame, text="Add Money", command=lambda: self.add_money(100))
        self.add_money_button.pack(side=tk.LEFT)

        self.remove_money_button = tk.Button(self.middle_frame, text="Remove Money", command=lambda: self.remove_money(10))
        self.remove_money_button.pack(side=tk.LEFT)

        self.bet_label = tk.Label(self.bottom_frame, text="Enter your bet:")
        self.bet_label.pack(side=tk.LEFT)

        self.bet_entry = tk.Entry(self.bottom_frame)
        self.bet_entry.pack(side=tk.LEFT)

        self.play_button = tk.Button(self.bottom_frame, text="Play", command=self.play)
        self.play_button.pack(side=tk.LEFT)

        self.result_label = tk.Label(self.bottom_frame, text="", font=("Arial", 16))
        self.result_label.pack(side=tk.LEFT)


# Create instance of SlotMachine class
game = SlotMachine()

# Create GUI widgets
game.create_widgets()

# Run main loop of GUI
game.window.mainloop()


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # prints 2
