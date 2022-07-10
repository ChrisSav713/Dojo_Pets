from my_modules import Ninja, Pets

pet = Pets.Pet("Penfold", "hamster","Eating", 25, 25)
ninja = Ninja.Ninja("Joe", "Smith", pet, "bone", "steak")

ninja.feed().walk().bathe()

ninja.print()

pet2 = Pets.Cat("Whiskers", 25, 25)
ninja.pet = pet2
ninja.feed().walk().bathe()
ninja.print()

pet3 = Pets.Dog("Spot", 25, 25)
ninja.pet = pet3
ninja.feed().walk().bathe()
ninja.print()