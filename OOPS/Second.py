
class Computer:
    
    
    def config(self):
        print("i3,8gb,1TB")
        

comp1 = Computer()
comp2 = Computer()
#print(type(comp1))
Computer.config(comp1)
Computer.config(comp2)
comp1.config()
comp2.config()
a = 5
a.bit_length()