
class Animal:
    def __init__(self,type,name):
        self.type = type
        self.name = name
    def display(self):
        print(f"My {self.type}, {self.name} is eating")
class Dog(Animal):
    def bark(self):
        print("Woof Woof")
class Cat(Animal):
    def meow(self):
        print("Meow Meow")
dog = Dog("Dog","Spike")
cat = Cat("Cat","Tom")
dog.display()
print()
cat.display()
dog.bark()
cat.meow()