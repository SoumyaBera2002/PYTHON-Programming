

class Animal:
    def makeSound(self):
        raise NotImplementedError("The method is not defined here !!")

class Dog(Animal):
    def makeSound(self):
        print("Woof")
class Cat(Animal):
    def makeSound(self):
        print("Meow")
class Cow(Animal):
    def makeSound(self):
        print("Moow")
def AnimalSounds(animals):
    for animal in animals:
        animal.makeSound()

animals = [Dog(),Cat(),Cow()]
AnimalSounds(animals)
