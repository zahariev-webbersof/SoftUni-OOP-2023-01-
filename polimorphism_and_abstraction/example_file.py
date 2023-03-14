import random

class SlotMachine:
    def __init__(self):
        self.icons = ['🍒', '🍊', '🍋', '🍉', '🍇', '🍓']
        self.bet = 0
        self.balance = 0

    def play(self):
        if self.balance <= 0:
            print("Sorry, you don't have enough money to play.")
            return

        while True:
            try:
                self.bet = int(input("\nPlace your bet: "))
                if self.bet <= 0 or self.bet > self.balance:
                    raise ValueError
                break
            except ValueError:
                print("Invalid bet. Please enter a number between 1 and", self.balance)

        reels = [random.choice(self.icons) for i in range(3)]
        print()
        print(" ".join(reels))

        if reels[0] == reels[1] == reels[2]:
            winnings = self.bet * 10
            print("JACKPOT!!! You won", winnings, "Leva!")
        elif reels[0] == reels[1] or reels[1] == reels[2]:
            winnings = self.bet * 2
            print("You won", winnings, "Leva!")
        else:
            winnings = 0
            print("Sorry, you didn't win this time...")

        self.balance += winnings - self.bet
        print("Your balance is now", self.balance, "Leva.")

    def add_money(self, amount):
        self.balance += amount
        print("Added", amount, "leva to your balance. Your new balance is", self.balance)

    def remove_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Removed", amount, "leva from your balance. Your new balance is:", self.balance)

machine = SlotMachine()
money_amount = int(input('Please insert money: '))
machine.add_money(money_amount)
print()
print('--- Welcome to MAGIC CASINO ---')

while machine.balance > 0:
    machine.play()