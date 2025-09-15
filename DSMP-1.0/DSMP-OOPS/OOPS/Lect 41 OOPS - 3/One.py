class Customer:

    def __init__(self , name , gender , address):
        self.name = name
        self.gender = gender
        self.__address  = address

    def getAddress(self):
        l=[]
        a1 = self.__address.city
        a2 = self.__address.state
        a3 = self.__address.pin
        l.append(a1)
        l.append(a2)
        l.append(a3)
        for i in l:
            print(i)


class Address:
    def __init__(self , state , city , pin):
        self.state = state
        self.city = city
        self.pin = pin

A1 = Address("UP" , "Haldwani" , "200001")
C1 = Customer("Vinod" , "Male" , A1);


print(C1.)