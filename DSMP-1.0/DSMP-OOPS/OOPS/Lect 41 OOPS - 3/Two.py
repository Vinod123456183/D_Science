class Baap:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Print(self):
        print(self.name , self.age)
        

class Beta(Baap):
    pass



b11 = Baap("Vinod" , 10)
b11.Print()