class Fruit:
    nutrient = "vitamin"
    def __init__(self, fruit_name,fruit_colour, number_of_seeds, fruit_texture):
        self.fruit_name = fruit_name
        self.fruit_colour = fruit_colour
        self.number_of_seeds = number_of_seeds
        self.fruit_texture = fruit_texture

    def make_juice(self):
        return f"Makes {self.fruit_colour} {self.fruit_name} juice when blended."
    def eat(self):
        return f"{self.fruit_name} is yummy."
    def remove_seed(self):
        return f"Cut the {self.fruit_name} to remove seeds."