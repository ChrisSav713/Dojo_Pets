class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("Making Noise...")
        return self

    def print(self):
        print(f"{self.name} {self.type} {self.tricks} {self.health} {self.energy}")

class Cat(Pet):
    def __init__(self, name, health, energy):
        super().__init__(name, "cat", "sleeping", health, energy)

    def noise(self):
        print("Meowing...")
        return self

class Dog(Pet):
    def __init__(self, name, health, energy):
        super().__init__(name, "dog", "fetching", health, energy)
    
    def noise(self):
        print("Barking...")
        return self
