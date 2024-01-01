# Compile-time Polymorphism :

class Calculator:
    def add(self, num1, num2, num3=None):
        if num3 is None:
            res = num1 + num2
            print("The result is(2): " + str(res))
        else:
            res = num1 + num2 + num3
            print("The result is(3): " + str(res))

calc = Calculator()

# Calling with two arguments
calc.add(10, 20)

# Calling with three arguments
calc.add(20, 30, 40)
