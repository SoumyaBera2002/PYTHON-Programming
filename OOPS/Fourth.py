
class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
    def display(self):
        print("The details of the dog is : "+self.name+" "+self.breed+" "+str(self.age))

dog = Dog("Lalu","Retriver",10)
dog.display()