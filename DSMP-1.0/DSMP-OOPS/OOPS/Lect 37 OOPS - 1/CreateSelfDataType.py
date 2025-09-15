class Fractions:

    def __init__(self , a , b):
        self.numer=a
        self.den=b

    def __str__(self):
        return '{}/{}'.format(self.numer,self.den)


    def __add__(self,other):
        newNum = self.numer*other.den + other.numer*self.den
        newDen = self.den*other.den
        return '{}/{}'.format(newNum,newDen)

    def __sub__(self,other):
        newNum = self.numer*other.den - other.numer*self.den
        newDen = self.den*other.den
        return '{}/{}'.format(newNum,newDen)


    def __mul__(self,other):
        newNum = self.numer*other.numer
        newDen = self.den*other.den
        return '{}/{}'.format(newNum,newDen)


    def __truediv__(self,other):
        newNum = self.numer*other.den
        newDen = self.den*other.numer
        return '{}/{}'.format(newNum,newDen)

    def ConvertToDecimal(self):
        return self.numer*self.den




c1 = Fractions(3,4);
c2 = Fractions(1,2);
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.ConvertToDecimal())


# operator overloadingx
# opens source make usin ops
# we can use args and kwargs