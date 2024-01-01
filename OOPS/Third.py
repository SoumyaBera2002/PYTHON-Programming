
class Computer:
    
    def __init__(self,cpu,ram,disk_size):
        self.cpu = cpu
        self.ram = ram
        self.disk_size = disk_size
    def config(self):
        print("The Configuration is : ",self.cpu,self.ram,self.disk_size)
        


comp1 = Computer("i3","8gb","1tb")
comp1.config()