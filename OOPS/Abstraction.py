from abc import ABC, abstractmethod

class Vehical:
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def start(self):
        print("Start the Car")
    def stop(self):
        print("Stop the car")

class Bicycle(Vehical):
    def start(self):
        print("Start the Bicycle")
    def stop(self):
        print("Stop the Bicycle")

car = Car()
bike = Bicycle()
car.start()
car.stop()
bike.start()
bike.stop()


