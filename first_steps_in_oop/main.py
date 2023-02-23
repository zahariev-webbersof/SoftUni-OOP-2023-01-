import random

class Game:
    def __init__(self, max_attempts=3):
        self.number = random.randint(1, 10)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.won = False

    def guess(self, number):
        self.attempts += 1

        if number == self.number:
            self.won = True
            print('\nCongratulations, you won!')
        elif number < self.number:
            print('The number is higher than your guess. Try again!')
        else:
            print('The number is lower than your guess. Try again!')

        if self.attempts == self.max_attempts and not self.won:
            print(f'Sorry, you lost.The number is {self.number}')

game = Game()

print('Welcome to SoftUni Advanced Game - "Guess the Number"')
while not game.won and game.attempts < game.max_attempts:
    number = int(input('Guess a number between 1 to 10: '))
    game.guess(number)
