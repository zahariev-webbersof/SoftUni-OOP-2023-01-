class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return 'meow'

class Dog(Animal):
    def make_sound(self):
        return 'woof-woof'

class Chicken(Animal):
    def make_sound(self):
        return 'cluck'

class Cow(Animal):
    def make_sound(self):
        return 'moo'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


cat = Cat('Goncho')
animal_sound(cat.make_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
