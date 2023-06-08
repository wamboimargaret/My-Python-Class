class Car:
    manufacture_country = "Germany"
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def display_details(self):
        return f"This is a {self.year} {self.make}, {self.model} from {self.manufacture_country} with {self.speed} speed."
    def start_car(self):
        return f"Vroom!"
    def accelerate(self, acceleration):
        self.speed += acceleration
        return self.speed