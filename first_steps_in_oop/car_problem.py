class Car:
    car_counter = 0

    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

kia = Car("Kia", "Rio", "1.3L B3 I4")
mercedes = Car("Mercedes", "ML", "550")

# print(kia.get_info())
print(mercedes.get_info())
print(Car.get_info())
